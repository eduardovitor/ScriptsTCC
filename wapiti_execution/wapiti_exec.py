import ast
import json
import subprocess
from time import sleep
from datetime import datetime
import csv
import argparse

def get_urls_from_file(filepath):
    urls = list(open(filepath))
    for i in range(len(urls)):
        urls[i] = urls[i].strip('\n')
    return urls

def get_city_dict_from_file(filepath):
    dict_from_csv = {}
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}
    return dict_from_csv

def get_severity_dict_from_file(filepath):
    with open(filepath,'r') as dict_file:
        dict_data = dict_file.read()
    dictionary = ast.literal_eval(dict_data)
    return dictionary

def update_owasp_classf(file_dict, owasp_dict, severity_dict):    
    for vul_key in file_dict:
        vul_value = file_dict[vul_key]
        vul_class = severity_dict[vul_key]
        if len(vul_value)!=0:
            owasp_dict[vul_key]=vul_class
    return owasp_dict

def define_report_name(url):
    name_to_save = url.replace("https://","")
    name_to_save = name_to_save.replace("http://","")
    name_to_save = name_to_save.replace("r/","r")
    return name_to_save

def update_wapiti_report(filepath, timestampInicio, timestampFinal, severity_dict, exp_round, city_dict):
    with open(filepath,'r+') as file:
        owasp_info_dict = {}
        file_data = json.load(file)
        owasp_info_dict = update_owasp_classf(file_data["vulnerabilities"],owasp_info_dict,severity_dict)
        owasp_info_dict = update_owasp_classf(file_data["anomalies"],owasp_info_dict,severity_dict)
        owasp_info_dict = update_owasp_classf(file_data["additionals"],owasp_info_dict,severity_dict)
        target_url = file_data["infos"]["target"]
        file_data["infos"]["start_timestamp"] = timestampInicio.strftime("%Y-%m-%d %H:%M:%S")
        file_data["infos"]["final_timestamp"] = timestampFinal.strftime("%Y-%m-%d %H:%M:%S")
        file_data["infos"]["exp_round"] = exp_round
        file_data["infos"]["city"] = city_dict[target_url]
        file_data["owasp_classification"] = owasp_info_dict
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    
def wapiti(urls, severity_dict, report_dir, exp_round, city_dict, max_scan_time, max_attack_time):
    cmd = 'wapiti'
    i = 0
    len_urls = len(urls)
    while(i<len_urls):
        sleep_time = 5
        home_folder = report_dir
        file_extension = '.json'
        name_to_save = define_report_name(urls[i])
        filepath = home_folder + name_to_save + '_' + exp_round + file_extension
        final_args = '-d 4 -v 2 -f json -o '+ filepath + '--max-scan-time' + ' ' + max_scan_time + ' ' + '--max-attack-time' + max_attack_time
        timestampInicio = datetime.now()
        final_command = cmd + ' ' + '-u' + ' ' + urls[i] + ' ' + final_args
        subprocess.run(final_command, shell=True)
        timestampFinal = datetime.now()
        sleep(sleep_time)
        update_wapiti_report(filepath,timestampInicio,timestampFinal,severity_dict, exp_round, city_dict)
        sleep(sleep_time)
        i+=1

parser = argparse.ArgumentParser(description='A script to automate Wapiti execution to attack many urls sequentially')
parser.add_argument("--exp_round", help="Adds the round information to the experiment (1,2,..)",required=True)
parser.add_argument("--report_dir", help="Adds the dir where wapiti reports will be stored",required=True)
parser.add_argument("--urls_path", help="Path to URLs file",default='lista_urls.txt')
parser.add_argument("--severity_dict_path", help="Path to severity dict file",default='owasp_severity_dict_pyformat.txt')
parser.add_argument("--city_dict_path", help="Adds the severity dict information to the experiment",default='url_cidade_dict.csv')
parser.add_argument("--max_scan_time", help="Defines the limit time for the scan", required=True)
parser.add_argument("--max_attack_time", help="Defines the limit time for each module attack phase", required=True)
args = parser.parse_args()
urls = get_urls_from_file(args.urls_path)
owasp_dict = get_severity_dict_from_file(args.severity_dict_path)
city_dict = get_city_dict_from_file(args.city_dict_path)
wapiti(urls, owasp_dict, args.report_dir, args.exp_round, city_dict, args.max_scan_time, args.max_attack_time)

