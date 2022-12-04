from flask import Flask , jsonify , request
import requests
import json

app = Flask(__name__)

lista = [
    { 'Nome' : 'Rafael',
      'Habilidade' : 'FullStack',
      'Tempo de casa': '5 anos'
    },
    {
        'Nome': 'João',
        'Habilidade': 'HTML / CSS',
        'Tempo de casa': '2 anos'
    },
    {
        'Nome': 'Ives',
        'Habilidade': 'CEO',
        'Tempo de casa': '10 anos'
    }
]
num_lista = len(lista)
@app.route("/dev/<int:id>/" , methods =['GET','PUT','DELETE'])
def desenvolvedor(id):
    valorLista = len(lista)
    if valorLista < id:
       return jsonify('Valor de ID Menor que a lista explicada')
    else:
            if request.method == 'GET':
              desenvolvedor = lista[id]
              print(desenvolvedor)
              return jsonify(desenvolvedor)
            elif request.method == 'PUT':
              dados = json.loads(request.data)
              lista[id] = dados
              return jsonify(dados)
            elif request.method == 'DELETE':
              lista.pop(id)
              return 'Deletado com Sucesso!'

@app.route("/cad" , methods =['GET','POST'])
def listaCriacao():
    if request.method == "GET":
        return jsonify(lista)
    elif request.method == "POST":
        dados = json.loads(request.data)
        lista.append(dados)
        return jsonify({'Mensagem':'Sucesso','Situação':'Cadastro Inserido'})



if __name__ == '__main__':
    app.run()