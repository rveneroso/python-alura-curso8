from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        if(tipo_documento.lower()=='cpf'):
            documento = str(documento)
            if(self.cpf_e_valido(documento)):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!!")
        elif(tipo_documento.lower()=='cnpj'):
            documento = str(documento)
            if(self.cnpj_e_valido(documento)):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!!")
        else:
            raise ValueError("Tipo de documento inválido!!")

    def __str__(self):
        if(hasattr(self, 'cpf')):
            return self.format_cpf()
        else:
            return self.format_cnpj()

    def cpf_e_valido(self, documento):
        if(len(documento)==11):
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def cnpj_e_valido(self, documento):
        if(len(documento)==14):
            validador = CNPJ()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


