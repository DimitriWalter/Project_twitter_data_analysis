from ast import Load
import json

with open("aitweets.json", 'r', encoding = 'utf-8') as file_json :
    jeu_tweet = file_json.readlines()

donnees = []
for ligne in jeu_tweet :
    tweet = json.loads(ligne)
    donnees.append(tweet)



## Extraire la liste des hashtags de la publication :

def liste_hashtags(dict) :
    if "#" in dict['TweetText'] : ## Tout d'abord, on vérifie la présence d'hashtags dans la publication
        tweet = dict["TweetText"].split("#") ## Si il y en a, alors on utilise .split("#") pour séparer les mots des hashtags
        return tweet[1:] ## On retourne la tweet à partir de l'indice 1 et non 0 car tweet[0] correspond au texte du tweet avant les hashtags
    else :
        tweet = []
        return tweet ## Si, au contraire il n'y en a pas, alors on renvoie une liste vide
    

## Extraire la liste des mentions de la publication :

