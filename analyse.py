import json
import traitement as td

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
    while k > len(top):  # On teste si la valeur k donnée n'est pas supérieur au nombre d'hashtags que l'on a
        k = int(input(f"Désolé je ne peux pas t'imprimer le top {k} des hashtags car il n'y en a que {len(top)}, donne moi un nombre + petit : "))  # Si k supérieur au nombre d'hashtags alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"\nTop {k} des hashtags qui reviennent le + souvent : \n")
    for i in range(k):
        print(f"- {i+1}) {top[i][0]} apparait {top[i][1]} fois.")  # On affiche le top K des hashtags avec le nombres d'occurences à chaque fois


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
    while k > len(top):  # On teste si la valeur k donnée n'est pas supérieur au nombre de mentions que l'on a
        k = int(input(f"Désolé je ne peux pas t'imprimer le top {k} des mentions car il n'y en a que {len(top)}, donne moi un nombre + petit : "))  # Si k supérieur au nombre de mentions alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"\nTop {k} des mentions qui reviennent le + souvent : \n")
    for i in range(k):
        print(f"- {i+1}) {top[i][0]} apparait {top[i][1]} fois.")  # On affiche le top K des mentions avec le nombres d'occurences à chaque fois


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
    while k > len(top):  # On teste si la valeur k donnée n'est pas supérieur au nombre de mentions que l'on a
        k = int(input(f"Désolé je ne peux pas t'imprimer le top {k} des utilisateurs car il n'y en a que {len(top)}, donne moi un nombre + petit : "))  # Si k supérieur au nombre de mentions alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"\nTop {k} des utilisateurs qui reviennent le + souvent : \n")
    for i in range(k):
        print(f"- {i+1}) {top[i][0]} apparait {top[i][1]} fois.")  # On affiche le top K des mentions avec le nombres d'occurences à chaque fois


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
    while k > len(top):
        k = int(input(f"Désolé je ne peux pas t'imprimer le top {k} des topics car il n'y en a que {len(top)}, donne moi un nombre + petit : "))  # Si k supérieur au nombre de mentions alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"\nTop {k} des topics qui reviennent le + souvent : \n")
    for i in range(k):
        print(f"- {i+1}) {top[i][0]} apparait {top[i][1]} fois.")  # On affiche le top K des mentions avec le nombres d'occurences à chaque fois


topk_topics()


# Le dictionnaire avec les hashtags, les utilisateurs, les topics regroupe leur nombres de publication chacun,
# alors on a déjà le nombre de publications par hashatgs, utilisateurs et topics.

# L'ensemble des tweets mentionnant un utilisateur spécifique :

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
