from ast import Load
import json
from textblob import TextBlob

with open("aitweets.json", 'r', encoding = 'utf-8') as file_json :
    jeu_tweet = file_json.readlines()

donnees = []
for ligne in jeu_tweet :
    tweet = json.loads(ligne)
    donnees.append(tweet)



## Extraire la liste des hashtags de la publication :

def liste_hashtags(tweet) : ## on prend le tweet en argument
    if "#" in tweet : ## Tout d'abord, on vérifie la présence d'hashtags dans la publication
        hashtag = tweet.split("#") ## Si il y en a, alors on utilise .split("#") pour séparer les mots des hashtags
        return hashtag[1:] ## On retourne la tweet à partir de l'indice 1 et non 0 car tweet[0] correspond au texte du tweet avant les hashtags
    else :
        hashtag = []
        return hashtag ## Si, au contraire il n'y en a pas, alors on renvoie une liste vide
    

## Analyser le sentiment du tweet :

def analys_feeling(tweet) :
    sentiment = ""
    tweet_blob = TextBlob(tweet)
    polarity = tweet_blob.sentiment.polarity
    if round(polarity,2) > (0.00) :
        sentiment += "+"
    elif round(polarity,2) < (0.00) : 
        sentiment += "-"
    else :
        sentiment += "0"
    return sentiment