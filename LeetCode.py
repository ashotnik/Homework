#!/usr/bin/python3
# Array 1 E

# nums=[7,2,5,4,5,3,6]
# target=9
# ml=[]
# for i in range(len(nums)):
#     if not nums[i]==nums[-1]:
#         # print(nums[i]+nums[i+1])
#         if nums[i]+nums[i+1]==target:
#             ml.append(i)
#             ml.append(i+1)
# print(ml)

# Array 4 H

# nums1=[1,3]
# nums2=[2,4,7,8]
#        for i in nums1:
#          nums2.append(i)
#        nums2.sort()
#        if len(nums2)%2==0:
#            return ((nums2[len(nums2)//2]+nums2[(len(nums2)//2)-1])/2)
#        else:
#            return (nums2[len(nums2)//2])

# Array 11 M

height = [1,8,6,2,5,4,8,3,7]

max=0
for i in range(len(height)):
    
    for j in range(len(height)):
        if height[j]>height[i]:
            n=height[i]
        else:
            n=height[j]
        a=((j+1)-(i+1))*n
        if max<a:
            max=a
    print(max)
