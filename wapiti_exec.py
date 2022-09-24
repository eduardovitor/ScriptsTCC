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
        for k in range(1,4):
            file_extension= '.json'
            filename= urls[i] + '-' + k + file_extension
            final_args='-f json -o '+ filename + ' --flush-attacks'
            timestampInicio = datetime.now()
            temp = subprocess.run(cmd+ ' ' + '-u' + ' ' + urls[i] + ' ' + final_args)
            timestampFinal = datetime.now()
            duracao=timestampFinal-timestampInicio
            new_data={
                "start_timestamp": timestampInicio,
                "final_timestamp": timestampFinal,
                "duration_minutes" : duracao.min
            }  
            
            with open(filename,'r+') as file:
                owasp_info_dict= {}
                file_data = json.load(file)
                for vul_key in file_data["vulnerabilities"]:
                    vul_value = file_data["vulnerabilities"][vul_key]
                    vul_class = severity_dict[vul_key]
                    if len(vul_value)!=0:
                        owasp_info_dict[vul_key]=vul_class
                file_data["infos"].append(new_data)
                file_data["owasp_classification"]=owasp_info_dict
                file.seek(0)
                json.dump(file_data, file, indent = 4)
            sleep(120)
            if k==3:
                i+=1
                k=1
  

    
urls = list(open('lista_cidades.txt'))
for i in range(len(urls)):
    urls[i] = urls[i].strip('\n')

with open('owasp_severity_dict.txt','r') as dict_file:
  dict_data = dict_file.read()

dictionary = ast.literal_eval(dict_data)

wapiti(urls, dictionary)

