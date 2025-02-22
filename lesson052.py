s = 'Python rocks!'
print(s[5])
print(s[0:5])
print(s[0:5+1])
print()

t = (1,2,3,4,5)
print(t[1:4])
print(type(t[1:4]))

l = [1,2,3,4,5]
print(l[1:4])
print(type(l[1:4]))
print()

l1 = [1,2,3,4,5]
l2 = l1[0:3]
print(l2)
print(l1 is l2)
l2[0] = 100
print(l2)
print(l1)
print()

l = [[0,0,0], [1,1,1], [2,2,2]]
sub = l[0:2]
print(sub)
print(sub is l)
sub[1] = 'Python'
print(sub)
print(l)
print(sub[0] is l[0])
sub[0][0] = 100
print(sub)
print(l)





