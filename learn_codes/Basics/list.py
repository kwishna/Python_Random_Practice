l = [1, 2, 'A', True, None, 'Hello']
print(l)

k = l[5][0] # It Goes To 5th Index, Finds A String. Then Finds 0th Index Of The String.
print(k)
print(l[::2]) # From 0 To Full, With Step 2
# print(l.clear())
# print(l)  # Prints Blank List. Means List Is Mutable
l[:2] = [3, 4]
print(l)

p=[]
p.append('Mouse') # Adds At The End
print(p)

m = l.copy()
print(m)

n = l + m
print(n)

l.insert(1, 'Computer')
print(l)



