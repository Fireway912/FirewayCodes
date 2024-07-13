import math
import copy

def printTable(table):
    for row in table:
        print('  ',end='')
        for element in row:
            print(element, end='|')
        print('\n----------------------')

def sudokuSolver(tableOrigin,depth):
    table = copy.deepcopy(tableOrigin) 
    lastlastSum= 999
    lastSum = 99
    sum=0      
    for i in table:
        sum = sum + i.count(0)
    #print(sum)
    while(sum>0):
        
        for column in range(9):
            for row in range(9):
                possible = [1,2,3,4,5,6,7,8,9]
                if(table[row][column]==0):   
                    for i in range(1,10):
                        #Verifica Colunas
                        for j in range(9):
                            if(table[j][column]==i and possible.count(i)>0):
                                possible.remove(i)
                        #Verifica Linhas
                        for j in range(9):
                            if(table[row][j]==i and possible.count(i)>0):
                                possible.remove(i)
                        #Verifica Quadrados
                        for j in range(3):
                            for k in range(3):
                                if(table[math.floor(row/3)*3+j][math.floor(column/3)*3+k]==i and possible.count(i)>0):
                                    possible.remove(i)
                #Se ja existe um numero no quadradinho então ele é a unica solução possivel    
                else:
                    possible = [table[row][column]]
                #Se existe apenas uma solução possivel para o quadradinho então ela é a solução    
                if(len(possible)==1):
                    table[row][column]=possible[0]
                #Se existem duas soluções para o quadradinho então teste as duas
                if(len(possible)==2 and lastSum==sum):
                    table[row][column]=possible[0]
                    stat1 = sudokuSolver(table,depth+1)
                    if(stat1['points']==0):
                        return stat1
                    #Primeira não funcionou, teste a segunda solução
                    table[row][column]=possible[1]
                    stat2 = sudokuSolver(table,depth+1)
                    if(stat2['points']==0):
                        return stat2
                    back = {'points':sum,'table':table}
                    return back
                #Se por tres iterações consecutivas não achou soluções então este é o fim da linha, volte e tente a outra solução
                if(lastlastSum == sum):
                    back = {'points':sum,'table':table}
                    return back

        lastlastSum = lastSum
        lastSum = sum
        sum=0      
        for i in table:
            sum = sum + i.count(0)

    back = {'points':sum,'table':table}
    return back

#Esta é uma tabela que demorei 32 min para resolver no braço
table = [[0, 0, 0, 8, 5, 0, 0, 7, 0],
         [7, 0, 0, 0, 9, 2, 0, 0, 0],
         [5, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 6, 9, 3, 4, 5],
         [0, 4, 0, 0, 0, 0, 0, 2, 0],
         [0, 0, 6, 0, 3, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 9, 0, 3],
         [0, 1, 0, 0, 0, 3, 6, 8, 7],
         [0, 0, 3, 9, 0, 0, 2, 5, 0]
         ]

#Imprimir bonitinho a matriz
printTable(sudokuSolver(table,0)['table'])
