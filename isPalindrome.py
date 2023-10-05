class Solution(object):
    def isPalindrome(self, x):
       x_string = str(x)
       x_reverse = x_string[::-1]

       if x_string == x_reverse:
           return True
       else:
           return False
        