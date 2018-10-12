import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin, urlparse, parse_qs

import codecs

import sys

import types

import time

import csv

from time import sleep

import subprocess

import json


#parameters

args = sys.argv



# HTTPリクエストシナリオ

http_request_scenario_arr = [

    {

        "url": "https://www.jc3.or.jp/topics/vm_index.html",

        "method": "get",

        "debug": False,

        "params": None,

    },

]



def request_http_scenario(scenario_arr):

    for scenario in http_request_scenario_arr:

        if scenario.get("disable"):

            continue

        print("-- params --")

        print(scenario["params"])

        print("-- params parsed --")

        print(parse_qs(scenario["params"], keep_blank_values=True))

        if scenario["method"] == "get":

            res = session.get(scenario["url"], params=parse_qs(scenario["params"], keep_blank_values=True))

        elif scenario["method"] == "post":

            res = session.post(scenario["url"], data=parse_qs(scenario["params"], keep_blank_values=True))

        res.raise_for_status()

        res.encoding = res.apparent_encoding

        resultText = res.text

        print("-- url --")

        print(scenario["url"])

        print("-- response cookie --")

        print(res.cookies)

        if scenario["debug"]:

            print("-- request header --")

            print(res.request.headers)

            print("-- request body --")

            print(res.request.body)

            print("-- response body --")

            print(resultText)

    return resultText



if (len(args) == 1) or (args[1] != "-jc3" and args[1] != "-csv") or (args[1] == "-csv" and len(args) != 3):

    print("Mail attachment information analysis")

    print(" Usage: -jc3  : Acquire information from JC 3 site and analyze")

    print(" Usage: -csv [filename]  : Analyze using CSV file")

    sys.exit()



attach_filenames = []

if args[1] == "-jc3":

    print("----- Start jc3 data analyze -----")

    # セッションを開始

    session = requests.session()

    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})

    resultText = request_http_scenario(http_request_scenario_arr)

    soup = BeautifulSoup(resultText, "html.parser")

    res = soup.find_all("td",attrs={"class": "item2"})

    for r in res:

        attach_filename = r.string

        if attach_filename != None:

            attach_filenames.append(attach_filename)

elif args[1] == "-csv":

    print("----- Start csv data analyze -----")

    csv_filename = args[2]

    csv_fileobj = open(csv_filename, "r", encoding="utf-8", errors="", newline="" )

    f = csv.reader(csv_fileobj, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    for row in f:

        for item in row:

            attach_filenames.append(item)

# HybridAnalysis、Virustotalでの解析
for i in range(len(attach_filenames)):
    hybrid_analysis_result = subprocess.check_output(['python3', 'vxapi.py', 'search', attach_filenames[i]])
    hy_result_dict = json.loads(hybrid_analysis_result.decode())
    hy_response = hy_result_dict['response']['result']

    url = "https://www.virustotal.com/vtapi/v2/file/report"
    
    for j in range(len(hy_response)):
        hy_sha256 = hy_response[j]['sha256']
        parameters = {'resource': hy_sha256, 'apikey': ''}
        response = requests.get(url, params=parameters)
        
        print(response.text)
        sleep(25)

