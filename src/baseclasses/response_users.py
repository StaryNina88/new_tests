from jsonschema import validate #validate - метод который будет валидировать нашу jsonschema


from src.enums.global_enums import GlobalErrorMessages

class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data') #добавили data из ответа метода
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            # если у нас объект это список то проверь так - для каждой единицы ответа проверь схему котр мы приняли на вход
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self #GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, self #GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self #чтоб возвращали сами себя

    def __str__(self): #magic method помогает описать представление объекта класса, например отобразить в консоли
        return \
            f'\nStatus code: {self.response_status} \n' \
            f'Requested url: {self.response.url} \n' \
            f'Response body: {self.response_json}'


