#1- Espião: Escreva uma função que receba uma lista de inteiros e retorne True se contém um 007 em ordem, mesmo
#que não contínuo.
lista = []
print('Construa sua lista com 10 números para procurar o ESPIÃO:')
for n in range(0, 10):
    lista.append(int(input('Digite um valor:  ')))
l1 = []
l2 = []
for cont in range (0, len(lista)):
    if (lista[cont] == 0):
        l1.append(cont)       
    if (lista[cont] == 7):
        l2.append(cont)
x = len(l2)-1        
if  (len(l1) >= 2) and (len(l2) >= 1):
    if l2[x] > l1[1]:
        print (f'True!!! A lista digitada foi: {lista}.\nEncontramos seu ESPIÃO!')
    else:
        print (f'False!!! A lista digitada foi: {lista}.\nEla não esconde um ESPIÃO!')
else:
    print (f'False!!! A lista digitada foi: {lista}.\nEla não esconde um ESPIÃO!')
