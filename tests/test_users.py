import requests


from src.baseclasses.response_users import Response
from src.schemas.user import User

def test_get():
    resp = requests.get(SERVICE_URL)
    print(resp.json())


def test_get_state():
  resp = requests.get(SERVICE_URL)
  print(resp.__getstate__()) #метод вернет доп данные (нр, системную информацию)
  print(resp.url)

# {
#   '_content': b
#   '{"meta":{"pagination":{"total":2957,"pages":296,"page":1,"limit":10,"links":{"previous":null,"current":"https://gorest.co.in/public/v1/users?page=1","next":"https://gorest.co.in/public/v1/users?page=2"}}},"data":[{"id":7938835,"name":"Deevakar Nayar","email":"deevakar_nayar@abshire.test","gender":"female","status":"inactive"},{"id":7938834,"name":"Achintya Ganaka","email":"achintya_ganaka@becker-frami.test","gender":"female","status":"active"},{"id":7938833,"name":"Arya Dubashi","email":"arya_dubashi@hilpert.test","gender":"male","status":"active"},{"id":7938832,"name":"Charumati Desai","email":"charumati_desai@pfannerstill.test","gender":"male","status":"active"},{"id":7938831,"name":"Padma Deshpande","email":"padma_deshpande@heaney.test","gender":"male","status":"inactive"},{"id":7938830,"name":"Divakar Butt","email":"divakar_butt@hayes-ward.test","gender":"male","status":"inactive"},{"id":7938829,"name":"Triloki Varrier","email":"triloki_varrier@dietrich.example","gender":"female","status":"inactive"},{"id":7938828,"name":"Bhadran Pillai","email":"bhadran_pillai@spencer.test","gender":"male","status":"active"},{"id":7938827,"name":"Indira Abbott IV","email":"iv_indira_abbott@rogahn.example","gender":"female","status":"active"},{"id":7938826,"name":"Mani Devar","email":"mani_devar@jacobson-schmitt.test","gender":"male","status":"inactive"}]}',
#   'status_code': 200,
#   'headers': {
#     'Date': 'Mon, 09 Jun 2025 20:24:56 GMT',
#     'Content-Type': 'application/json; charset=utf-8',
#     'Transfer-Encoding': 'chunked',
#     'Connection': 'keep-alive',
#     'Cache-Control': 'max-age=0, private, must-revalidate',
#     'Etag': 'W/"6888e78d64d95e35c7873c78c2b7ec0a"',
#     'Feature-Policy': "camera 'none'; gyroscope 'none'; microphone 'none'; usb 'none'; fullscreen 'self'",
#     'Referrer-Policy': 'strict-origin-when-cross-origin',
#     'Vary': 'Origin',
#     'X-Content-Type-Options': 'nosniff',
#     'X-Download-Options': 'noopen',
#     'X-Frame-Options': 'SAMEORIGIN',
#     'X-Permitted-Cross-Domain-Policies': 'none',
#     'X-Request-Id': '6252a08e-13af-4c09-9a3d-6d5541fa0457',
#     'X-Runtime': '0.025628',
#     'X-Xss-Protection': '0',
#     'Cf-Cache-Status': 'DYNAMIC',
#     'Nel': '{"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}',
#     'Report-To': '{"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=Dqe3vVmjxxTQDjJOXw%2BnT99ti4fj8KVWv0TlLHoW8lCm7Jl9aGyBctlTb2f8gN3dnoUeNR5T3P4RxY1Om8pyu9gjMinrp45l671Duw%3D%3D"}]}',
#     'Content-Encoding': 'gzip',
#     'Server': 'cloudflare',
#     'CF-RAY': '94d35af7bca7f351-ARN',
#     'alt-svc': 'h3=":443"; ma=86400'
#   },
#   'url': 'https://gorest.co.in/public/v1/users',
#   'history': [],
#   'encoding': 'utf-8',
#   'reason': 'OK',
#   'cookies': <RequestsCookieJar[]>, 'elapsed': datetime.timedelta(microseconds=364367), 'request': <PreparedRequest [GET]>
# }


def test_getting_users_list(get_users): #при выполнении теста pytest найдет файлик conftest и среди всех промаркированных фикстур найдет функцию с именем say_hello, запускает ДО теста
  #после выполнения фикстуры pytest положит результа ее выполнения
  Response(get_users).assert_status_code(200).validate(User)


# z = {
#   "meta": #в мета обычно содержится общая информация, тех инфа для фронта для пагинации
#     {
#     "pagination": {
#       "total": 2959,
#       "pages": 296,
#       "page": 1,
#       "limit": 10,
#       "links": {
#         "previous": null,
#         "current": "https://gorest.co.in/public/v1/users?page=1",
#         "next": "https://gorest.co.in/public/v1/users?page=2"
#       }
#     }
#   },
#   "data": #инфа для отображения фронта по объектам
#     [
#     {
#       "id": 7938836,
#       "name": "Balamani Bandopadhyay",
#       "email": "balamani_bandopadhyay@koepp-hand.test",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 7938835,
#       "name": "Deevakar Nayar",
#       "email": "deevakar_nayar@abshire.test",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 7938834,
#       "name": "Achintya Ganaka",
#       "email": "achintya_ganaka@becker-frami.test",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 7938833,
#       "name": "Arya Dubashi",
#       "email": "arya_dubashi@hilpert.test",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 7938832,
#       "name": "Charumati Desai",
#       "email": "charumati_desai@pfannerstill.test",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 7938831,
#       "name": "Padma Deshpande",
#       "email": "padma_deshpande@heaney.test",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 7938830,
#       "name": "Divakar Butt",
#       "email": "divakar_butt@hayes-ward.test",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 7938829,
#       "name": "Triloki Varrier",
#       "email": "triloki_varrier@dietrich.example",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 7938828,
#       "name": "Bhadran Pillai",
#       "email": "bhadran_pillai@spencer.test",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 7938827,
#       "name": "Indira Abbott IV",
#       "email": "iv_indira_abbott@rogahn.example",
#       "gender": "female",
#       "status": "active"
#     }
#   ]
# }