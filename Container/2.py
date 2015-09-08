al = ['A', 'B', 'C', 'D']

print(len(al)) # 4
al.append('E')

print(al) #['A', 'B', 'C', 'D', 'E']
print('A' in al) # True

del(al[0])
print(al) #['B', 'C', 'D', 'E']
print('A' in al) # False

print(min(al)) # B
print(max(al)) # E

al.reverse()
print(al) # ['E', 'D', 'C', 'B']
