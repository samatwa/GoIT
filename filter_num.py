payment = [100, -3, 400, 35, -100]
def positive_values(list_payment):
    return [i for i in filter(lambda i: i>0, list_payment)]


print(positive_values(payment))