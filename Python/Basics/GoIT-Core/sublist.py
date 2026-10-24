data=[[1, 2, 3]]
def all_sub_lists(data):
    sub_lists = [[]]  
    for i in range(len(data)):
        for j in range(i + 1, len(data) + 1):
            sub_lists.append(data[i:j])
    return sorted(sub_lists, key=len)

print(all_sub_lists(data))

