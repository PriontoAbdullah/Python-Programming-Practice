name,age=input('Enter your Name & Age: ').split()
age=int(age)
if (name[0]=='A' or name[0]=='a') and age>=10:
    print('You can watch coco movie!')
else:
    print("Sorry! You can't watch.")