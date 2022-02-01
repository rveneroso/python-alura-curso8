class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if(self.cpf_eh_valido(documento)):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, documento):
        if(len(documento)==11):
            return True
        else:
            return False

    def format_cpf(self):
        grupo1 = self.cpf[:3]
        grupo2 = self.cpf[3:6]
        grupo3 = self.cpf[6:9]
        grupo4 = self.cpf[9:]
        return "{}.{}.{}-{}".format(grupo1, grupo2, grupo3, grupo4)

