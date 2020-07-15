def palindrome(s):
  if s == s[::-1]:
    return True
  return False

s=input("Enter a name: ")
palindrome(s)