def gen(nums):
    for i in nums:
        yield i
it =gen([1,2,3])
print([next(it) for _ in range(3)])
# it = gen([[1,2,3],[4,5,6]])
# it = gen([1,2,3])
# print(type(it))
# print([next(it)for _ in range(1,3)])
# print([next(gen([[1,2,3],[4,5,6]]))])


# def gen2(nums):
#     for i in nums:
#         yield i
# print([next(gen2([6,7,8])) for _ in range(3)])