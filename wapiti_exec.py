import subprocess  
from time import sleep
from datetime import datetime

def wapiti(urls):
    cmd = 'wapiti'
    i=0
    len_urls=len(urls)
    while(i<len_urls):
        for k in range(1,4):
            final_args='-f json -o ~/'+ urls[i] + '-' + k + '.json' + ' --flush-attacks'
            timestampInicio = datetime.now()
            temp = subprocess.run(cmd+ ' ' + '-u' + ' ' + urls[i] + ' ' + final_args)
            timestampFinal = datetime.now()
            duracao=timestampFinal-timestampInicio
            duracaoMin=duracao.min
            nomeArquivoDuracao=urls[i]+'-'+k+'-duracao'+'.txt'  # Talvez colocar esse dado no json logo
            with open(nomeArquivoDuracao, 'w') as writer:
                writer.write(duracaoMin)
            sleep(120)
            if k==3:
                i+=1
                k=1
  

    
urls = list(open('lista_cidades.txt'))
for i in range(len(urls)):
    urls[i] = urls[i].strip('\n')

wapiti(urls)