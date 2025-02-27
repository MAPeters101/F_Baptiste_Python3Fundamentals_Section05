l1 = [1,2,3]
l2 = l1[:]
print(l1)
print(l2)
print(l1 is l2)
l2.append(10)
print(l1)
print(l2)
print('-'*80)

l3 = l1.copy()
print(l1)
print(l3)
print(l1 is l3)
l3.append(10)
print(l1)
print(l3)
print('-'*80)

