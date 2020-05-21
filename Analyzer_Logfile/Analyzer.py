import argparse
import re
import json
import glob
from collections import defaultdict, OrderedDict
from tkinter import messagebox

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='file', action='store', help='Path to logfile', default=glob.glob('Analyzer_Logfile/Log/*'))
args = parser.parse_args()

dict_ip_method = defaultdict(lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0})
dict_method = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
dict_ip = defaultdict(int)
dict_response = defaultdict(str)


def analysis_log(logfile):
    with open(logfile) as file:
        for index, line in enumerate(file.readlines()):
            ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0]
            response = re.search(r" \d{3} ", line).group()

            dict_ip_method[ip][method] += 1
            dict_method[method] += 1
            dict_ip[ip] += 1
            dict_response[ip] = response

        return index


def get_count_query(logfile):
    return len(open(logfile).readlines())


def get_top_ip():
    return OrderedDict(sorted(dict_ip.items(), key=lambda t: -t[1]))


def get_top_time():
    return OrderedDict(sorted(dict_time.items(), key=lambda time: time[1]))


if args.file.find(".log") == -1:
    var = glob.glob(args.file + "*.log")
    for log in var:
        analysis_log(log)
        count = get_count_query(log)
else:
    analysis_log(args.file)
    count = get_count_query(args.file)

if dict_ip_method == {}:
    messagebox.showwarning(title="Ошибка", message="Файл не содержит логов")
else:

    with open('Analyzer_Logfile/Log/AllQueryLog.json', 'w') as file:
        file.write(json.dumps(dict_ip_method, indent=4))

    with open('Analyzer_Logfile/Log/MethodsLog.json', 'w') as file:
        file.write(json.dumps(dict_method, indent=4))

    with open('Analyzer_Logfile/Log/IPlog.json', 'w') as file:
        file.write(json.dumps(get_top_ip(), indent=4))

    with open('Analyzer_Logfile/Log/Responce.json', 'w') as file:
        file.write(json.dumps(dict_response, indent=4))






