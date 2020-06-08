inputString = input("Enter the cipher text or plain text: ")
key = input("Enter the key for encryption or decryption: ")
numberOfIteration = len(inputString)
outputString = ""


for i in range(numbOfIteration):
    current = inputString[i]
    currentKey = key[i%len(key)]
    outputString += chr(ord(current) ^ ord(currentKey))


print("Here's the output: ", outputString)
