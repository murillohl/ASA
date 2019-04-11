from flask import Flask, url_for, request, json, jsonify
from cliente import Cliente
from produtos import Produto
from venda import Venda
from json import dumps
#from bottle import response

app = Flask(__name__)
myCliente = []
myVenda = []
myProduto = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'

@app.route('/hello')
def api_hello(): #http://127.0.0.1:5000/hello?name=Luis
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"



@app.route('/getcliente', methods = ['GET'])
def api_getcliente():
    global myClient
    cliente_data = request.get_json() # 
    print(cliente_data)
    codCliente = cliente_data['codigo']
    print(codCliente)
    print(myCliente[0].getNome())
    res = {'status': 'usuario nao encontrado'}
    for elem in myCliente:
        if(int(codCliente) == elem.getId()):
            res = {'nome': elem.getNome()}
        
    return jsonify(res)

@app.route('/getproduto', methods = ['GET'])
def api_getproduto():
    global myProduto
    produto_data = request.get_json() # 
    print(produto_data)
    codProduto = produto_data['codigo']
    print(codProduto)
    print(myProduto[0].getNome())
    res = {'status': 'produto nao encontrado'}
    for elem in myProduto:
        if(int(codProduto) == elem.getId()):
            res = {'nome': elem.getNome()}
        
    return jsonify(res)

@app.route('/addcliente', methods = ['POST'])
def api_newcliente():
    global myCliente
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    new_cliente = Cliente(id, nome, idade, cidade)
    myCliente.append(new_cliente)
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/addproduto', methods = ['POST'])
def api_newproduto():
    global myProduto
    req_data = request.get_json()

    idproduto = req_data['idproduto']
    nome = req_data['nome']
    valor = req_data['valor']
    new_produto = Produto(idproduto, nome, valor)
    myProduto.append(new_produto)
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/listclientes', methods = ['GET'])
def api_listCliente():
    payload = []
    content = {}
    
    for elem in myCliente:        
        content = {'id': str(elem.getId()),'[nome]': elem.getNome(), 
        '[idade]': str(elem.getIdade()), '[cidade]': elem.getCidade()}
        payload.append(content)
        content = {}

    res =  json.dumps(payload)       
    
    return jsonify(ClienteList=res)

@app.route('/listprodutos', methods = ['GET'])
def api_listProduto():
    payload = []
    content = {}
    
    for elem in myProduto:        
        content = {'id': str(elem.getId()),'[nome]': elem.getNome(), 
        '[valor]': str(elem.getValor())}
        payload.append(content)
        content = {}

    res =  json.dumps(payload)       
    
    return jsonify(ProdutoList=res)

@app.route('/addvendas', methods = ['POST'])
def api_newvenda():
    global myVenda
    req_data = request.get_json()

    idcliente = req_data['idcliente']
    idproduto = req_data['idproduto']
    quantidade = req_data['quantidade']
    total = 0
    for elem in myProduto:
        if idproduto == elem.getId():
            total = int(elem.getValor()) * int(quantidade)
    new_venda = Venda(idcliente, idproduto, quantidade, total)
    myVenda.append(new_venda)
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/totalcliente/<id_cliente>', methods = ['GET'])
def api_totalcliente(id_cliente):
    cliente = id_cliente
    payload = []
    content = {}
    total = 0
    
    for elem in myVenda:
        if cliente == elem.getId():
            total = total + int(elem.getTotal())
            content = {'idCliente': str(elem.getId()),'[totalGasto]': str(total)}
            payload.append(content)
            content = {}
            

    res = json.dumps(payload)
    return jsonify(Vendas=res)

if __name__ == '__main__':
    app.run()


