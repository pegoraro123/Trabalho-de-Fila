import queue
idoso= queue.Queue()
gestante= queue.Queue()
normal= queue.Queue()
rodando= True
lista1=[]
lista2=[]
lista3=[]
while rodando == True:
    print ('1 - inserir na fila')
    print ('2 - mostrar fila')
    print ('3 - remover pessoa')
    print ('4- sair')
    opcoes= int(input('digite uma opção:'))      
    if opcoes == 1:
        fila= str(input('qual fila deseja ? idoso/gestante/normal:'))
        nome= str(input('digite seu nome:'))
        if fila == 'idoso':
            idoso.put(nome)
            lista1.append(nome)
        elif fila == 'gestante':
            gestante.put(nome)
            lista2.append(nome)
        elif fila == 'normal':
            normal.put(nome)
            lista3.append(nome)
        else:
             print('digite fila desejada')
    elif opcoes == 2:
        print('fila de idoso')
        print(lista1)
        print('fila de gestante')
        print(lista2)
        print('fila normal')
        print(lista3)
    elif opcoes == 3:
        if idoso.empty() == False:
            print ('remove da fila', idoso.get())
        elif gestante.empty == False:
            print('remove da fila', gestante.get())
        elif normal.empty() == False:
            print ('remove da fila', normal.get())
    elif opcoes == 4:
        rodando == False
        print ('VOLTE SEMPRE')
        
            
                      
            
          
        

