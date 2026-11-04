# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

#for x in newval:
    #newVal2 = print(x)
# write the list comprehension equivalent to the `for` loop

newval2 = [ print(x) for x in newval]
neval = [ print(x) for x in newval]
# does this exact same thing the for loop does also takes up way less lines