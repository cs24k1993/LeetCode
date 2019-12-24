nums = [1,1,1,1,0,0,0,1,0,1,0,1]
a = ''.join(map(str, nums)).split('0')
print(a)
# .split('0')
b = max(map(len, ''.join(map(str, nums)).split('0')))

print(b)