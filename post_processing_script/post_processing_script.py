import glob
import json
import csv

# Part 1 - additional information csv
additional_data = []
dir = 'exp_data'
files = glob.glob( dir + '/*', recursive=True)

for single_file in files:
  with open(single_file, 'r') as f:
    json_file = json.load(f)
    additional_data.append([
    json_file["infos"]["exp_round"],
    json_file["infos"]["city"],
    json_file["infos"]["target"],
    json_file["infos"]["start_timestamp"],
    json_file["infos"]["final_timestamp"],
    json_file["infos"]["duration"],
    json_file["infos"]["scope"],
    json_file["infos"]["crawled_pages_nbr"]
    ])

# Sort the data
additional_data.sort()

# Add headers
additional_data.insert(0, ['exp_round', 'city', 'url', 'start_timestamp', 'final_timestamp', 'duration', 'scope', 'crawled_pages'])

with open('additional_info.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(additional_data)

print("Additional information csv updated")

# Part 2 - vulnerabilities data

def add_vulnerabilities_to_list(name_dicts_vul,json_file,vul_data):
    previous_vul = {}
    for vul_cat in name_dicts_vul: # percorrendo todos os nomes de dicionários de vulnerabilidade
                file_dict = json_file[vul_cat] # pegando o dicionário correspondente ao nome da categoria de vulnerabilidade
                for vul_key in file_dict: # percorrendo cada chave dentro de cada dicionário de categoria de vulnerabilidades
                    vul_value = file_dict[vul_key] # pegando as listas de vulnerabilidades dentro de cada chave do dicionário
                    if len(vul_value)!=0: # se existir vulnerabilidade
                        for vul_el in vul_value: # para cada lista de vulnerabilidades        
                            vul_to_append = [
                                json_file["infos"]["city"],
                                json_file["infos"]["target"],
                                vul_key,
                                json_file["owasp_classification"][vul_key],
                                vul_el["info"],
                                vul_el["path"]
                               ]
                            exist_count = vul_data.count(vul_to_append)
                            if exist_count==0:
                                vul_data.append(vul_to_append)


vul_data=[]
for single_file in files:
  with open(single_file, 'r') as f:
    json_file = json.load(f)
    name_dicts_vul = ["vulnerabilities","anomalies","additionals"]
    add_vulnerabilities_to_list(name_dicts_vul,json_file,vul_data)

# Sort the data
vul_data.sort()

# Add headers
vul_data.insert(0, ['city', 'url', 'vul_category', 'vul_classification_owasp', 'vul_info', 'path'])

with open('vul_data.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(vul_data)

print("Vulnerabilities data csv updated")

