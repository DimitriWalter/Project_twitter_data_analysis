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
        liste_h = [] ## initialise la liste qui va contenier les différents hashtags
        split = tweet.split() ## Si il y en a, alors on utilise .split() pour séparer les mots du tweet
        for elmnt in split : ## On parcoure tous les éléments
            if "#" in elmnt : ## Si il y a un # dans un élément cela signifie que c'est un des hashtag du tweeet
                liste_h.append(elmnt) ## J'ajoute alors mon élément contenant le hashtag à ma liste
        return liste_h ## je retourne ma liste contenant la liste des hashtags
    else :
        liste_h = []
        return liste_h ## Si, au contraire il n'y en a pas, alors on renvoie une liste vide

        
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