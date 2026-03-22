def pyramid(word, count):
    if len(word) == 1:
        return word

    print(" "*count + word[1:-1] + " "*count)

    return pyramid(word[1: -1], count+1)

while True:
    word = input("Input a word you want to make a pyramid for: ")
    if len(word) <= 2:
        print("The length of the input word should be more than 2 characters.")
        continue
    
    break

count=1
print(word)

pyramid(word, count)