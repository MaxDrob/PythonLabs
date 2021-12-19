print(dir(tuple))
help(list.index)
help(list.count)

seq = (2,8,23,97,92,44,17,39,11,12)
# seq.count(8)
# seq.index(44)
print(seq.count(2))
print(seq.index(12))

listseq = list(seq)
print(listseq)
print("Correct?", type(listseq))

D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
D['food']
D['quantity'] += 10
print(D)


dp = {}
decName =  input("type name: ")
decAge = input("type age: ")
D[decName] = decAge
print(D)



# Storage nesting

rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
'job': ['dev', 'mgr'],
'age': 25
}

print('first name', rec['name']['firstname'])
rec['job'].append('janitor')
print(rec)