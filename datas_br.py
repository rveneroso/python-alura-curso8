from datetime import datetime
class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        nomes_meses = [
            'janeiro',
            'fevereiro',
            'março',
            'abril',
            'maio',
            'junho',
            'julho',
            'agosto',
            'setembro',
            'outubro',
            'novembro',
            'dezembro'
        ]
        return nomes_meses[self.momento_cadastro.month-1]

    def dia_semana_cadastro(self):
        dias_semana = [
            'segunda-feira',
            'terça-feira',
            'quarta-feira',
            'quinta-feira',
            'sexta-feira',
            'sábado',
            'domingo'
        ]
        return dias_semana[self.momento_cadastro.weekday()]

    def format_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%m")