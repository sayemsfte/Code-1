# message = "Hello Python"
# for letter in message:
#     print(letter)


message = "Sayem's Project to Github"
shift = 0
for i in range(1,6):
    shifted = message[shift:] + message [:shift]
    print(shifted)
    shift +=1
