class Solution(object):

    def remove_duplicates_more_than_twice(self,lst):
        # Create a dictionary to store the counts of elements
        element_counts = {}

        # Iterate through the list from left to right
        result = []
        for element in lst:
            # Increment the count for the current element
            element_counts[element] = element_counts.get(element, 0) + 1

            # If the count is less than or equal to 2, add the element to the result
            if element_counts[element] <= 3:
                result.append(element)

        return result


    def findtriple(self, nums):
        nums.sort()  # Sort the input list

        triplets = set()
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates to avoid duplicate triplets

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplets.add(tuple(triplet))

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        unique_triplets = [list(triplet) for triplet in triplets]
        return unique_triplets



    def threeSum(self, nums):

        permContainer = []
        nums = self.remove_duplicates_more_than_twice(nums)
        permContainer = self.findtriple(nums)

        return permContainer


s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))
