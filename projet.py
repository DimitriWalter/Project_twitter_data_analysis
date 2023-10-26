from ast import Load
import json
from textblob import TextBlob

with open("aitweets.json", 'r', encoding = 'utf-8') as file_json :
    jeu_tweet = file_json.readlines()

donnees = []
for ligne in jeu_tweet :
    tweet = json.loads(ligne)
    donnees.append(tweet)

list_nb = [str(i) for i in range(0,10)]
list_maj = [chr(i) for i in range(65,91)]
list_min =  [chr(i) for i in range(97,123)]


## Extraire la liste des hashtags de la publication :

def liste_hashtags(tweet) : ## on prend le tweet en argument
    s = 0
    listez = []
    liste_h = [] ## initialise la liste qui va contenier les différents hashtags ou pas
    if "#" in tweet : ## Tout d'abord, on vérifie la présence d'hashtags dans la publication
        split = tweet.split() ## Si il y en a, alors on utilise .split() pour séparer les mots du tweet
        for elmnt in split : ## On parcoure tous les éléments
            if "#" in elmnt and elmnt[0] == "#" : ## Si il y a un # dans un élément cela signifie que c'est un des hashtag du tweet
                for c in elmnt[1:] :
                    if c not in list_min and c not in list_maj and c not in list_nb :
                        s = 1
                        hash = elmnt.split(c)
                    if s == 1 :
                        liste_h.append(hash[0])
                if s == 0 :
                    liste_h.append(elmnt.lower())
            elif "#" in elmnt and elmnt[0] != "#" :
                for chr in elmnt :
                    pass
    return liste_h



## Extraire la liste des mentions de la publication :

def liste_mentions(tweet) :
    liste_m = []
    if "@" in tweet :
        split = tweet.split()
        if split[0] == "RT" :
            liste_m.append(split[1][:-1])
            for elt in split[2:] :
                if "@" in elt :
                    liste_m.append(elt)
        else : 
            for elt in split :
                if "@" in elt :
                    liste_m.append(elt)
        return liste_m
    else :
        return liste_m


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


liste_hash = []
liste_ment = []
for i in range(len(donnees)) : 
    liste_hash.append(liste_hashtags(donnees[i]["TweetText"]))
    liste_ment.append(liste_mentions(donnees[i]["TweetText"]))

for elt in liste_hash :
    for c in elt : 
        if "#" in c and c[0] != "#" :
            print(elt,liste_hash.index(elt))
'''
for elt in liste_ment :
    for h in elt :
        for i in range(65,91) :
            if h[-1] == chr(i) or h[-1] == chr(i+22) or h[-1] == "0" or h[-1] == "1" or h[-1] == "2" or h[-1] == "3" or h[-1] == "4" or h[-1] == "5" or h[-1] == "6" or h[-1] == "7" or h[-1] == "8" or h[-1] == "9"   :
                s = 1
                break
            else : 
                s= 0
        if s == 0 :
            print(h,liste_ment.index(elt))


list_temp = []
list_count = []
dicK_hashtags = {}
for elt in liste_hash :
    if elt != [] :
        for h in elt :
            if h not in list_temp :
                list_temp.append(h)
                list_count.append(1)
            else :
                i = list_temp.index(h)
                list_count[i] += 1

'''
def topK_hashtags(k) :
    pass