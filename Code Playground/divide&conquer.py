#divide & conquer
# (求和)
def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])
print(f"sum([1, 2, 3, 4, 5]) = {sum([1, 2, 3, 4, 5])}")

# (计算列表元素个数)
def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])
print(f"count([1, 2, 3, 4, 5]) = {count([1, 2, 3, 4, 5])}")

# (找出列表中最大数字)
def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(f"max([1, 2, 3, 4, 5]) = {max([1, 2, 3, 4, 5])}")

# (二分查找)
def binary_search(list, item):
    if len(list) == 1:
        return list[0]+1 if list[0] == item else None
    mid = len(list) // 2
    if list[mid] == item:
        return mid+1
    if list[mid] > item:
        return binary_search(list[:mid], item)
    else:
        return binary_search(list[mid+1:], item)

print(f"binary_search([1, 2, 3, 4, 5], 3) = {binary_search([1, 2, 3, 4, 5], 3)}")

# (计算GCD)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(f"gcd(1680, 640) = {gcd(1680, 640)}")