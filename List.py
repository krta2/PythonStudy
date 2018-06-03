print(type('egoing')) #<class 'str'>
name = 'egoing'
print(name) #egoing
print(type(['egoing', 'leezche', 'graphittie'])) #<class 'list'>
names = ['egoing', 'leezche', 'graphittie']
print(names) 
print(names[2]) #graphittie
egoing = ['programmer', 'seoul', 25, False]
egoing[1] = 'busan'
print(egoing) #['programmer', 'busan', 25, False]

al = ['A', 'B', 'C', 'D']
print(len(al)) # 4
al.append('E')
print(al) #['A', 'B', 'C', 'D', 'E']
del(al[0])
print(al) #['B', 'C', 'D', 'E']