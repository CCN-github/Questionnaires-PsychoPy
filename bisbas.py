# -*- coding: utf-8 -*-
'''
This script presents the Dutch version of the BIS BAS questionnaire, and logs all responses. 

The BIS BAS questionnaire was originally published here

Carver, Charles S., and Teri L. White. “Behavioral Inhibition, Behavioral Activation, and Affective Responses to Impending Reward and Punishment: The BIS/BAS Scales.” Journal of Personality and Social Psychology 67, no. 2 (1994): 319.

by David Wisniewski (david.wisniewski@ugent.be)

'''


def bisbas (win, subjectnumber,outdir):
    

    
    import random
    import csv
    import myFun
    from psychopy import visual, core, event
    
    leftKeys=[]; rightKeys=[]; acceptKeys=[]
      
    # Instructions
    myFun.showText(win, "Hierna volgen 20 beweringen. De bedoeling is dat je deze beweringen doorleest en dat je nagaat of zij von toepassing zijn op jou. Onder elke bewering staan vier antwoordmogelijkheden die varieren can *helemaal mee oneens* tot *helemaal mee eens*. Het is de bedoeling dat je met de muis klikt op het kadertje dat aangeeft in hoeverre een bewering op jou can toepassing is. Neem je tijd, maar denk niet al te lang na over een vraag. Druk space om te beginnen. ")
    event.waitKeys(keyList=['space'])
    
    
    # Item presentation
    def ratingScreen (win, itemText='default item text'):
        bisbasRating = visual.RatingScale (win, pos=(0,-.25), low=1, high=4, markerStart=1, stretch=1.5, textSize=0.5, marker='circle', markerColor='Red', showAccept=False, singleClick=True, respKeys=['a','s','d','f'], tickMarks=[1,2,3,4], labels=["Helemaal mee oneens", "Beetje mee oneens", "Beetje mee eens", "Helemaal mee eens"])
        bisbasItem = visual.TextStim(win, alignHoriz="center", text=itemText, wrapWidth=20, pos=(0,2), height=0.5,font='Lucida Sans')
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
    
    
    
    i1, i1RT, i1Pos = ratingScreen (win, 'Als ik denk dat er iets onprettigs gaat gebeuren, raak ik meestal behoorlijk *opgefokt*.')
    
    i2, i2RT, i2Pos = ratingScreen (win, 'Ik ben bezorgd om het maken van fouten.')
    
    i3, i3RT, i3Pos = ratingScreen (win, 'Als ik iets wil, ga ik er meestal helemaal voor.')
    
    i4, i4RT, i4Pos = ratingScreen (win, 'Vaak doe ik dingen om geen andere reden dan dat het wel eens leuk zou kunnen zijn.')
    
    i5, i5RT, i5Pos = ratingScreen (win, 'Kritiek of een standje raken mij behoorlijk.')
    
    i6, i6RT, i6Pos = ratingScreen (win, 'Als ik iets krijg wat ik wil, voel ik me opgewonden en opgeladen.')
    
    i7, i7RT, i7Pos = ratingScreen (win, 'Ik doe een hoop moeite om dingen die ik wil te krijgen.')
    
    i8, i8RT, i8Pos = ratingScreen (win, 'Ik verlang sterk naar spanning en nieuwe sensaties.')
    
    i9, i9RT, i9Pos = ratingScreen (win, 'Ik voel me behoorlijk overstuur als ik denk of weet dat iemand boos op me is.')
    
    i10, i10RT, i10Pos = ratingScreen (win, 'Ik ben altijd bereid iets nieuws te proberen als ik denk dat het leuk zal zijn.')
    
    i11, i11RT, i11Pos = ratingScreen (win, 'Als il iets goed doe, wil ik er graag mee doorgaan.')
    
    i12, i12RT, i12Pos = ratingScreen (win, 'Zelfs als mij ergs staat te gebeuren, ervaar ik zelden angst of nervositeit.')
    
    i13, i13RT, i13Pos = ratingScreen (win, 'Ik handel vaak zoals het moment me ingeeft.')
    
    i14, i14RT, i14Pos = ratingScreen (win, 'Als ik een kans zie iets te krijgen wat ik wil, ga ik er meteen op af.')
    
    i15, i15RT, i15Pos = ratingScreen (win, 'Als mij goede dingen overkomen, raakt dat me stark.')
    
    i16, i16RT, i16Pos = ratingScreen (win, 'Ik voel me bezorgd als ik denk dat ik slecht heb gepresteerd op iets.')
    
    i17, i17RT, i17Pos = ratingScreen (win, 'Ik zou het spannend vinden een wedstrijd te winnen.')
    
    i18, i18RT, i18Pos = ratingScreen (win, 'Vergeleken met mijn vrienden heb ik erg weinig angsten.')
    
    i19, i19RT, i19Pos = ratingScreen (win, 'Als ik een mogelijkheid zie iets te krijgen wat ik leuk vind, word ik direct opgewonden.')
    
    i20, i20RT, i20Pos = ratingScreen (win, 'Als ik ergens werk van maak, gooi ik ook mijn volle gewicht er tegenaan.')
    
    
    # calculate summary scores
    bis = i1 + i2 + i5 + i9 + (5-i12) + i16 + (5-i18)
    reward = i6 + i11 + i15 + i17 + i19
    drive = i3 + i7 + i14 + i20
    fun = i4 + i8 + i10 + i13
    bas = reward + drive + fun 
    
    
    #log responses
    datafile = myFun.openDataFile(subjectnumber,'bisbas',outdir)  # open data output file
    writer = csv.writer(datafile, delimiter=";")    # connect it with a csv writer
    writer.writerow([
        "subject",
        "bis",
        "bas",
        "reward",
        "drive",
        "fun",
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
        "i20Pos"
        ])
        
        
        
    writer.writerow([
        subjectnumber,
        bis,
        bas,
        reward,
        drive,
        fun,
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
        i20Pos
        ])
