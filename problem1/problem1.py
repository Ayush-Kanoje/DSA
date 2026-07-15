# import array as arr
from array import *
num = array('i',[2, 3, 4, 5, 6])

count_even = 0
count_odd = 0
for i in num:
    if i%2==0:
        count_even += 1
    else:
        count_odd += 1

print(f"Even number count in array is :{count_even}\nOdd number count in array is: {count_odd}")
