import json
import traitement as td
import matplotlib.pyplot as plt


with open("zone_d'atterissage.json", 'r', encoding='utf-8') as file_json:
    data = json.load(file_json)

# Opérations analyse de données :

# TopK des hashtags :

dicK_hashtags = {}  # Initialisation d'un dictionnaire qui contiendra touts les différents hashtags avec leur nombre d'occurences
for elt in td.liste_hash:  # On parcoure notre liste contenant tous les hastags de chaque publication
    for h in elt:  # On parcoure les hashtags un à un des publications
        if h not in dicK_hashtags:  # On teste si le hashtags n'est pas déjà dans les clés du dictionnaire
            dicK_hashtags[h] = 1  # Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
        else:
            dicK_hashtags[h] += 1  # Sinon, on ajoute +1 à l'occurence du hashtag déjà existant

dicK_hashtags = dict(sorted(dicK_hashtags.items(), key=lambda item: item[1], reverse=True))  # Trier le dictionnaire avec les hashtags par ordre décroissant


def topK_hashtags():
    k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des hashtags : "))
    top = list(dicK_hashtags.items())  # On créé une liste contenant les items du dictionnaire
    l_hashtags = []
    n_hashtags = []
    for elmnt in top[:k]:
        l_hashtags.append(elmnt[0])  # création de la liste pour les valeurs en ordonnées
        n_hashtags.append(elmnt[1])  # création de la liste pour les valeurs en abscisse
    plt.bar(l_hashtags, n_hashtags)
    plt.xticks(rotation=30, ha='right')
    plt.xlabel("Hashtags")
    plt.ylabel("Nombre")
    plt.title(f"Tops {k} des hashtags : ")
    plt.subplots_adjust(bottom=0.255, top=0.93)
    plt.show()


'''

topK_hashtags()

'''

# TopK des mentions :

dicK_mentions = {}  # Initialisation d'un dictionnaire qui contiendra toutes les différentes mentions avec leur nombre d'occurences
for elt in td.liste_ment:  # On parcoure notre liste contenant toutes les mentions de chaque publication
    for m in elt:  # On parcoure les mentions unes à unes des publications
        if m not in dicK_mentions:  # On teste si la mention n'est pas déjà dans les clés du dictionnaire
            dicK_mentions[m] = 1  # Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
        else:
            dicK_mentions[m] += 1  # Sinon, on ajoute +1 à l'occurence de la mention déjà existante

dicK_mentions = dict(sorted(dicK_mentions.items(), key=lambda item: item[1], reverse=True))  # Trier le dictionnaire avec les mentions par ordre décroissant


def topK_mentions():
    k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des mentions : "))
    top = list(dicK_mentions.items())  # On créé une liste contenant les items du dictionnaire
    l_mentions = []
    n_mentions = []
    for elmnt in top[:k]:
        l_mentions.append(elmnt[0])  # création de la liste pour les valeurs en ordonnées
        n_mentions.append(elmnt[1])  # création de la liste pour les valeurs en abscisse
    plt.bar(l_mentions, n_mentions)
    plt.xticks(rotation=30, ha='right')
    plt.xlabel("Mentions")
    plt.ylabel("Nombre")
    plt.title(f"Tops {k} des Mentions : ")
    plt.subplots_adjust(bottom=0.255, top=0.93)
    plt.show()


'''

topK_mentions()

'''

# Top k utilisateurs :

dicK_users = {}  # Initialisation d'un dictionnaire qui contiendra touts les différentes users avec leur nombre d'occurences
for user in td.liste_autor:  # On parcoure notre liste contenant les users de chaque publication
    if user not in dicK_users:  # On teste si l'user n'est pas déjà dans les clés du dictionnaire
        dicK_users[user] = 1  # Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
    else:
        dicK_users[user] += 1  # Sinon, on ajoute +1 à l'occurence du user déjà existant

dicK_users = dict(sorted(dicK_users.items(), key=lambda item: item[1], reverse=True))  # Trier le dictionnaire avec les users par ordre décroissant


def topk_users():
    k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des utilisateurs : "))
    top = list(dicK_users.items())  # On créé une liste contenant les items du dictionnaire
    l_users = []
    n_users = []
    for elmnt in top[:k]:
        l_users.append(elmnt[0])  # création de la liste pour les valeurs en ordonnées
        n_users.append(elmnt[1])  # création de la liste pour les valeurs en abscisse
    plt.bar(l_users, n_users)
    plt.xticks(rotation=30, ha='right')
    plt.xlabel("Users")
    plt.ylabel("Nombre")
    plt.title(f"Tops {k} des Users : ")
    plt.subplots_adjust(bottom=0.255, top=0.93)
    plt.show()


'''

topk_users()

'''

# Top k topics :

dicK_topics = {}
for elt in td.liste_topics:
    for t in elt:
        if t not in dicK_topics:
            dicK_topics[t] = 1
        else:
            dicK_topics[t] += 1

dicK_topics = dict(sorted(dicK_topics.items(), key=lambda item: item[1], reverse=True))


def topk_topics():
    k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des topics : "))
    top = list(dicK_topics.items())
    l_topics = []
    n_topics = []
    for elmnt in top[:k]:
        l_topics.append(elmnt[0])  # création de la liste pour les valeurs en ordonnées
        n_topics.append(elmnt[1])  # création de la liste pour les valeurs en abscisse
    plt.bar(l_topics, n_topics)
    plt.xticks(rotation=30, ha='right')
    plt.xlabel("Topics")
    plt.ylabel("Nombre")
    plt.title(f"Tops {k} des Topics : ")
    plt.subplots_adjust(bottom=0.255, top=0.93)
    plt.show()


'''

topk_topics()

'''

# Le dictionnaire avec les hashtags, les utilisateurs, les topics regroupe leur nombres de publication chacun,
# alors on a déjà le nombre de publications par hashatgs, utilisateurs et topics.

# L'ensemble des tweets mentionnant un utilisateur spécifique :


def tweets_par_mentions():

    tweets_mentions = {}

    for tweet in data:
        temp = ""
        if td.liste_mentions(tweet) != []:
            for elt in td.liste_mentions(tweet):
                if td.liste_mentions(tweet).count(elt) == 1:
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

# Test :

for elt in tweets_mentions:
    for tweet in tweets_mentions[elt] :
        if tweets_mentions[elt].count(tweet) != 1 :
            print(tweet,False)

'''


# L'ensemble des tweets d'un utilisateur spécifique:


def tweets_par_users():
    tweets_users = {}
    for tweet in data:
        if tweet["Autor"] not in tweets_users:
            tweets_users[tweet["Autor"]] = []
            tweets_users[tweet["Autor"]].append(tweet["TweetText"])
        else:
            tweets_users[tweet["Autor"]].append(tweet["TweetText"])


'''

# Test :

l = []
for tweet in data :
    if tweet["Autor"] == "gkUva" :
        l.append(tweet["TweetText"])

print(tweets_users["gkUva"] == l)

'''

# Utilisateurs mentionnant un hashtag spécifique :

tweets_mentions = {}

for tweet in data:
    if td.liste_hashtags(tweet) != []:
        for elt in td.liste_hashtags(tweet):
            if elt not in tweets_mentions:
                tweets_mentions[elt] = []
                tweets_mentions[elt].append(tweet['Autor'])
            else:
                if tweet["Autor"] not in tweets_mentions[elt]:
                    tweets_mentions[elt].append(tweet["Autor"])

'''

# Test :

ltest = []

for tweet in data:
    if "#ai" in td.liste_hashtags(dict):
        if tweet["Autor"] not in ltest:
            ltest.append(tweet["Autor"])

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

for tweet in data:
    if tweet["Autor"] not in users_andMent:
        users_andMent[tweet["Autor"]] = []
    for mention in td.liste_mentions(tweet):
        if mention not in users_andMent[tweet["Autor"]]:
            users_andMent[tweet["Autor"]].append(mention)

'''

# Test :

for elt in users_andMent:
    for tweet in data:
        if tweet["Autor"] == elt:
            for mention in liste_mentions(tweet):
                if mention not in users_andMent[elt]:
                    print(False)

'''
