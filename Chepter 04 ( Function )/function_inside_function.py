def big(a,b):
  if a>b:
    return a
  return b

def bigger(a,b,c):
  return big(big(a,b),c)

a=int(input())
b=int(input())
c=int(input())

print(f"The bigest number is: {bigger(a,b,c)} ")