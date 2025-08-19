def write_append():
    text = input("Write your text: ")
    with open('output.txt', 'w') as f:
        f.write(text + '\n')

    extra = input("Write extra text: ")
    with open('output.txt', 'a') as f:
        f.write(extra + "\n")

    with open("output.txt", 'r') as f:
        print(f.read())

write_append()
