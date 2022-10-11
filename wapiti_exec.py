import ast
import json
import subprocess
from time import sleep
from datetime import datetime


def get_urls_from_file(filepath):
    urls = list(open(filepath))
    for i in range(len(urls)):
        urls[i] = urls[i].strip('\n')
    return urls

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

def update_wapiti_report(filepath, timestampInicio, timestampFinal, severity_dict, duration, exp_round):
    with open(filepath,'r+') as file:
        owasp_info_dict = {}
        file_data = json.load(file)
        owasp_info_dict = update_owasp_classf(file_data["vulnerabilities"],owasp_info_dict,severity_dict)
        owasp_info_dict = update_owasp_classf(file_data["anomalies"],owasp_info_dict,severity_dict)
        owasp_info_dict = update_owasp_classf(file_data["additionals"],owasp_info_dict,severity_dict)
        file_data["infos"]["start_timestamp"] = timestampInicio.strftime("%m/%d/%Y, %H:%M:%S")
        file_data["infos"]["final_timestamp"] = timestampFinal.strftime("%m/%d/%Y, %H:%M:%S")
        file_data["infos"]["duration"] = str(duration)
        file_data["infos"]["exp_round"] = str(exp_round)
        file_data["owasp_classification"] = owasp_info_dict
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    
def wapiti(urls, severity_dict, exp_round):
    cmd = 'wapiti'
    i = 0
    len_urls = len(urls)
    while(i<len_urls):
        sleep_time = 5
        home_folder = '/home/ubuntu/'
        file_extension = '.json'
        name_to_save = define_report_name(urls[i])
        filepath = home_folder + name_to_save + file_extension
        final_args = '-v 2 -f json -o '+ filepath
        timestampInicio = datetime.now()
        final_command = cmd + ' ' + '-u' + ' ' + urls[i] + ' ' + final_args
        subprocess.run(final_command, shell=True)
        timestampFinal = datetime.now()
        duration = timestampFinal-timestampInicio
        sleep(sleep_time)
        update_wapiti_report(filepath,timestampInicio,timestampFinal,severity_dict,duration, exp_round)
        sleep(sleep_time)
        i+=1

exp_round=1
urls = get_urls_from_file('lista_cidades_teste.txt')
dictionary = get_severity_dict_from_file('owasp_severity_dict_pyformat.txt')
wapiti(urls, dictionary, exp_round)

