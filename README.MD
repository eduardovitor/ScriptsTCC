
# Análise de vulnerabilidades dos portais web das câmaras municipais alagoanas


## 📖 Descrição

Esse projeto foi o meu trabalho de conclusão de curso da graduação de Sistemas de Informação do Ifal Campus Arapiraca. Trata-se de uma análise de vulnerabilidades dos sites das câmaras municipais alagoanas (100 sites no total). Em resumo, verifiquei o nível de segurança de tais sites expondo as vulnerabilidades (fraquezas) encontradas conforme classificação da [OWASP 2021](https://owasp.org/Top10/pt_BR/).


## 📁 Estrutura de arquivos

- ```/exp-automation```: Diretório com códigos referentes a descrição da infraestrutura de máquinas na nuvem ([Terraform](https://www.terraform.io/)). Além disso, possui código referente a automação da configuração e execução ([Ansible](https://www.ansible.com/)) da ferramenta de detecção de vulnerabilidades nas máquinas;

- ```/extractors```: Diretório com códigos usados para extração das URLs das câmaras municipais e dos nomes das cidades;

- ```/post_processing_script```: Diretório com um arquivo de código usado para geração de um csv de análise a partir dos arquivos json de relatório de vulnerabilidades gerado pela ferramenta;

- ```/R_analysis```: Diretório com um arquivo R markdown usado para análise dos dados do csv com as vulnerabilidades;

- ```/tests```: Diretório com arquivos usados para testes manuais de código;

- ```/wapiti_containers_script```: Diretório que contém arquivos que seriam usados para execução da ferramenta de detecção de vulnerabilidades em containers [Docker](https://www.docker.com/);

- ```/wapiti_execution```: Diretório com dois arquivos referentes a scripts de automação de execução da ferramenta para coleta dos dados das vulnerabilidades. O que diferencia os dois é a forma de passar parâmetros, um utiliza variáveis de ambiente, o outro, inputs manuais.

## 📡 Tecnologias utilizadas

<div align="center"> 
<img align="left" height="30" width="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>
<img align="left" height="30" width="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ansible/ansible-original.svg"/>
<img align="left" height="30" width="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/terraform/terraform-original.svg"/>
<img align="left" height="30" width="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg"/>
<img align="left" height="30" width="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg"/>
<img align="left" height="30" width="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg"/>
  
</div>
<br/><br/>

## ⏳ Detalhes de projeto

Esse projeto foi desenvolvido usando a ferramenta de detecção de vulnerabilidades [Wapiti](https://wapiti-scanner.github.io/) e uma infraestrutura de máquinas na nuvem, além de um conjunto de tecnologias de suporte: [Python](https://www.python.org/), [Bash](https://www.gnu.org/software/bash/), [Terraform](https://www.terraform.io/), [Ansible](https://www.ansible.com/), [R](https://www.r-project.org/) e [Go](https://go.dev/). 

<br>


<br/>

## 🚀 Resumo dos resultados

O  número  total de  vulnerabilidades  encontrado  foi  de  667.  Com  relação  à proporção  de  vulnerabilidades  críticas:  81%  dos  portais  apresentaram  vulnerabilidades não   críticas,   10%   apresentaram   vulnerabilidades   críticas   e   9%   não   apresentaram vulnerabilidades.

<br/>

## 🤵🤵‍♀️ Colaboradores

Eu (Eduardo Vítor) e [Daniel Fireman](https://github.com/danielfireman) como orientador.

<br/>

## 📰 Publicações

[Análise de vulnerabilidades dos portais web das câmaras municipais alagoanas - SBSI 2023](https://sol.sbc.org.br/index.php/sbsi_estendido/article/view/24586/24407)

[Análise de vulnerabilidades dos portais web das câmaras municipais alagoanas - Brazilian Journal of Development](https://ojs.brazilianjournals.com.br/ojs/index.php/BRJD/article/view/61717/44465)

<br/>

## 🔎 Status do Projeto

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Finalizado-blue)

<br/>

## 📑 Referências

[Wapiti](https://wapiti-scanner.github.io/)

[Python](https://www.python.org/)

[Bash](https://www.gnu.org/software/bash/)

[Terraform](https://www.terraform.io/)

[Ansible](https://www.ansible.com/)

[R](https://www.r-project.org/)

[Go](https://go.dev/)