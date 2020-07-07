m=int(input('Enter your marks: '))
if m<0 or m>100:
    print('Invalid choice!')
elif 80<=m<=100:
    print('A+')
elif 70<=m<=79:
    print('A')
elif 60<=m<=69:
    print('A-')
else:
    print('Fail')