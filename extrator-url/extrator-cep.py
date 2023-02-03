import re
endereco = "Rua das flores 72, apartamento 1002, Laranjeira, Rio de Janeiro, RJ, 43 9 8817-0261"

padrao = re.compile("[0-9]{2}[ ]{1}[9]{1}[ ]{1}[0-9]{4}[-]{1}[0-9]{4}")
busca = padrao.search(endereco)

if busca:
    telefone = busca.group()
    print(telefone)


