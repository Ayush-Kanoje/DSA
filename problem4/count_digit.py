n = 546213
num = n
# count = 0

# while num>0:
#     count +=1 
#     num = num // 10

# print(f"total count of no present inside a int variable: {count}")


def digitcount(num):
    return len(str(num))

print(digitcount(n))  # Output: 6
