# fail alles vaid sentimentaalsetel põhjustel, ei ole kasutuses
# lennart type beat
from random import *

sonads = ["aed", "meeter", "pärtel", "skiso", "sigma", "raha", "kell"]

read = {
    "t1": ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ü', 'õ'],
    "t2": ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
    "t3": ['z', 'x', 'c', 'v', 'b', 'n', 'm']
  }

sormed =  {
    "v": ["a", "z", "<", "q", "w", "s", "x", "e", "d", "c", "r", "t", "f", "g", "v", "b"],
    "p": ["p", "ü", "õ", "ö", "ä", "'", "-", "o", "l", ".", ",", "k", "i", "m", "n", "j", "h", "u", "y"],
    "m" : ["a", "z", "<", "q", "w", "s", "x", "e", "d", "c", "r", "t", "f", "g", "v", "b", "p", "ü", "õ", "ö", "ä", "'", "-", "o", "l", ".", ",", "k", "i", "m", "n", "j", "h", "u", "y"]
}

def tase1(rida, kasi):
    tekst = ""
    if kasi == "vasak": kas = "v"
    elif kasi == "parem": kas = "p"
    elif kasi == "molemad": kas = "m"
    
    #valib millist rida harjutab ja arvutab välja mitte harjutatava käe
    if rida == "esimene":
        gene = [item for item in read["t1"] if item in sormed[kas]]
    elif rida == "teine":
        gene = [item for item in read["t2"] if item in sormed[kas]]
    elif rida == "kolmas":
        gene = [item for item in read["t3"] if item in sormed[kas]]
    elif rida == "koik":
        gene = [item for item in (read["t1"] + read["t2"] + read["t3"]) if item in sormed[kas]]
    
    for i in range(4):
        tekst += (str(2*gene[randint(0, len(gene)-1)])+" ")
    return tekst

def tase2(rida, kasi):
    tekst = ""
    if kasi == "vasak": kas = "v"
    elif kasi == "parem": kas = "p"
    elif kasi == "molemad": kas = "m"
    
    #valib millist rida harjutab ja arvutab välja mitte harjutatava käe
    if rida == "esimene":
        gene = [item for item in read["t1"] if item in sormed[kas]]
    elif rida == "teine":
        gene = [item for item in read["t2"] if item in sormed[kas]]
    elif rida == "kolmas":
        gene = [item for item in read["t3"] if item in sormed[kas]]
    elif rida == "koik":
        gene = [item for item in (read["t1"] + read["t2"] + read["t3"]) if item in sormed[kas]]
    
    for i in range(9):
        if i != 4: tekst += gene[randint(0, len(gene)-1)]
        else: tekst += " "
    return tekst

def tase3(sonad):
    tekst = ""
    for i in range(2):
        tekst += sonad[randint(0, len(sonad)-1)] + " "
    
    return tekst

print(tase1("esimene", "molemad"))
print(tase2("esimene", "vasak"))
print(tase3(sonads))