# -*- coding: utf-8 -*-

'''
This is a wrapper function that presents different questionnaires in PsychoPy (based on Python 2)

Includes the 
- BISBAS (Carver, Charles S., and Teri L. White. “Behavioral Inhibition, Behavioral Activation, and Affective Responses to Impending Reward and Punishment: The BIS/BAS Scales.” Journal of Personality and Social Psychology 67, no. 2 (1994): 319.)
- SPSRQ (Torrubia, Rafael, César Ávila, Javier Moltó, and Xavier Caseras. “The Sensitivity to Punishment and Sensitivity to Reward Questionnaire (SPSRQ) as a Measure of Gray’s Anxiety and Impulsivity Dimensions.” Personality and Individual Differences 31, no. 6 (October 15, 2001): 837–62. )
- NFC (Catioppo Petty Kao 1984 The efficient assessment of need for cognition. J Personality Assessment 48 306-307)
- BIS11 (Patton Stanford Barratt 1995 Factor structure of the barratt impulsiveness scale. J Clin Psychol 51 768-774)
- EHI (Oldfield, R. C. (1971). The assessment of handedness: The Edinburgh inventory. Neuropsychologia, 9, 97–113.)

All credits to the authors of those questionnaires. Please look into the original papers for licensing information. 

by David Wisniewski (david.wisniewski@ugent.be)

'''

## --------------
## Import modules
## --------------

from psychopy import visual, core, logging, monitors                                # psychopy modules
import myFun                                                                        # my own helper functions functions
import bisbas as bb                                                                 # BIS BAS questionnaire
import ehi                                                                          # edinburgh handedness inventory
import spsrqs                                                                       # sensitivity to reward and punishment questionnaire
import nfc                                                                          # need for cognition
import bis11                                                                        # implsivity

## -------------
## Setup Section
## -------------

# define output directory
outdir = "file path where to save results to"

# define a window
win = visual.Window (size=(1920,1080), fullscr=False, monitor='enter monitor name', units='cm', color=(-1,-1,-1), colorSpace='rgb')

# get the subject number 
input = myFun.getString(win, 'Please enter subject number: ')
subjectnumber = int(input)


## ----------------------
## Present Questionnaires
## ----------------------

# BIS BAS
bb.bisbas (win,subjectnumber,outdir)

# Need for Cognition
nfc.nfc(win, subjectnumber,outdir)

# Sensitivity to Punishment / Sensitivity to Reward
spsrqs.spsrqs(win,subjectnumber,outdir)

# Barratt impulsiveness scale
bis11.bis11(win,subjectnumber,outdir)

# Edinburgh handedness inventory
ehi.handedness(win, subjectnumber,outdir)


## ---------------
## Closing Section
## ---------------

win.close()
core.quit()
