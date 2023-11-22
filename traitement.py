import json
from textblob import TextBlob
import pandas as pd
import numpy as np

# Modules pour les topics :

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import models, corpora


with open("zone_d'atterissage.json", 'r', encoding='utf-8') as file_json:
    data = json.load(file_json)


# Listes des lettres maj et min et les chiffres, qu'on utilisera pour détecter un caractère non-alphanumérique

lang_not_ascii = ["und", "fa", "ja", "ar", "ko"]

list_nb = [str(i) for i in range(0, 10)]
list_min = [chr(i) for i in range(65, 91)]
list_maj = [chr(i) for i in range(97, 123)] + ["-", "_"]

# Opérations de traitements :

# Identification de l'auteur :

liste_autor = []

for dic in data:
    liste_autor.append(dic["Autor"])

# Extraire la liste des hashtags de la publication :


def liste_hashtags(dict):  # on prend notre liste de data en argument avec la ligne que l'on veut
    tweet = dict['TweetText']
    liste_h = []  # On initialise la liste qui va contenir les différents hashtags ou pas
    temp = 0  # Initialisation d'une variable temporaire qu'on utilisera pour traiter les hashtags

    if dict["TweetLanguage"] in lang_not_ascii:  # Si les caractères de la langue ne sont pas dans le code ASCII, alors je vais traiter différemment
        if "#" in tweet:
            split = tweet.split()
            for elmnt in split:
                if "#" in elmnt and elmnt[-1] != ":":
                    liste_h.append(elmnt)
                elif "#" in elmnt and elmnt[-1] == ":":
                    liste_h.append(elmnt[:-1])
    else:  # Si les caracteres de la langue sont dans le code ASCII
        if "#" in tweet:  # Tout d'abord, on vérifie la présence d'hashtags dans la publication
            split = tweet.split()  # Si il y en a, alors on utilise .split() pour séparer les mots du tweet
            for elmnt in split:  # On parcoure tous les mots du tweet

                if "#" in elmnt and elmnt[0] == "#":  # 1er cas, si il y a un # dans le mot, c'est un des hashtag du tweet et on va traiter les hashtags précédés d'aucun caractère avant donc il commence par "#"
                    for c in elmnt[1:]:  # On parcoure la chaîne de caractère du hashtag
                        if (c not in list_min and c not in list_maj and c not in list_nb):  # On teste si le caractère est un chiffre ou une lettre (miniscule ou majuscule)
                            temp = 1  # variable temporaire à 1 si un caractère remplit les conditions
                            hash = elmnt.split(c)  # On sépare notre mot avec split() et comme argument le caractère spécial en question pour l'enlever du hashtag
                            break  # Ainsi on stoppe la boucle for quand on l'a trouvé

                        else:
                            temp = 0

                    if temp == 1 and hash[0] != "#":  # Si temp == 1 alors on est passé dans le if et on a split, la deuxième condition ne prends les hashtags tout seul sans mot après
                        liste_h.append(hash[0].lower())  # On append donc le 1er élément de la liste (split) car notre hashtag n'est précédé par d'autres caractères (car le split se fera au premier chr spécial qui arrivera apres le hashtag)
                    if temp != 1 and elmnt != "#":  # Sinon, je ne suis pas rentrer dans la liste càd pas de caractère spécial dans le mot contenant le hashtag
                        liste_h.append(elmnt.lower())  # On l'append (à noter qu'on utilise lower() pour que les hashtags soit tous en miniscules et qu'on puisse les comparer facilement)

                elif "#" in elmnt and elmnt[0] != "#":  # Deuxième cas, si le mot contient un "#" mais qu'il ne commence pas par ce dernier donc par un caractère spe tel que , ou par une parenthèse etc
                    for c in elmnt:  # On parcoure chaque caractère du mot
                        if c == "#":  # On teste si le caractère correspond au hashtag
                            i = elmnt.index(c)  # Si oui, alors je prends son indice dans le mot avec index()
                            hash2 = elmnt.split(elmnt[i-1])  # Et je split au caractère juste avant pour le séparer du hashtag
                            break  # Je stoppe ma boucle si je l'ai trouvé
                    for h in hash2:  # Ensuite je parcoure ma liste split pour faire comme dans le 1er cas càd dans spliter si le hashtag est suivi d'un caractère spécial que je ne veux pas
                        if "#" in h:  # On teste si l'élément dans ma liste corresponds au hashtag
                            for c in h:  # Si oui alors je parcours chaque caractère du mot
                                if c not in list_min and c not in list_maj and c not in list_nb and c != "#":  # Le if ici est pour savoir si le hashtag est suivi d'un caractère spécial, et on vérifie que ce caractère n'est pas un hashtag
                                    temp = 2  # Si oui, variable temp à 2
                                    hash_final = h.split(c)  # Et je split au caractère spécial
                                    break  # Je stoppe une fois le caractère trouvé
                                else:
                                    temp = 0
                            if temp == 2 and hash_final[0] != "#":  # Si temp == 2 , alors je suis rentré dans le if
                                liste_h.append(hash_final[0].lower())  # On append donc le 1er élément du split car notre hashtag n'est précédé par d'autres caractères donc le split se fera au premier chr spécial qui arrivera apres le hashtag
                            if temp != 2 and h != "#":  # Sinon, je ne suis pas rentrer dans la liste càd pas de caractère spécial dans le mot contenant le hashtag
                                liste_h.append(h.lower())  # On l'append normalement

    return liste_h


# Extraire la liste des mentions de la publication :


def liste_mentions(dict):
    tweet = dict['TweetText']
    liste_m = []
    temp = 0

    if dict["TweetLanguage"] in lang_not_ascii:
        if "@" in tweet:
            split = tweet.split()
            for elmnt in split:
                if "@" in elmnt and elmnt[-1] != ":":
                    liste_m.append(elmnt)
                elif "@" in elmnt and elmnt[-1] == ":":
                    liste_m.append(elmnt[:-1])
    else:
        if "@" in tweet:
            split = tweet.split()
            for elmnt in split:

                if "@" in elmnt and elmnt[0] == "@":
                    for c in elmnt[1:]:
                        if (c not in list_min and c not in list_maj and c not in list_nb):
                            temp = 1
                            mention = elmnt.split(c)
                            break
                        else:
                            temp = 0

                    if temp == 1 and mention[0] != "@":
                        liste_m.append(mention[0])
                    if temp != 1 and elmnt != "@":
                        liste_m.append(elmnt)

                elif "@" in elmnt and elmnt[0] != "@":
                    for c in elmnt:
                        if c == "@":
                            i = elmnt.index(c)
                            mention2 = elmnt.split(elmnt[i-1])
                            break
                    for m in mention2:
                        if "@" in m:
                            for c in m:
                                if c not in list_min and c not in list_maj and c not in list_nb and c != "@":
                                    temp = 2
                                    ment_final = m.split(c)
                                    break
                                else:
                                    temp = 0

                            if temp == 2:
                                liste_m.append(ment_final[0])
                            if temp != 2:
                                liste_m.append(m)

    return liste_m


# Analyser le sentiment du tweet :


def analys_feeling(tweet):
    sentiment = ""
    tweet_blob = TextBlob(tweet)
    polarity = tweet_blob.sentiment.polarity
    if round(polarity, 2) > (0.00):
        sentiment = "positif"
    elif round(polarity, 2) < (0.00):
        sentiment = "négatif"
    else:
        sentiment = "neutre"
    return sentiment


# Création de 2 listes contenant respectivement tous les hashtags et toutes les mentions de chaque publication


liste_hash = []
liste_ment = []

for dic in data:
    liste_hash.append(liste_hashtags(dic))
    liste_ment.append(liste_mentions(dic))

# Test pour liste hashtag et liste mention :

'''

for elt in liste_hash :
    for c in elt :
        if c[-1] not in list_maj and c[-1] not in list_min and c[-1] not in list_nb:
            print(elt,liste_hash.index(elt))


for elt in liste_ment :
    for h in elt :
        for c in h[1:] :
            if c not in list_maj and c not in list_min and c not in list_nb :
                print(h,liste_ment.index(elt))

'''

# Création d'une liste contenant le sentiment positif ou négatif pour chaque tweet :

sentiment = []

for tweet in data:
    sentiment.append(analys_feeling(tweet["TweetText"]))


# Extraction des topics :

# Téléchargement des données nécessaires pour le module nltk :

nltk.download('stopwords')
nltk.download('punkt')


all_stopwords = {}  # Dict qui contiendra touts les différents stopwords des différentes langues
all_lang = []  # Liste qui contiendra toutes les langues des tweets

for tweet in data:
    if tweet["TweetLanguage"] not in all_lang:
        all_lang.append(tweet["TweetLanguage"])

'''

all_lang = ['en', 'in', 'es', 'und', 'pt', 'it', 'fr', 'fa', 'ja', 'ca', 'ro', 'da', 'fi', 'ar', 'ko', 'de']

'''

# Création du dict all_stopwords avec tous les stopwords selon les langues :

for lang in all_lang:
    if lang == "en":
        all_stopwords["en"] = set(stopwords.words('english'))
    if lang == "ca":
        all_stopwords["ca"] = set(stopwords.words('english'))
    if lang == "ro":
        all_stopwords["ro"] = set(stopwords.words('english'))
    if lang == "in":
        all_stopwords["in"] = set(stopwords.words('indonesian'))
    if lang == "es":
        all_stopwords["es"] = set(stopwords.words('spanish'))
    if lang == "pt":
        all_stopwords["pt"] = set(stopwords.words('portuguese'))
    if lang == "it":
        all_stopwords["it"] = set(stopwords.words('italian'))
    if lang == "fr":
        all_stopwords["fr"] = set(stopwords.words('french'))
    if lang == "da":
        all_stopwords["da"] = set(stopwords.words("danish"))
    if lang == "und":
        all_stopwords["und"] = set(stopwords.words("english"))
    if lang == "ja":
        all_stopwords["ja"] = set(stopwords.words("english"))
    if lang == "fi":
        all_stopwords["fi"] = set(stopwords.words("finnish"))
    if lang == "ar":
        all_stopwords["ar"] = set(stopwords.words("arabic"))
    if lang == "de":
        all_stopwords["de"] = set(stopwords.words("german"))

for key in all_stopwords.keys():  # ajout des mentions pour ne pas les confondre avec les topics
    for line in liste_ment:
        for m in line:
            if m not in all_stopwords[key]:
                all_stopwords[key].add(m[1:].lower())
    all_stopwords[key].add("rt")  # ajout de qqles mots qui ne sont pas des topics
    all_stopwords[key].add("https")
    all_stopwords[key].add("read")
    all_stopwords[key].add("via")

# Les stopwords sont des mots couramment utilisés qui sont généralement supprimés dans le traitement
# du langage naturel car ils ne portent pas une signification importante, ici on les importe dans une liste contenant touts les stopwords dans différentes langues


def preprocess_text(text, stop_words):  # fonction de prétraitement de texte en utilisant la bibliothèque NLTK en Python.
    words = word_tokenize(text)  # divise le texte en mots (tokens) avec la variable la fonction word_tokenize de NLTK
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]  # créer une liste en appliquant les transformations .lower() et .isalpha() (vérifie si le mot est composé uniquement de caractères alphabétiques)
    return words  # retourne une chaîne sans les stopwords


def extract_topics(tweet):
    liste_t = []
    if tweet["TweetLanguage"] != "ko" and tweet["TweetLanguage"] != "fa":  # le corréen et le persan ne sont pas dans le module nltk

        tweet_traitée = preprocess_text(tweet["TweetText"], all_stopwords[tweet["TweetLanguage"]])
        if tweet_traitée != []:
            temp = []
            temp.append(tweet_traitée)  # On traite le tweet et on l'ajoute à une liste

            dico = corpora.Dictionary(temp)
            corpus = [dico.doc2bow(text) for text in temp]
            lda_model = models.LdaModel(corpus, num_topics=1, id2word=dico, passes=30)
            topics = lda_model.show_topics(formatted=False)

            for elt in topics[0][1]:
                liste_t.append(elt[0])
    return liste_t


# On fait une fct maj_topics qui s'activera dans collecte data si un tweet est rajouté (voir maj_data), on charge le résultat dans un fichier json la 1ère fois et on le récupère après à chaque fois 
# sans réexécuter notre code qui prends beaucoup de temps donc le code s'exécutera + vite et il prendra du temps que si un tweet est rajouté :


def maj_topics():
    extract = []
    for tweet in data:
        extract.append(extract_topics(tweet))
    
    liste_temp = []
    for ligne in extract:
        for elt in ligne:
            if elt not in liste_temp:
                t = 0
                for ligne in extract:
                    t += ligne.count(elt)
                x = (elt, t)
            liste_temp.append(x)

    topics = []
    for elt in set(liste_temp):
        if elt[1] > 10:
            topics.append(elt[0])


    liste_final = []
    for tweet in data:
        tp = []
        for elt in extract_topics(tweet):
            if elt in topics:
                tp.append(elt)
            liste_final.append(tp)

    with open("topics.json","w") as f:
        all_topics = []
        for elt in liste_final:
            dico = {}
            dico[liste_final.index(elt)] = elt
            all_topics.append(dico)
    
        json.dump(contenu,f)



with open("topics.json",'r') as fjson:
    contenu = json.load(fjson)

liste_topics = []
for top in contenu:
    liste_topics.append(top[f"{contenu.index(top)}"])


df = pd.DataFrame(columns=["Autor", "Hashtags", "Mentions", "Sentiment", "Topics"],
                  index=[np.arange(1, len(data)+1)])


for i in range(0, df.shape[0]):
    df.iloc[i]["Autor"] = liste_autor[i]
    if liste_hash[i] != []:
        temp = ""
        for elt in liste_hash[i]:
            if elt == liste_hash[i][-1]:
                temp += elt
            else:
                temp += elt + ", "

        df.iloc[i]["Hashtags"] = temp
    if liste_ment[i] != []:
        temp = ""
        for elt in liste_ment[i]:
            if elt == liste_ment[i][-1]:
                temp += elt
            else:
                temp += elt + ", "

        df.iloc[i]["Mentions"] = temp
    if liste_topics[i] != []:
        temp = ""
        for elt in liste_topics[i]:
            if elt == liste_topics[i][-1]:
                temp += elt
            else:
                temp += elt + ", "

        df.iloc[i]["Topics"] = temp
    df.iloc[i]["Sentiment"] = sentiment[i]
