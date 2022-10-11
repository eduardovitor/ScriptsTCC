import glob
import json
import csv

# Part 1 - additional information csv
data = []
dir = 'exp_data'
files = glob.glob( dir + '/*', recursive=True)

for single_file in files:
  with open(single_file, 'r') as f:
    json_file = json.load(f)
    data.append([
    json_file["infos"]["exp_round"],
    json_file["infos"]["city"],
    json_file["infos"]["target"],
    json_file["infos"]["start_timestamp"],
    json_file["infos"]["final_timestamp"],
    json_file["infos"]["scope"],
    json_file["infos"]["crawled_pages_nbr"]
    ])

# Sort the data
data.sort()

# Add headers
data.insert(0, ['exp_round', 'city', 'url', 'start_timestamp', 'final_timestamp', 'duration', 'scope', 'crawled_pages'])

with open('additional_info.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Additional information csv updated")
