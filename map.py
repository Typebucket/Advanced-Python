list1 = [12, 3, 56, 9, 8]
list2 = [45, 44, 67, 1, 90]
list3 = map(lambda first, second: first+second,list1,list2)
print("The addition of the two list is: ", list(list3))

def newsquare(x):
    return x*x

squaredlist = list(map(newsquare, list2))
print("The new list which has all the squared items is: ", squaredlist)