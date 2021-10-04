import pytest


@pytest.fixture
def tester():
    name = "Manjil"
    email = "abc@gmail.com"
    password = "Password123"
    return (name, email, password)


def test1(tester):
    first_name = "Manjil"
    assert tester[0] == first_name


def test2(tester):
    email = "abc@gmail.com"
    assert tester[1] == email


def test_3(tester):
    password_check = "Password123"
    assert tester[2] == password_check
