s1='klmshoppingmallklmjewelleryklmlehanklmgasklm'
s2='klm'
k=0
c=0
ac=0
for i in s1:
    if s2[k]==i:
        c+=1
        k+=1
    if c==len(s2):
        k=0
        c=0
        ac+=1
print(ac)
