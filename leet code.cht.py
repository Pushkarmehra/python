class Solution:
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers
        p1 = m - 1  # Pointer for the end of the initialized elements in nums1
        p2 = n - 1  # Pointer for the end of nums2
        p = m + n - 1  # Pointer for the end of nums1's total space

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# Example usage:
solution = Solution()

# Test cases
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

nums1 = [1]
m = 1
nums2 = []
n = 0
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

