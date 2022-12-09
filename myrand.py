import random

randlist = []
i = 0

## generating a list
while i < 400:
    randlist.append(random.randint(0, 9))
    i += 1

## printing out 40 number per row
cnt = 0
for num in randlist:
    if cnt % 40 == 0:
        print("\n")
    print(num, end = " ")
    cnt += 1

## finding an average
sum = 0
for num in randlist:
    sum += num
print("\n\nThe mean value is ", sum/len(randlist))

## mode
mode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for k in randlist:
    mode[k] += 1

mode_val = 0
j = 1
while j < len(mode):
    if mode[j] > mode[mode_val]:
        mode_val = j
    j += 1
print("\n\nThe mode is ", mode_val)

## median
randlist.sort()
if len(randlist) % 2 == 1:
    print("\n\nThe median (odd) is ", randlist[len(randlist)//2])
else:
    print("\n\nThe median (even) is ", (randlist[ (len(randlist)//2) ] + randlist[ (len(randlist)//2)-1 ])/2 )
