POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type':'number'},
        'title':{'type':'string'} #можно добавть enum чтоб приходило только указанное значение , {'type':'string', 'enum': ['POST']}
    },
    'required':['id'] #те параметры которые обязательны
}
#[{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]