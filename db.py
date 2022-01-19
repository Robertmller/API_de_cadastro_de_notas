import sqlite3

with sqlite3.connect('admin.db') as conexao:
    sql = conexao.cursor()

    sql.execute(
        'create table IF NOT EXISTS aluno(nome text, turma text, nota1 float, nota2 float, nota3 float, nota4 float, media float);')
    sql.execute(
        'create table IF NOT EXISTS professor(nome text, turma text, email text);')


def mediax(a, b, c, d):
    return (a + b + c + d) / 4


while True:  # loop infinito
    nome = input("Nome do aluno: ")
    turma = input("informe a turma: ")
    nota1 = float(input('entre com a primeira nota: '))
    nota2 = float(input('entre com a segunda nota: '))
    nota3 = float(input('entre com a terceira nota: '))
    nota4 = float(input('entre com a quarta nota: '))
    media = mediax(nota1, nota2, nota3, nota4)

    sql.execute('insert into aluno values(?,?,?,?,?,?,?)', [nome, turma,
                nota1, nota2, nota3, nota4, media])
    conexao.commit()

    print(media)

    if media < 4:
        print('aluno reprovado')
    elif media < 6 > 4:
        print('aluno em recuperação')
    else:
        print("aluno aprovado")

    if input('para sair digite (fim) para continuar (enter) ') == 'fim':
        break  # se digitar "fim", sai do while True
