tup1=(1,2,3,4,5,2,3)
rep=[]
for i  in tup1:
    if tup1.count(i)>1 and i not in rep:
        rep.append(i)

print("repeated items are:",rep)