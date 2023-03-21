from pytest import fixture
from main.services.validators.customer_validator import customer_validator

@fixture
def setup() -> tuple:

    return ("Tomas Kaique Assun",
            "942.554.492-10",
            "28/02/2002",
            "Quadra 12 Conjunto F, 311")


def test_name_is_alpha(setup: tuple) -> None:
    print(setup)
    check_data, check_id, check_cpf = customer_validator()

    notifications = check_data(setup)

    assert [] == notifications
