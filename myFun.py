'''
A collection of helper functions. 

by David Wisniewski (david.wisniewski@ugent.be)

'''
  
from psychopy import core, visual, event, clock
import csv, os, time
from ctypes import windll

# Get a string input
def getString(window, question="Type: text followed by return"):
    string = ""
    while True:
        message = visual.TextStim(window, text=question+string, color = 'white')
        message.draw()
        window.flip()
        c = event.waitKeys()
        if c[0] == 'return':
            return string
        else:
            string = string + c[0]

# create a log file
def openDataFile(ppn=0,type='default_setting',directory= 'CHOOSE A DIRECTORY'):
    """open a data file for output with a filename that nicely uses the current date and time"""
    #directory= "data"
    #directory = "C:/Users/pp02/Desktop/David/IntRewBehPilot1/RawData"
    #directory = "F:/Data/Projects/2017_01_IntRew_Exp1/5-ExperimentFMRI/2-RawData"
               
    if not os.path.isdir(directory):
        os.mkdir(directory)
    try:
        filename="{}/Sub{}_{}_{}.csv".format(directory, '{:02g}'.format(ppn), type, time.strftime('D%Y-%m-%d_T%H:%M:%S')) # ISO compliant
        datafile = open(filename, 'wb')
    except Exception as e:
        filename="{}/Sub{}_{}_{}.csv".format(directory, '{:02g}'.format(ppn), type, time.strftime('D%Y-%m-%d_T%H-%M-%S')) #for MS Windows
        datafile = open(filename, 'wb')
    return datafile          

# show text in the center of the screen
def showText(window, inputText="Text"):
    message = visual.TextStim(window, alignHoriz="center", alignVert="center",text=inputText, color = 'white', font='Lucida Sans', wrapWidth=15, height=0.5)
    message.draw()
    window.flip()


