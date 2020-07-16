import vk
def vk_create_post(message):
    login = '' #логин
    pswd = '' #пароль
    app = ''  #vk приложение
    owner_id = '' #id группы со знаком -
    session = vk.AuthSession(app_id = app, user_login = login, user_password = pswd, scope='wall') #авторизация
    api = vk.API(session) #сессия
    api.wall.post(owner_id = owner_id, friends_only = 0, message = message, attachments = message, v = '5.120') #отправка на стену в группе вк

vk_create_post('Содержание поста')
