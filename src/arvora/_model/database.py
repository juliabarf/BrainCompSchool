from tinydb import TinyDB, Query
import os
import json

LOCAL_FOLDER = (os.path.abspath(os.path.join(os.path.dirname(__file__))))
db = TinyDB(os.path.join(LOCAL_FOLDER, 'brain.json'))
db_user = TinyDB(os.path.join(LOCAL_FOLDER, 'users_brain.json'))

Article = Query()

"""

Gerenciando o banco de dados:

Estrutura do Artigo--
-- Titulo
-- Corpo
-- Data de cração/postagem

Estrutura Usuário
-- Nome
-- Senha
-- Email

"""

"""
levantamento de requisitos

determinamos a ordem de execução deles

começo das atividades tentar concluir os requisitos semanalmente

estudos das tecnologias necessarias pro desenvolvimento do projeto



"""
class User:
    @classmethod
    def login(cls, form):
        User = Query()
        user_data = json.loads(form.decode('utf-8'))
        email = user_data['email']
        password = user_data['password']
        print(email)
        if(db_user.search(User.email == email)):
            print("asdasda")
            return "ok"
            if db_user.search(User.password == password):
                 return "ok"
            else:
                return "error"

        else:
            print("asdasda1")
            return "error"

    @classmethod
    def create(cls, user):
        User = Query()
        _user = json.loads(user)
        if db_user:
            print("dadhasuifr")
            if not db_user.search(User.email == _user.get("email")):
                db_user.insert(_user)
            else:
                print("coe")
                return {"message": "error"}
        else:
            db_user.insert(_user)

        return "ok"
        # if db_user:
        #     if not (db_user.search(User.email==_user.get("email")):
        #     db_user.insert(_user)
        #         print("Usuário cadastrado!")
        #
        #     else:
        #         print("Usuário já existente")
class Article:
    @classmethod
    def load_articles(cls):
        return db.all()

    @classmethod
    def insert(cls, data):
        article = json.loads(data.decode('utf-8'))
        print(article['title'])
        # article = {
        #     "title": data.title,
        #     #"autor": data.author,
        #     "body": data.body,
        #     #"published": data.published
        # }
        db.insert(article)

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass


