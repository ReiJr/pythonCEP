#! /usr/bin/env python  
# -*- coding: iso-8859-1 -*-  
# Criado por: Felipe Olivaes  
import urllib  
import cgi  
  
#  
#   Busca CEP  
#  
cep_busca   = '91370370';  
url         = "http://cep.republicavirtual.com.br/web_cep.php?cep=" + cep_busca + "&formato=query_string"  
pagina      = urllib.urlopen(url)  
conteudo    = pagina.read();  
resultado   = cgi.parse_qs(conteudo);  
  
if resultado['resultado'][0] == '1':  
    print "Endereço com cidade de CEP único: "  
    print resultado['tipo_logradouro'][0]  
    print resultado['logradouro'][0]  
    print resultado['bairro'][0]  
    print resultado['cidade'][0]  
    print resultado['uf'][0]  
