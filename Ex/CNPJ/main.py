import validador
import re


# cnpj = input('Digite seu CNPJ:  ')

# clean_cnpj = re.sub(r'[^0-9]','', cnpj)

# if validador.func.validate(cnpj) == clean_cnpj:
#     print(f'O CNPJ: {cnpj} é válido')
# else: 
#     print(f'O CNPJ: {cnpj} é inválido')
#     # print(validador.func.validate(cnpj))

new_cnpj = validador.func_generator.generator_cnpj()
print(new_cnpj)

