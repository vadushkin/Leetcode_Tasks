"""
You can perform two types of operations on any element
The deviation of the array is the maximum difference between
Return the minimum deviation the array can have after performing

* Example 1:
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

* Example 2:
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

* Example 3:
Input: nums = [2,10,8]
Output: 3

Constraints:

* 2
* [1,2,3,4]
* 2
* [1,2,3,4]
* n == nums.length
* 2 <= n <= 5 * 104
* 1 <= nums[i] <= 109
"""