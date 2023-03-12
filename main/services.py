from sqlite3 import Cursor, connect, Connection


def new_costumer_values() -> tuple:
    name = input('Nome: ').strip()
    cpf = input('CPF:').strip()
    data_nascimento = input('data de nascimento (DD/MM/AAAA): ').strip()
    endereco = input('Endereço: ').strip()
    return (name, cpf, data_nascimento, endereco)


def update_costumer_values(costumer, ID: int) -> tuple:

    result = costumer['get_costumer_by_id'](ID)

    values_dict = {
        'nome': result[1],
        'cpf': result[2],
        'data_nascimento': result[3],
        'endereço': result[4], }

    print(result, '\n dê enter para manter os valores atuais.')
    for key in values_dict:
        novo_valor = input(f"novo valor para {c}: ").strip()
        if novo_valor != "":
            dados[key] = novo_valor

    return (values_dict['nome'],
            values_dict['cpf'],
            values_dict['data_nascimento'],
            values_dict['endereço'], ID)
