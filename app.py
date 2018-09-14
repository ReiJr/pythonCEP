#! /usr/bin/env python  
# -*- coding: utf-8 -*-  
# Criado por: Felipe Olivaes  
#import urllib  
import cgi  
import os
from flask import Flask
from flask import request
from flask import make_response
from urllib.request import urlopen
from base64 import b64encode
# Flask app should start in global layout
app = Flask(__name__)

@app.route("/")
def hello():
        cep = "11463180"
        print (cep)
        r = buscaCEP(cep).encode('utf-8')
        print (r)
        return "seu endereço "

#  
#   Busca CEP  
#  
def buscaCEP(cep):
        url = "http://cep.republicavirtual.com.br/web_cep.php?cep=" + cep + "&formato=query_string"
        pagina      = urlopen(url).read()  
        conteudo    = pagina.decode('utf-8') #pagina.encode('utf-8')
        resultado   = cgi.parse_qs(pagina)
        #print (pagina.encode('utf-8'))
        print (resultado)
        #if resultado['resultado'][0] == '1':
        #        endereco = resultado['tipo_logradouro'][0].encode('utf-8') #+ " " + str(resultado['logradouro'][0])
        #print (endereco)
        return "ok" #.encode('utf-8')     
      
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
