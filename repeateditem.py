my_tuple = (1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 3)
item_count = {}
for item in my_tuple:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1
print("Repeated items are:")
for item, count in item_count.items():
    if count > 1:
        print(item)
