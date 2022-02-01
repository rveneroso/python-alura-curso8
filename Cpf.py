from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if(self.cpf_eh_valido(documento)):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, documento):
        if(len(documento)==11):
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


