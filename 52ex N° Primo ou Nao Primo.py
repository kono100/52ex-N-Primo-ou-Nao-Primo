
#52. Faça uma função que receba um número inteiro, retorne true se o número for primo e false
#se não for primo (idem exemplo anterior, porém, agora com função).



num = int(input('Digite um número: '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, 'não é primo')
            break
    else:
        print(num, 'é primo')