int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print("1")
print("int_a id is ",id(int_a)," , ","str_b id is ",id(str_b)," , ",
      "set_c id is ",id(set_c)," , ","lst_d id is ",id(lst_d)," , ",
      "dict_e id is ",id(dict_e))

print('\n',"2")
lst_d.append(4)
lst_d.append(5)
print("lst_d after append is ",lst_d)
print("lst_d id after append is ",id(lst_d))

print('\n',"3")
print("int_a is ",type(int_a),", ","str_b is ",type(str_b),", ",
      "set_c is ",type(set_c),", ","lst_d is ",type(lst_d),", ",
      "dict_e is ",type(dict_e))

print('\n',"4")
print(isinstance(int_a,int))
print(isinstance(str_b,str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

print('\n',"5")
print("Anna has {} apples and {} peaches.".format(2,3))

print('\n',"6")
print("Anna has {0} apples and {1} peaches.".format("three","one thousand"))

print('\n',"7")
print("Anna has {b1} apples and {b2} peaches.".format(b1="three",b2="one thousand"))

print('\n',"8")
print("Anna has {0:>5s} apples and {1:>3s} peaches.".format("three","one thousand"))

print('\n',"9")
var1="three"
var2="one thousand"
print(f"Anna has {var1} apples and {var2} peaches.")

print('\n',"10")
var1="three"
var2="one thousand"
print('Anna has %s apples and %s peaches.' % (var1,var2))

print('\n',"11")
var1="three"
var2="one thousand"
data_dict={"one": var1, "two": var2}
print('Anna has %(one)s apples and %(two)s peaches.' % data_dict)

print('\n',"12")
print("before")
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
print("after")
lst=[num**2 if num%2==1 else num ** 4 for num in range (10)]
print(lst)

print('\n',"13")
print("before")
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
print("after")
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)


print(list_comprehension)

print('\n',"14")
print("before")
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
print("after")
d1={num: num**2 for num in range (1,11) if num%2==1}
print(d1)

print('\n',"15")
print("before")
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
print("after")
d1={num: num**2 if num%2==1 else num//0.5 for num in range (1,11)}
print(d1)

print('\n',"16")
print("before")
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
print("after")
d1={}
for x in range(10):
    if x**3%4==0:
        d1[x]=x**3
print(d1)

print('\n',"17")
print("before")
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
print("after")
d1={}
for x in range(10):
    if x**3%4==0:
        d1[x]=x**3
    else:
        d1[x]=x
print(d1)

print('\n',"18")
print("before")
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(1,2))
print("after")
foo1=lambda x,y:x if (x<y) else y
print(foo1(1,2))

print('\n',"19")
print("before")
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(1,2,3))
print("after")
def foo1 (x,y,z):
    if y<x and x>z:
        return z
    else:
        return y
print (foo1(1,2,3))

import functools
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print('\n',"20")
print("old list ",lst_to_sort)
print("sorted min to max ",sorted(lst_to_sort))

print('\n',"21")
print("old list ",lst_to_sort)
print("sorted max to min ",sorted(lst_to_sort, reverse=True))

print('\n',"22")
print("old list ",lst_to_sort)
new_lst=list(map(lambda x:x*2,lst_to_sort))
print("multiplied elements by 2 ", new_lst)

print('\n',"23")
list_A=[2,3,4]
list_B=[5,6,7]
print("list A",list_A)
print("list B",list_B)
new_lst=list(map(lambda x,y:x**y,list_A,list_B))
print("raised list",new_lst)

print('\n',"24")
print("old list ",lst_to_sort)
new_lst=list(filter(lambda x:(x%2==1),lst_to_sort))
print("list filtered by x%2==1 ", new_lst)

print('\n',"25")
b= list(range (-10,10))
print(b)
new_lst=list(filter(lambda x:(x<0),b))
print(new_lst)

print('\n',"26")
list_1=[1,2,3,5,7,9]
list_2=[2,3,5,6,7,8]
new_lst=list(filter(lambda x:(x in list_2),list_1))
print(new_lst)
