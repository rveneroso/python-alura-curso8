from acesso_cep import BuscaEndereco
import requests

cep = 30510550
objeto_cep = BuscaEndereco(cep)

# Não sabia que é possível fazer esse tipo de atribuição no Python.
bairro, cidade, uf = objeto_cep.consulta_cep()
print(bairro)
print(cidade)
print(uf)
