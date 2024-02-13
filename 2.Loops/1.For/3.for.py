# Looping Through Multiple Lists Simultaneously
# You can use the zip() function to iterate over multiple lists simultaneously:

list1 = [1, 2, 3]
list2 = list("abc")

# for i in range(len(list1)):
#     print(list1[i],list2[i])

for item1, item2 in zip(list1,
                        list2):  # it takes two or more data sets and "zips" them together containing pairs of items from the data sets.
    print(item1, item2)
