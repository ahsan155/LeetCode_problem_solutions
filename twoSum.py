class Solution(object):
    def twoSum(self, nums, target):
       indices = []
       counter = 0
       solFound = False

       for element in nums:
           remain = target - element
           
           otherCounter = 0
           for item in nums:
               if remain == item and otherCounter != counter:
                   indices.append(counter)
                   indices.append(otherCounter)
                   solFound = True
               otherCounter+=1

           if solFound:
               break

           counter+=1

       return indices
