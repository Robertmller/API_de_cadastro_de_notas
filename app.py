#from crypt import methods
#from crypt import methods
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'

db = SQLAlchemy(app)
db: SQLAlchemy


# Funções do Banco de Dados
class Aluno(db.Model):
    __tablename__ = 'aluno'
    id_aluno = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    turma = db.Column(db.String)
    nota1 = db.Column(db.Float)
    nota2 = db.Column(db.Float)
    nota3 = db.Column(db.Float)
    nota4 = db.Column(db.Float)
    media = db.Column(db.Float)


# Criando a classe Professor

class Professor(db.Model):
    __tablename__ = 'professor'
    id_professor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    turma = db.Column(db.String)


def inicializar_db():
    # Limpa estrutura do Banco de Dados
    db.drop_all()
    # Cria a estrutura nova
    db.create_all()


# Objetivo da API
# Cadastrar ALuno + notas, Ver todos os alunos e suas notas


# Listar alunos
# http://localhost:5000/alunos
@app.route('/alunos')
def obter_alunos():
    # Extraindo dados da tabela
    alunos = Aluno.query.all()
    lista_de_alunos = []
    for aluno in alunos:
        aluno_atual = {}
        # professor_atual['id_professor'].professor.id_professor
        aluno_atual['nome'] = aluno.nome
        aluno_atual['turma'] = aluno.turma
        aluno_atual['nota1'] = aluno.nota1
        aluno_atual['nota2'] = aluno.nota2
        aluno_atual['nota3'] = aluno.nota3
        aluno_atual['nota4'] = aluno.nota4
        aluno_atual['media'] = aluno.media

        lista_de_alunos.append(aluno_atual)

    return jsonify({'alunos': lista_de_alunos})


# URI de cadastro de alunos
# http://localhost:5000/cadastraraluno
@app.route('/cadastraraluno', methods=['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    aluno = Aluno(nome=novo_aluno['nome'], turma=novo_aluno['turma'], nota1=novo_aluno['nota1'],
                  nota2=novo_aluno['nota2'], nota3=novo_aluno['nota3'], nota4=novo_aluno['nota4'], media=novo_aluno['media'])

    db.session.add(aluno)
    db.session.commit()

    return jsonify({'mensagem': 'Aluno adcionado com sucesso'})


# Buscar aluno por ID
# http://localhost:5000/aluno/ID
@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def obter_aluno_por_id(id_aluno):
    aluno = Aluno.query.filter_by(id_aluno=id_aluno).first()
    if not aluno:
        return jsonify(f'Aluno não encontrado')
    aluno_atual = {}
    # professor_atual['id_professor'].professor.id_professor
    aluno_atual['nome'] = aluno.nome
    aluno_atual['turma'] = aluno.turma
    aluno_atual['nota1'] = aluno.nota1
    aluno_atual['nota2'] = aluno.nota2
    aluno_atual['nota3'] = aluno.nota3
    aluno_atual['nota4'] = aluno.nota4
    aluno_atual['media'] = aluno.media

    return jsonify({'aluno': aluno_atual})


# Cadastrar professor, Ver professores cadastrados

# Listar professores
# http://localhost:5000/professores
@app.route('/professores')
def obter_professores():
    # Extraindo dados da tabela
    professores = Professor.query.all()
    lista_de_professores = []
    for professor in professores:
        professor_atual = {}
        # professor_atual['id_professor'].professor.id_professor
        professor_atual['nome'] = professor.nome
        professor_atual['turma'] = professor.turma
        lista_de_professores.append(professor_atual)

    return jsonify({'professores': lista_de_professores})


# URI de cadastro de professores
# http://localhost:5000/cadastrarprofessor

@app.route('/cadastrarprofessor', methods=['POST'])
def novo_professor():
    novo_professor = request.get_json()
    professor = Professor(
        nome=novo_professor['nome'], turma=novo_professor['turma'])

    db.session.add(professor)
    db.session.commit()

    return jsonify({'mensagem': 'Professor adcionado com sucesso'})

# Buscar professor por ID
# http://localhost:5000/professor/ID


@app.route('/professores/<int:id_professor>', methods=['GET'])
def obter_professor_por_id(id_professor):
    professor = Professor.query.filter_by(id_professor=id_professor).first()
    if not professor:
        return jsonify(f'Professor não encontrado')
    professor_atual = {}
    # professor_atual['id_professor'].professor.id_professor
    professor_atual['nome'] = professor.nome
    professor_atual['turma'] = professor.turma

    return jsonify({'professor': professor_atual})


# Calculando as notas
def mediax(a, b, c, d):
    return (a + b + c + d) / 4


# while True:  # loop infinito
#     nome = input("Nome do aluno: ")
#     turma = input("informe a turma: ")
#     nota1 = float(input('entre com a primeira nota: '))
#     nota2 = float(input('entre com a segunda nota: '))
#     nota3 = float(input('entre com a terceira nota: '))
#     nota4 = float(input('entre com a quarta nota: '))
#     media = mediax(nota1, nota2, nota3, nota4)

#     aluno = Aluno(nome=nome, turma=turma, nota1=nota1,
#                   nota2=nota2, nota3=nota3, nota4=nota4, media=media)

#     db.session.add(aluno)
#     db.session.commit()

#     print(media)

#     if media < 4:
#         print('aluno reprovado')
#     elif media < 6 > 4:
#         print('aluno em recuperação')
#     else:
#         print("aluno aprovado")

#     if input('para sair digite (fim) para continuar (enter) ') == 'fim':
#         break  # se digitar "fim", sai do while True

#########
# Start do servidor
app.run(port=5000, host='localhost', debug=True)

if __name__ == "__main__":
    inicializar_db
