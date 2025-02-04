# 1c
# Alternativt namn på fun1: multiply
def fun1(x, y):
    return x * y

return_value = fun1(3, 5)
print(return_value)

# 1d
def fun2(i):
    return 5 * i

x = 2
y = 3
fx = fun2(x)  # fun2(2) == 5 * 2 == 10
fy = fun2(y)  # fun2(3) == 5 * 3 == 15
a = fun2(fx + fy)  # fun2(10 + 15) == fun2(25) == 5 * 25 == 125

# 1e
a = 5
def fun3(a):
    a += 1

a += 2
print(a)
