list1 = [12, 34, 6, 57, 9]
list2 = ["gg", 56, 78, "gg", 7]
list3 = list(zip(list1, list2))
print(list3)

for x,y in zip(list1, list2[::-1]):
    print(x,y)

newdic = {list1 : list2 for list1, list2 in zip(list1,list2)}
print(newdic)