path='test.txt'
def get_credentials_users(path):
    with open(path,'rb') as file:
        my_list=[]
        for i in file:
            s=i.strip().decode()
            my_list.append(s)
    
        
    return my_list   

print(get_credentials_users(path))