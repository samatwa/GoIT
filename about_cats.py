import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

a=[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
b=[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
def convert_list(cats):
    my_list=[]
    for i in cats:
        if isinstance(i,dict):
            my_list.append(Cat(nickname=i["nickname"],age=i["age"],owner=i["owner"]))

        elif isinstance(i,tuple):
            d={}
            d["nickname"]=i.nickname
            d["age"]=i.age
            d["owner"]=i.owner
            my_list.append(d)

    return my_list

print(convert_list(b))