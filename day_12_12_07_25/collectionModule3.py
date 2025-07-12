# deque Problem:
#
# You are given a list of integers and a window size k.
# Write a Python function to return the max number in each sliding window of size k, using a deque.
from collections import deque
# dq = deque(sorted([1,3,-1]))
# print(len(dq))
# print('dq=',dq)
# print('dq',dq.pop())
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# m = 0
# dq2 = deque([])
# dq3 = deque(nums)
# for num in dq3:
#     if len(dq2) == 2:
#         dq3 = dq3.popleft()
#
#         continue
#     dq2.append(num)
#
# print(dq2)

# step 1 take 3 from nums
# step 2 get the maximum value for windowK
# step 3 store it in the output
# step 4 repeat for next iteration
# output =[]
# print(nums.remove(nums[0]))
# while len(nums) >2:
#  windowK = []
#  for num in nums:
#     windowK.append(num)
#     if len(windowK)  == 3:
#         print('window', windowK)
#         output.append(max(windowK))
#         nums.remove(nums[0])
#         print('dumb',nums)
#         break
#
# print('final output:', output)


# effecient code for above (chatgpt)

def sliding_window_max(nums, k):
    output = []
    dq = deque()  # stores indices, not values

    for i in range(len(nums)):
        # 1️⃣ Remove indices outside the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # 2️⃣ Remove indices whose values are less than current num
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 3️⃣ Add current index
        dq.append(i)

        # 4️⃣ If window has at least k elements, append current max to output
        if i >= k - 1:
            output.append(nums[dq[0]])

    return output

print(sliding_window_max(nums, k))



