def math_magic(number):
    total=number*number
    total+=number
    total/number
    total-=number
    total/=6
    return total


number=int(input("Give me a positive integer."))
total=math_magic(number)

print(total)
print("wowwwwww!")
