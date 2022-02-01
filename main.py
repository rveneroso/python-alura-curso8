from datetime import datetime, timedelta
from datas_br import DatasBr
print(datetime.today())

cadastro = DatasBr()
print(cadastro.dia_semana_cadastro())
