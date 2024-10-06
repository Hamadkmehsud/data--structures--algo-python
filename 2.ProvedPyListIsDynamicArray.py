import sys
l = []

print(sys.getsizeof(l))

for i in range(1):
    l.append(i)
    print(sys.getsizeof(l))

def check():
    if (0.1000 + 0.2000) == 0.3:
        print('True')
        print(0.01+0.02)
    else:
        print('False')
        print(0.01 + 0.02)
#this is false because it stores in binary format and computer represent floating in binary we work with
#base 10 but computer work by base 2 so if we write 0.1 its close to 0.1 but not actual 0.1
check()