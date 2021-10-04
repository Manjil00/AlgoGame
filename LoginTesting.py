import pytest

@pytest.fixture
def tester():
    name = "Manjil"
    password = "Password123"
    return (name, password)


def test1(tester):
    first_name = "Manjil"
    assert tester[0] == first_name


def test_2(tester):
    password_check = "Password123"
    assert tester[1] == password_check
