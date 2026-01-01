#!/usr/bin/env python
# coding: utf-8

# 23/12/2025
# # Chapter-9
# ## Advance OOP & Numpy
# 1. Polymorphism
# - method overloading
# - method overriding
# - operation overloading
# 2. Inheritance
# - different 5 types of inheritance
# - concept of MRO (Method Resolution Order)
# - Abstract class
# ### Numpy
# - creation of Array(Indexing, shaping, slicing)
# - functions on Array.
# 
# ## 1. Polymorphism
# #### Method Overloading
# - Allow programmers to write methods that can process a variety of different types of functionalities with the same name.
# - Method overloading is a compile type polymorphism using which we can define two or more methods in same class with the same name but with a different parameter list.

# In[2]:


def sum_num(*args):
    result=0
    for num in args:
        result+=num
    print("Sum:",result)
print("Similar to method overloading concept")
print("Single Argument --> ",end="")
sum_num(10)
print("Two Argument --> ",end="")
sum_num(10,20)
print("Multiple Argument --> ",end="")
sum_num(10,20,30,40)


# In[8]:


def fun(a):
    print("Hello")
def fun(a,b):
    print("How are you?")
def fun(a,b,c):
    print("Welcome")
fun(10)


# In[9]:


fun(10,20)


# In[10]:


fun(10,20,30)


# #### Method overriding
# - A child class method overrides the parent class method of the same, name, parameters and return type. It is used to overwrite or redefine a parent class method in the derived class.

# In[13]:


class A:
    def first(self):
        print("First function of class A")
    def second(self):
        print("Second function of class A")
class B(A):
    def first(self):   # overridden method
        print("First function of class A in class B")
    def display(self):
        print("Display function of child class")
obj=B()
obj.first()
obj.second()
obj.display()


# #### Operation overloading
# - giving extends meaning beyond their predefined operational meaning.
# - add two integers
# - join two strings
# - merge two lists

# In[15]:


print(2+3)
print("Hi"+"Hello")
print([1,2,3]+[4,5,6])
# Same built in operation shows different behaviour for objects of different classes.


# In[5]:


class D:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
obj1=D(5)
obj2=D(3)
obj3=D("Hello")
obj4=D("Hi")
print(obj1+obj2)
print(obj3+obj4)
print(obj1.__add__(obj2))
print(obj3.__add__(obj4))
print(D.__add__(obj1,obj2))
print(D.__add__(obj3,obj4))


# In[6]:


class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if self.a>other.a:
            return True
        else:
            return False
obj1=A(5)
obj2=A(7)
if obj1>obj2:
    print("obj1 is greater.")
else:
    print("obj2 is greater.")


# ### Mathematical Operations
# - operation    ------------------     Magic Method
#  1.  '+'       ------------------  '__add__(self,other)'
#  2.  '-'       ------------------  '__sub__(self,other)'
#  3.  '*'       ------------------  '__mul__(self,other)'
#  4.  '/'       ------------------  '__truediv__(self,other)'
#  5.  '//'      ------------------  '__floordiv__(self,other)'
#  6.  '%'       ------------------  '__mod__(self,other)'
#  7.  '**'      ------------------  '__Dow__(self,other)'
#  
# ### Comparison Operators
# - operation    ------------------     Magic Method
#  1.  '>'       ------------------  '__gt__(self,other)'
#  2.  '<'       ------------------  '__lt__(self,other)'
#  3.  '>='      ------------------  '__ge__(self,other)'
#  4.  '<='      ------------------  '__le__(self,other)'
#  5.  '=='      ------------------  '__eq__(self,other)'
#  6.  '!='      ------------------  '__ne__(self,other)'

# In[8]:


class A:
    def __init__(self,a):
        self.a=a
    def __mul__(self,other):
        return self.a*other.a
    def __mod__(self,other):
        return self.a%other.a
    def __ge__(self,other):
        if self.a>=other.a:
            return True
        else:
            return False
    def __eq__(self,other):
        if self.a==other.a:
            return True
        else:
            return False
obj1=A(10)
obj2=A(15)
obj3=A(20)
obj4=A(10)
print(obj1.__mul__(obj2))
print(A.__mod__(obj1,obj3))
if obj1>=obj3:
    print("Obj1 is greater or equal.")
else:
    print("Obj3 is greater.")
if obj1==obj4:
    print("Both are equal.")
else:
    print("Both are not equal.")


# ## Inheritance
# - We can use existing class to create a new class rather then creating it from a scratch.
# - Allows the program to reuse the code.
# - With inheritance, child class gains access to all data members, functions and properties defined in the parent class.
# - A child class may also offer its particular implementation of the parent class's functions.
# - A derived class can inherit from its base class by simple putting its name in brackets after the derived class name.
# 
# 1. Single Inheritance (Simple Inheritance):
# ![image.png](attachment:image.png)

# In[9]:


class parent:
    def func1(self):
        print("Hello parent")
class child(parent):
    def func2(self):
        print("Hello child")
obj=child()
obj.func1()
obj.func2()


# 2. Multiple Inheritance: 
# ![image.png](attachment:image.png)

# In[16]:


class parent1:
    def fun1(self):
        print("Parent class1")
class parent2:
    def fun2(self):
        print("Parent class2")
class parent3:
    def fun2(self):
        print("Parent class3")
class child(parent1,parent3,parent2):   # in which sequence we given to child class as per that it gives output.
    # In sequence which come first child class take output from that class(if its method name is same).
    def fun3(self):
        print("Child class")
obj=child()
obj.fun1()
obj.fun2()
obj.fun3()
print(child.__mro__)
# mro shows in which sequence it work or the flow of sequence.
# if in child class there is method name fun2() then child class run it self first. child gives first priority to itself.


# 3. Multilevel Inheritance: 
# ![image.png](attachment:image.png)

# In[18]:


class Grandparent:
    def func1(self):
        print("Hello Grandparent")
class Parent(Grandparent):
    def func2(self):
        print("Hello Parent")
class child(Parent):
    def func3(self):
        print("Hello Child")
obj=child()
obj.func1()
obj.func2()
obj.func3()


# 4. Hierarchical Inheritance:
# ![image.png](attachment:image.png)

# In[24]:


class parent:
    def fun1(self):
        print("Parent class")
class child1(parent):
    def fun2(self):
        print("Child class1")
class child2(parent):
    def fun3(self):
        print("Child class2")
obj1=child1()
obj2=child2()
obj1.fun1()
obj1.fun2()
obj2.fun1()
obj2.fun3()


# 5. Hybrid Inheritance:
# ![image-3.png](attachment:image-3.png)

# In[26]:


class parent1:
    def fun1(self):
        print("Parent class1")
class parent2:
    def fun2(self):
        print("Parent class2")
class child1(parent1):
    def fun3(self):
        print("Child class1")
class child2(child1,parent2):
    def fun4(self):
        print("Child class2")
        
obj=child2()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()


# In[28]:


obj2=child1()
obj2.fun1()
obj2.fun3()


# 24/12/2025
# ## Special functions in python inheritance
# 1. super()

# In[2]:


class parent:
    def __init__(self):
        self.altr1=50
        self.altr2=60
class child(parent):
    def __init__(self):
        super().__init__()
        self.altr3=45
obj=child()
print(obj.altr3)
print(obj.altr1)
print(obj.altr2)


# In[4]:


class parent:
    def display(self):
        print("Parent class")
class child(parent):
    def display(self):
        print("Child class")
        super().display()
obj=child()
obj.display()


# 2. issubclass()

# In[5]:


class parent:
    def fun1(self):
        print("Parent class")
class child(parent):
    def fun2(self):
        print("Child class")
print(issubclass(child,parent))
print(issubclass(parent,child))


# 3. isinstance()

# In[6]:


A=child()
B=parent()
print(isinstance(A,child))
print(isinstance(A,parent))
print(isinstance(B,child))
print(isinstance(B,parent))


# ## Method Resolution Order(MRO)
# - it denotes a way a programming language resolves a method or attributes.
# - MRO defines the order in which the base classes are searched when executing method.
# - First the method is searched within the class and then it follows the order we specified while inheriting.

# In[19]:


class A:
    def rk(self):
        print("Class A")
class B(A):
    def rk(self):
        print("Class B")
class C(A):
    def rk(self):
        print("Class C")
class D(B,C):
    pass
obj=D()
obj.rk()
obj2=C()
obj2.rk()


# In[20]:


D.__mro__


# In[42]:


class p1:
    def foo(self):
        print("foo from p1")
class p2:
    def foo(self):
        print("foo from p2")
    def bar(self):
        print("bar from p2")
class c1(p1,p2):
    pass
class c2(p1):
    def bar(self):
        print("bar from c2")
class c3(p2):
    def bar(self):
        print("bar from c3")
class c4(p1,p2):
    def bar(self):
        print("bar from c4")
class GC1(c1,c2):
    pass
class GC2(c1,c3):
    pass
class GC3(c1,c4):
    pass
obj1=GC1()
obj1.bar()
obj1.foo()
obj2=GC2()
obj2.bar()
obj2.foo()
obj3=GC3()
obj3.bar()
obj3.foo()


# In[45]:


GC1.__mro__


# In[46]:


GC2.__mro__


# In[47]:


GC3.__mro__


# ## Abstract class
# 
#     from abc import ABC
#     class class_name(ABC):
#         #body of the class
#     abc -> abstract base class

# In[67]:


from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,shape_name):
        print("1")
        self.shape_name=shape_name
    @abstractmethod
    def draw(self):
        print("2")
        print("Drawing:",self.shape_name)


# In[68]:


obj=shape()
obj.draw()
# Abstract class does not have any object. It is only a blueprint.


# In[71]:


class Circle(shape):
    def __init__(self):
        super().__init__("circle")
        print("3")
    def draw_circle(self):
        print("4")
        print("Drawing:",self.shape_name)
    def draw(self):
        print("5")
        pass
obj=Circle()
obj.draw_circle()
# it gives error when you write draw_circle method only
# abstract class ni badhi j method e class ma hovi joi jama tama abstract class bolavo cho ama


# In[86]:


class Book:
    def __init__(self,name,no_of_author,list_of_author,publisher,ISBN,year):
        name=(input("Enter your name:"))
        no_of_author=int(input("Enter number of authors:"))
        list_of_author=[]
        for i in range(0,no_of_author):
            a=input("Enter the name of author:")
            list_of_author.append(a)
        publisher=input("Enter name of publisher:")
        ISBN=int(input("Enter any number for ISBN:"))
        year=int(input("Enter the year:"))
        self.name=name
        self.no_of_author=no_of_author
        self.list_of_author=list_of_author
        self.publisher=publisher
        self.ISBN=ISBN
        self.year=year
    def display(self):
        print("--------------INFO------------------")
        print("Name:",self.name)
        print("Number of authors:",self.no_of_author)
        print("List of authors:",self.list_of_author)
        print("Publisher:",self.publisher)
        print("ISBN:",self.ISBN)
        print("Year:",self.year)
        print("-----------------------------------")
class courseBook(Book):
    def __init__(self,course_name):
        super().__init__(name,no_of_author,list_of_author,publisher,ISBN,year)
        self.course_name=course_name
    def display(self):
        super().display()
        print("Course Name:",self.course_name)

course_name=input("Enter the course name:")
obj=courseBook(course_name)
obj.display()


# 26/12/2025 

# In[15]:


class Products:
    menu={'HDD':5000,"RAM":2000,'Printer':6000,'Pendrive':800}
    price={'HOD':0,'RAM':0,'Printer':0,'Pendrive':0}
       
    for i,j in menu.items():
        print(i,j)
        a=input("You want this item?(y/n):")
        if a.lower()=='y':
            q1=int(input("Enter the quantity:"))
            price[i]=q1*j
        elif a.lower()=='n':
            pass
        else:
            print("Invalid input")
        print()

            
    def __init__(self):
        print("1. Cash payment")
        print("2. Cheque payment")
        p=int(input("Which payment method do you like?"))
        if p==1:
            cashpayment()
            
        elif p==2:
            chequepayment()
            
        else:
            print("Invalid input")
        
        
class cashpayment(Products):
    def __init__(self):
        print()
        print("Payment method is Cash Payment")
        sum=0
        for x in self.price.values():
            sum+=x
        print("Total payment is:",sum)
        d={'2000 Rs. Notes':2000,'500 Rs. Notes':500,'200 Rs. Notes':200,'100 Rs. Notes':100,'50 Rs. Notes':50,'20 Rs. Notes':20,'10 Rs. Notes':10}
        print()
        for i,j in d.items():
            if sum>=j:
                print(i+":",sum//j)
                sum=sum%j
            
class chequepayment(Products):
    def __init__(self):
        print()
        print("Payment method is Cheque Payment")
        sum=0
        for x in self.price.values():
            sum += x
        print("Total Payment is:",sum)
        print()
        Chq_No = int(input("Enter Cheque Number:"))
        Bank = input("Enter Bank Name:")
        print()
        print("Cheque Details:")
        print("Cheque Number:",Chq_No)
        print("Bank Name:",Bank)
        

customer=Products()


# # Numpy
# - Numpy = Numerical Python

# In[16]:


import numpy as np
import sys
 
#List
s=range(1000)
print("Size of Each element of list in bytes:",sys.getsizeof(s))
print("Size of Whole list in bytes:",sys.getsizeof(s)*len(s))


# In[18]:


#Array
d=np.arange(1000)
print("Size of Each element of Numpy array in bytes:",d.itemsize)
print("Size of Whole Numpy array in bytes:",d.itemsize*d.size)


# In[21]:


import numpy as np
arr=np.array(42)
print(arr)
print(type(arr))
print(arr.ndim)   #dim means dimenssion


# In[21]:


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
# difference between array and list is comma
print(list(arr))
print(type(arr))
print(arr.ndim)


# In[23]:


import numpy as np
arr=np.array([[1,2,3,4,5]])
print(arr)
print(type(arr))
print(arr.ndim)


# In[41]:


import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])  # 1 list x 2 list x 2 list x 3 elements = 12
print(arr)
print(type(arr))
print(arr.ndim)
print(arr[0,1,1])
print(arr[1,0,2])
print(arr[-2,-2,-2])
print(arr[0:2,0:2,0:2])
print(arr.shape)


# In[27]:


import numpy as np
arr=np.array([[[1,2,3],[4,5]],[[7,8,9],[10,11,12]]])
print(arr)
print(type(arr))
print(arr.ndim)


# In[42]:


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[0])
print(arr[4]+arr[2])
print(arr.shape)
print(arr[5])


# In[31]:


import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(arr[1,3])


# In[32]:


print(arr[1][3])


# In[40]:


import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[:1,:3])   #This is 2 dimenssion because of 2 slicing
print(arr[1,:3])   # This is 1 dimenssion because 1 is index and other is slicing
print(arr[1:])
print(arr.shape)


# In[46]:


import numpy as np
arr=np.array([1,2,3,4,5],ndmin=5)
print(arr)
print(arr.shape)


# In[47]:


import numpy as np
arr=np.array([1,2,3,4,5])
new=arr.reshape(2,3)


# In[50]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
new=arr.reshape(2,3)
print(new)
new=arr.reshape(3,2)
print(new)


# 30/12/2025
# 

# In[57]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
new=arr.reshape(2,3,1)
print(new)
print('------------------')
new=arr.reshape(2,3,1).base
print(new)
print()
new=arr.reshape(2,-1)
print(new)
print()
for x in arr:
    print(x)


# In[9]:


arr=np.array([[1,2,3,4],[5,6,7,8]])
for x in arr:
    print(x)
print()
for x in arr:
    for i in x:
        print(i)


# In[10]:


arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for j in x:
        for i in j:
            print(i)


# In[11]:


arr=np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr):
    print(x)                #with the help of nditer we can fatch all the elements from the array in a single elements.
    # with the help of single loop.


# In[18]:


arr=np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[0:1,::2]):
    print(x)
print()
for x in np.nditer(arr[:,::2]):
    print(x)


# ## Built-in Functions
# 1. concatenate()

# In[19]:


arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr3=np.array([7,8,9])
arr=np.concatenate((arr1,arr2,arr3))
print(arr)


# In[27]:


arr1=np.array([[1,2],[5,6]])
arr2=np.array([[3,4],[7,8]])
arr=np.concatenate((arr1,arr2))
print(arr)
print()
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)


# 2. split 

# In[32]:


arr1=np.array([1,2,3,4])
newarr=np.array_split(arr1,4)
print(newarr)
newarr=np.array_split(arr1,3)
print(newarr)
newarr=np.array_split(arr1,2)
print(newarr)
newarr=np.array_split(arr1,5)
print(newarr)


# In[36]:


arr=np.array([[1,2],[3,4],[5,6],[7,8]])
newarr=np.array_split(arr,4,axis=1)
print(newarr)  # it gives output as column wish combination


# 3. where

# In[38]:


arr1=np.array([1,2,3,4,5,6,4,2,3])
x=np.where(arr1==4)
print(x)
print()
y=np.where(arr1%2==0)
print(y)


# In[40]:


arr1=np.array([[1,2],[3,4],[5,6],[4,8]])
x=np.where(arr1==4)
print(x)


# In[42]:


arr1=np.array([[[1,2,9],[3,4,7]],[[5,6,4],[4,8,4]]])
x=np.where(arr1==4)
print(x)


# 4. sort()
# 

# In[43]:


arr1=np.array([1,2,3,4,5,6,4,2,3])
print(np.sort(arr1))
arr2=np.array(['apple','cherry','banana'])
print(np.sort(arr2))
arr3=np.array([True,False,True])
print(np.sort(arr3))


# In[49]:


arr=np.array([[7,4,1],[1,4,3],[4,2,5]])
print(np.sort(arr))
print()  # by default axis value is -1 so it sorts inside the brackets
print(np.sort(arr,axis=0))
print()   # in axis 0 it sorts with its column and give ans in column wish
print(np.sort(arr,axis=1))


# In[56]:


arr1=np.array([[[3,2,8],[7,9,3]],
               [[6,7,2],[9,6,4]]])   # in these it sorts with 2 dimenssion block ex :- 3 & 6; 2 & 7; 8 & 2; and so on
                                    # it gives ans in there position
print(np.sort(arr1))
print('----------------')
print(np.sort(arr1,axis=0))
print('----------------')
print(np.sort(arr1,axis=1))      # it sorts in form of arr[0][0][0] & arr[0][0][1] etc ex:-3&7; 2&9; 8&3; and so on
print()                          # it gives ans in there position which switches


# ## Random Module

# In[64]:


from numpy import random
x=random.randint(100)         # in these it is like [0,100) means 0 is included but 100 is excluded.
print(x)


# In[65]:


x=random.randint(10,100)
print(x)


# In[143]:


x=random.randint(10,100,size=(5))
print(x)


# In[116]:


x=random.randint(1,100,size=(3,5))
print(x)


# In[147]:


x=random.rand(5)  # it gives element between 0 to 1 means it gives decimal numbers
print(x)


# In[158]:


x=random.choice([1,2,3,4,5])
print(x)


# In[156]:


x=random.choice([1,3,5,7,9],size=(5))
print(x)


# In[2]:


from numpy import random
x=random.randint(1,100)
a=True
for i in range(6,-1,-1):
    n=int(input("Enter the number:"))
    if x==n:
        break
    else:
        print("Wrong gusse")
        if x>n:
            print("Number is greater then the number you gusse")
        else:
            print("Number is lesser then the number you gusse")
        print("You have",i,"attempts left:")
        a=False
if a==False:
    print("Game over")
    print("Correct number is ",x)
else:
    print("Your gusse is correct. Number is ",x)


# In[ ]:




