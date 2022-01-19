from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'


db = SQLAlchemy(app)
db: SQLAlchemy

# Criando a classe aluno


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
