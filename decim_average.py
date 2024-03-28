from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec=signs_count
    total=Decimal(0)
    for i in number_list:
        total+=Decimal(i)
    b=len(number_list)
    average=Decimal(total)/Decimal(b)
    return average






print(decimal_average([3, 5, 77, 23, 0.57], 6))