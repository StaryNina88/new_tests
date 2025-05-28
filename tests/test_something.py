import requests

from configuration import SERVICE_URL

# from src.enums.global_enums import GlobalErrorMessages
# from src.baseclasses.response import Response
# #from src.schemas.post import POST_SCHEMA
# from src.pydantic_schemas.post import Post
#
# def test_getting_posts():
#     r = requests.get(url=SERVICE_URL)
#     response = Response(r)
#     #response.assert_status_code(400).validate(POST_SCHEMA)
#     response.assert_status_code(200).validate(Post)
#
#
#
#
#     #print(received_posts)
#     #assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
#     # валидируем статус код ответа
#     #assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
#     # валидируем количество полученных постов в ответе
#     #for item in received_posts:
#         #validate(item,POST_SCHEMA)
#     # валидируем схему, будем массивом идти по полученным постам и передавать validate
#     # Сначала пишем assert, ключевое слово, потом то, что между собой сравниваем, слева ответ который пришел в тесте, а справа то что ожидаем
#     # Если указанное условие ложно (False), assert вызывает исключение AssertionError, сигнализируя разработчику о потенциальной ошибке.
#     # Сообщение: позволяет дополнительно передавать строку сообщения об ошибке для пояснения причины сбоя утверждения.
#
# #ответ с постами
# #[{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
# #массив, объекты, в них id и title, такой контракт, мы его должны проверить

def test_get():
    resp = requests.get(f'{SERVICE_URL}/todos')
    print(resp.json())