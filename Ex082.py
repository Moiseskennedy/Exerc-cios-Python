lista, par, impar = [], [], []
continuar = ' '

print('*' * 40)
print('Digite alguns números! \nVamos separar os números em dois grupos, \033[1;34mÍMPARES\033[m e \033[1;35mPARES\033[m')
print('*' * 40)
while True:
        n = int(input('Digite um número: '))
        lista.append(n)
        
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
            
        continuar = input('Deseja continuar? S/N: ').upper()
        print()
            
        while continuar != 'S' and continuar != 'N':
            print('\033[1;33mDados inválidos!!! Tende novamente...\033[m')
            continuar = input('Deseja continuar? S/N: ').upper()
            print()
            
        if continuar == 'N':
            break
            
print('-' * 40)
print(f'Lista de todos números: \033[1;32m{lista}\033[m')    
print(f'Lista dos números pares:\033[1;35m {par}\033[m')
print(f'Lista dos números ímpares \033[1;34m{impar}\033[m')