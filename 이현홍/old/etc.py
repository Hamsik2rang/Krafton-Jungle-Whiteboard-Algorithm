lst1 = ["a", "b", "c"]
lst2 = ["b", "c", "a"]
lst3 = ["c", "a"]
lambdaMix = list(map(lambda x, y, z: x + y + z, lst1, lst2, lst3))
# print(lambdaMix)

string1 = "A-yo man!"
string2 = "What's up?"
string3 = "How to survive jungle?"
lamdaString = "".join(list(map(lambda x, y, z: x + y + z, string1, string2, string3)))
# print(lamdaString)

numbers = list(range(1, 100))
*a, b, c = numbers
# print(a, b, c)
a, *b, c = numbers
# print(a, b, c)
a, b, *c = numbers
# print(a, b, c)


lambdaSum = list(map(lambda x, y: x + y, numbers[::2], numbers[1::2]))
# print(lambdaSum)

tplLst = [(1, 2), (3, 4), (5, 6)]
# try:
#     a, c, e = tplLst
#     print(a, c, e)
# except:
#     print("try1: error")


""" unpack from 2D list """
# try:
#     a, b, c, d, e, f = tplLst
#     print(a, b, c, d, e, f)
# except:
#     print("try2: error")

""" unpack from tuples """
# try:
#     a, c, e = tplLst
#     a, b, c, d, e, f = a, c, e
#     print(a, b, c, d, e, f)
# except:
#     print("try3: error")

""" unpack from unpacked tuple"""
# try:
#     a, c, e = tplLst
#     a, b, c, d, e, f = *a, *c, *e
#     print(a, b, c, d, e, f)
# except:
#     print("try4: error")

""" list comprehension """
# try:
#     a, b, c, d, e, f = [element for sublst in tplLst for element in sublst]
#     print(a, b, c, d, e, f)
# except:
#     print("try5: error")
# tmp = [tplLst]
# try:
#     tmp = [tplLst]
#     a, b, c, d, e, f = [element for sublst in tmp for subtpl in sublst for element in subtpl]
#     print(a, b, c, d, e, f)
# except:
#     print("try5.1: error")

""" sum ??? """
# try:
#     a, b, c, d, e, f = sum(tplLst, ())
#     print(a, b, c, d, e, f)
# except:
#     print("try6: error")


""" itertools.chain - unpack 1D"""
# from itertools import chain

# tmp = [tplLst]
# print(tmp)
# print(list(chain.from_iterable(tmp)))
# print(list(chain.from_iterable(chain.from_iterable(tmp))))
# test = [1, 2, 3, tplLst]
# print(test)
# print(list(chain.from_iterable(test)))
