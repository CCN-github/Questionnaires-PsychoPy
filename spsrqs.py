# -*- coding: utf-8 -*-
'''
This script presents the English version of the sensitivity to punishment and reward questionnaire, short form. 

The questionnaire was originally published in:
Torrubia, Rafael, César Ávila, Javier Moltó, and Xavier Caseras. “The Sensitivity to Punishment and Sensitivity to Reward Questionnaire (SPSRQ) as a Measure of Gray’s Anxiety and Impulsivity Dimensions.” Personality and Individual Differences 31, no. 6 (October 15, 2001): 837–62. 

by David Wisniewski (david.wisniewski@ugent.be)

'''

def spsrqs (win, subjectnumber,outdir):
    
    import random
    import csv
    import myFun
    from psychopy import visual, core, event
    
    leftKeys=[]; rightKeys=[]; acceptKeys=[]
    
    # Instructions
    myFun.showText(win, "Please answer each following question with either 'YES' or 'NO'. There are no right or wrong answers or trick questions. Work quickly and don't think too much about the exact wording of the questions. Press space to start.")
    event.waitKeys(keyList=['space'])
    
    # Item presentation
    def ratingScreen (win, itemText='default item text'):
        bisbasRating = visual.RatingScale (win, pos=(0,-.30), low=1, high=2, markerStart=1, stretch=0.5, textSize=1, marker='circle', markerColor='Red', showAccept=False, singleClick=True, respKeys=['a','s'], tickMarks=[1,2], labels=["YES","NO"])
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
    
    
    #R
    i1, i1RT, i1Pos = ratingScreen (win, 'Does the good prospect of obtaining money motivate you strongly to do some things?')
    #P
    i2, i2RT, i2Pos = ratingScreen (win, 'Are you often afraid of new or unexpected situations?')
    #P
    i3, i3RT, i3Pos = ratingScreen (win, 'Is it difficult for you to telephone someone you do not know?')
    #R
    i4, i4RT, i4Pos = ratingScreen (win, 'Do you often do things to be praised?')
    #R
    i5, i5RT, i5Pos = ratingScreen (win, 'Do you like being the centre of attention at a party or a social meeting?')
    #P
    i6, i6RT, i6Pos = ratingScreen (win, 'In tasks that you are not prepared for, do you attach great importance to the possibility of failure?')
    #P
    i7, i7RT, i7Pos = ratingScreen (win, 'Are you easily discouraged in difficult situations?')
    #P
    i8, i8RT, i8Pos = ratingScreen (win, 'Are you a shy person?')
    #R
    i9, i9RT, i9Pos = ratingScreen (win, 'When you are in a group, do you try to make your opinions the most intelligent or the funniest?')
    #P
    i10, i10RT, i10Pos = ratingScreen (win, 'Whenever possible, do you avoid demonstrating your skills for fear of being embarrassed?')
    #R
    i11, i11RT, i11Pos = ratingScreen (win, 'Do you often take the opportunity to pick up people you find attractive?')
    #P
    i12, i12RT, i12Pos = ratingScreen (win, 'When you are with a group, do you have difficulties selecting a good topic to talk about?')
    #R
    i13, i13RT, i13Pos = ratingScreen (win, 'Do you generally give preference to those activities that imply an immediate gain?')
    #P
    i14, i14RT, i14Pos = ratingScreen (win, 'Whenever you can, do you avoid going to unknown places?')
    #R
    i15, i15RT, i15Pos = ratingScreen (win, 'Do you like to compete and do everything you can to win?')
    #P
    i16, i16RT, i16Pos = ratingScreen (win, 'Are you often worried by things that you said or did?')
    #P
    i17, i17RT, i17Pos = ratingScreen (win, 'Do you, on a regular basis, think that you could do more things if it was not for your insecurity and fear?')
    #R
    i18, i18RT, i18Pos = ratingScreen (win, 'Do you sometimes do things for quick gains?')
    #P
    i19, i19RT, i19Pos = ratingScreen (win, 'Comparing yourself to people you know, are you afraid of many things?')
    #P
    i20, i20RT, i20Pos = ratingScreen (win, 'Do you often find yourself worrying about things to the extent that performance in intellectual abilities is impaired?')
    #P
    i21, i21RT, i21Pos = ratingScreen (win, 'Do you often refrain from doing something you like in order not to be rejected or disapproved for by others?')
    #R
    i22, i22RT, i22Pos = ratingScreen (win, 'Would you like to be a socially powerful person?')
    #P
    i23, i23RT, i23Pos = ratingScreen (win, 'Do you often refrain from doing something because of your fear of being embarrassed?')
    #R
    i24, i24RT, i24Pos = ratingScreen (win, 'Do you like displaying your physical abilities even though this may involve danger?')
    
    
    # calculate summary score
    
    # recode item scores from 1,2 to 1,0
    i1=(i1-2)*-1
    i2=(i2-2)*-1
    i3=(i3-2)*-1
    i4=(i4-2)*-1
    i5=(i5-2)*-1
    i6=(i6-2)*-1
    i7=(i7-2)*-1
    i8=(i8-2)*-1
    i9=(i9-2)*-1
    i10=(i10-2)*-1
    i11=(i11-2)*-1
    i12=(i12-2)*-1
    i13=(i13-2)*-1
    i14=(i14-2)*-1
    i15=(i15-2)*-1
    i16=(i16-2)*-1
    i17=(i17-2)*-1
    i18=(i18-2)*-1
    i19=(i19-2)*-1
    i20=(i20-2)*-1
    i21=(i21-2)*-1
    i22=(i22-2)*-1
    i23=(i23-2)*-1
    i24=(i24-2)*-1
    
    # get the summary scores
    SR = i1+i4+i5+i9+i11+i13+i15+i18+i22+i24
    SP = i2+i3+i6+i7+i8+i10+i12+i14+i16+i17+i19+i20+i21+i23
    
    
    #log responses
    datafile = myFun.openDataFile(subjectnumber,'spsrqs',outdir)  # open data output file
    writer = csv.writer(datafile, delimiter=";")    # connect it with a csv writer
    writer.writerow([
        "subject",
        "SR",
        "SP",

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
        "i24Pos"
        
        
        ])
        
        
        
    writer.writerow([
        subjectnumber,
        SR,
        SP,
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
        i24Pos
        
        
        ])

