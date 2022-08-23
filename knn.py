lista=[]
with open('iris_data.csv', 'r') as f:
    for linha in f.readlines():
        a=linha.replace('\n','').split(';')
        lista.append(a)

def countclasses(lista):
    setosa = 0
    versicolor = 0
    virginica = 0
    
    for i in range(len(lista)):
        if lista[i][4] == "Iris-setosa":
            setosa += 1
        if lista[i][4] == "Iris-versicolor":
            versicolor += 1
        if lista[i][4] == "Iris-virginica":
            virginica += 1
    return [setosa,versicolor,virginica]

# Porcentagem de treinamento
p = 0.6

setosa,versicolor, virginica = countclasses(lista)

treinamento, teste = [], []

max_setosa, max_versicolor, max_virginica = int(p*setosa), int(p*versicolor), int(p*virginica)
total1 = 0
total2 = 0
total3 = 0

for lis in lista:
    if lis[-1]=="Iris-setosa" and total1< max_setosa:
        treinamento.append(lis)
        total1 +=1
    elif lis[-1]=="Iris-versicolor" and total2<max_versicolor:
        treinamento.append(lis)
        total2 +=1
    elif lis[-1]=="Iris-virginica" and total3<max_virginica:
        treinamento.append(lis)
        total3 +=1
    else:
        teste.append(lis)

from ast import parse
import math

def dist_euclidiana(v1,v2):
    dim, soma = len(v1), 0
    for i in range(dim -1):
        soma += math.pow(float(v1[i]) - float(v2[i]),2)
    return math.sqrt(soma)

def knn(treinamento, nova_amostra, K):
    dists, len_treino = {}, len(treinamento)
    for i in range(len_treino):
        d= dist_euclidiana(treinamento[i], nova_amostra)
        dists[i] = d
    
    k_vizinhos = sorted(dists, key= dists.get)[:K]
    
    qtd_setosa, qtd_versicolor, qtd_virginica = 0, 0, 0
    for indice in k_vizinhos: 
        if treinamento[indice][-1] == "Iris-setosa":
            qtd_setosa +=1
        elif treinamento[indice][-1] == "Iris-versicolor":
            qtd_versicolor +=1
        else:
            qtd_virginica +=1
            
    a=[qtd_setosa, qtd_versicolor, qtd_virginica]

    if a.index(max(a)) == 1.0 :
        return "Iris-setosa"
    elif a.index(max(a)) == 2.0 : 
        return "Iris-versicolor"
    else:
        return "Iris-virginica"

    # return a.index(max(a)) +1.0

acertos,K = 0, 8
for amostra in teste:
    classe = knn(treinamento, amostra, K)
    if amostra[-1] == classe:
        acertos +=1

print("Porcentagem de acertos:", 100*acertos/len(teste))