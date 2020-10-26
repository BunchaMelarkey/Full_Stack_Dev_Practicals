import random

def replaceAll(guess, word, letter):
    for pos in range(len(guess)):
        if word[pos] == letter:
            guess = guess[:pos] + letter + guess[pos+1:]
    return guess

def getWords(numberOfLetters):
    wordsFound=[]
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if len(word) == numberOfLetters:
            wordsFound.append(word)
    fin.close()		
    return wordsFound

options = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u" "v",
    "w", "x", "y", "z"]

numberOfLetters = int(input("Enter word length: "))
words = getWords(numberOfLetters)
print("There are {} words with {} letters \n". \
             format(len(words),numberOfLetters))

guessWord = words[random.randint(0,len(words)-1)]
print("Guessing the word: {}".format(guessWord))

lives = 6
guessString = "_" * numberOfLetters

while lives > 0:
    print("Letters Available: " + "".join(options))
    thisLetter = input("Guess a letter: ")
    options = [w.replace(thisLetter, "_") for w in options]
    if thisLetter in guessWord:
        guessString = replaceAll( \
            guessString,guessWord,thisLetter)
        if guessString == guessWord:
            print("You guessed the word!")
            break
    else:
        lives = lives-1
        print("Letter not found - lives remaining: {} \n".format(lives))
    print(guessString)

if lives == 0:
    print("\n--- Out of lives! - Your word was " + guessWord + " ---\n")

if lives > 0:
    
    player = input("Enter player name: ")
    fout = open("hangmanScores.txt", "a+")

    score = lives * numberOfLetters
    previousScore = False
    newScoreText = "{}, {}\n".format(player, score)

    for line in fout:
        score = line.strip()
        if (score.__contains__(player)):
            fout.write(line.replace(newScoreText))
            previousScore = True
            print(player + " your new score has been updated!")
        else: 
            break

    if previousScore == False:
        fout.write(newScoreText)

    fout.close()