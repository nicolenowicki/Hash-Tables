key = ['000','987','xyz', 'ddd','ccc','bbb', 'aaa','fff', 'EEE']
num = ""
for n in key[1]:
    num += str(ord(n))
num = (int(num)//2)
num *= len(str(num))
num = str(num)
length = len(num)//2

new = str((int(num[length+1]) * int(num[length-1]))**2) + str((int(num[length+2]) * int(num[length-2]))**2)
if new[-1] == '0':
    new = new[:-1] + new[0]
new = int(new)%15
print(new)