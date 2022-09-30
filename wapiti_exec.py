import ast
import json
import subprocess
from time import sleep
from datetime import datetime

def wapiti(urls, severity_dict):
    cmd = 'wapiti'
    i=0
    len_urls=len(urls)
    while(i<len_urls):
        sleep_time=15
        home_folder='/home/ubuntu/'
        file_extension= '.json'
        name_to_save=urls[i].replace("https://","")
        name_to_save=name_to_save.replace("http://","")
        name_to_save=name_to_save.replace("r/","r") 
        filepath= home_folder + name_to_save + file_extension
        final_args='-v 2 -f json -o '+ filepath
        timestampInicio = datetime.now()
        final_command= cmd + ' ' + '-u' + ' ' + urls[i] + ' ' + final_args
        subprocess.run(final_command, shell=True)
        timestampFinal = datetime.now()
        sleep(sleep_time)
        with open(filepath,'r+') as file:
            owasp_info_dict= {}
            file_data = json.load(file)
            for vul_key in file_data["vulnerabilities"]:
                vul_value = file_data["vulnerabilities"][vul_key]
                vul_class = severity_dict[vul_key]
                if len(vul_value)!=0:
                    owasp_info_dict[vul_key]=vul_class
                file_data["infos"]["start_timestamp"]=timestampInicio.strftime("%m/%d/%Y, %H:%M:%S")
                file_data["infos"]["final_timestamp"]=timestampFinal.strftime("%m/%d/%Y, %H:%M:%S")
                file_data["owasp_classification"]=owasp_info_dict
                file.seek(0)
                json.dump(file_data, file, indent = 4)
        sleep(sleep_time)
        i+=1

urls = list(open('lista_cidades_teste.txt'))
for i in range(len(urls)):
    urls[i] = urls[i].strip('\n')

with open('owasp_severity_dict_pyformat.txt','r') as dict_file:
  dict_data = dict_file.read()

dictionary = ast.literal_eval(dict_data)

wapiti(urls, dictionary)

