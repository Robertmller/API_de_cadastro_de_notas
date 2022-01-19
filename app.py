#from crypt import methods
#from crypt import methods
from flask import Flask, jsonify, request


app = Flask(__name__)

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
app.run(port=5000, host='localhost', debug=True)
