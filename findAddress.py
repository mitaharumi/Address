import requests
from accessCep import Cep
class FindAddress:
    def __init__(self, cep):
        address = Cep(cep)
        if (address):
            self.state = address.accessState()
            self.city = address.accessCity()
            self.district = address.accessDistrict()
            self.street = address.accessStreet()
        else:
            raise ValueError('CEP ERROR')



