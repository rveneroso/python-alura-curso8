from acesso_cep import BuscaEndereco
import requests

cep = 30510550
objeto_cep = BuscaEndereco(cep)
print(objeto_cep.consulta_cep())

a = objeto_cep.consulta_cep()
print(a)
