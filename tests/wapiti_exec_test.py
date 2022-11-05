import ast
import json
import subprocess
from time import sleep
from datetime import datetime
import csv
import argparse

def get_severity_dict_from_file(filepath):
    with open(filepath,'r') as dict_file:
        dict_data = dict_file.read()
    dictionary = ast.literal_eval(dict_data)
    return dictionary

def get_city_dict_from_file(filepath):
    dict_from_csv = {}
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}
    return dict_from_csv

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

def update_wapiti_report(filepath, timestampInicio, timestampFinal, severity_dict, duration, exp_round, city_dict):
    with open(filepath,'r+') as file:
        owasp_info_dict = {}
        file_data = json.load(file)
        owasp_info_dict = update_owasp_classf(file_data["vulnerabilities"],owasp_info_dict,severity_dict)
        owasp_info_dict = update_owasp_classf(file_data["anomalies"],owasp_info_dict,severity_dict)
        owasp_info_dict = update_owasp_classf(file_data["additionals"],owasp_info_dict,severity_dict)
        target_url = file_data["infos"]["target"]
     #   file_data["infos"]["start_timestamp"] = timestampInicio.strftime("%m/%d/%Y, %H:%M:%S")
     #   file_data["infos"]["final_timestamp"] = timestampFinal.strftime("%m/%d/%Y, %H:%M:%S")
     #   file_data["infos"]["duration"] = str(duration)
        file_data["infos"]["exp_round"] = str(exp_round)
        file_data["infos"]["city"] = city_dict[target_url]
        file_data["owasp_classification"] = owasp_info_dict
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def wapiti(severity_dict, exp_round, city_dict):
    cmd = 'ls'
    sleep_time=2
    filepath = "www.barradesaomiguel.al.leg.br_2.json"
    timestampInicio = datetime.now()
    final_command= cmd + ' ' + '-la' 
    subprocess.run(final_command, shell=True)
    timestampFinal = datetime.now()
    duration=timestampFinal-timestampInicio
    sleep(sleep_time)
    update_wapiti_report(filepath,timestampInicio,timestampFinal,severity_dict,duration, exp_round, city_dict)
    sleep(sleep_time)

parser = argparse.ArgumentParser(description='A script to automate Wapiti execution to attack many urls sequentially')
parser.add_argument("--exp_round", help="Adds the round information to the experiment (1,2,..)",required=True)
parser.add_argument("--severity_dict_path", help="Path to severity dict file",default='owasp_severity_dict_pyformat.txt')
parser.add_argument("--city_dict_path", help="Adds the severity dict information to the experiment",default='url_cidade_dict.csv')
args = parser.parse_args()
dictionary = get_severity_dict_from_file(args.severity_dict_path)
city_dict = get_city_dict_from_file(args.city_dict_path)
wapiti(dictionary,args.exp_round,city_dict)

