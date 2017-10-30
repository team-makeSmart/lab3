# Warm Up

def getPic():
    """ prompts a user to pick a file to be converted to a jython picture """
    
    return makePicture(pickAFile())
    
def halfRed():
    """ Reduces red in a given image by 1/2 """
    
    lessRed(.5)
    
def noBlue():
    """ Removes all blue values from a given image """
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        b = getBlue(p)
        setBlue(p, b * 0)
    repaint(pic)
    
    
# Problem 1

def lessRed(percentage):
    """ Reduces the red in an image by a given percentage 
    
    Args:
        percentage (float): Amount of red that will be reduced in the image
    
    """
    
    if not (percentage > 0 and percentage < 1):
        print("lessRed Error - Expected float between 0 and 1. \"%s\" given." % percentage)
        return
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        setRed(p, r * percentage)
    repaint(pic)
  
  
# Problem 2

def  moreRed(value):
  """increases the red in each pixel of an image""" 
  """sets the setColorWrapAround() to false to prevent out of range RGB values"""
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    setColorWrapAround(0)
    r = getRed(p)
    setRed(p, r*value)
  repaint(pic)
  

# Problem 3

def roseColoredGlasses():
  """sets the G and B values to the percentage""" 
  """required for a pink color while R stays at 255"""
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)     
    setGreen(p, g * .41)
    setBlue(p, b * .75)  
    setRed(p, r)   
  repaint(pic)
  

# Probelm 4

def lightenUp():
  """lightens each pixel in a picture"""
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    oldColor = getColor(p)
    newColor = makeLighter(oldColor)
    setColor(p, newColor)
  repaint(pic)
  
  
    
# Problem 5

def makeNegative():
    """ Makes a negative copy of an image """

    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        r = 255 - r
        g = 255 - g
        b = 255 - b
        setRed(p, r)
        setGreen(p, g)
        setBlue(p, b)
    repaint(pic)
    
    
# Problem 6

def BnW():
    """ Converts an image to gray-scale """
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        luminance = (r + g + b) / 3
        setRed(p, luminance)
        setGreen(p, luminance)
        setBlue(p, luminance)
    repaint(pic)
    
def betterBnW():
    """ Converts an image to gray-scale """
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        luminance = r*0.299 + g*0.587 + b*0.114
        setRed(p, luminance)
        setGreen(p, luminance)
        setBlue(p, luminance)
    repaint(pic)
    
