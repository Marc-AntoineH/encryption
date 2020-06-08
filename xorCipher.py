inputString = raw_input("Enter the cipher text or plain text: ")
key = raw_input("Enter the key for encryption or decryption: ")
numbOfIteration = len(inputString)
outputString = ""


for i in range(numbOfIteration):
    current = inputString[i]
    currentKey = key[i%len(key)]
    outputString += chr(ord(current) ^ ord(currentKey))


print ("Here's the output: ", outputString)