from pydantic import BaseModel, validator, field_validator, ValidationError, Field


class Post(BaseModel):
    id: int
    title: str
    #name: str = Field(alias= '_name')

    # описали модель коротко в сравнении с jsonschema
    # если имя начинается с нижн подчеркивания - не сможем его провалидировать, будет считаться приватной переменной
    # записываем через элиас - из джейсона будем парсить
    # можем писать свои валидаторы

    @field_validator('id')
    def check_that_id_is_less_tha_two(cls, v):
        if v > 2:
            raise ValidationError('Id is not less than two')
        else:
            return v
    # либо написать валидацию в 1 строчку id: int = Field(le=2)


# {'id': 1, 'title': 'Post 1', '_name':'Igor'}
