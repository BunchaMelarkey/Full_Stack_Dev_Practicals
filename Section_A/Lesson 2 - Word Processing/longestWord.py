fin = open("words.txt", "r")
biggest, numOfWords=0, 0
for line in fin:
    word = line.strip()
    numOfWords = numOfWords+1
    if len(word) > biggest:
        biggest = len(word)

print("The longest of the {} words contains {} characters".format(numOfWords, biggest))

fin.seek(0)
fout = open("biggest.txt", "w")
for line in fin:
    word = line.strip()
    if len(word) == biggest:
        output = word + "\n"
        fout.write(output)
        print(word)  
fin.close()		
fout.close()