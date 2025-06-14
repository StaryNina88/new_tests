from pydantic import BaseModel, validator, field_validator
from src.enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel): #базовый класс в pydantic, от кот мы наследуемся
    id: int = 0 #если ничего нет то будет 0, если не написать то поле будет обязательным
    name: str
    email: str
    gender: Genders
    status: Statuses

    @field_validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)