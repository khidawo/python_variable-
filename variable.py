#an integer assignment
age=45
#a floating point
salary=16222.83
#a string
student="John"

print(age)
print(salary)
print(student)

#assigning a sinlge value to multiple variables
a=b=c=39
print(a)
print(b)
print(c)

#assigning a different values to multiple variables
a,b ,c =23, 34.3,"love python"
print(a)
print(b)
print(c)

#uses global because there is no local "a"
def f():
    print('insisde f(): ',a)
#variable 'a'  is redefined as a local   
def g():
    global
    a=56
    print('inside g():',a)
#uses global keyword to modify global 'a'    
def h():
    global 
    a=443
    print('inside h():',a)

#global scope
print('global:',a) 
f()   
print('global:',a)
g()

print('global:',a)rint('global:',a)
h()