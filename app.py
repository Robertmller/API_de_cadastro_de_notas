#from crypt import methods
#from crypt import methods
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'

db = SQLAlchemy(app)
db: SQLAlchemy


# Objetivo da API

alunos = [
    {
        'nome': 'Marcos',
        'turma': 'M4'
    },
    {
        'nome': 'Julia',
        'turma': 'M4'
    },
    {
        'nome': 'Beny',
        'turma': 'M4'
    },
    {
        'nome': 'Roberto',
        'turma': 'M4'
    }
]


# Cadastrar ALuno + notas, Ver todos os alunos e suas notas

# Listar alunos
# http://localhost:5000/alunos
@app.route('/alunos')
def obter_professores():
    return jsonify(alunos)


# URI de cadastro de alunos
# http://localhost:5000/cadastraraluno
@app.route('/cadastraraluno', methods=['POST'])
def novo_aluno():
    aluno = request.get_json()
    alunos.append(aluno)

    return jsonify(aluno)


# Buscar aluno por ID
# http://localhost:5000/aluno/ID
@app.route('/alunos/<int:indice>', methods=['GET'])
def obter_aluno_por_id(indice):
    return jsonify(alunos[indice])

# Cadastrar professor, Ver professores cadastrados
# Listar professores
# http://localhost:5000/professores


# URI de cadastro de professores
# http://localhost:5000/cadastrarprofessor


# Buscar professor por ID
# http://localhost:5000/professor/ID
# Start do servidor


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


db.drop_all()
db.create_all()


app.run(port=5000, host='localhost', debug=True)
