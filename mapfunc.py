list2={3,9,8,6,12}

def sqr(x):
    return x * x

a = list(map(sqr,list2))
print(a)

#for using lambda and map together 
print(list(map(lambda x: x*2 ,list2)))