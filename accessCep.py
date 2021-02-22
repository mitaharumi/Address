import requests

class Cep:
    def __init__(self, cep):
        cep = str(cep)
        # check by amount
        if self.cepAmount(cep):
            # check by API viacep

            if 'erro' in (requests.get('https://viacep.com.br/ws/{}/json'.format(cep))).text:
                print('aaaaaaa')
                raise ValueError("CEP invalid")
            else:
                self.cep = cep
        else:
            raise ValueError("CEP amount digits invalid")

    # def __str__(self):
    #     return self.cepFormat()

    # returns cep in format xxxxx-xxx
    def cepFormat(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def cepAmount(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def accessAddress(self):
        url = 'https://viacep.com.br/ws/{}/json'.format(self.cep)
        return requests.get(url)

    def accessState(self):
        state = self.accessAddress().json()['uf']
        return state

    def accessCity(self):
        city = self.accessAddress().json()['localidade']
        return city

    def accessDistrict(self):
        city = self.accessAddress().json()['bairro']
        return city

    def accessStreet(self):
        street = self.accessAddress().json()['logradouro']
        return street
