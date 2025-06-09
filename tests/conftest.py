import pytest
import requests

from configuration import SERVICE_URL

@pytest.fixture(scope = 'session')#можно добавлять параметры например (scope = 'function' - исп.по умолчаюнию, означет что фикстура каждый раз будет выоплняться)
#параметр scope = 'session' - будет возвращаться 1 и тот же результат, единожды что-то сделали и результат кэшируется, чтоб не перегружать систему
#параметр afteruse - по умолчанию false, true - будет выполняться для каждого нашего теста, если не указывать фикстуру в автотестах
def get_users():
    response = requests.get(SERVICE_URL)
    return response
