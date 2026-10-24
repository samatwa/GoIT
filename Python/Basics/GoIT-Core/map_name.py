list_name=['olga','boris','andrei']
def normal_name(list_name):
    return [i for i in map(lambda i: i.title(),list_name)]
print(normal_name(list_name))