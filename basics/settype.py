s={10,20,30,"XYZ",10,20,10}
#add to set
s.update([88,99])

print(type(s))

#You can not have duplicates in set, can not uses indexing, slicing, or repitition

s.remove(30)
print(s)
#frozen sets can't have values removed or updated
f=frozenset(s)