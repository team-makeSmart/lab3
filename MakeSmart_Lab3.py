# Warm Up

def getPic():
    """ prompts a user to pick a file to be converted to a jython picture """
    
    return makePicture(pickAFile())
    
def halfRed():
    """ Reduces red in a given image by 1/2 """
    
    lessRed(50)
    
def noBlue():
    """ Removes all blue values from a given image """
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        getBlue(p)
        setBlue(p,0)
    repaint(pic)
    
  
# Problem 1

def lessRed(percentage):
    """Reduces the red in an image by a given percentage""" 
    """Args: percentage (int): Amount of red that will be reduced in the image"""
    
    """If statement is for exception handling for out of range"""
    if (percentage < 0 or percentage > 100):
        print("lessRed Error - Expected value is from 0 to 100. Value given was %s" % percentage)
        return
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        setRed(p, r - ( r * percentage * .01) )
    repaint(pic)
  
  
# Problem 2

def  moreRed(percent):
#Increase the red in each pixel"""
#Args: percentage to increase redness""" 
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    value = r+(r*percent*.01)
    if value < 0 :
      value = 0
    elif value > 255 :
      value = 255
    setRed(p,value) 
  repaint(pic)

# Problem 3

def roseColoredGlasses():
  """ Adjusts relative value of each RGB to create a pink hue in image""" 
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)   
    b = getBlue(p)
    setRed(p,(r + g + b)*.25)
    setGreen(p,(r + g + b)*.12)
    setBlue(p,(r + g + b)*.18)  
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
    
