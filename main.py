import phonenumbers

from phonenumbers import geocoder

print('')
print('                               Digite o número como no exemplo:')
print('')
print('                ############################################################')
print('                #                   Exemplo: +5578996112299                #')
print('                ############################################################')
print('')
Number = str(input("Digite o número do celular: "))

ch_number = phonenumbers.parse(Number, "CH")
print('')
print('Local:', geocoder.description_for_number(ch_number, "en"))
print('')
from phonenumbers import carrier
service_number = phonenumbers.parse(Number, "RO")
print('Operadora:', carrier.name_for_number(service_number, "en"))