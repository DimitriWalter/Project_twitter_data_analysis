import json

with open("aitweets.json", 'r', encoding = 'utf-8') as file_json :
    donnees = file_json.readlines()

i = 0
for ligne in donnees : 
    if i == 26 :
        print(ligne)
        break
    i += 1