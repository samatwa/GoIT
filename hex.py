def formatted_numbers():
    new_list=[]
    new_list.append("|{:^10}|{:^10}|{:^10}|".format('decimal','hex','binary'))
    for i in range(0,16):
        new_list.append('|{:<10}|{:^10}|{:>10}|'.format(i,format(i,'x'),format(i,'b')))
    return new_list
for el in formatted_numbers():
    print(el)