path='test.txt'
def get_cats_info(path):
    with open(path,'r') as cats:
        info=[]
        for cat in cats:
            d={}
            a=cat.strip().split(',')
            print(a)
            d['id']=a[0]
            d['name']=a[1]
            d['age']=a[2]
            info.append(d)
    return info
print(get_cats_info(path)) 