class ListNode(object):

     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution(object):

    def recursion(self, node, value):
      if node == None:
        return ListNode(val=value, next=None)
      else:
        node.next = self.recursion(node.next, value)
        return node

    def addTwoNumbers(self, l1, l2):

      l1_string = ""
      while l1.next != None:
        l1_string += str(l1.val)
        l1 = l1.next
      l1_string += str(l1.val)

      l2_string = ""
      while l2.next != None:
        l2_string += str(l2.val)
        l2 = l2.next
      l2_string += str(l2.val)

      l1_num = int(l1_string[::-1])
      l2_num = int(l2_string[::-1])
      sum = l1_num + l2_num
      sum_string = str(sum)[::-1]
      counter = 0

      node = None
      while counter < len(sum_string):
        node = self.recursion(node, int(sum_string[counter]))
        counter+=1

      return node
