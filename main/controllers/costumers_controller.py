from typing import Callable


def costumer_controller(services: Callable):

    @services
    def create(*args, **kwargs) -> dict:

        print("args>>>>>>>", args)

        # name
        # cpf
        # data_nascimento
        # endereco = args

        # services = kwargs
        # services["add"](args)

        return {"message": "Cliente cadastrado com sucesso"}

    @services
    def get_costumer(*args, **kwargs):

        services = kwargs

        costumers = services["all"]()

        return {"costumers": costumers}

    return {'create': create,
            'get_costumer': get_costumer}