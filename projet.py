import random as rd # noqa
import json
from textblob import TextBlob
import re

with open("aitweets.json", 'r', encoding='utf-8') as file_json:
    jeu_tweets = json.load(file_json)


# Listes des lettres maj et min et les chiffres, qu'on utilisera pour détecter un caractère non-alphanumérique

lang_not_ascii = ["und", "fa", "ja", "ar", "ko"]

list_nb = [str(i) for i in range(0, 10)]
list_min = [chr(i) for i in range(65, 91)]
list_maj = [chr(i) for i in range(97, 123)] + ["-", "_"]

# Stockage dans zone d'atterissage :


def zone_atterissage(dict):
    tweet = dict["TweetText"]
    new_tweet = tweet.replace("\n\n", " ").replace("\n", " ")
    tweet_nettoye = re.sub(r'[^\w\s.,!?;:()"^`@#/-]', ' ', new_tweet)
    dict["TweetText"] = tweet_nettoye
    return dict


'''

with open("zone_d'atterissage.json", "w",encoding='utf-8') as zone_att:
    data = jeu_tweets
    for tweet in data:
        tweet = zone_atterissage(tweet)
    json.dump(data, zone_att,indent=2)

'''


with open("zone_d'atterissage.json", "r", encoding='utf-8') as fichier:
    donnees = json.load(fichier)


# Création de notre liste des différents auteurs :


'''

creation_autor =[]
l_temp = []
l_temp.append(list_maj)
l_temp.append(list_min)


for i in range(200) :
    j = rd.randint(4,11)
    temp = ""
    for k in range(j) :
        t = rd.choice(l_temp)
        c = rd.choice(t)
        temp += c
    creation_autor.append(temp)

'''

# Résultat de notre code au-dessus :

creation_autor = ['bQoBTcaoGF', 'nvWLmLP', 'LbZzWfDZL_J', 'XHOk', 'KSkjXifu', 'td_uXWCZVc', 'nCNYrE', 'cwOnU', 'OoqE-Jn', 'RDuj', 'RNOmpKu_lW', 'EVwnLaUO', 'jbBheKHP',
                  'KQDaMDU', 'UrxlM', 'LsiMhk', 'xGvBpvfX', 'BBXyUra', 'qWI_CZdxcQ', 'UdgIO-AhaZ', 'ifbCjF', 'Eg_spzD', 'vaoDg', 'SNUvK', 'FtMxILoSV', '-EAMxOYM', '-gEakGDX_',
                  'nguYCjiuu', 'vOAnZd', 'CVhDukeJyD', 'HbAVnjQ', 'RUMDk', 'rrGisAeWr', 'RkxSl-p_MTl', 'bFtt', 'xKVk', 'MaeDgycAi', 'jdoPV', 'InXuiS', 'fLtRgcspWio',
                  'GAhiPQW', 'nLNs_OR', 'Andze', 'bIgt', 'IoIy', 'XKEuj', 'AkUMCgGZ', 'kA-kUsolJJQ', 'ttdkvVdZ', 'dxWRRDmAbma', 't-SlYwRap', 'KxAbMB', 'sgDQx', 'BmXxVLNW', 'dqCXuk', 'gQ-T',
                  'ImYR', 'EWktbLHU', 'ydCeh', 'TbvL', 'jOhEZIg', 'lKTDRNKrUHh', 'BvvArd', 'sMZMytB', 'l-JqIY', 'mLZfvZRxT', 'slcbkwTtRYx', 'aOmVMx', 'JEkx', 'alKpczQ', 'roPNPOu',
                  'Ic-BCXOh', 'zInV', 'EcSYgj', 'Tt_m', 'tMMJXl', 'eFwuGW', 'eLbQFGR', 'vwTZ_FjbnN', 'owNOfEJsS', 'fvVXS', 'ZTvXRBpyb_', 'PbDDtxkShP', 'q_PdBNV', 'W-cka', 'xXgYOdcim',
                  'kbZSvWx', 'Qpwlh', 'ZVl_BJDHIW', 'kxgqyeDSPH', 'EjvTiaovQq', 'eGZv', 'vfgIl', 'XGpvCL_JKi', 'SVIS', 'wpvV-yaqd', 'DVMyGe', 'ViQrZQddkV', 'cmeuEJxPuN', 'CJfJGNkO',
                  'oS_gSU_-', 'ROAxw', 'sVHKHo', 'lskVug', 'yrHmcdeEqd', 'LBNksKv', '-JlyHvyZR', 'BHaUEm_nYaZ', 'sCgudeDyx', 'f-BDzNxq', 'HLI_IM', 'uVVPE', 'DHjRxj', 'nj-x-YO',
                  'YJdOld', 'FDKC', 'CeDR_KRa_n', 'E-RymAXdG', 'HcAhcJIyTZ', 'cOFPMmRMUOV', 'gkUva', 'yKqKL', 'CIqCKbyaKZD', 'kBGv', 'ENDNX', 'NEnXLWFTAy', 'sHirz-qB', 'yWHHaOi',
                  'hHUhxwlFTl', 'FnqN', 'OgtVXXjG', 'BUSdoVDqE', '-eVC', 'fpBStDcvV', 'HgFO', 'GIVwz', 'mBBnCVrRCf', 'JQXeThDiX', 'dDYAIXg-HX', 'rEHUe', 'ClN-FiOMW', 'ysrxvPWcn',
                  'UYBA', 'UXdM', 'aKtalHEVBpa', 'ZOTPWCt', 'YFWt', 'hoFYHGv', 'cZbXxiMSIhh', 'kFVWu_yrv', 'IHzXR', 'aRfxi', 'E-pI', 'rSVEXP', 'MyTrInLrbRe', 'rEWzWyhhuK',
                  'Asp-rtjyYC', 'tRJCQUMu', 'frWeeerEaM', 'FAcQwf', 'nGxkX', 'eDQFdAbFgcN', 'WA_qIaoRW', 'MyxKrj-Y', 'XVtO', 'wVplcKaZR', 'SJZbkiqQVd', 'TqMUdFJFQ', 'WBwWrlp',
                  'XBrdhy_M', 'QENk', 'HGil', 'cDLutGaEjeg', 'LVAdh', 'LUVVicKQ', 'GWyUX', 'haIen', 'nhrLpLGwG', 'stGisQXTgo_', 'PLELwexzOo', 'vANIN', 'dZFDq', 'TIKxWN', 'yKgyqpf',
                  'AWdnrz', 'nwpno', 'RrOx', 'qQiS', 'jf_MJHUKPLE', 'ebK-Wus', 'wApb', 'mB-QpawgcHH', 'uEeqD_GbEcT', 'bfcHeMMr', 'omAjKQ', 'ytYIFh', 'qvLIZfO', 'niicEgxDTo',
                  'eeDMgzLP', 'rych']


# Ajout des auteurs à chaque dictionnaire d'un tweet et ajout dans le fichier json d'une clé "Autor"
#  avec comme valeur l'auteur attribué:

'''

for dic in donnees :
    autor_temp = rd.choice(creation_autor)
    dic["Autor"] = autor_temp



with open("aitweets.json","w",encoding='utf-8') as fjson :
    json.dump(donnees,fjson)

'''


# Opérations de traitements :

# Identification de l'auteur :

liste_autor = []

for dic in donnees:
    liste_autor.append(dic["Autor"])

# Extraire la liste des hashtags de la publication :


def liste_hashtags(dict):  # on prend notre liste de data en argument avec la ligne que l'on veut
    tweet = dict['TweetText']
    liste_h = []  # On initialise la liste qui va contenier les différents hashtags ou pas
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
                    if temp != 1 and elmnt != "#…":  # Sinon, je ne suis pas rentrer dans la liste càd pas de caractère spécial dans le mot contenant le hashtag
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
                            if temp == 2:  # Si temp == 2 , alors je suis rentré dans le if
                                liste_h.append(hash_final[0].lower())  # On append donc le 1er élément du split car notre hashtag n'est précédé par d'autres caractères donc le split se fera au premier chr spécial qui arrivera apres le hashtag
                            if temp != 2:  # Sinon, je ne suis pas rentrer dans la liste càd pas de caractère spécial dans le mot contenant le hashtag
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
                    if temp != 1 and elmnt != "@…":
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
        sentiment += "+"
    elif round(polarity, 2) < (0.00):
        sentiment += "-"
    else:
        sentiment += "0"
    return sentiment


# Création de 2 listes contenant respectivement tous les hashtags et toutes les mentions de chaque publication


liste_hash = []
liste_ment = []

for dic in donnees:
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


# Opérations analyse de données :

# TopK des hashtags :

dicK_hashtags = {}  # Initialisation d'un dictionnaire qui contiendra touts les différents hashtags avec leur nombre d'occurences
for elt in liste_hash:  # On parcoure notre liste contenant tous les hastags de chaque publication
    for h in elt:  # On parcoure les hashtags un à un des publications
        if h not in dicK_hashtags:  # On teste si le hashtags n'est pas déjà dans les clés du dictionnaire
            dicK_hashtags[h] = 1  # Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
        else:
            dicK_hashtags[h] += 1  # Sinon, on ajoute +1 à l'occurence du hashtag déjà existant

dicK_hashtags = dict(sorted(dicK_hashtags.items(), key=lambda item: item[1], reverse=True))  # Trier le dictionnaire avec les hashtags par ordre décroissant


def topK_hashtags(k):
    top = list(dicK_hashtags.items())  # On créé une liste contenant les items du dictionnaire
    while k > len(top):  # On teste si la valeur k donnée n'est pas supérieur au nombre d'hashtags que l'on a
        k = int(input(f"Désolé je ne peux pas t'imprimer le top {k} des hashtags car il n'y en a que {len(top)}, donne moi un nombre + petit : "))  # Si k supérieur au nombre d'hashtags alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"Voici le top {k} des hashtags qui reviennent le + souvent : \n")
    for i in range(k):
        print(f"- {i+1}) {top[i][0]} apparait {top[i][1]} fois.")  # On affiche le top K des hashtags avec le nombres d'occurences à chaque fois


'''

k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des hashtags : "))
topK_hashtags(k)

'''

# TopK des mentions :

dicK_mentions = {}  # Initialisation d'un dictionnaire qui contiendra toutes les différentes mentions avec leur nombre d'occurences
for elt in liste_ment:  # On parcoure notre liste contenant toutes les mentions de chaque publication
    for m in elt:  # On parcoure les mentions unes à unes des publications
        if m not in dicK_mentions:  # On teste si la mention n'est pas déjà dans les clés du dictionnaire
            dicK_mentions[m] = 1  # Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
        else:
            dicK_mentions[m] += 1  # Sinon, on ajoute +1 à l'occurence de la mention déjà existante

dicK_mentions = dict(sorted(dicK_mentions.items(), key=lambda item: item[1], reverse=True))  # Trier le dictionnaire avec les mentions par ordre décroissant


def topK_mentions(k):
    top = list(dicK_mentions.items())  # On créé une liste contenant les items du dictionnaire
    while k > len(top):  # On teste si la valeur k donnée n'est pas supérieur au nombre de mentions que l'on a
        k = int(input(f"Désolé je ne peux pas t'imprimer le top {k} des mentions car il n'y en a que {len(top)}, donne moi un nombre + petit : "))  # Si k supérieur au nombre de mentions alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"Voici le top {k} des mentions qui reviennent le + souvent : \n")
    for i in range(k):
        print(f"- {i+1}) {top[i][0]} apparait {top[i][1]} fois.")  # On affiche le top K des mentions avec le nombres d'occurences à chaque fois


'''

k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des mentions : "))
topK_mentions(k)

'''

# Top k utilisateurs :

dicK_users = {}  # Initialisation d'un dictionnaire qui contiendra touts les différentes users avec leur nombre d'occurences
for user in liste_autor:  # On parcoure notre liste contenant les users de chaque publication
    if user not in dicK_users:  # On teste si l'user n'est pas déjà dans les clés du dictionnaire
        dicK_users[user] = 1  # Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
    else:
        dicK_users[user] += 1  # Sinon, on ajoute +1 à l'occurence du user déjà existant

dicK_users = dict(sorted(dicK_users.items(), key=lambda item: item[1], reverse=True))  # Trier le dictionnaire avec les users par ordre décroissant


def topk_users(k):
    top = list(dicK_users.items())  # On créé une liste contenant les items du dictionnaire
    while k > len(top):  # On teste si la valeur k donnée n'est pas supérieur au nombre de mentions que l'on a
        k = int(input(f"Désolé je ne peux pas t'imprimer le top {k} des utilisateurs car il n'y en a que {len(top)}, donne moi un nombre + petit : "))  # Si k supérieur au nombre de mentions alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"Top {k} des utilisateurs qui reviennent le + souvent : \n")
    for i in range(k):
        print(f"- {i+1}) {top[i][0]} apparait {top[i][1]} fois.")  # On affiche le top K des mentions avec le nombres d'occurences à chaque fois


'''

k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des utilisateurs : "))
topk_users(k)

'''

# Le dictionnaire avec les hashtags, les utilisateurs regroupe leur nombres
# de publication chacun,
# alors on a déjà le nombre de publications par hashatgs, utilisateurs.

# L'ensemble des tweets mentionnant un utilisateur spécifique :

tweets_mentions = {}

for tweet in donnees:
    temp = ""
    if liste_mentions(tweet) != []:
        for elt in liste_mentions(tweet):
            if liste_mentions(tweet).count(elt) == 1:
                if elt not in tweets_mentions:
                    tweets_mentions[elt] = []
                    tweets_mentions[elt].append(tweet['TweetText'])
                else:
                    tweets_mentions[elt].append(tweet["TweetText"])
            else:
                if temp != elt:
                    if elt not in tweets_mentions:
                        tweets_mentions[elt] = []
                        tweets_mentions[elt].append(tweet['TweetText'])
                    else:
                        tweets_mentions[elt].append(tweet["TweetText"])
                temp = elt


'''
²
# Test :

for elt in tweets_mentions:
    for tweet in tweets_mentions[elt] :
        if tweets_mentions[elt].count(tweet) != 1 :
            print(tweet,False)

'''


# L'ensemble des tweets d'un utilisateur spécifique:

tweets_users = {}

for tweet in donnees:
    if tweet["Autor"] not in tweets_users:
        tweets_users[tweet["Autor"]] = []
        tweets_users[tweet["Autor"]].append(tweet["TweetText"])
    else:
        tweets_users[tweet["Autor"]].append(tweet["TweetText"])

'''

# Test :

l = []
for dict in donnees :
    if dict["Autor"] == "gkUva" :
        l.append(dict["TweetText"])

print(tweets_users["gkUva"] == l)

'''

# Utilisateurs mentionnant un hashtag spécifique :

tweets_mentions = {}

for tweet in donnees:
    if liste_hashtags(tweet) != []:
        for elt in liste_hashtags(tweet):
            if elt not in tweets_mentions:
                tweets_mentions[elt] = []
                tweets_mentions[elt].append(tweet['Autor'])
            else:
                if tweet["Autor"] not in tweets_mentions[elt]:
                    tweets_mentions[elt].append(tweet["Autor"])

'''

# Test :

ltest = []

for dict in donnees:
    if "#ai" in liste_hashtags(dict):
        if dict["Autor"] not in ltest:
            ltest.append(dict["Autor"])

for elt in tweets_mentions["#ai"]:
    if elt not in ltest:
        print(False)

ltest2 = []
for autor in tweets_mentions['#ai']:
    ltest2.append(tweets_mentions['#ai'].count(autor))


for elt in ltest2:
    if elt != 1:
        print("errror")

'''


# Utilisateurs mentionnés par un utilisateur spécifique :

users_andMent = {}

for tweet in donnees:
    if tweet["Autor"] not in users_andMent:
        users_andMent[tweet["Autor"]] = []
    for mention in liste_mentions(tweet):
        if mention not in users_andMent[tweet["Autor"]]:
            users_andMent[tweet["Autor"]].append(mention)

'''

# Test :

for elt in users_andMent:
    for tweet in donnees:
        if tweet["Autor"] == elt:
            for mention in liste_mentions(tweet):
                if mention not in users_andMent[elt]:
                    print(False)

'''
