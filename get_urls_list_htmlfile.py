
from bs4 import BeautifulSoup

with open('resumo_dev_indice.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

urls=soup.findAll('a')
urls_cidades_fixed=[]
for url in urls:
    url_cidade=url['href']
    url_cidade=url_cidade.replace('/portal/','')
    url_cidade=url_cidade.replace('/transparencia/','')
    url_cidade=url_cidade.replace('/transparencia','')
    url_cidade=url_cidade.replace('/trans','')
    url_cidade=url_cidade.replace('/trans/','')
    url_cidade=url_cidade.replace('acesso_lai/1','')
    urls_cidades_fixed.append(url_cidade)

with open('lista_cidades.txt','w') as writer:
    for url in urls_cidades_fixed:
        writer.write(url+'\n')

