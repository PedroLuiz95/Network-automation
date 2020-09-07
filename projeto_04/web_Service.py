#!/usr/bin/python3
#_*_ coding:utf-8 _*_
from flask import Flask,request
from flask_restful import Resource , Api
import get_ip_interface as gii
class main():
    def __init__(self):
        fl.start_flask()

class executa_requisicao(Resource):
    def get(self):
        interface = gii.main()
        saida = interface.saida
        return saida
    def post(self):
        interface = gii.main()
        saida = interface.saida
        return saida


class fl():
    def start_flask():
        app = Flask(__name__)
        api = Api(app)
        api.add_resource(executa_requisicao,'/')
        app.run(debug=True,host='192.168.80.130',port=8081)
if __name__ == "__main__":
    main()
