def test_func(compute):
    res = compute(1,2)
    return res

def add(x,y):
    return  x+y
##################################
res1 = test_func(add)
print(res1)

res2 = test_func(lambda x,y:x+y)
print(res2)
