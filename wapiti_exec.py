import json
import subprocess  
from time import sleep
from datetime import datetime

def wapiti(urls):
    cmd = 'wapiti'
    i=0
    len_urls=len(urls)
    while(i<len_urls):
        for k in range(1,4):
            final_args='-f json -o '+ urls[i] + '-' + k + '.json' + ' --flush-attacks'
            timestampInicio = datetime.now()
            temp = subprocess.run(cmd+ ' ' + '-u' + ' ' + urls[i] + ' ' + final_args)
            timestampFinal = datetime.now()
            duracao=timestampFinal-timestampInicio
            new_data={
                "start_timestamp": timestampInicio,
                "final_timestamp": timestampFinal,
                "duration_minutes" : duracao.min
            }  
            filename= urls[i] + '-' + k + '.json'
            with open(filename,'r+') as file:
                file_data = json.load(file)
                file_data["infos"].append(new_data)
                file.seek(0)
                json.dump(file_data, file, indent = 4)
            sleep(120)
            if k==3:
                i+=1
                k=1
  

    
urls = list(open('lista_cidades.txt'))
for i in range(len(urls)):
    urls[i] = urls[i].strip('\n')

wapiti(urls)

