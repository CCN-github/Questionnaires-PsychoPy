# -*- coding: utf-8 -*-
'''
This script presents the English version of the barratt impulsiveness scale (version 11).

This questionnaire was originally pblished in
Patton Stanford Barratt 1995 Factor structure of the barratt impulsiveness scale. J Clin Psychol 51 768-774

by David Wisniewski (david.wisniewski@ugent.be)

'''

def bis11 (win, subjectnumber,outdir):
    
    import random
    import csv
    import myFun
    from psychopy import visual, core, event
    
    leftKeys=[]; rightKeys=[]; acceptKeys=[]
    
    # Instructions
    myFun.showText(win, "People differ in the ways they act and think in different situations. This is a test to measure some of the ways in which you act and think. Read each statement and indicate the appropriate answer. Do not spend too much time on any statement. Answer quickly and honestly. Press space to start.")
    event.waitKeys(keyList=['space'])
    
    # Item presentation
    def ratingScreen (win, itemText='default item text'):
        bisbasRating = visual.RatingScale (win, pos=(0,-.30), low=1, high=4, markerStart=1, stretch=1.5, textSize=.5, marker='circle', markerColor='Red', showAccept=False, singleClick=True, respKeys=['a','s','d','f'], tickMarks=[1,2,3,4], labels=["rarely/never","occasionally","often","almost always/always"])
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
    
    
    
    i1, i1RT, i1Pos = ratingScreen (win, 'I plan tasks carefully.')
    
    i2, i2RT, i2Pos = ratingScreen (win, 'I do things without thinking.')
    
    i3, i3RT, i3Pos = ratingScreen (win, 'I make-up my mind quickly.')
    
    i4, i4RT, i4Pos = ratingScreen (win, 'I am happy-go-lucky.')
    
    i5, i5RT, i5Pos = ratingScreen (win, "I don't 'pay attention'.")
    
    i6, i6RT, i6Pos = ratingScreen (win, "I have 'racing' thoughts.")
    
    i7, i7RT, i7Pos = ratingScreen (win, 'I plan trips well ahead of time.')
    
    i8, i8RT, i8Pos = ratingScreen (win, 'I am self controlled.')
    
    i9, i9RT, i9Pos = ratingScreen (win, 'I concentrate easily.')
    
    i10, i10RT, i10Pos = ratingScreen (win, 'I save regularly.')
    
    i11, i11RT, i11Pos = ratingScreen (win, "I 'squirm' at plays or lectures.")
    
    i12, i12RT, i12Pos = ratingScreen (win, 'I am a careful thinker.')
    
    i13, i13RT, i13Pos = ratingScreen (win, 'I plan for job security.')
    
    i14, i14RT, i14Pos = ratingScreen (win, 'I say thinkgs without thinking.')
    
    i15, i15RT, i15Pos = ratingScreen (win, 'I like to think about complex problems.')
    
    i16, i16RT, i16Pos = ratingScreen (win, 'I change jobs.')
    
    i17, i17RT, i17Pos = ratingScreen (win, "I act 'on impulse'.")
    
    i18, i18RT, i18Pos = ratingScreen (win, 'I get easily bored when solving thought problems.')
    
    i19, i19RT, i19Pos = ratingScreen (win, 'I act on the spur of the moment.')
    
    i20, i20RT, i20Pos = ratingScreen (win, 'I am a steady thinker.')
    
    i21, i21RT, i21Pos = ratingScreen (win, 'I change residences.')
    
    i22, i22RT, i22Pos = ratingScreen (win, 'I buy things on impulse.')
    
    i23, i23RT, i23Pos = ratingScreen (win, 'I can only think about one thing at a time.')
    
    i24, i24RT, i24Pos = ratingScreen (win, 'I change hobbies.')
    
    i25, i25RT, i25Pos = ratingScreen (win, 'I spend or charge more than I earn.')
    
    i26, i26RT, i26Pos = ratingScreen (win, 'I often have extraneous thoughts when thinking.')
    
    i27, i27RT, i27Pos = ratingScreen (win, 'I am more interested in the present than the future.')
    
    i28, i28RT, i28Pos = ratingScreen (win, 'I am restless at the theater or lectures.')
    
    i29, i29RT, i29Pos = ratingScreen (win, 'I like puzzles.')
    
    i30, i30RT, i30Pos = ratingScreen (win, 'I am future oriented.')
    
    # calculate summary score
    
    # recode reverse coded item  
    i1=5-i1
    i7=5-i7
    i8=5-i8
    i9=5-i9
    i10=5-i10
    i12=5-i12
    i13=5-i13
    i15=5-i15
    i20=5-i20
    i29=5-i29
    i30=5-i30
    
    # get the summary scores
    attention = i5 + i9 + i11 + i20 + i28
    coginst = i6 + i24 + i26
    motor = i2 + i3 + i4 + i17 + i19 + i22 + i25
    persev = i16 + i21 + i23 + i30
    selfcontrol = i1 + i7 + i8 + i12 + i13 + i14
    cogcomplex = i10 + i15 + i18 + i27 + i29
    
    attention2 = attention + coginst
    motor2 = motor + persev
    nonplanning2 = selfcontrol + cogcomplex
    
    total = attention2 + motor2 + nonplanning2
    
    #log responses
    datafile = myFun.openDataFile(subjectnumber,'bis11',outdir)  # open data output file
    writer = csv.writer(datafile, delimiter=";")    # connect it with a csv writer
    writer.writerow([
        "subject",
        
        "attention",
        "cognitiveInstability",
        "motor",
        "perseverence",
        "selfControl",
        "cognitiveComplexity",
        "attention2order",
        "motor2order",
        "nonplanning2order",
        "total",

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
        "i19",
        "i20",
        "i21",
        "i22",
        "i23",
        "i24",
        "i25",
        "i26",
        "i27",
        "i28",
        "i29",
        "i30",
        
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
        "i19RT",
        "i20RT",
        "i21RT",
        "i22RT",
        "i23RT",
        "i24RT",
        "i25RT",
        "i26RT",
        "i27RT",
        "i28RT",
        "i29RT",
        "i30RT",
        
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
        "i18Pos",
        "i19Pos",
        "i20Pos",
        "i21Pos",
        "i22Pos",
        "i23Pos",
        "i24Pos",
        "i25Pos",
        "i26Pos",
        "i27Pos",
        "i28Pos",
        "i29Pos",
        "i30Pos"
        
        
        ])
        
        
        
    writer.writerow([
        subjectnumber,
        
        attention, 
        coginst,
        motor,
        persev,
        selfcontrol,
        cogcomplex, 
        attention2,
        motor2,
        nonplanning2,
        total,
        
        
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
        i19,
        i20,
        i21,
        i22,
        i23,
        i24,
        i25,
        i26,
        i27,
        i28,
        i29,
        i30,
        
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
        i19RT,
        i20RT,
        i21RT,
        i22RT,
        i23RT,
        i24RT,
        i25RT,
        i26RT,
        i27RT,
        i28RT,
        i29RT,
        i30RT,
        
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
        i18Pos,
        i19Pos,
        i20Pos,
        i21Pos,
        i22Pos,
        i23Pos,
        i24Pos,
        i25Pos,
        i26Pos,
        i27Pos,
        i28Pos,
        i29Pos,
        i30Pos,
        
        
        
        ])

