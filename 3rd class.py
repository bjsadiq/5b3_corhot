# def test_function ():
#     print(4*2+2)

# test_function()

# def fun2 (n : int):
#     print(n**2)
# fun2(77)

# def fun3(a,b,c):
#         print(a,b,c)
# fun3(1,2,3)
# fun3(b=1,c=3,a=2)
# fun3(1,b=3,c=2)

# from unittest import result


# def fun2(n:int):
#     global result
#     result = n**2
#     return result
#     # print("I just ran")

# print(fun2(4))

# print(result)



def mean(arr):
    mean_value = sum(arr)/len(arr)
    return round(mean_value, 2)

print("calculate your mean")
print("Enter your numbers seperated by comma")
vals = input(":>").split(',')
print(vals)
mapped = map(int,vals)
print(mapped)



