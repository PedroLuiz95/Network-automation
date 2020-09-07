#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import telnetlib,re,json
from multiprocessing import Pool
import time 
class main():
    def __init__(self):
        equipamentos = [{'ip':'10.95.1.1','usuario':'usuario1','senha':'senha1','hostname':"R1"},\
            {'ip':'10.95.1.3','usuario':'usuario2','senha':'senha2','hostname':"R2"}] 
        instancias = []
        dado_saida = []
        with Pool(2) as p:
            instancias.append(p.map(conexao_equipamento,equipamentos))
        for i in instancias:
            for k in i:
                dado_saida.append(k.dado_host)
        self.saida = dado_saida
    def get_dado(self):
        return self.saida

class conexao_equipamento():
    def __init__(self,dado):
        self.ip = dado['ip']
        self.usuario = dado['usuario']
        self.senha = dado['senha']
        self.hostname = dado['hostname']
        self.start_conn()
        saida = self.get_ip()
        lista_interface = texto.extract_ip(saida)
        self.dado_host = {self.hostname:lista_interface}
    def send_command(self,command,new_line=True):
        if(new_line):
            self.tn.write((command+'\n').encode())
        else:
            self.tn.write((command).encode())
    def read_command(self,pattern,return_exit=False):
        saida = self.tn.read_until(pattern.encode()).decode()
        if(return_exit):
            return saida

    def start_conn(self):
        self.tn = telnetlib.Telnet()
        self.tn.open(self.ip,'23',100)
        self.read_command(':')
        self.send_command(self.usuario)
        self.read_command(':')
        self.send_command(self.senha)
        self.read_command('#')
    
    def get_ip(self):
        self.send_command("show ip int brief")
        saida = self.read_command("#",True) 
        return saida

class texto():
    def extract_ip(dado):
        dado = dado.split("\n")
        dado = dado[2:len(dado)-1]
        lista_interface = []
        for i in dado:
            i = re.sub(r'\s+',' ',i)
            interface = i.split(' ')
            lista_interface.append({'interface':interface[0],'ip':interface[1],\
                'status':interface[4]})
        return lista_interface
if __name__ == "__main__":
    main()