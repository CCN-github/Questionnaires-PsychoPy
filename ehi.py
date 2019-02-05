# -*- coding: utf-8 -*-

'''
This script presents the Dutch version of the Edinburgh handedness inventory, and logs all responses. 

This questionnaire was originally published in
Oldfield, R. C. (1971). The assessment of handedness: The Edinburgh inventory. Neuropsychologia, 9, 97–113.
                         
by David Wisniewski (david.wisniewski@ugent.be)

'''

def handedness (win, subjectnumber,outdir):
    
    import random
    import csv
    import myFun
    from psychopy import visual, core, event
    
    leftKeys=[]; rightKeys=[]; acceptKeys=[]
    
    # Instructions
    myFun.showText(win, "Duid a.u.b. uw hand handvoorkeur aan voor de volgende activiteiten. Bij sommige van de activiteiten heeft u beide handen nodig. In deze gevallen wordt de handvoorkeur gevraagd voor het voorwerp of activiteit tussen haakjes. Druk space om te beginnen. ")
    event.waitKeys(keyList=['space'])
    
    
    
    # Item presentation
    def ratingScreen (win, itemText='default item text'):
        bisbasRating = visual.RatingScale (win, pos=(0,-.30), low=1, high=5, markerStart=1, size=1.5, textSize=0.5, marker='circle', markerColor='Red', showAccept=False, singleClick=True, respKeys=['a','s','d','f','g'], tickMarks=[1,2,3,4,5], labels=["voorkeur links \nzo sterk dat u nooit \nzou rechts proberen", "voorkeur \nlinks", "om het even", "voorkeur \nrechts", "voorkeur rechts \nzo sterk dat u nooit \nzou links proberen"])
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
    
    
    
    i1, i1RT, i1Pos = ratingScreen (win, 'Schrijven')
    
    i2, i2RT, i2Pos = ratingScreen (win, 'Tekenen')
    
    i3, i3RT, i3Pos = ratingScreen (win, 'Werpen')
    
    i4, i4RT, i4Pos = ratingScreen (win, 'Schaar')
    
    i5, i5RT, i5Pos = ratingScreen (win, 'Tandenborstel')
    
    i6, i6RT, i6Pos = ratingScreen (win, 'Mes (zonder vork)')
    
    i7, i7RT, i7Pos = ratingScreen (win, 'Lepel')
    
    i8, i8RT, i8Pos = ratingScreen (win, 'Borstel (bovenste hand)')
    
    i9, i9RT, i9Pos = ratingScreen (win, 'Lucifer aanstrijken (lucifer)')
    
    i10, i10RT, i10Pos = ratingScreen (win, 'Doos openen (deksel)')
    
    i11, i11RT, i11Pos = ratingScreen (win, 'Welke voet verkies je om mee te schoppen?')
    
    i12, i12RT, i12Pos = ratingScreen (win, 'Welk ook gebruik je als je er slechts 1 gebruikt?')
    
    # calculate summary score
    
    # transform item scores into L and R scores
    def getRL (itemscore,sumR,sumL):
        if itemscore==1:
            sumL=sumL+2
        elif itemscore==2:
            sumL=sumL+1
        elif itemscore==3:
            sumL=sumL+1
            sumR=sumR+1
        elif itemscore==4:
            sumR=sumR+1
        elif itemscore==5:
            sumR=sumR+2
        
        return sumR, sumL
    
    sumR=0
    sumL=0
    
    [sumR, sumL]=getRL(i1,sumR,sumL)
    [sumR, sumL]=getRL(i2,sumR,sumL)
    [sumR, sumL]=getRL(i3,sumR,sumL)
    [sumR, sumL]=getRL(i4,sumR,sumL)
    [sumR, sumL]=getRL(i5,sumR,sumL)
    [sumR, sumL]=getRL(i6,sumR,sumL)
    [sumR, sumL]=getRL(i7,sumR,sumL)
    [sumR, sumL]=getRL(i8,sumR,sumL)
    [sumR, sumL]=getRL(i9,sumR,sumL)
    [sumR, sumL]=getRL(i10,sumR,sumL)
    [sumR, sumL]=getRL(i11,sumR,sumL)
    [sumR, sumL]=getRL(i12,sumR,sumL)
    
    # get the summary score from the L and R scores
    
    ehiScore = ((sumR-sumL)/(sumR+sumL))*100
    print(ehiScore)
    
    #log responses
    datafile = myFun.openDataFile(subjectnumber,'ehi',outdir)  # open data output file
    writer = csv.writer(datafile, delimiter=";")    # connect it with a csv writer
    writer.writerow([
        "subject",
        "ehiScore",
        "scoreR",
        "scoreL",
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
        "i12Pos"
        
        ])
        
        
        
    writer.writerow([
        subjectnumber,
        ehiScore,
        sumR,
        sumL,
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
        i12Pos
        
        ])

