# -*- coding: utf-8 -*-
'''
This script presents the Dutch short version (14 items) right-wing authoritarianism scale (RWA).

This questionnaire is based on 
Altemeyer, Bob. “The Other ‘Authoritarian Personality.’” In Advances in Experimental Social Psychology, edited by Mark P. Zanna, 30:47–92. Academic Press, 1998. 

by David Wisniewski (david.wisniewski@ugent.be)

'''

def rwa14 (win, subjectnumber,outdir):
    
    import random
    import csv
    import myFun
    from psychopy import visual, core, event
    
    leftKeys=[]; rightKeys=[]; acceptKeys=[]
    
    # Instructions
    myFun.showText(win, "Lees alle instructies zorgvuldig voor het invullen. Lees elke uitspraak zorgvuldig. Omcirkel achter elke uitspraak het getal dat uw mening het beste weergeeft. Let er op dat U geen regels overslaat. Druk space om te beginnen.")
    event.waitKeys(keyList=['space'])
    
    # Item presentation
    def ratingScreen (win, itemText='default item text'):
        bisbasRating = visual.RatingScale (win, pos=(0,-.30), low=1, high=5, markerStart=1, stretch=1.5, textSize=.5, marker='circle', markerColor='Red', showAccept=False, singleClick=True, respKeys=['a','s','d','f','g'], tickMarks=[1,2,3,4,5], labels=["helemaal niet akkoord","","neutral","","helemaal akkoord"])
        bisbasItem = visual.TextStim(win, alignHoriz="center", text=itemText, wrapWidth=10, pos=(0,1), height=0.5,font='Lucida Sans')
        bisbasRating.setDescription(' ')
        # set the marker start position randomly to avoid possible anchoring biases 
        x=list(range(5))
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
    
    
    
    i1, i1RT, i1Pos = ratingScreen (win, 'Gehoorzaamheid en respect voor gezag zijn de belangrijkste deugden die kinderen moeten leren.')
    
    i2, i2RT, i2Pos = ratingScreen (win, 'Jongeren krijgen soms opstandige ideeen maar als ze ouder worden horen ze daar overheen te groeien.')
    
    i3, i3RT, i3Pos = ratingScreen (win, 'Een fatsoenlijk uiterlijk is nog steeds het waarmerk van een heer, en in het bijzonder van een dame.')
    
    i4, i4RT, i4Pos = ratingScreen (win, 'Het traditionele gezin (vader is gezinshoofd en kinderen moeten gehoorzamen) kan beter verdwijnen.')
    
    i5, i5RT, i5Pos = ratingScreen (win, "Wetten moeten strikt worden toegepast, zeker als het gaat om oproerkraaiers en revolutionairen.")
    
    i6, i6RT, i6Pos = ratingScreen (win, "Er is niets 'immoreel' of 'ziek' aan mensen die homoseksueel zijn.")
    
    i7, i7RT, i7Pos = ratingScreen (win, 'De rechters pakken druggebruikers terecht niet te hard aan. Straf zou toch niet goed werken.')
    
    i8, i8RT, i8Pos = ratingScreen (win, 'De feiten over criminaliteit en seksueel gedrag tonen dat we harder moeten optreden tegen uitschot.')
    
    i9, i9RT, i9Pos = ratingScreen (win, 'Onze regels over bescheidenheid en seksueel gedrag zijn niet beter dan de regels die anderen volgen.')
    
    i10, i10RT, i10Pos = ratingScreen (win, 'Er is absoluut niets verkeerd aan verenigingen van mensen die bloot willen lopen.')
    
    i11, i11RT, i11Pos = ratingScreen (win, "De echte sleutels tot het goede leven zijn gehoorzaamheid, discipline en op het rechte pad blijven.")
    
    i12, i12RT, i12Pos = ratingScreen (win, 'Het is goed dat jongeren tegenwoordig de kans krijgen te protesteren tegen de gevestigde orde.')
    
    i13, i13RT, i13Pos = ratingScreen (win, 'Het is belangrijk dat de rechten van zij die protesteren tegen de gevestigde orde beschermd worden.')
    
    i14, i14RT, i14Pos = ratingScreen (win, 'Het is beter te vertrouwen op autoriteiten dan te luisteren naar zij die hun gezag willen ondermijnen.')
    
    
    # calculate summary score
    
    # recode reverse coded item  
    i4=6-i4
    i6=6-i6
    i7=6-i7
    i9=6-i9
    i10=6-i10
    i12=6-i12
    i13=6-i13
    
    
    # get the summary scores
    rwa = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13 + i14
    
    
    #log responses
    datafile = myFun.openDataFile(subjectnumber,'rwa14',outdir)  # open data output file
    writer = csv.writer(datafile, delimiter=";")    # connect it with a csv writer
    writer.writerow([
        "subject",
        
        "rwa",
        
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
        "i14Pos"        
        ])
        
        
        
    writer.writerow([
        subjectnumber,
        
        rwa, 
        
        
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
        i14Pos
        
        
        
        
        ])

