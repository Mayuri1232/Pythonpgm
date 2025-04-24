my_dict = {'apple': 10, 'banana': 3, 'cherry': 7, 'date': 5, 'kiwi': 2}


def get_value(item):
    return item[1]


asc = sorted(my_dict.items(),key=get_value)
print("Ascending:", asc)


desc = sorted(my_dict.items(),key=get_value, reverse=True)
print("Descending:", desc)