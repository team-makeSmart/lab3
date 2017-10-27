# Warm Up

def getPic():
    """prompts a user to pick a file to be converted to a jython picture"""
    
    return makePicture(pickAFile())

def halfRed():
    """ Reduces red in a given image by 1/2 """
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        setRed(p, r * .05)
    repaint(pic)
    
def noBlue():
    """ Removes all blue values from a given image """
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        b = getBlue(p)
        setBlue(p, b * 0)
    repaint(pic)
    
