from flask import Request, Response
from typing import Callable, Any
from infra.db.db_context import Connection, execute_connect
from infra.dependency_injector import container
from traceback import format_exc


def check_form_data(request: Request, check_params):

    def decorator(fn):

        def wrapper(*args, **kwargs):

            try:
                if check_params(request):
                    return fn(*args, **kwargs)
            except Exception:
                return {}

        return wrapper
    return decorator



# def services_decorator(request: Request, get_service: Callable, get_method: Callable, data_base: str, type_service: str) -> Callable:
def services_decorator(*args) -> Callable:

    request, check_params, get_service, data_base, type_service = args

    def decorator(func: Callable) -> Callable:

        def wrapper() -> Response:

            conn: Connection | None = None

            result: dict = {}

            try:

                conn = execute_connect(data_base)

                result = func(check_params(request),
                                services=get_service(container(conn.cursor()), type_service))

            except Exception:
                # TODO: Criar funcionalidade para armazenar log de erros
                print(format_exc())
                result.update({"data": "Erro no servidor", "status_code": 500})
                if conn:
                    conn.rollback()
            else:
                conn.commit()
            finally:

                if conn:
                    conn.close()

                return Response(result["data"],
                                status=result["status_code"],
                                mimetype='application/json')

        return wrapper

    return decorator
