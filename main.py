from telefones_br import TelefonesBr
import re

telefone = TelefonesBr("553198041531")
print(telefone)

# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# resposta = re.findall(padrao,telefone)
#
# print(resposta)