path='test.txt'
d={'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
def save_credentials_users(path, users_info):
    with open(path,'wb') as my_file:
        for key, value in users_info.items():
            my_list=f'{key}:{value}\n'
            bt=my_list.encode()
            my_file.write(bt)


save_credentials_users(path,d)          