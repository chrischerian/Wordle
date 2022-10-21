import random
from re import I, M
import class_keys
import class_tiles
# Wordle Program


def welcome():
    print("\n")
    print("\n")
    print("==================")
    print("Welcome to Wordle")
    print("==================")
    print("\n")

#WORDLE SET UP
def generateWord():
    wordList = ["adult", "agent", "apple", "award", "basis", "beach", "block", "beard", "brain", "chest", "chief", "child", "clock", "coach", "dream",
    "drama,", "drive", "drink", "earth", "enemy", "entry", "error", "faith", "fruit", "glass", "grass", "green", "heart", "horse", "hotel", "house","image",
    "index", "judge", "layer", "level", " limit", "major", "match", "metal", "model", "money", "noise", "north", "novel", "nurse", "order", "owner", "panel",
    "paper", "party", "peace", "poker", "pound", "queen", "ratio", "reply", "right", "river", "scene", "scope", "shape", "share", "sheep", "shift", "shock",
    "sight", "skill", "sleep", "taste", "total", "touch", "train", "trend", "uncle"," union", "value", "video", "voice", "waste", "watch", "white", "whole",
    "woman", "world","young"]
    wordle = random.choice(wordList)
    wordle = "CHEST"
    return wordle

def checkTriple(wordle):
    wordle = wordle.upper()
    for i in wordle:
        if wordle.count(i) > 2:
            return True
        else:
            continue
    return False

def checkDouble(wordle):
    wordle = wordle.upper()

    if checkTriple(wordle) == False:
        for i in wordle:
            if wordle.count(i) == 2:
                return True
            else:
                continue
    return False
    
def findTriple(wordle):
    wordle = wordle.upper()

    for i in wordle:
        if wordle.count(i) > 2:
            return i
        else:
            continue

def findDoubles(wordle):
    wordle = wordle.upper()
    doubles = []

    for i in wordle:
        if wordle.count(i) == 2:
            doubles.append(i)
        else:
            continue
    return doubles

#User Intake
def userGuess():
    guess = input("Guess a 5 letter word: \n > ")
    return guess

def validateInput(guess):
    try:
        int(guess)
    except ValueError:
        if type(guess) == str:
            if len(guess) == 5:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#Initializers for Keyboard and Tiles
def initializeKeyboard():

    keyboard = []

    qKey = class_keys.keys("Q", "Q", False, False, False)
    keyboard.append(qKey)
    wKey = class_keys.keys("W", "W", False, False, False)
    keyboard.append(wKey)
    eKey = class_keys.keys("E", "E", False, False, False)
    keyboard.append(eKey)
    rKey = class_keys.keys("R", "R", False, False, False)
    keyboard.append(rKey)
    tKey = class_keys.keys("T", "T", False, False, False)
    keyboard.append(tKey)
    yKey = class_keys.keys("Y", "Y", False, False, False)
    keyboard.append(yKey)
    uKey = class_keys.keys("U", "U", False, False, False)
    keyboard.append(uKey)
    iKey = class_keys.keys("I", "I", False, False, False)
    keyboard.append(iKey)
    oKey = class_keys.keys("O", "O", False, False, False)
    keyboard.append(oKey)
    pKey = class_keys.keys("P", "P", False, False, False)
    keyboard.append(pKey)
    aKey = class_keys.keys("A", "A", False, False, False)
    keyboard.append(aKey)
    sKey = class_keys.keys("S", "S", False, False, False)
    keyboard.append(sKey)
    dKey = class_keys.keys("D", "D", False, False, False)
    keyboard.append(dKey)
    fKey = class_keys.keys("F", "F", False, False, False)
    keyboard.append(fKey)
    gKey = class_keys.keys("G", "G", False, False, False)
    keyboard.append(gKey)
    hKey = class_keys.keys("H", "H", False, False, False)
    keyboard.append(hKey)
    jKey = class_keys.keys("J", "J", False, False, False)
    keyboard.append(jKey)
    kKey = class_keys.keys("K", "K", False, False, False)
    keyboard.append(kKey)
    lKey = class_keys.keys("L", "L", False, False, False)
    keyboard.append(lKey)
    zKey = class_keys.keys("Z", "Z", False, False, False)
    keyboard.append(zKey)
    xKey = class_keys.keys("X", "X", False, False, False)
    keyboard.append(xKey)
    cKey = class_keys.keys("C", "C", False, False, False)
    keyboard.append(cKey)
    vKey = class_keys.keys("V", "V", False, False, False)
    keyboard.append(vKey)
    bKey = class_keys.keys("B", "B", False, False, False)
    keyboard.append(bKey)
    nKey = class_keys.keys("N", "N", False, False, False)
    keyboard.append(nKey)
    mKey = class_keys.keys("M", "M", False, False, False)
    keyboard.append(mKey)
    
    return keyboard

def initializeTiles(guess):
    
    tiles = []

    tile1 = class_tiles.tiles("",False)
    tiles.append(tile1)
    tile2 = class_tiles.tiles("",False)
    tiles.append(tile2)
    tile3 = class_tiles.tiles("",False)
    tiles.append(tile3)
    tile4 = class_tiles.tiles("",False)
    tiles.append(tile4)
    tile5 = class_tiles.tiles("",False)
    tiles.append(tile5)

    count = 0
    for i in tiles:
        i.value = guess[count].upper()
        count += 1

    return tiles

#FEEDBACK
# Color Tiles & Keyboard
def colorTiles(guess, wordle, tiles):
    guess = guess.upper()
    wordle = wordle.upper()
    tiles = tiles
    
    #Allows all tiles to be edited
    for i in tiles:
        i.unlockTile()

    #Check & Find Triples
    tripleCount = 0
    hasTriple = False
    doubleCount = 0
    hasDouble = False

    if(checkTriple(wordle)):
        triple = findTriple(wordle)
        hasTriple = True
    else:
        triple = ""
    
    if(checkDouble(wordle)):
        doubles = findDoubles(wordle)
        hasDouble = True
    else:
        doubles = []

    #Colors correct tiles green
    count = 0
    for i in guess:
        if i == wordle[count]:
            tiles[count].setColor("green")
            tiles[count].lockTile()
            if i == triple:
                tripleCount += 1
            if i in doubles:
                doubleCount += 1
        count += 1
    
    #Colors incorrect tiles yellow or black
    count = 0
    for i in guess:
        if i in wordle:
            if i == wordle[count]:
                variable = True
            else:
                if(hasTriple and i == triple):
                    if tripleCount > 3:
                        tiles[count].setColor("black")
                    else:
                        tiles[count].setColor("yellow")
                        tripleCount += 1
                elif(hasDouble and i in doubles):
                    if doubleCount > 2:
                        tiles[count].setColor("black")
                    else:
                        tiles[count].setColor("yellow")
                        doubleCount += 1
                elif((i not in doubles) and (guess.count(i) > 1)):
                    tiles[count].setColor("black")
                elif((i != triple) and (guess.count(i) > 2)):
                    tiles[count].setColor("black")
                else:
                    tiles[count].setColor("yellow")
        else:
            tiles[count].setColor("black")
        count += 1
    return tiles

def colorKeyboard(guess, answer, keyboard):
    keyboard = keyboard
    guess = guess.upper()
    answer = answer.upper()

    i = 0
    while i < (len(guess)):
        if guess[i] == answer[i]:
            for j in keyboard:
                if j.value == guess[i]:
                    j.setColor("green")
            i += 1
            continue
        elif guess[i] in answer:
            for j in keyboard:
                if j.value == guess[i]:
                    j.setColor("yellow")
            i += 1
            continue
        else:
            for j in keyboard:
                if j.value == guess[i]:
                    j.setColor("black")
            i += 1
            continue

    return keyboard

#Check Guess
def checkGuess(guess,wordle):
    guess = guess.upper()
    wordle = wordle.upper()

    if guess == wordle:
        complete = True
    else:
        complete = False
    
    return complete

#Print Tiles and Keyboard
def printTiles(tiles):
    tiles = tiles
    for i in tiles:
        print(i.value, end="")

def printKeyboard(keyboard):
    keyboard = keyboard
    for i in keyboard:
        print(i.color + "  ", end="")
        if keyboard.index(i) == 9:
            print("\n")
            print(" ", end="")
        if keyboard.index(i) == 18:
            print("\n")
            print("   ", end="")
    print("\n")

#GAME
def init():
    welcome()

    #Initialize keyboard and wordle
    keyboard = initializeKeyboard()
    wordle = generateWord()

    #First run of Wordle
    printKeyboard(keyboard) #provide blank keyboard
    guess = userGuess() #intake guess

    while(not validateInput(guess)):
        print("\n")
        print("Guess must be a 5 letter word. Try again")
        guess = userGuess() #intake guess
        

    #Initialize and print tiles in response to guess
    tiles = initializeTiles(guess)
    tiles = colorTiles(guess,wordle,tiles)
    print("\n")
    printTiles(tiles)
    print("\n")

    #OLD CODE TO DELETE
    keyboard = colorKeyboard(guess,wordle,keyboard)
    printKeyboard(keyboard)
    complete = checkGuess(guess, wordle)

    counter = 1
    while((not complete) and counter < 6):
        guess = userGuess()
        while(not validateInput(guess)):
            print("\n")
            print("Guess must be a 5 letter word. Try again")
            guess = userGuess()
        tiles = initializeTiles(guess)
        tiles = colorTiles(guess,wordle,tiles)
        print("\n")
        printTiles(tiles)
        print("\n")
        keyboard = colorKeyboard(guess,wordle,keyboard)
        printKeyboard(keyboard)
        complete = checkGuess(guess, wordle)
        counter += 1

    if(complete):
        print("\n")
        print("Congratulations! You got it in " + str(counter) + " guess(es)!")
    else:
        print("\n")
        print("The word was " + wordle)
    quit()

init()