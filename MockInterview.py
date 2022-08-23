def sortedAscList(nums):

    for i in range(len(nums)-1):
        if nums[i + 1] == nums[i]:
            nums.remove(nums[i])
    
    return nums
print(sortedAscList([-1, -1, 0,0,1,3,3]))


def sortedAscList2(numbers):
    i=0
    j=1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            numbers.remove(numbers[i])
        else:
            j += 1
            i += 1

    return numbers
print(sortedAscList2([-1,-1,-1,0,0,3,3]))

def reverseList(s):
    sList = s.split(' ')
    l = 0
    r = len(sList) -1
    while l < r:

        sList[l], sList[r] = sList[r], sList[l]
        l += 1
        r -= 1
    return " ".join(sList)

    #return split.reverse.join

print(reverseList("Hello World I am Here"))