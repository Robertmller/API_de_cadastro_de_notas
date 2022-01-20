from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'

db = SQLAlchemy(app)
db: SQLAlchemy


# Funções do Banco de Dados
# Criando a classe Aluno
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
    resultado = db.Column(db.String)


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
# Cadastrar ALuno + notas, listar todos os alunos, suas notas e resultado
@app.route('/')
def main():
    return jsonify(f'Tela inicial')


# Listar alunos
# http://localhost:6000/alunos
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
# http://localhost:6000/cadastraraluno
@app.route('/cadastraraluno', methods=['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    aluno = Aluno(nome=novo_aluno['nome'], turma=novo_aluno['turma'], nota1=novo_aluno['nota1'],
                  nota2=novo_aluno['nota2'], nota3=novo_aluno['nota3'], nota4=novo_aluno['nota4'], media=novo_aluno['media'], resultado=novo_aluno['resultado'])

    db.session.add(aluno)
    db.session.commit()

    return jsonify({'mensagem': 'Aluno adcionado com sucesso'})


# Buscar aluno por ID
# http://localhost:6000/aluno/ID
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


# Cunsulta de notas por ID do Aluno
# http://localhost:6000/notas/ID
@app.route('/notas/<int:id_aluno>', methods=['GET'])
def obter_nota_por_id(id_aluno):
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
    aluno_atual['resultado'] = aluno.resultado

    return jsonify({'aluno': aluno_atual})


# Cadastrar professor, Ver professores cadastrados

# Listar professores
# http://localhost:6000/professores
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
# http://localhost:6000/cadastrarprofessor

@app.route('/cadastrarprofessor', methods=['POST'])
def novo_professor():
    novo_professor = request.get_json()
    professor = Professor(
        nome=novo_professor['nome'], turma=novo_professor['turma'])

    db.session.add(professor)
    db.session.commit()

    return jsonify({'mensagem': 'Professor adcionado com sucesso'})


# Buscar professor por ID
# http://localhost:6000/professor/ID

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


# Start do servidor
if __name__ == "__main__":
    inicializar_db
    app.run(port=6000, host='0.0.0.0', debug=True)
