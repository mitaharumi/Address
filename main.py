from accessCep import Cep
from findAddress import FindAddress


import requests

cepTest = '86041340'
cepObject = Cep(cepTest)
address = FindAddress(cepTest)

# # dir returns all atributes and methods that object has
#
# print(dir(cepObject.accessAddress()))
# print(cepObject.accessAddress().text)
# print(type(cepObject.accessAddress().text))
# print(cepObject.accessAddress().json())
# print(type(cepObject.accessAddress().json()))
# print(cepObject.accessAddress().json()['bairro'])
# print(cepObject.accessCity())

print(address)

