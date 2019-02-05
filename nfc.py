# -*- coding: utf-8 -*-

'''
This script presents the English version of the need for cognition questionnaire, 18 item form.

The NFC was originally published in 
Catioppo Petty Kao 1984 The efficient assessment of need for cognition. J Personality Assessment 48 306-307

by David Wisniewski (david.wisniewski@ugent.be)

'''

def nfc (win, subjectnumber,outdir):
    
    import random
    import csv
    import myFun
    from psychopy import visual, core, event
    
    leftKeys=[]; rightKeys=[]; acceptKeys=[]
    
    # Instructions
    myFun.showText(win, "Please indicate your agreement or disagreement with the following statements. Remember, there are no right or wrong answers. Press space to start.")
    event.waitKeys(keyList=['space'])
    
    # Item presentation
    def ratingScreen (win, itemText='default item text'):
        bisbasRating = visual.RatingScale (win, pos=(0,-.30), low=1, high=9, markerStart=1, stretch=2.5, textSize=.5, marker='circle', markerColor='Red', showAccept=False, singleClick=True, respKeys=['a','s','d','f','g','h','j','k','l'], tickMarks=[1,2,3,4,5,6,7,8,9], labels=["very strong \ndisagreement","strong \ndisagreement", "moderate \ndisagreement","slight\ndisagreement","neither agreement \nnor disagreement","slight \nagreement","moderate \nagreement","strong \nagreement","very strong \nagreement"])
        bisbasItem = visual.TextStim(win, alignHoriz="center", text=itemText, wrapWidth=10, pos=(0,1), height=0.5,font='Lucida Sans')
        bisbasRating.setDescription(' ')
        # set the marker start position randomly to avoid possible anchoring biases 
        x=list(range(4))
        random.shuffle(x)
        x=x[0]
        bisbasRating.setMarkerPos(x)
        while bisbasRating.noResponse:
            bisbasItem.draw()
            bisbasRating.draw()
            win.flip()
        currRating = bisbasRating.getRating()
        currDecisionTime = bisbasRating.getRT()
        win.flip()

        # return results
        return currRating, currDecisionTime, x
    
    
    
    i1, i1RT, i1Pos = ratingScreen (win, 'I would prefer complex to simple problems.')
    
    i2, i2RT, i2Pos = ratingScreen (win, 'I like to have the responsibility of handling a situation that requires a lot of thinking.')
    
    i3, i3RT, i3Pos = ratingScreen (win, 'Thinking is not my idea of fun.')
    
    i4, i4RT, i4Pos = ratingScreen (win, 'I would rather do something that requires little thought than something that is sure to challenge my thinking abilities.')
    
    i5, i5RT, i5Pos = ratingScreen (win, 'I try to anticipate and avoid situations where there is likely a chance I will have to think in depth about something.')
    
    i6, i6RT, i6Pos = ratingScreen (win, 'I find satisfaction in deliberating hard and for long hours.')
    
    i7, i7RT, i7Pos = ratingScreen (win, 'I only think as hard as I have to.')
    
    i8, i8RT, i8Pos = ratingScreen (win, 'I prefer to think about small, daily projects to long-term ones.')
    
    i9, i9RT, i9Pos = ratingScreen (win, "I like tasks that require little thought once I've learned them.")
    
    i10, i10RT, i10Pos = ratingScreen (win, 'The idea of relying on thought to make my way to the top appeals to me.')
    
    i11, i11RT, i11Pos = ratingScreen (win, 'I really enjoy a task that involves coming up with new solutions to problems.')
    
    i12, i12RT, i12Pos = ratingScreen (win, "Learning new ways to think doesn't excite me very much.")
    
    i13, i13RT, i13Pos = ratingScreen (win, 'I prefer my life to be filled with puzzles that I must solve.')
    
    i14, i14RT, i14Pos = ratingScreen (win, 'The notion of thinking abstractly is appealing to me.')
    
    i15, i15RT, i15Pos = ratingScreen (win, 'I would prefer a task that is intellectual, difficult, and important to one that is somewhat important but does not require much thought.')
    
    i16, i16RT, i16Pos = ratingScreen (win, 'I feel relief rather than satisfaction after completing a task that required a lot of mental effort.')
    
    i17, i17RT, i17Pos = ratingScreen (win, "It's enough for me that something gets the job done; I don't care how or why it works.")
    
    i18, i18RT, i18Pos = ratingScreen (win, 'I usually end up deliberating about issues even when they do not affect me personally.')
    
    
    
    # calculate summary score
    
    # recode item scores 
    # normal items
    i1=i1-5
    i2=i2-5
    i6=i6-5
    i10=i10-5
    i11=i11-5
    i13=i13-5
    i14=i14-5
    i15=i15-5
    i18=i18-5
    
    #reverse coded items
    i3=(i3-5)*-1
    i4=(i4-5)*-1
    i5=(i5-5)*-1
    i7=(i7-5)*-1
    i8=(i8-5)*-1
    i9=(i9-5)*-1
    i12=(i12-5)*-1
    i16=(i16-5)*-1
    i17=(i17-5)*-1
    
    
    # get the summary scores
    nfc = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13 + i14 + i15 + i16 + i17 + i18 
    
    
    #log responses
    datafile = myFun.openDataFile(subjectnumber,'nfc',outdir)  # open data output file
    writer = csv.writer(datafile, delimiter=";")    # connect it with a csv writer
    writer.writerow([
        "subject",
        "nfc",
        

        "i1",
        "i2",
        "i3",
        "i4",
        "i5",
        "i6",
        "i7",
        "i8",
        "i9",
        "i10",
        "i11",
        "i12",
        "i13",
        "i14",
        "i15",
        "i16",
        "i17",
        "i18",
        
        
        "i1RT",
        "i2RT",
        "i3RT",
        "i4RT",
        "i5RT",
        "i6RT",
        "i7RT",
        "i8RT",
        "i9RT",
        "i10RT",
        "i11RT",
        "i12RT",
        "i13RT",
        "i14RT",
        "i15RT",
        "i16RT",
        "i17RT",
        "i18RT",
        
        
        "i1Pos",
        "i2Pos",
        "i3Pos",
        "i4Pos",
        "i5Pos",
        "i6Pos",
        "i7Pos",
        "i8Pos",
        "i9Pos",
        "i10Pos",
        "i11Pos",
        "i12Pos",
        "i13Pos",
        "i14Pos",
        "i15Pos",
        "i16Pos",
        "i17Pos",
        "i18Pos"
        
        
        
        ])
        
        
        
    writer.writerow([
        subjectnumber,
        nfc,
        i1,
        i2,
        i3,
        i4,
        i5,
        i6,
        i7,
        i8,
        i9,
        i10,
        i11,
        i12,
        i13,
        i14,
        i15,
        i16,
        i17,
        i18,
       
        
        i1RT,
        i2RT,
        i3RT,
        i4RT,
        i5RT,
        i6RT,
        i7RT,
        i8RT,
        i9RT,
        i10RT,
        i11RT,
        i12RT,
        i13RT,
        i14RT,
        i15RT,
        i16RT,
        i17RT,
        i18RT,
       
        
        i1Pos,
        i2Pos,
        i3Pos,
        i4Pos,
        i5Pos,
        i6Pos,
        i7Pos,
        i8Pos,
        i9Pos,
        i10Pos,
        i11Pos,
        i12Pos,
        i13Pos,
        i14Pos,
        i15Pos,
        i16Pos,
        i17Pos,
        i18Pos
       
        
        
        ])

