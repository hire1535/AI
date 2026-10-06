import itertools
variable=["A","B","C"]
color=["Red","Blue","green"]
all_assignment=itertools.product(color,repeat=len(variable))
def isvalid(i):
    A,B,C=i
    if(A!=B and B!=C and A!=C):
        return True
solution=[]
for i in all_assignment:
    if isvalid(i):
        solution.append(dict(zip(variable,i)))
for sol in solution:
    print(sol)