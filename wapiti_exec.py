import subprocess  
from time import sleep
from datetime import datetime

def wapiti(urls):
    cmd = 'wapiti'
    i=0
    len_urls=len(urls)
    while(i<len_urls):
        for k in range(0,3):
            if(k==1):
                final_args='-f csv -o ~/'+urls[i]+'.csv'+' --flush-attacks'
            else:
                final_args='-f csv -o ~/'+urls[i]+'.csv'
            timestampInicio = datetime.now()
            temp = subprocess.run(cmd+ ' ' + '-u' + ' ' + urls[i] + ' ' + final_args)
            timestampFinal = datetime.now()
            duracao=timestampFinal-timestampInicio
            duracaoMin=duracao.min
            nomeArquivoDuracao=urls[i]+'-'+(k+1)+'-duracao'+'.txt'  # Talvez colocar esse dado no csv logo
            with open(nomeArquivoDuracao, 'w') as writer:
                writer.write(duracaoMin)
            sleep(120)
            if k==2:
                i+=1
                k=0
  

    
urls = list(open('lista_cidades.txt'))
for i in range(len(urls)):
    urls[i] = urls[i].strip('\n')

outputlist=wapiti(urls)