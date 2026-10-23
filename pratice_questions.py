 # 1 reverse a string and find wheather it is palindrome or not 
def reversestring(s):
  result= ""
  for  ch in s:
    result= ch + result 
  return result  

def ispalindrome(s):
  return s== reversestring(s)

word=input("enter the word ")
print(reversestring(word))

if ispalindrome(word):
  print (f'the word {word} is aplindrome')
else:
  print("not palindrome")
