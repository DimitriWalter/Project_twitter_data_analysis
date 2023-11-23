import json
import re
import random as rd
import traitement as tr

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


# Stockage dans zone d'atterissage :


def zone_atterissage(dict):
    tweet = dict["TweetText"]  # affectation du TweeText à une variable tweet
    new_tweet = tweet.replace("\n\n", " ").replace("\n", " ")  # On remplace les sauts de ligne et les retours à la ligne par des espaces
    tweet_nettoye = re.sub(r'[^\w\s.,!?;:()"^`@#/-_]', ' ', new_tweet)  # On nettoie le tweet en gardant les espaces, les lettres de touts les alphabets et des car. de ponctuation
    dict["TweetText"] = tweet_nettoye  # on l'assigne, une fois nettoyé, à notre TweetText
    return dict


# Mise à jour des données :

# Création d'une copie des ancienne données de aitweets.json :

'''

with open("aitweets.json", 'r', encoding='utf-8') as file_json:
        jeu_tweets = json.load(file_json)


with open("copie_tweets.json", 'w', encoding='utf-8') as file_json:
        json.dump(jeu_tweets,file_json)

'''

# Fonction méttant à jour les données


def maj_data():

    with open("aitweets.json", 'r', encoding='utf-8') as file_json:
        jeu_tweets = json.load(file_json)

    with open("copie_tweets.json", 'r', encoding='utf-8') as file_json:
        copy_tweets = json.load(file_json)

    if len(jeu_tweets) > len(copy_tweets):
        for tweet in jeu_tweets[len(copy_tweets):]:
            autor_temp = rd.choice(creation_autor)
            tweet["Autor"] = autor_temp
        tr.maj_topics()

    with open("zone_d'atterissage.json", "w", encoding='utf-8') as zone_att:
        data = jeu_tweets
        for tweet in data:
            tweet = zone_atterissage(tweet)
        json.dump(data, zone_att, indent=2)
