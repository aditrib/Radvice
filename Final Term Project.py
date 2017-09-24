######################################################
# Name: Aditri Bhagirath
# Andrew ID: abhagira
######################################################

# Citations:

"""
Events barebones #0 has been taken from the course website.
rgbString taken from course website

Dataset obtained from:
http://www2.informatik.uni-freiburg.de/~cziegler/BX/


image loading help : 
http://stackoverflow.com/questions/6582387/image-resize-under-photoimage 

Learnt to use webbrowser from https://pymotw.com/2/webbrowser/

Page flip sound from https://www.soundjay.com/page-flip-sounds-1.html

Audio playing code obtained from:
http://simpleaudio.readthedocs.io/en/latest/ (the playSound() function)

Debugging thumbnail display help:
https://github.com/smileychris/easy-thumbnails/issues/95

My friend, Suann Chi, helped me out with some color schemes

"""

import tkinter
from tkinter import *
# used to load the images
import PIL.Image
from PIL import Image, ImageTk
# used to create a random subsample of a list
import subsample
import random

from tkinter import *
# used to open up a different link
import webbrowser
import string
# used to implement the sounds
import simpleaudio as sa
# used to obtain image from an internet link and convert it to usable form
import requests
# used to read the content of an image from an internet link
from io import BytesIO
# os import used for text- to voice
import os




################################################################################
# used for custom colors
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

################################################################################

# Initialising the data

def loadBackgrounds(data):
    loadInstructions(data)
    loadBackspaceButton(data)
    loadLibraryImage(data)
    loadRecommendationScreen(data)
    loadNoRecommendations(data)
    loadIntro(data)
    loadSearchImage(data)
    loadModeSelection(data)
    loadStar(data)
    loadHighlightedStar(data)
    loadBook0(data)
    loadBook1(data)
    loadBook2(data)
    loadBook3(data)
    loadBook4(data)
    
    
    

def init(data):
    data.mode = "introScreen"
    data.score = 0
    loadBackgrounds(data)
    
    data.introText = ["R", "a", "d", "v", "i", "c", "e"]
    # Centers at two different levels to create bouncing letters
    data.centers1 = [data.height/9, data.height/9-5]*4
    data.centers2 = [data.height/9-5, data.height/9]*4
    data.centers = data.centers1
    data.username = None
    # This keeps track of how many times we have clicked "More Books" to 
    # display the next ten most popular books.
    
    
    data.mostPopularCounter = 0
    data.searchResultsCounter = 0
    data.searchCounter = 0
    # Keeps track of the current ratings
    
    loadAllDictionaries(data)
    
    data.searchResultsList = None

    data.submitActivate = False
   
    data.currentUserRecommendations = None
    data.searchResults = None
    # current search string
    data.search = ""
    data.enterMode = False

def loadAllDictionaries(data):
    data.currentRatings = {}
    # Books rated in "rate popular books" mode
    data.popularSelections = {}
    data.popularSelectionRatings = {}
    # Books rated in search mode
    data.searchSelectionFrequencies = {}
    data.searchSelectionRatings = {}
    data.permSearchSelectionRatings = {}
    # Final selection (popular and searched books)
    data.finalSelection = {}
    # values that enter the recommendation algorithm
    data.enterValues = {}
 

################################################################################
# Functions for the different sounds played: This is not my code.
    
def playSound():
    wave_obj = sa.WaveObject.from_wave_file('/Users/aditribhagirath/Desktop/pageFlip.wav')
    play_obj = wave_obj.play()
    play_obj.wait_done()
    


################################################################################

# Load all the thumbnail images we require
  
def loadBook0(data):
    filename = '/Users/aditribhagirath/Desktop/temp0.jpg'
    data.book0Image = PIL.ImageTk.PhotoImage(file = filename)
    
def loadBook1(data):
    filename = '/Users/aditribhagirath/Desktop/temp1.jpg'
    data.book1Image = PIL.ImageTk.PhotoImage(file = filename)
    
def loadBook2(data):
    filename = '/Users/aditribhagirath/Desktop/temp2.jpg'
    data.book2Image = PIL.ImageTk.PhotoImage(file = filename)

def loadBook3(data):
    filename = '/Users/aditribhagirath/Desktop/temp3.jpg'
    data.book3Image = PIL.ImageTk.PhotoImage(file = filename)
    
def loadBook4(data):
    filename = '/Users/aditribhagirath/Desktop/temp4.jpg'
    data.book4Image = PIL.ImageTk.PhotoImage(file = filename)
    
################################################################################
# Text that is read out as summary

def lovelyBonesSummary():
    
    os.system("""say 'The Lovely Bones is the story of a family devastated by
     a gruesome murder -- a murder recounted by the teenage victim from
     her vantage point in heaven.'&""") 

def daVinciCodeSummary():
    os.system("""say 'An ingenious code hidden in the works of Leonardo da 
    Vinci. A desperate race through the cathedrals and castles of Europe. 
    An astonishing truth concealed for centuries . . . unveiled at last.'""") 
    
def redTentSummary():
    os.system("""say 'Her name is Dinah. In the Bible, her life is only hinted 
    at in a brief and violent detour within the more familiar chapters of the
    Book of Genesis that are about her father. Told in the voice of Dinah, 
    this novel reveals the traditions and turmoils of ancient womanhood--the
    world of the red tent.'""")

################################################################################
# load all the miscellaneous images needed
    
    
def loadStar(data):
    filename = '/Users/aditribhagirath/Desktop/star.jpg'
    data.star = PIL.ImageTk.PhotoImage(file = filename)
    
def loadHighlightedStar(data):
    filename = '/Users/aditribhagirath/Desktop/highlightedStar.jpg'
    data.highlightedStar = PIL.ImageTk.PhotoImage(file = filename)
    
def loadLibraryImage(data):
    filename = '/Users/aditribhagirath/Desktop/blueBack.jpg'
    data.libraryImage = PIL.ImageTk.PhotoImage(file = filename)
    
def loadBackspaceButton(data):
    filename = '/Users/aditribhagirath/Desktop/backspaceButton.jpg'
    data.backspaceButton = PIL.ImageTk.PhotoImage(file = filename)
    
def loadIntro(data):
    filename = '/Users/aditribhagirath/Desktop/blueBack 5.jpg'
    data.intro = PIL.ImageTk.PhotoImage(file = filename)
    
def loadModeSelection(data):
    filename = '/Users/aditribhagirath/Desktop/blueBack 6.jpg'
    data.modeSelection = PIL.ImageTk.PhotoImage(file = filename)
    
def loadNoRecommendations(data):
    filename = '/Users/aditribhagirath/Desktop/blueBack 8.jpg'
    data.noRecommendationsScreen = PIL.ImageTk.PhotoImage(file = filename)

def loadSearchImage(data):
    filename = '/Users/aditribhagirath/Desktop/blueBack 4.jpg'
    data.searchImage = PIL.ImageTk.PhotoImage(file = filename)

def loadInstructions(data):
    filename = '/Users/aditribhagirath/Desktop/blueBack 3.jpg'
    data.instructions = PIL.ImageTk.PhotoImage(file = filename)
    
def loadRecommendationScreen(data):
    filename = '/Users/aditribhagirath/Desktop/blueBack 7.jpg'
    data.recommendationScreen = PIL.ImageTk.PhotoImage(file = filename)
    

    
################################################################################
 
# Functions to call the functions of the appropriate mode

def mousePressed(event, data):
    if data.mode == "introScreen":
        introScreenMousePressed(event, data)
    elif data.mode == "loginScreen":
        loginScreenMousePressed(event, data)
    elif data.mode == "rateBooks":
        rateBooksMousePressed(event, data)
    elif data.mode == "recommendationScreen":
        recommendationScreenMousePressed(event, data)
    elif data.mode == "searchScreen":
        searchScreenMousePressed(event, data)
    elif data.mode == "helpScreen":
        helpScreenMousePressed(event, data)
    elif data.mode == "searchRatings":
        searchRatingsMousePressed(event, data)
        
    
def keyPressed(event, data):
    if data.mode == "introScreen":
        introScreenKeyPressed(event, data)
    elif data.mode == "loginScreen":
        loginKeyPressed(event, data)
    elif data.mode == "rateBooks":
        rateBooksKeyPressed(event, data)
    elif data.mode == "recommendationScreen":
        recommendationScreenKeyPressed(event, data)
    elif data.mode == "searchScreen":
        searchScreenKeyPressed(event, data)
    elif data.mode == "helpScreen":
        helpScreenMousePressed(event, data)
    elif data.mode == "searchRatings":
        searchRatingsKeyPressed(event, data)
        
def timerFired(data):
    if data.mode == "introScreen":
        introScreenTimerFired(data)
    elif data.mode == "loginScreen":
        loginScreenTimerFired(data)
    elif data.mode == "rateBooks":
        rateBooksTimerFired(data)
    elif data.mode == "recommendationScreen":
        recommendationScreenTimerFired(data)
    elif data.mode == "searchScreen":
        searchScreenTimerFired(data)
    elif data.mode == "helpScreen":
        helpScreenTimerFired(data)
    elif data.mode == "searchRatings":
        searchRatingsTimerFired(data)
    
def redrawAll(canvas, data):
    if data.mode == "introScreen":
        introScreenRedrawAll(canvas, data)
    elif data.mode == "loginScreen":
        loginRedrawAll(canvas, data)
    elif data.mode == "rateBooks":
        rateBooksRedrawAll(canvas, data)
    elif data.mode == "recommendationScreen":
        recommendationScreenRedrawAll(canvas, data)
    elif data.mode == "searchScreen":
        searchScreenRedrawAll(canvas, data)
    elif data.mode == "helpScreen":
        helpScreenRedrawAll(canvas, data)
    elif data.mode == "searchRatings":
        searchRatingsRedrawAll(canvas, data)
        

################################################################################

# Intro Screen Functions

def introScreenMousePressed(event, data):
    if data.mode == "introScreen" and loginButtonPressed(event, data):
        return
    


def loginButtonPressed(event, data):
    
    # check if get started has been pressed
    if (event.x >= data.width/2 - 75 and event.x <= data.width/2 + 75
      and event.y >= data.height/2.5 + 24 and event.y <= data.height/2.5 + 76):
        playSound()
        data.mode = "loginScreen"
       
        data.username = generateUsername(data,shortenedDict)
        while data.username in shortenedDict:
            uniqueUsername = generateUsername(data, shortenedDict)
            data.username = uniqueUsername
        shortenedDict[data.username] = {}
    # check if the question mark is pressed, and direct to helpscreen.
    elif (event.x <= data.width/2 + 25 and event.x >= data.width/2 - 25 and 
         event.y <= 3*data.height/4+25 and event.y >= 3*data.height/4-25):
        playSound()
        data.mode = "helpScreen"
    return False


def introScreenKeyPressed(event, data):
    pass

def introScreenTimerFired(data):
    if data.centers == data.centers1:
        data.centers = data.centers2
    else:
        data.centers = data.centers1
       

def introScreenRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2,image = data.intro)
    
    # padding is the space between bouncing letters
    padding = [-3, -2, -1, 0, 1, 2, 3]
    for i in range(len(data.introText)):
        canvas.create_text(data.width/2 + padding[i]*60,
        data.centers[i], text = data.introText[i],
        font = "Arial 60 ", fill = rgbString(0, 0, 91))
   
                            
   
################################################################################

def helpScreenTimerFired(data):
    pass
    
def helpScreenMousePressed(event, data):
    # Check is rate is pressed
    if (event.x <= 135 and event.x >= 25 and
    event.y <= 625 and event.y >= 575):
        playSound()
        data.mode = "loginScreen"
    # Check if learn more is pressed
    elif (event.x <= 470 and event.x >= 360 and
    event.y <= 625 and event.y >= 575):
        playSound()
        webbrowser.open("http://recommender-systems"+
                       ".org/collaborative-filtering/")
    # Check if "Get data" is pressed
    elif (event.x >= 200 and event.x <= 300 and
    event.y <= 625 and event.y >= 575):
        playSound()
        # Data set I used for my project
        webbrowser.open("http://www2.informatik.uni-freiburg.de/~cziegler/BX/")
        
def helpScreenKeyPressed(event, data):
    pass
    
def helpScreenRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.instructions)
   
    

################################################################################

# mode selection functions
def loginScreenTimerFired(data):
    pass
    
    
def loginScreenMousePressed(event, data):
    if data.mode == "loginScreen" and rateButtonPressed(event, data):
        data.mode = "rateBooks"
    if data.mode == "loginScreen" and searchButtonPressed(event, data):
        data.mode = "searchScreen"
    
def loginScreenKeyPressed(event, data):
    pass


def loginRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2,image = data.modeSelection)
    createSearchButton(canvas, data)                        
    createRateButton(canvas, data)

    
def createSearchButton(canvas, data):
    coolTurquoise = rgbString(153, 205, 204)
    deepBlue = rgbString(25,67,124)
    # outer rectangle
    canvas.create_rectangle(data.width/2 - 83, data.height/2 + 50- 18,
                            data.width/2 + 83, data.height/2 + 50 + 18, 
                            fill = coolTurquoise, outline = deepBlue, width = 2)
    # inner rectangle
    canvas.create_rectangle(data.width/2 - 80, data.height/2 + 50- 15, 
                            data.width/2 + 80, data.height/2 + 50 + 15, 
                            fill = coolTurquoise, outline = deepBlue, width = 2)
    canvas.create_text(data.width/2, data.height/2+ 50,
                  text = "Search for Books to rate!", fill = deepBlue)
    
def createRateButton(canvas, data):
    coolTurquoise = rgbString(153, 205, 204)
    deepBlue = rgbString(25,67,124)
    # outer rectangle
    canvas.create_rectangle(data.width/2 - 73, data.height/2 - 18,
                            data.width/2 + 73, data.height/2 + 18,
                            fill = coolTurquoise, outline = deepBlue, width = 2)
    # inner rectangle
    canvas.create_rectangle(data.width/2 - 70, data.height/2 - 15,
                            data.width/2 + 70, data.height/2 + 15, 
                            fill = coolTurquoise, outline = deepBlue, width = 2)
                            
    canvas.create_text(data.width/2, data.height/2, text ="Rate popular Books!",
                 fill = deepBlue)
                            
    

def searchButtonPressed(event,data):
    if (event.x >= data.width/2 - 80 and event.x <= data.width/2 + 80
      and event.y >= data.height/2 + 35 and event.y <= data.height/2 + 65 ):
        playSound()
        return True
    return False
            

def rateButtonPressed(event, data):
    if (event.x >= data.width/2 - 55 and event.x <= data.width/2 + 55
      and event.y >= data.height/2 - 20 and event.y <= data.height/2 + 20):
        playSound()
        return True
    return False
    
# Randomly generates a new username, using capital letters and numbers   
def generateUsername(data, shortenedDict):
    codeSpace = string.ascii_uppercase + string.digits
    prefix = "user"
    randomGeneration = random.sample(list(codeSpace), 8)
    return prefix + ''.join(randomGeneration)

################################################################################
 # Search screen functions

def searchScreenMousePressed(event, data):
    # check if text entry mode is on
    if (event.x <= data.width/2 + 80 and event.x >= data.width/2-80,
        event.y <= 30 and event.y >= 10):
        data.enterMode = not data.enterMode
    # check if the backspace button has been clicked, and removes last
    # letter of string
    if (event.x <= data.width/2 + 200 and event.x >= data.width/2 + 160 
     and event.y >= data.height/6-30 and event.y <= data.height/6+ 20):
        if len(data.search) > 0:
            data.search = data.search[:-1]
    # checks if the back button has been pressed, brings us back to mode
    # selections screen
    if event.x <= 100 and event.x >= 0 and event.y <= 52 and event.y >= 0:
        
        playSound()
        data.mode = "loginScreen"
    # checks if the magnifying glass has been pressed, and runs search     
    if (event.x >= data.width/2 -50  and event.x<= data.width/2 + 50 and
     event.y >= data.height/2 and event.y <= data.height/2 + 100):
        data.mode = "searchRatings"
       
        data.searchResults = searchFunction(searchMap, data)
        print("Search results: ", data.searchResults)
        data.search = ""
        
        
        
    
def searchScreenRedrawAll(canvas, data):
    
    canvas.create_image(data.width/2, data.height/2,image = data.searchImage)
    
    
    drawBackButton(canvas, data)
    # This is the text box
    canvas.create_rectangle(data.width/2-200, data.height/6-50,data.width/2+200,
                            data.height/6+ 50, fill = "white")
    canvas.create_image(data.width/2 + 180, data.height/6-20,
                             image = data.backspaceButton)
    # The text the user types is drawn in the text box
    canvas.create_text(data.width/2, data.height/6, text = data.search)
    
                            
                            
    
def searchScreenKeyPressed(event, data):
    if data.enterMode == True:
        # check if delete button is pressed
        if event.keysym == "Delete":
            if len(data.search) > 0:
                data.search = data.search[:-1]
        else:
            data.search += event.char
        # draw text on new line once line width exceeds 50 characters
        if len(data.search) % 50 == 0:
            data.search += "\n"

def searchScreenTimerFired(data):
    pass


################################################################################
# Search ratings functions


    
def searchRatingsKeyPressed(event, data):
    pass
    
    
def searchRatingsTimerFired(data):
    pass
    
    
def searchRatingsMousePressed(event, data):
    # The next books in the list are displayed 
    if data.mode == "searchRatings" and nextTenButtonPressed(event, data):
        data.searchResultsCounter += 1
    # The previous in the list are displayed 
    elif (data.mode=="searchRatings" and previousTenButtonPressed(event,data)and
        data.searchResultsCounter > 0):
        data.searchResultsCounter -= 1 
    #checks if the back button has been pressed, bringing us back to 
    # the main search screen
    elif event.x <= 100 and event.x >= 0 and event.y <= 52 and event.y >= 0:
        data.mode = "searchScreen"
        
        #############
        resetData(data)
        if data.finalSelection2 != None:
            for (key,value) in data.finalSelection2.items():
                i = key[0]
                counterValue = key[1]
                # get book from i and counter
                book = data.searchResultsList[i + 3*counterValue]
                # convert book title to ISBN
                try:
                    
                    ISBNNumber = booksToISBNs[book]
                    data.enterValues[ISBNNumber] = value
                except: print("Oops!")
  
        data.permSearchSelectionRatings = {}
        #############
    if data.submitActivate == True:
        checkSubmitPressed(event, data)
    checkSearchRatings(event, data)
    
def resetData(data):
        
    data.permSearchSelectionRatings = data.searchSelectionRatings
    data.searchSelectionRatings= {}
    data.searchSelectionFrequencies = {}
    
    data.finalSelection2 = data.permSearchSelectionRatings
    data.permSearchSelectionRatings = {}    

    
def checkSearchRatings(event, data):
    data.searchResultsList = list(data.searchResults)
    
    searchResults = list(data.searchResults)
    
    startIndex = data.searchResultsCounter*3
    endIndex = startIndex + 3
    bookDisplayList =  searchResults[startIndex:endIndex]
    
    for i in range(len(bookDisplayList)):
        
        book = bookDisplayList[i]
        rectanglesBeginningWidth = data.width/20
        rectanglesBeginningHeight = (data.height/5)*(i+1.5) + 10
        rectanglesEndWidth = data.width - rectanglesBeginningWidth
        
        cellWidth = (rectanglesEndWidth-rectanglesBeginningWidth)/10
        rectanglesEndHeight = rectanglesBeginningHeight + cellWidth
        cellHeight = cellWidth
        # gets the dimesion of each individual star
        for score in range(10):
            left = rectanglesBeginningWidth + score*cellWidth
            top = rectanglesBeginningHeight
            right = left + cellWidth
            bottom = top + cellHeight
            if (event.x <= right and event.x >= left and event.y >= top
                and event.y <= bottom):
                
                selection = (i,data.searchResultsCounter)
                pick = (i,data.searchResultsCounter, score)
                
                # checks how many times the star has been clicked, and 
                # appropriate toggle occurs
                addScore(data, pick, score, selection)
                
               
                
    if data.searchCounter + len(data.popularSelectionRatings)>=10:
        data.submitActivate = True 
    else:
        data.submitActivate = False
    
def addScore(data, pick, score, selection):
    data.searchSelectionFrequencies[pick] = data.searchSelectionFrequencies.get(pick, 0) + 1
    if data.searchSelectionFrequencies[pick] % 2 == 1:
    
        data.searchSelectionRatings[selection] = score + 1
        data.searchCounter += 1
        
        data.permSearchSelectionRatings[selection] = score + 1

    else:
        del data.searchSelectionRatings[selection]
        data.searchCounter -= 1
        del data.permSearchSelectionRatings[selection]   

def drawBackground(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.libraryImage)
    drawBackButton(canvas, data)
    canvas.create_rectangle(0, data.height/6,
         data.width, 4*data.height/5, fill = "white")
 
def drawBackgroundText(canvas, data):
    canvas.create_text(data.width/2, 80, 
    text = "Please rate 10 or more books!", font = "Arial 26")
    canvas.create_text(data.width/2, 50, text = "Books rated so far: %d" 
        %((data.searchCounter)+ len(data.popularSelectionRatings)))

def searchRatingsRedrawAll(canvas, data):
    drawBackground(canvas, data)
    loadThumbnails(data)
    searchResults = list(data.searchResults)
    
    if len(searchResults) != 0:
        drawBackgroundText(canvas, data)
        # Displays 3 books at a time depending on how many times 
        #next has been clicked
        startIndex = data.searchResultsCounter*3
        endIndex = startIndex + 3
        bookDisplayList =  searchResults[startIndex:endIndex]
        
        bookImages = makeBookImageDict(bookDisplayList)
    
        allThumbnails = [data.book0Image, data.book1Image, data.book2Image, 
                       data.book3Image, data.book4Image]
        for i in range(len(bookDisplayList)):
        
            book = bookDisplayList[i]
            bookText = book
            # ensures that the title of the book and the image do not overlap
            if len(book) > 35: bookText = book[:32] + "..."
            thumbnail = bookImages[book]
            try: response = requests.get(thumbnail)
            except:
                link='http://images.amazon.com/images/P/0312117388.01.THUMBZZZ.jpg'
                response = requests.get(link)
            # convert image from internet link into usable image    
            img = PIL.Image.open(BytesIO(response.content))    
            if img.mode != "RGB": img = img.convert("RGB")
                
            img.save("temp%d.jpg" %(i))
            # draw the image at the required location, along with the name of 
            # the book
            canvas.create_text(data.width/2, (data.height/5)*i+ 175,
                              text = bookText, font = "Arial 16")
            canvas.create_image(4*data.width/5,(data.height/5)*i+ 175,
                            image = allThumbnails[i])
            drawSearchRectanglesHelper(i, canvas, data)
        drawScreenButtons(canvas, data, searchResults)
    else: drawNoMatches(canvas, data)
    
def drawScreenButtons(canvas, data, searchResults):
    # draw next button only if more than 3 books are in the search,
    # or until we're at the last few books        
    if (len(searchResults) > 3 and (data.searchResultsCounter+1)*3 
        < len(searchResults)):  drawNextButton(canvas, data)
        
    
    # Display the option to display previous top 10 only if the next button
    # has been clicked at least one time
    if data.submitActivate == True:  drawSubmitButton(canvas, data)
        
    
    if data.searchResultsCounter > 0: drawPreviousButton(canvas, data)
            
def drawSearchRectanglesHelper(i, canvas, data):
    
    
    rectanglesBeginningWidth = data.width/20
    rectanglesBeginningHeight = (data.height/5)*(i+1.5) + 10
    rectanglesEndWidth = data.width - rectanglesBeginningWidth
    
    cellWidth = (rectanglesEndWidth-rectanglesBeginningWidth)/10
    rectanglesEndHeight = rectanglesBeginningHeight + cellWidth
    cellHeight = cellWidth
    
    
    for score in range(10):
        left = rectanglesBeginningWidth + score*cellWidth
        top = rectanglesBeginningHeight
        right = left + cellWidth
        bottom = top + cellHeight
        canvas.create_image((left+right)/2, (top+bottom)/2, image = data.star)
        
    # if a star has been clicked, checks whether score is being toggled,
    # or another star has been clicked, and accordingly adds the appropriate
    # score and draws highlighted/ normal star    
        if ((i,data.searchResultsCounter,score) in 
data.searchSelectionFrequencies 
and data.searchSelectionFrequencies[(i, data.searchResultsCounter,score)]%2 ==1
and (i, data.searchResultsCounter) in data.searchSelectionRatings and 
data.searchSelectionRatings[(i, data.searchResultsCounter)] == score+1):
                
            canvas.create_image((left+right)/2, (top+bottom)/2, 
                                image = data.highlightedStar)
       
        textCX = (right+left)/2
        textCY = (top+bottom)/2
        canvas.create_text(textCX, textCY, text = score+1)
        
            

def drawNoMatches(canvas, data):
    canvas.create_text(data.width/2, data.height/3, 
        text = "Oops! No books matched your search.", font = "Arial 25")
    canvas.create_text(data.width/2, data.height/3 + 60, 
                text = "Please try again.", font = "Arial 25")
        
        
################################################################################
    
# Draw a list of the recommended books
    

def recommendationScreenKeyPressed(event, data):
    pass
    
def recommendationScreenTimerFired(data):
    pass
    
def recommendationScreenMousePressed(event, data):
    xLoc = event.x
    yLoc = event.y
    if data.currentUserRecommendations != None:
    
        for i in range(len(data.currentUserRecommendations)):
            book = data.currentUserRecommendations[i]
            # These are the locations of the "get book" button
            left = data.width/2 - 40
            right = data.width/2 + 40
            top = (data.height/7)*i + 100
            bottom = top + 30
            # checks which of the get book buttons has been pressed
            # and accordingly googles that book
            if xLoc <= right and xLoc >= left and yLoc >= top and yLoc <=bottom:
                
                webbrowser.open("http://www.google.com/search?q=" +book+" book")
        # Checks if the visualise button has been pressed, and if so,
        # draws the graph
        if (event.x <= data.width/2 + 115 and event.x >=  data.width/2+25
            and event.y >= 5*data.height/6-5 and event.y <= 5*data.height/6+55):
            plotRecommendationGraph(data)
         
        
        if (event.x <= data.width/2 -25 and event.x >=  data.width/2-115
            and event.y >= 5*data.height/6 and event.y <=  5*data.height/6+50):
            data.mode = "loginScreen"
    else:
        if (event.x <= data.width/2 +45 and event.x >=  data.width/2-45
            and event.y >= 5*data.height/6 and event.y <=  5*data.height/6+50):
            data.mode = "loginScreen"

    
        
import matplotlib.pyplot as plt

# draws a graph for the rating the user gave a book against the
# average rating of the book
def plotRecommendationGraph(data):
    
    bookAverages = []
    # Ratings of the user for a particular book
    userRatings = data.enterValues
    # points that need to be plotted
    choices = []
    bookNames = []
    
    for book in userRatings:
       
        bookAverages.append(averageRatingOfBook(book, shortenedDict))
        
        bookNames.append(bookMappings[book])
        
        choices.append(userRatings[book])
        
    fig, ax = plt.subplots()
    ax.scatter(choices, bookAverages)
    # labels for the x and y axes
    plt.ylabel('Book Average Rating')
    plt.xlabel('Your Rating')
    for i in range(0,len(bookNames)):
        book = bookNames[i]
        # annotates the particular point with the name of the book
        ax.annotate(book, ( choices[i], bookAverages[i]))
    
    fig.show()
    
    
       
def createRecommendationButtons(canvas, data):
    bluishGreen = rgbString(179,226,224)
    outlineColor = rgbString(21,85,119)
    # This creates the "rate more" button at the lower left corner
    # outer rectangle
    canvas.create_rectangle(data.width/2-115, 5*data.height/6-5, 
                           data.width/2 -25, 5*data.height/6+55,
                           fill = bluishGreen, outline = outlineColor,width = 3)
    # inner rectangle
    canvas.create_rectangle(data.width/2-110, 5*data.height/6, data.width/2 -30,
                           5*data.height/6+50,
                           fill = bluishGreen, outline = outlineColor, width= 3)
    canvas.create_text(data.width/2-70, 5*data.height/6+25, text = "Rate more!",
                       fill =outlineColor )
     # This creates the "visualise" button at the lower right corner
     # outer rectangle
    canvas.create_rectangle(data.width/2+25,5*data.height/6-5,data.width/2+115, 
                            5*data.height/6+55,
                           fill = bluishGreen, outline = outlineColor,width = 3)
    # inner rectangle
    canvas.create_rectangle(data.width/2+30, 5*data.height/6, data.width/2+110, 
                           5*data.height/6+50,
                           fill = bluishGreen, outline = outlineColor, width=3)
    canvas.create_text(data.width/2+70, 5*data.height/6+25, text = "Visualize!",
                           fill =outlineColor )
    
    
def loadThumbnails(data):
    loadBook0(data)
    loadBook1(data)
    loadBook2(data)
    loadBook3(data)
    loadBook4(data)
    

def recommendationScreenRedrawAll(canvas, data):
    
    loadThumbnails(data)
    
    if data.currentUserRecommendations != None:
        
        canvas.create_image(data.width/2, data.height/2,
                          image = data.recommendationScreen)
        bookImages = makeBookImageDict(data.currentUserRecommendations)
        allThumbnails = [data.book0Image, data.book1Image, data.book2Image, 
                         data.book3Image, data.book4Image]
                
            
            
        for i in range(len(data.currentUserRecommendations)):
        
            book = data.currentUserRecommendations[i]
            bookText = book
            # Truncate the displayed title so it does not overlap with image
            if len(book) > 35: bookText = book[:32] + "..."
                
            thumbnail = bookImages[book]
        
            try:
                response = requests.get(thumbnail)
                
            except:
                link =('http://images.' +
                 'amazon.com/images/P/0312117388.01.THUMBZZZ.jpg')
                response = requests.get(link)
                
            img = PIL.Image.open(BytesIO(response.content)) 
            
            # If the image is encoded in another format,
            # change mode to RGB   
            if img.mode != "RGB": img = img.convert("RGB")
            # dynamically updates the saved file so we don't have to 
            # download the entire database of images.
            img.save("temp%d.jpg" %(i))
                
            canvas.create_image(4*data.width/5,(data.height/7)*i+ 120,
                                image = allThumbnails[i])
            drawGetBookButtons(canvas, i, data)
            
            book = data.currentUserRecommendations[i]
            canvas.create_text(data.width/2,(data.height/7)*i+80,text= bookText)
            
        createRecommendationButtons(canvas, data)
    else: drawNoRecommendationsScreen(canvas, data)
        

def drawGetBookButtons(canvas, i, data):
    bluishGreen = rgbString(179,226,224)
    outlineColor = rgbString(21,85,119)
    left = data.width/2 - 40
    right = data.width/2 + 40
    top = (data.height/7)*i + 100
    bottom = top + 30
    getCenter = (top + bottom)/2
    # outer rectangle
    canvas.create_rectangle(left-5, top-5, right+5, bottom+5, 
                 fill = bluishGreen, outline = outlineColor, width = 2)
    # inner rectangle
    canvas.create_rectangle(left, top, right, bottom, fill = bluishGreen,
                outline = outlineColor, width = 2)
    canvas.create_text(data.width/2, getCenter, 
                    text = "Get Book!", fill = outlineColor)
    
        
def drawNoRecommendationsScreen(canvas, data):
    bluishGreen = rgbString(179,226,224)
    outlineColor = rgbString(21,85,119)
        
    canvas.create_image(data.width/2, data.height/2, image = 
                           data.noRecommendationsScreen)
    drawRateMoreButton(canvas, data)
    
def drawRateMoreButton(canvas, data):
    # outer rectangle    
    bluishGreen = rgbString(179,226,224)
    outlineColor = rgbString(21,85,119)
    canvas.create_rectangle(data.width/2-45, 5*data.height/6-5, 
                           data.width/2 +45, 5*data.height/6+55,
                        fill = bluishGreen, outline = outlineColor, width = 3)
    # inner rectangle
    canvas.create_rectangle(data.width/2-40, 5*data.height/6, data.width/2 +40,
                         5*data.height/6+50,
                        fill = bluishGreen, outline = outlineColor, width = 3)
    canvas.create_text(data.width/2, 5*data.height/6+25, text = "Rate more!", 
                        fill =outlineColor )
        
  
        
################################################################################

# Rate mode functions


def checkSubmitPressed(event, data):
    # checks that the submit button has been pressed, changes the mode
    # to recommendations
    if (event.x >= data.width/2 - 50 and event.x <= data.width/2 + 50
      and event.y >= (data.height/8)*7-20 and event.y <= (data.height/8)*7+20):
        data.mode = "recommendationScreen"
        
        # gets two separate dictionaries, one with ratings from popular mode
        # and other from search mode. We cannot have the same dectionary,
        # otherwise clicks in popular mode will also transfer to search
        data.finalSelection1 = data.popularSelectionRatings 
    
        resetSearchDicts(data)
    
        # checks that popular ratings are not empty
        if data.finalSelection1 != None:
            for (key,value) in data.finalSelection1.items():
                i = key[0]
                counterValue = key[1]
                # get book from i and counter
                book= mostPopularBooks[len(mostPopularBooks)-1-3*counterValue-i]
                # convert book title to ISBN
                try:
                    ISBNNumber = booksToISBNs[book]
                    data.enterValues[ISBNNumber] = value
                except: print("Oops!")
        # checks that search ratings are not empty            
        if data.finalSelection2 != None:
            for (key,value) in data.finalSelection2.items():
                i = key[0]
                counterValue = key[1]
                # get book from i and counter
                book = data.searchResultsList[i + 3*counterValue]
                # convert book title to ISBN
                try:
                    
                    ISBNNumber = booksToISBNs[book]
                    data.enterValues[ISBNNumber] = value
                except: print("Oops!")
  
        shortenedDict[data.username] =(data.enterValues)
        averagesOfUsers[data.username] = averageRatingOfCurrentUser(data.username, shortenedDict)
        data.currentUserRecommendations = topBookRecommendations(data, shortenedDict)
       
def resetSearchDicts(data):
    data.searchSelectionFrequencies = {}
    data.searchSelectionRatings = {}
    data.finalSelection2 = data.permSearchSelectionRatings
    data.permSearchSelectionRatings = {}

def rateBooksMousePressed(event, data):
    if data.mode == "rateBooks" and nextTenButtonPressed(event, data):
        data.mostPopularCounter += 1
    elif (data.mode=="rateBooks" and previousTenButtonPressed(event, data) and
        data.mostPopularCounter > 0):
        data.mostPopularCounter -= 1  
    # if the back button is pressed, brings us back to mode selection screen
    elif event.x <= 100 and event.x >= 0 and event.y <= 52 and event.y >= 0:
        data.mode = "loginScreen"
    if data.submitActivate == True:
        checkSubmitPressed(event, data)
    checkRatings(event, data)
    
def checkRatings(event, data):
    bookNumber = len(mostPopularBooks)
    startIndex = bookNumber-1-data.mostPopularCounter*3
    endIndex = bookNumber-1-data.mostPopularCounter*3-3
    bookDisplayList = mostPopularBooks[startIndex:endIndex:-1]
    for i in range(len(bookDisplayList)):
       
        book = bookDisplayList[i]
        checkRatingsHelper(i, event, data)
      
    # The total number of books rated is greater than or equal to 10  
       
    if (data.searchCounter) + len(data.popularSelectionRatings)>=10:
        data.submitActivate = True 
    else:
        data.submitActivate = False
    print(data.popularSelectionRatings)
    
def checkRatingsHelper(i, event, data):
    # The dimensions of the rectangle in which the stars are drawn
    rectanglesBeginningWidth = data.width/20
    rectanglesBeginningHeight = (data.height/5)*(i+1.5) + 10
    rectanglesEndWidth = data.width - rectanglesBeginningWidth
    
    # We define the dimensions of the rectangle surrounding every star
    # in order to determine where we've clicked so that the appropriate
    # score can be registered
    cellWidth = (rectanglesEndWidth-rectanglesBeginningWidth)/10
    rectanglesEndHeight = rectanglesBeginningHeight + cellWidth
    cellHeight = cellWidth
    for score in range(10):
        left = rectanglesBeginningWidth + score*cellWidth
        top = rectanglesBeginningHeight
        right = left + cellWidth
        bottom = top + cellHeight
        if (event.x <= right and event.x >= left and event.y >= top
            and event.y <= bottom):
            selection = (i,data.mostPopularCounter)
            pick = (i,data.mostPopularCounter, score)
            
            # these conditions allow us to toggle our rating/ change to a new
            # rating by clicking on another star.
            data.popularSelections[pick]=data.popularSelections.get(pick,0) + 1
            if data.popularSelections[pick] % 2 == 1:
            
                data.popularSelectionRatings[selection]=score+1
            else:
                
                del data.popularSelectionRatings[selection]
        # Checks if, for the first three books, the cover of the book has been
        # clicked; and if so, plays a short summary.
        # I have only implemented this feature for the first few books
        elif (data.mostPopularCounter==0 and event.x <= 4*data.width/5 + 25 and
             event.x >= 4*data.width/5 - 25 and event.y <=(data.height/5*i +225)
             and event.y >= (data.height/5*i + 125)):
            
            if i == 0:
                lovelyBonesSummary()
                break
            elif i == 1:
                daVinciCodeSummary()
                break
            elif i == 2:
                redTentSummary()
                break
            
################################################################################
            
    
def nextTenButtonPressed(event, data):
    if (event.x >= (data.width/8)*7-60 and event.x <= (data.width/8)*7+60
      and event.y >= (data.height/8)*7-20 and event.y <= (data.height/8)*7+20):
        playSound()
        return True
        


def previousTenButtonPressed(event, data):
    if (event.x >= (data.width/8)-60 and event.x <= (data.width/8)+60
      and event.y >= (data.height/8)*7-20 and event.y <= (data.height/8)*7+20):
        playSound()
        return True   
                       

    
def rateBooksKeyPressed(event, data):
    pass
    
        
def rateBooksTimerFired(data):
    pass
    
    
def rateRedrawAllHelper(canvas,data):
    loadThumbnails(data)
  
    deepBlue = rgbString(0, 0, 91)
    
    canvas.create_image(data.width/2, data.height/2, image = data.libraryImage)
    # makes the white rectangle enveloping the books
    drawBackButton(canvas, data)
    canvas.create_rectangle(0, data.height/6,
         data.width, 4*data.height/5, fill = "white")
    
    canvas.create_text(data.width/2, 80, 
     text = "Please rate 10 or more books!", fill = deepBlue,
              font = "Arial 26 bold")
    canvas.create_text(data.width/2, 50, text = "Books rated so far: %d"
     %((data.searchCounter) + len(data.popularSelectionRatings)),
                      fill = deepBlue,
      font = "Arial 20 bold")
  
def drawBackButton(canvas, data):
    deepBlue = rgbString(0, 0, 91)
    canvas.create_rectangle(2,2, 100, 52, outline = deepBlue, width = 3)
    canvas.create_text(50, 26, text = "Back", fill = deepBlue, font = "bold")
    
    
def rateBooksRedrawAll(canvas, data):
    # Images have to be reloaded because they change every time next 
    # or previoud is pressed
    rateRedrawAllHelper(canvas,data)
    
    bookNumber = len(mostPopularBooks)
    # We start at the end, to ensure most popular books display first.
    startIndex = bookNumber-1-data.mostPopularCounter*3
    endIndex = bookNumber-1-data.mostPopularCounter*3-3
    bookDisplayList = mostPopularBooks[startIndex:endIndex:-1]
    
    
    bookImages = makeBookImageDict(bookDisplayList)
    
    allThumbnails = [data.book0Image, data.book1Image, data.book2Image,
              data.book3Image, data.book4Image]
    
    for i in range(len(bookDisplayList)):
       
        book = bookDisplayList[i]
        bookText = book
        # Truncate title so it does not spill onto image
        if len(book) > 35:
            bookText = book[:32] + "..."
        thumbnail = bookImages[book]
       
        try:
            response = requests.get(thumbnail)
            
        except:
            link ='http://images.amazon.com/images/P/0312117388.01.THUMBZZZ.jpg'
            response = requests.get(link)
            
        img = PIL.Image.open(BytesIO(response.content))    
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save("temp%d.jpg" %(i))
        # Draw the different titles of the book
        canvas.create_text(data.width/2,(data.height/5)*i+ 175,text = bookText,
                           font = "Arial 16")
        # Create cover thumbnails at appropriate spots
        canvas.create_image(4*data.width/5,(data.height/5)*i+ 175,
                    image = allThumbnails[i])
        
        drawRectanglesHelper(i, canvas, data)
    drawNextButton(canvas, data)                               
   

    # Display the option to display previous top 10 only if the next button
    # has been clicked at least one time
    if data.submitActivate == True: drawSubmitButton(canvas, data)
       
        
    if data.mostPopularCounter > 0: drawPreviousButton(canvas, data)
        
        
def drawRectanglesHelper(i, canvas, data):
    
    # The beginning of the point from which the stars are drawn
    rectanglesBeginningWidth = data.width/20
    rectanglesBeginningHeight = (data.height/5)*(i+1.5) + 10
    # End width of the stars
    rectanglesEndWidth = data.width - rectanglesBeginningWidth
    
    cellWidth = (rectanglesEndWidth-rectanglesBeginningWidth)/10
    rectanglesEndHeight = rectanglesBeginningHeight + cellWidth
    cellHeight = cellWidth
    
    
    for score in range(10):
        # dimensions of the each star; so that we can figure out where to 
        # draw the image
        left = rectanglesBeginningWidth + score*cellWidth
        top = rectanglesBeginningHeight
        right = left + cellWidth
        bottom = top + cellHeight
        canvas.create_image((left+right)/2, (top+bottom)/2, image = data.star)
        
        # check the conditions to see whether the rating has been toggled,
        # or to see whether another score has been picked
        if ((i, data.mostPopularCounter,score) in data.popularSelections
and data.popularSelections[(i, data.mostPopularCounter,score)]%2 ==1
and (i, data.mostPopularCounter) in data.popularSelectionRatings and 
data.popularSelectionRatings[(i, data.mostPopularCounter)] == score+1):
            # accordingly, we draw a normal or highlighted star.
            canvas.create_image((left+right)/2, (top+bottom)/2, 
             image = data.highlightedStar)
      
        textCX = (right+left)/2
        textCY = (top+bottom)/2
        canvas.create_text(textCX, textCY, text = score+1)
        
            

def drawNextButton(canvas, data):
    deepBlue = rgbString(0, 0, 91)
    paleTurquoise = rgbString(64,224,208)
    left = (data.width/8)*7-60
    top = (data.height/8)*7-20
    right = (data.width/8)*7+60
    bottom = (data.height/8)*7+20
    canvas.create_rectangle(left,top ,right, bottom,
                                 outline = deepBlue, width = 3)
    canvas.create_text(data.width/8*7, data.height/8*7,
                        text = "Next 3 books", fill = deepBlue, font = "bold")
            

def drawSubmitButton(canvas, data):
    deepBlue = rgbString(0, 0, 91)
    canvas.create_rectangle((data.width/2)-50, (data.height/8)*7-20,
                            (data.width/2) + 50, 
                            (data.height/8)*7+20, outline = deepBlue, width = 3)
    canvas.create_text((data.width/2),(data.height/8)*7, text = "Submit!",
                       fill = deepBlue, font = "bold")

def drawPreviousButton(canvas, data):
    deepBlue = rgbString(0, 0, 91)
    canvas.create_rectangle((data.width/8)-60, (data.height/8)*7-20,
                (data.width/8)+60, (data.height/8)*7+20, outline = deepBlue,
                width = 3)
    canvas.create_text(data.width/8, (data.height/8)*7,
            text = "Previous 3 books",fill = deepBlue, font = "bold")    

# This maps the book titles to their respective thumbnail image links    
def makeBookImageDict(bookDisplayList):
    bookImageDict = {}
    for i in range(len(bookDisplayList)):
        bookName = bookDisplayList[i]
        ISBN = booksToISBNs[bookName]
        thumbnail = ISBNToThumbnails[ISBN]
        bookImageDict[bookName] = thumbnail
    return bookImageDict

################################################################################
# This is where the algorithm part of the code begins and the UI stops

# Here, default dict is used to create a 2D dictionary (dictionary inside 
# dictionary)
from collections import defaultdict
import math
import random
import csv
import PIL
import PIL.Image
from PIL import Image, ImageTk
import tkinter 
from tkinter import *

# These are used to visualise the data using graphs
import matplotlib.pyplot as plt


################################################################################


# This makes a matrix, so that we can access the matrix as follows:
# matrix[userID][ISBN] = rating
dict2D = defaultdict(dict)

# Here,the nonlocal variable x is used simply to tell us which lines have errors
with open("/Users/aditribhagirath/Desktop/BX-Book-RatingsUTF.csv",
      encoding = "utf-8") as f:
          
    # We want to specify a delimiter as new line character, otherwise
    # the csv reader will split on commas within book titles. 
    # this originally led to several bugs in the code.
    ratingsFile = csv.reader(f, delimiter = "\n")
    x = 0
    for line in ratingsFile:
        # Sometimes, the CSV file contains unreadable characters.
        try:
            element = line[0]
            elementComponents = element.split(";")
            userID = elementComponents[0]
            ISBN = elementComponents[1][1:-1] # removes quotation marks
            rating = int(elementComponents[2][1:-1]) # removes quotation marks
            
            if rating != 0:
                dict2D[userID][ISBN] = rating
                x += 1
        # sometimes, the file may contain non-ascii, unreadable characters.
        # we do not want the program to crash in those cases.  
        except:
            print(x, "Error") 
       


bookMappings = {}

# Maps the ISBN to the link of the thumbnail image
ISBNToThumbnails = {}

i = 0
with open("/Users/aditribhagirath/Downloads/BX-CSV-Dump-4/BX-Bookslb.csv", 
          encoding = "utf-8") as g:
              
    # We want to specify a delimiter as new line character, otherwise
    # the csv reader will split on commas within book titles. 
    # this originally led to several bugs in the code.
    books = csv.reader(g, delimiter = '\n')
    
  
    for line in books:
        try:
          
            book = line[0].replace('"', "")
        
            information = book.split(";")
            
            number = information[0]
            
            title = information[1]
            # the link for the thumbnail occurs at index 5
            thumbnail = information[5]
            
            ISBNToThumbnails[number] = thumbnail
        
            
            bookMappings[number] = title
            i += 1
        # sometimes, the file may contain non-ascii, unreadable characters.
        # we do not want the program to crash in those cases.
        except:
            print(i, "Error")

                   
def correlation(user1, user2):
    
    
    user1Ratings = shortenedDict[user1]
    user2Ratings = shortenedDict[user2]
    
   
    user1Average = averagesOfUsers[user1]
    user2Average = averagesOfUsers[user2]
   
    
    # Now, we want to implement the formula
    numeratorSummation = 0
    denominatorSummationTerm1 = 0
    denominatorSummationTerm2 = 0
    
    
    # If all of the user's ratings are the same, the correlation between that
    # And any other user comes out to be zero,because if a user rates everything
    # the same, we assume their opinion does not matter as they lack
    # preferences
   
    # For each ISBN in user1Ratings
    for key in user1Ratings:
        if key in user2Ratings:
   
            
            user1Diff = user1Ratings[key] - user1Average
            user2Diff = user2Ratings[key] - user2Average
            
            numeratorSummation += user1Diff*user2Diff
            
            denominatorSummationTerm1 += user1Diff**2
            denominatorSummationTerm2 += user2Diff**2
    
    
    denominator = math.sqrt(denominatorSummationTerm1*denominatorSummationTerm2)
    if denominator != 0:    
        return (numeratorSummation/denominator)
    else:
        return 0
        
# This function narrows our vast user base to only consider those 
# individuals who have read 10 books or more, so that we can get some 
# useful correlation information between their choices. If they have rated
# a very small number of books, it is hard to tell much about their choices.

# Search function implementation attempt

def requiredUserDict(dict2D):
    requiredDict = {}
    for user in dict2D:
        userBookNumber = len(dict2D[user])
        if userBookNumber >= 10:
            requiredDict[user] = dict2D[user]
    return requiredDict
    
shortenedDict = requiredUserDict(dict2D)


# This returns a dictionary mapping the book titles to ISBNs,
# so we can use these to get the recommendations
def invertBookMappings(bookMappings):
    booksToISBN = {}
    for (key,value) in bookMappings.items():
        booksToISBN[value] = key
        
    return booksToISBN
        
booksToISBNs = invertBookMappings(bookMappings)    
      


def bookFrequenciesDict(shortenedDict):
    bookFrequencies = {}
    for user in shortenedDict:
        for book in shortenedDict[user]:
            if book in bookFrequencies:
                bookFrequencies[book] += 1
            else:
                bookFrequencies[book] = 1
    return bookFrequencies

# This simply maps the book to the number of readers
bookFrequencies = bookFrequenciesDict(shortenedDict)  

# This returns a list of books, sorted by order of how many times they have
# appeared.  
sortedBookFrequencies = list(sorted(bookFrequenciesDict(shortenedDict).items(), 
                             key=lambda x:x[1]))

# Makes a list of the books that have beenread by a lot of people
def popularBooksList(sortedBookFrequencies):
    ascendingBookList = []
    for book in sortedBookFrequencies:
        ISBNvalue = book[0]
        if ISBNvalue in bookMappings:
            ascendingBookList.append(bookMappings[ISBNvalue])
    # We reverse the list so that the most popular books are displayed first.
    return ascendingBookList
        
mostPopularBooks = popularBooksList(sortedBookFrequencies)
    
def sortedFrequencyOfBooks(shortenedDict):
    bookFrequencies = {}
    for user in shortenedDict:
        for book in shortenedDict[user]:
            if book in bookFrequencies:
                bookFrequencies[book] += 1
            else:
                bookFrequencies[book] = 1
    sortedFrequencies=list( sorted(bookFrequencies.items(), key=lambda x:x[1]))
    return sortedFrequencies
    
# Returns the average rating that the current user gives to books
def averageRatingOfCurrentUser(currUser, shortenedDict):
    
    total = 0
    count = 0
    for book in shortenedDict[currUser]:
        total += shortenedDict[currUser][book]
        count += 1
    return (total/count)




# Computes the averages of all the different users at once so we
# can directly access these in subsequent prediction functions    

def averageRatingOfUser(user, shortenedDict):
    total = 0
    count = 0
    for book in shortenedDict[user]:
        total += shortenedDict[user][book]
        count += 1
    return (total/count)
    
def userAveragesDict(shortenedDict):
    userAverages = {}
    for user in shortenedDict:
        userAverages[user] = averageRatingOfUser(user, shortenedDict)
    return userAverages

averagesOfUsers = userAveragesDict(shortenedDict)


# This function finds the predicted rating for a user, for books
# They have not yet read, based on the ratings of all other people who
# have read this book.

def ISBNtoReaders(shortenedDict):
    bookToReaders = {}
    for reader in shortenedDict:
        books = shortenedDict[reader]
        for book in books:
            bookToReaders[book] = bookToReaders.get(book, set())
            bookToReaders[book].add(reader)
    return bookToReaders

# Maps ISBNs to the usernames who have read these books   
booksToReaders = ISBNtoReaders(shortenedDict)   

def predictedRatingForItem(data, item, shortenedDict, booksToReaders):
   
    numerator = 0
    personAverage = averagesOfUsers[data.username]
    # These are the total number of users who have read the book.
    totalReaders = len(booksToReaders[item])
    denominator = 0
    
    readersOfItem = booksToReaders[item]
    
    # finds correlation of current user to every other user in the dataset
    for user in readersOfItem:
        userAverage = averagesOfUsers[user]
        
        correlationX = correlation(user, data.username)
        numerator += int(shortenedDict[user][item]-userAverage)*correlationX
        
        denominator += abs(correlationX)
        
    if totalReaders != 0 and denominator != 0:
        predictedBookRating = numerator/denominator
    else:
        predictedBookRating = 0
    # add the person's average; this is called normalising the prediction
    return personAverage + (predictedBookRating)    


# Simply takes in the dictionary, and returns the books mapped to their 
# respective frequencies.

def booksAndReaderNumber(shortenedDict):
   
    bookReaderNumbers = {}
    for user in shortenedDict:
        for book in shortenedDict[user]:
            bookReaderNumbers[book] =  bookReaderNumbers.get(book, 0) + 1
    return bookReaderNumbers
        


# This function takes in the 2D dictionary of users, and outputs the 
# predicted ratings for all users, for all books that they have not yet read,
# based on the prediction function we have designed above.
    

def prediction2dDict(data, shortenedDict):
   
    
    bookReaderNumbers  = booksAndReaderNumber(shortenedDict)
   
    # Makes a new 2D dictionary, which will have the predicted ratings
    # for each user, for every single book in te 
    # database that they have not read.
    predicted2dDict = defaultdict(dict)
    for book in bookReaderNumbers:
        # ensures that at least ten people have read the particular book
        if (book not in shortenedDict[data.username] and 
                                          bookReaderNumbers[book] > 10) :
            #predictedRating = predictedRatingForItem(user, book, requiredDict)
            #if predictedRating!= None and predictedRating >= 9:
            prediction = predictedRatingForItem(data, book, shortenedDict,
                                                booksToReaders)
            
            # When we normalize the prediction (add the user's average to the
            #  prediction, certain ratings may be between 10 and 11
            # if the user's predicted score is more than 8, add it to their
            # recommendations
            if prediction != None and prediction > 8:
                if prediction > 10:
                    prediction = 10
                predicted2dDict[data.username][book]  =  prediction
    
    return predicted2dDict

# This function returns a random sample of books for which the predicted 
# rating of the user is 9 or heigher, so that the user does not get the 
# same recommendations every single time.   

def topBookRecommendations(data, shortenedDict):
    bookList = []
    topBookDict = prediction2dDict(data, shortenedDict)
    for book in topBookDict[data.username]:
        if book in bookMappings:
            bookList.append(bookMappings[book])
    # If some recommendations more than 5 are obtained, return a random sample
    if len(bookList) >= 5:
        return random.sample(bookList, 5)
    else:
        return None
    
    
################################################################################

# Evaluation functions

# These are testing functions, to evaluate the authenticity of the various
# ratings that we get for a particular user

# Due to certain csv characters, sometimes a book may not be found.
# if it is not, set normalMean to 5
def averageRatingOfBook(book, shortenedDict):
    normalMean = 5
    total = 0
    count = 0
    for user in shortenedDict:
        if book in shortenedDict[user]:
            total += int(shortenedDict[user][book])
            count += 1
    if count != 0:
        return (total/count)
    else:
        return normalMean
        

                  
"""
Here is a test case to help see how all of my functions link together.

The book under consideration is 'Little Altars Everywhere: A Novel'

(Getting the ISBN number of 'Little Altars Everywhere')
booksToISBNs['Little Altars Everywhere: A Novel'] = '0060976845'

(Returns a user who satisfies the following two conditions:
-he is the user who has read the maximum number of books out of all those who
have not read Little Alters.)
usersWhoHaveNotRead(dict2D, '0345353145')
'11676'

# The average rating of this user is about 7.3
In [6]: averageRatingOfUser('11676', shortenedDict)
Out[6]: 7.284322928889932

# And, the average rating of the book is about 7.5
In [7]: averageRatingOfBook('0345353145', shortenedDict)
Out[7]: 7.494623655913978


Note: This is the original prediction function that has been adapted for the
UI. Here, I have used this to show how predictions have been made.
def predictedRatingForItem(person, item, shortenedDict):
  
    numerator = 0
    personAverage = averagesOfUsers[person]
    # These are the total number of users who have read the book.
    
    totalReaders = 0
    denominator = 0
    
    
    for user in shortenedDict:
        if item in shortenedDict[user]:
            userAverage = averagesOfUsers[user]
            correlationX = correlation(user, person)
            numerator += int(shortenedDict[user][item]-userAverage)*correlationX
           
            totalReaders += 1
            denominator += abs(correlationX)

    if totalReaders != 0 and denominator != 0:
        predictedBookRating = numerator/denominator
    else:
        return None
    
    return personAverage + (predictedBookRating)

# Now, we predict 11676's rating for Little Alters (approx 7.2)
In [5]: predictedRatingForItem('11676', '0345353145', dict2D)
Out[5]: 7.188988629261849


His predicted rating seems to be fairly reasonable.

-------------------------------------------------------------------------------

(user who has read max number of books among those who have read 
Little Altars)
usersWhoHaveRead(shortenedDict, '0060976845')
'16795'

shortenedDict['16795']['0060976845'] (His actual rating)
7

RemoveBookForPerson returns a new dictionary, where the given book has been
removed, for the person.
In [1]: predictedRatingForItem('16795', '0060976845', 
         removeBookForPerson('16795','0060976845', shortenedDict))
Out[1]: 6.969639889806534

Hence, we can see that his predicted rating is extremely close to his 
actual rating.
"""

# This is a test function to see the accuracy of predictions
# if a person has already read the particular book, we can remove it from
# his dictionary and use our predictions to check what his rating is and compare
def removeBookForPerson(person, book, randomDict):
    
    personDictWithoutBook = {}
    for item in randomDict[person]:
        if item != book:
            personDictWithoutBook[item] = randomDict[person][item]
    randomDict[person] = personDictWithoutBook
    return randomDict
 

    
        
# This is simply a function to find the users who have not read a particular
# Book, for testing purposes for our correlation function.

def usersWhoHaveNotRead(dict2D, item):
    userID = 0
    maxBooks = 0
    hasNotRead = []
    for key in dict2D:
        if item not in dict2D[key]:
            if len(dict2D[key]) > maxBooks:
                userID = key
                maxBooks = len(dict2D[key])
    return userID


# This function is purely for testing purposes. Given a particular book,
# We are finding the person who has read the maximum number of books, who
# Has also read this particular book, so we can find his predicted rating and
# Compare it to his actual rating.
    
def usersWhoHaveRead(dict2D, item):
    userID = None
    maxBooks = 0
    hasRead = []
    for key in dict2D:
        if item in dict2D[key]:
            if len(dict2D[key]) > maxBooks:
                userID = key
                maxBooks = len(dict2D[key])
    return userID
 


# This is the search feature, which works by analysing word frequencies
# in the book titles and returns all the revelant book titles.
################################################################################

# We first count the total occurences of words that are occuring
# in all of the book titles.

def getBookTitleWords(bookFrequencies):
    bookList = bookFrequencies.keys()
    wordFrequencies = {}
    for book in bookList:
        if book in bookMappings:
          
            titleWords = title.split()
            
            for word in titleWords:
                wordFrequencies[word] = wordFrequencies.get(word, 0) + 1
    return wordFrequencies
    


# global wordfrequencies so we don't have to make it again and again
wordFrequencies = getBookTitleWords(bookFrequencies)

# We only care about the words that are not occuring too frequently
# (such as and, the to, etc.) and so we remove these words.    
def shortenedWordList(wordList):
    keyWords = {}
    maxFrequency = 10000
    for word in wordList:
        if wordList[word] < maxFrequency:
            keyWords[word] = wordList[word]
    return keyWords
    
shortenedWordFrequencies = shortenedWordList(wordFrequencies)
 
# This function maps each relevant word to all the books that it appears in.
# A relevant word is any word whose frequency is less than 10000
def searchMappings(wordList, bookMappings):
    wordToBooks = {}
    books = set(bookMappings.values())
    
    # if the word is in the book, add it to the word's set     
    for book in books:
        titleWords = book.lower().split()
        for word in titleWords:
           
            wordToBooks[word] = wordToBooks.get(word, set())
            wordToBooks[word].add(book)
            
    return wordToBooks

# Make a global searchMap so we don't have to call it again and again
searchMap = searchMappings(shortenedWordFrequencies, bookMappings)
    
def searchFunction(searchMap, data):
    userSearch = data.search
    # get all words in the search
    words = userSearch.lower().split()
    
    bookSet = set()
    for word in words:
        
        if word in searchMap:
           # get the intersection of all of the relevant words
            currentWordSet = searchMap[word]
            if bookSet == set():
                bookSet = currentWordSet
            else:
                bookSet = bookSet & currentWordSet
    
    return bookSet    
        
    # Now return the intersection of all the sets in the setlist
    
def testAll():
    def testRemoveBookForPerson():
        sampleDict = defaultdict(dict)
        sampleDict = {"alan":{"A":1, "B":4, "C":2},
                    "lexi": {"B":9, "C":10, "F":5, "R":2, "M":4},
                    "joe": {"H":10, "I":8, "J":3, "K":4}}
        assert(removeBookForPerson("alan", "B", sampleDict) ==
        {"alan":{"A":1, "C":2},
                    "lexi": {"B":9, "C":10, "F":5, "R":2, "M":4},
                    "joe": {"H":10, "I":8, "J":3, "K":4}})
                    
    def testAverageRatingOfBook():
        sampleDict = defaultdict(dict)
        sampleDict = {"alan":{"A":1, "B":4, "C":2},
                    "lexi": {"B":9, "C":10, "F":5, "R":2, "M":4},
                    "joe": {"H":10, "I":8, "J":3, "K":4}}
        assert(averageRatingOfBook("B", sampleDict)==6.5)
        sampleDict = {"alan":{"A":1, "B":4, "C":2},
                    "lexi": {"B":9, "C":10, "F":5, "R":2, "M":4},
                    "joe": {"H":10, "B":8, "J":3, "K":4}}
        assert(averageRatingOfBook("B", sampleDict)==7)
        
    def testGetBookTitleWords():
        testFrequencies =  {'3442455707': 6,
                            '0679967400': 1,
                            '1551664208': 3,
                            '0061093335': 9,
                            '972575235': 1,
                            '2070406962': 6}
                            
        """ Books corresponding to these ISBNs:
        des chr√?¬©tiens et des maures
        milit√?¬§rmusik.
        glasses for d.w. (step-into-reading, step 3)
        nora, nora: a novel
        tender malice"""
        assert(getBookTitleWords(testFrequencies) =={'(step-into-reading,': 1,
                                                        '3)': 1,
                                                        'a': 1,
                                                        'chr√?¬©tiens': 1,
                                                        'd.w.': 1,
                                                        'des': 2,
                                                        'et': 1,
                                                        'for': 1,
                                                        'glasses': 1,
                                                        'malice': 1,
                                                        'maures': 1,
                                                        'milit√?¬§rmusik.': 1,
                                                        'nora,': 1,
                                                        'nora:': 1,
                                                        'novel': 1,
                                                        'step': 1,
                                                        'tender': 1})

################################################################################

def run(width=300, height=300):
    
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    
    
    # create the root and the canvas
    root = tkinter.Toplevel()
    #root.config(cursor = 'boat blue blue')
    init(data)
    canvas = Canvas(root,cursor = "circle",width=data.width,height=data.height)
    canvas.pack()
    
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 700)