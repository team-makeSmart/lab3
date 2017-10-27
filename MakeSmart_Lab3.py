# Warm Up

def getPic():
    """ prompts a user to pick a file to be converted to a jython picture """
    
    return makePicture(pickAFile())

def lessRed(percentage):
    """ Reduces the red in an image by a given percentage 
    
    Args:
        percentage (float): Amount of red that will be reduced in the image
    
    """
    
    if not (percentage > 0 and percentage < 1):
        print("lessRed Error - Expected float between 0 and 1. \"%s\" given" % percentage)
        return
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        setRed(p, r * percentage)
    repaint(pic)
    
    

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
    
