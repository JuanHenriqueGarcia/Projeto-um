# Meu prieiro projeto Python! 

# Lendo Nome, Notas, Média de vários alunos, utilizando o método LISTA e mostrar nota de aluno específico ao final dela. 


lista = list()
resposta = ''
linha = '-'*30
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar? '))
    if resposta in 'nN':
        break
print(linha)
print(f'{"Nº.":<4} {"NOME":<10} {"MédiaFinal":>8}')
print(linha)
for indice, aluno in enumerate(lista):
    print(f'{indice:<4} {aluno[0]:<8} {aluno[2]:>8}')
while True:
    opção = int(input('Mostrar notas de qual aluno? (999 para INTERROMPER) :'))
    if opção == 999:
        break
    if opção <= len(lista) -1:
        print(f'As notas do aluno: {lista[opção][0]} são {lista[opção][1]}')
