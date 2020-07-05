name='abc'
age=24
n,a=input('Enter name & age: ').split()
a=int(a)
if name==n and age==a:
    print('You are right')
else: 
    if name==n or age==a:
        print('Something wrong!')