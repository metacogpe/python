

리스트 = [3,-20,-3,44]
for i in 리스트:
    if i <0:
        print(i)

리스트 = [3,-100,23,44]
for i in 리스트:
    if i %3 ==0:
        print(i)



리스트 = [13,21,12,14,30,18]
for i in 리스트:
    if i <20 and i %3 ==0:
        print(i)


리스트 = ['I', 'Language', 'Python']
for i in 리스트:
    if len(i)>=3:
        print(i)

리스트 = ['A','b','c','D']
for i in 리스트:
    if i.isupper():  # i.islower()
        print(i)


리스트 = ['dog','cat','parrot']
for i in 리스트:
    print(i.capitalize())

리스트 = ['hello.py','ex01.py','intro.hwp']
for i in 리스트:
    print(i.split(".")[0])

리스트 = ['hello.py','ex01.py','intro.hwp']
for i in 리스트:
    name, ext = i.split('.')
    print(name,ext)


리스트 = ['intra.h','intra.c', 'define.h']
for i in 리스트:
    if i.endswith('.h'):
        print(i)

리스트 = ['intra.h','intra.c', 'define.h']
for i in 리스트:
    if i.endswith(('.h', 'c')):
        print(i)

