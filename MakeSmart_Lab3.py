# Warm Up

def getPic():
    """prompts a user to pic a file to be converted to a jython picture"""
    
    return makePicture(pickAFile())

def halfRed():
    """ Reduces red in a chosen image by 1/2 """
    
    pic = getPic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        setRed(p, r * .05)
    repaint(pic)
    