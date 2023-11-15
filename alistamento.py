print("Alistamento Militar")
from datetime import date
atual = date.today().year

nome = str(input("Digite seu nome completo: "))
idade = int(input("Digite sua idade: "))
def formatar_cpf(cpf_digitado):
    # Remova todos os caracteres não numéricos do CPF
    cpf_digitado = ''.join(c for c in cpf_digitado if c.isdigit())

    # Adicione os pontos à medida que o usuário digita
    if len(cpf_digitado) >= 3:
        cpf_formatado = cpf_digitado[:3] + '.'
    else:
        cpf_formatado = cpf_digitado

    if len(cpf_digitado) >= 6:
        cpf_formatado += cpf_digitado[3:6] + '.'
    else:
        cpf_formatado = cpf_formatado

    if len(cpf_digitado) >= 9:
        cpf_formatado += cpf_digitado[6:9] + '-'
    else:
        cpf_formatado = cpf_formatado

    cpf_formatado += cpf_digitado[9:]

    return cpf_formatado

cpf_digitado = ""
while len(cpf_digitado) < 11:
    cpf_digitado = input("Digite seu CPF (apenas números): ")
    cpf_formatado = formatar_cpf(cpf_digitado)


estado = int(input("""Selecione seu estado: 
1° Alagoas
2° Pernambuco
3° São Paulo
4° Rio de janeiro
"""))

def formata_telefone(telefone):
    telefone = ''.join(c for c in telefone if c.isdigit())

    if len(telefone) >= 4:
        formata_telefone = telefone[:4] + '-'
    else:
        formata_telefone = telefone
    if len(telefone) >= 4:
        formata_telefone += telefone[4:8]
    return formata_telefone
telefone = ""
while len(telefone) < 8:
    telefone = input("Digite seu telefone (apenas números): ")
    telefone_formatado = formata_telefone(telefone)







civil = int(input("""
Qual e o seu estado civil:
1° Solteiro
2° Casado
3° Divorciado
4° Viúvo
5° Separado judicialmente
6° União Estável
"""))
escolar = int(input("""
Qual e a sua escolaridade:
1° Analfabeto
2° Ensino Fundamental Incompleto/Completo
3° Ensino Médio Incompleto/Completo                   
4° Ensino Técnico
5° Ensino Superior Incompleto/Completo
6° Pós-Graduação
7° Outros Cursos
"""))
profissao = str(input("Digite sua profissão: "))
saude = str(input("Possui algum problema de saude [S/N]: ")).lower()


nascimento = atual - idade
anolist = nascimento + 18

print(f"Nome: {nome}")

if idade == 18:
    print("Você está na idade de se alistar.")
elif idade < 18:
    print(f"Você nasceu em {nascimento}. Pode se alistar a partir de {anolist}.")
elif 18 < idade <= 29:
    print("Você passou da idade de se alistar.")
else:
    print("Você pode ter que pagar multa por não se alistar.")

if estado == 1:
    print("Alagoas")
elif estado == 2:
    print("Pernambuco")
elif estado == 3:
    print("São Paulo")
elif  estado == 4:
    print("Rio de Janeiro")

print("CPF:", cpf_formatado)

print("Telefone: ", telefone_formatado)


if civil == 1:
    print("Solteiro")
elif civil == 2:
    print("Casado")
elif civil == 3:
    print("Divorciado")
elif civil == 4:
    print("Viúvo")
elif civil == 5:
    print("Separado judicialmente")
elif civil == 6:
    print("União Estável")


if escolar == 1:
    print("Analfabeto")
elif escolar == 2:
    print("Ensino Fundamental Incompleto/Completo")
elif escolar == 3:
    print("Ensino Médio Incompleto/Completo ")
elif escolar == 4:
    print("Ensino Técnico")
elif escolar == 5:
    print("Ensino Superior Incompleto/Completo")
elif escolar == 6:
    print("Pós-Graduação")
elif escolar == 7:
    print("Outros Cursos")
    
print("Profissão: ", profissao)




if saude == "s":
    print("Possui problema de saúde")
elif saude == "n":
    print("Não possui problema de saúde")
else: 
    print("Error")
