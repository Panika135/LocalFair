from django.test import TestCase


def containsDuplicate(nums) -> bool:
    set_1 = set(nums)
    if len(set_1) == len(nums):
        return True
    else:
        return False


a = containsDuplicate([1,2,3,1])
print(a)