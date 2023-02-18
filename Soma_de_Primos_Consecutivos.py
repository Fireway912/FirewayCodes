#################################################
##               Project Euler                 ## 
## Problema 50 - A soma de primos consecutivos ##
#################################################

# Autor: Adriano Claysson da Silva Lima
# Data: 17 de Fevereiro de 2023

# Qual o maior numero primo menor que n(=1000000)
# resultado da soma de consecutivos numeros primos?
n = 1000000
# Inicializar o vetor que ira conter todos os numeros
# primos menores que 'n'
primo = [2]

# Inicializar uma variavel para armazenar a soma de
# primos consecutivos
soma = 0

# Inicializar uma variavel para armazenar a soma de
# primos consecutivos que também for primo
maiorSomaPrimo = 0
tamanhoMSP = 0
# Este laco de repeticao cria e armazena no vetor
# todos os numeros primos
for i in range(2,n):
    # para todos os numeros menores que n...
    sePrimo = 1
    
    for j in range(len(primo)):
        #...se o resto da divisao dele com
        # algum dos primos anteriores a ele for zero...
        if((i%primo[j])==0):
            #...entao ele nao e um numero primo...
            sePrimo = 0
            break
        
    #... se ele for um numero primo...     
    if(sePrimo):
        #...entao armazene-o no vetor de primos.
        primo.append(i)
        print(i)


# esse laco de repeticao soma conssecutivos primos comecando do m-esimo primo... 
for m in range(len(primo)-1):
    # inicializando contador k
    k = 0
    soma = 0
    #  e nesse laco de repeticao a soma prossegue ate o valor atinja n...
    while(soma<n):
        
        soma = soma + primo[k+m]
        #...e se essa soma de primos consecutivos tambem e um primo...
        for l in range(len(primo)):
            if((soma==primo[l])):
                #... e caso positivo se esse numero novo e resultado da soma
                # de mais elementos do que o primo resultante da soma anterior
                # entao o novo numero e o novo maior soma de primos
                print(str(soma)+" e a soma dos primos de "+str(primo[m])+" ate "+str(primo[k+m]))
                if((l-m)>tamanhoMSP):
                    print("\n\n\n\n%%"+str(soma)+" # "+str(tamanhoMSP)+"\n\n\n")
                    maiorSomaPrimo = soma
                    tamanhoMSP = l-m
        k=k+1
    print("###################################")
# mostra na tela o maior numero primo resultado
# da soma de primos consecutivos
print(maiorSomaPrimo)

