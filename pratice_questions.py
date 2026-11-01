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

#Write a Python function is_palindrome(s) that returns True if the string s is a palindrome, otherwise False.

#Ignore case (so "Madam" counts as a palindrome)
#Ignore spaces and punctuation (so "A man, a plan, a canal: Panama" counts too)

def reverse(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

def is_palindrome(s):
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    return cleaned == reverse(cleaned)

print(is_palindrome("Madam"))                           # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("manoj"))                           # False

#count vowels in a string 

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count


#find max in a list 

def find_max(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest

print(find_max([3, 7, 2, 9, 4]))   # 9
print(find_max([-5, -1, -8]))      # -1
print(find_max([10]))              # 10


