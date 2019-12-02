#lab07.py
# Student(s): Zachary Friedland and Peter Brede
# Make sure to read the comments for each function.
letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,\
                'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,\
                'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
                's':1, 't':1, 'u':1, 'v':4,  'w':4, 'x':8,\
                'y':4, 'z':10}

def createWordList(filename):
  '''
  Reads in the filename and creates a list L which contains all the words. 
  You must remove the newline character ('\n') at the end of each word.  

  :param filename: the string which represents the filename you are reading from.
  :return: A list of strings  
  '''

  infile = open(filename)
  allWords = infile.read()
  infile.close()
  x = allWords.split()
  cleanList = []
  for word in x:
      cleanList.append(word.strip('\n'))
  return cleanList
   
      
  


def canWeMakeIt(myWord, myLetters):
  '''
  Takes in a word and a string of letters and checks whether the word can be made with those letters.  

  :param myWord: the string we are checking.
  :param myLetters: a string of letters we can use to build a string. 
  :return: A bool whether the string can be made or not.  
  '''
  if type(myWord) != str or type(myLetters) != str:
    return False
  letterList = list(myLetters)
  for letter in myWord:
    if letter not in letterList:
      return False
    elif letter in letterList:
      newList = letterList.remove(letter)
  return True
    
    


def getWordPoints(myWord, letterPoints):
  '''
  Returns the total points of a given word. 

  :param myWord: the string you want to calculate points for
  :param LetterPoints: a dictionary of (letter, value) pairs which gives the point value of each letter
  :return: The total point value of the word.   
  '''
  total = 0
  for letter in myWord:
    if letter in letterPoints:
      total+=letterPoints[letter]
  return total
    

def outputWordPointPairs(pointWordList, filename, toFile):
  '''
  Outputs the contents of pointWordList in a specified format to a file (see lab instructions).
    
  :param pointWordList: a list of tuples to print or output to a file, each tuple 
   contains a (pointValue, word) pair
  :param filename: a string that you will name the file with if toFile is True
  :param toFile: a boolean to decide whether I want to print to file or not. If True then output to file else output to terminal.
  :return: None
  '''
  pointWordList.sort(reverse = True)
  length = len(filename) + 4
  if toFile == False:
    for word in pointWordList:
      specific = length - len(word[1])
      spaces = ' ' * specific
      print("{0}{1}{2}".format(word[1], spaces, word[0]))
  else:
    writeFile = open(filename + '.txt', 'w')
    for word in pointWordList:
      specific = length - len(word[1])
      spaces = ' ' * specific
      writeFile.write("{0}{1}{2}\n".format(word[1], spaces, word[0]))
    writeFile.close()
    


def scrabbleWords(myLetters):
  '''
  A function which takes in a string of letters and shows what words can be constructed from it.
  It should use the helper functions defined above to do so. 

  :param myLetters: a string of letters we are using. 
  :return: None
  '''
  listOfStrings = createWordList('wordlist.txt')
  theWordList = []
  for word in listOfStrings:
    if canWeMakeIt(word,myLetters) == True:
      wordPoints = getWordPoints(word, letterPoints)
      theWordList.append((wordPoints, word))
  outputWordPointPairs(theWordList, myLetters, False)
  outputWordPointPairs(theWordList, myLetters, True)
  
if __name__=="__main__":
  #scrabbleWords("buoni")
  #scrabbleWords('zach')
  scrabbleWords('supercalifragilisticexpialidocious')
  # Manual test cases...

