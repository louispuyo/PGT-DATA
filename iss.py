
listok = [3, 4, 2, 76, 2, 3, 5, 2, 2, 2, 4, 2, 3, 3, 43, 35, 46546,
          4, 6, 464, 4, 6, 4, 64, 4, 6, 46, 4, 456, 56, 4, 5645]

notOK = frozenset(listok)
print(notOK)
print('frozenset convert a list or a tuple into a dict',
      type(notOK))
hell_word = hasattr(listok, 'e')
print(hell_word)

listok = list(reversed(listok))
print(listok)

print(3 << 45)
print(39 << 83)


comment = '''
filter function take obviously a function and an iterable
'''


def filter_function(x):
    x = abs(x)
    ls = [i for i in range(x) if i > 100]
    return ls


seletion = list(filter(filter_function, listok))
print(seletion)

print([x for x in (iter(listok))])

re_file = file.read()
cache = bytearray(re_file, 'utf-8')
memo_stk = memoryview(cache)
print(memo_stk)
delattr(obj, 'act')
try:
    print(obj.act)
except:
    AttributeError
print(obj.co)


restult = obj(38)._return_square()
