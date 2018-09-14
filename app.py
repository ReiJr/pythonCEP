#! /usr/bin/env python  
# -*- coding: iso-8859-1 -*-  
# Criado por: Felipe Olivaes  
import urllib  
import cgi  

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route("/")
def hello():
        cep = 11463180
        r = buscaCEP(cep)
        return "seu endereço " + r

#  
#   Busca CEP  
#  
def buscaCEP(cep):
        url = "http://cep.republicavirtual.com.br/web_cep.php?cep=" + str(cep) + "&formato=query_string"
        pagina      = urllib.urlopen(url)  
        conteudo    = pagina.read();  
        resultado   = cgi.parse_qs(conteudo);
        if resultado['resultado'][0] == '1':
                endereço = resultado['tipo_logradouro'][0] + " " + resultado['logradouro'][0]
        return endereço     
      
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
