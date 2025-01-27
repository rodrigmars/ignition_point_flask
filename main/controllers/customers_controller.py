from typing import Callable
from flask import request
from utils.enum_utils import TypeException


def customers_controller(controller: Callable) -> dict:

    @controller
    def create(services: dict) -> tuple:

        if request.headers['Content-Type'] != 'application/json':
            raise Exception(TypeException.CUSTOMER,
                            {"error": 'Header Error'}, 415)

        customer = tuple(request.get_json().values())

        services["add"](customer)

        return "Cliente cadastrado com sucesso", 200

    @controller
    def get_customers(services: dict) -> tuple:

        return {"customers": services["all"]()}, 200

    @controller
    def get_by_id(services: dict, **kwargs: dict) -> tuple:

        return {"customer": services["get_by_id"]((kwargs.get("customer_id"),))}, 200

    @controller
    def get_by_cpf(services: dict, **kwargs: dict) -> tuple:

        return {"customer": services["get_by_cpf"]((kwargs.get("cpf"),))}, 200

    @controller
    def get_by_name(services: dict, **kwargs: dict) -> tuple:
    
        return {"customer": services["get_by_name"]((kwargs.get("name"),))}, 200

    return {'create': create,
            'all': get_customers,
            'get_by_id': get_by_id,
            'get_by_cpf': get_by_cpf,
            'get_by_name': get_by_name}
