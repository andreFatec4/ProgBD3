#2- Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver em alguma posição da lista um 3 do lado de outro 3.'''

lista = []
print('Construa sua lista com 10 números para procurarmos o "33"')
for n in range(0, 10):
    lista.append(int(input('Digite um valor:  ')))
l1 = []
for cont in range (0, len(lista)):
    if (lista[cont] == 3):
        l1.append(cont)  
print (l1)
x = 1
achei = 0
while x <= len(l1)-1:
    if l1[x] == ( l1[x-1] + 1 ):
        achei += 1
        break
    else:
        x += 1
if (achei == 1):
    print (f'True!!! A lista criada foi {lista}, nela encontramos o "33".') 
else: 
    print (f'False!!! A lista criada foi {lista}, nela não consta o "33"')
    
