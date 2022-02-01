from datetime import datetime, timedelta
from datas_br import DatasBr
# print(datetime.today())
#
# cadastro = DatasBr()
# print(cadastro.dia_semana_cadastro())

hoje = datetime.today()
# formato_data = "%d/%m/%Y %H:%m"
# print(hoje.strftime(formato_data))
hoje = DatasBr()
print(hoje)
