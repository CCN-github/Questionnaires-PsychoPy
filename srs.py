# -*- coding: utf-8 -*-
'''
This script presents the Dutch version of the Social Responsiveness Scale (Copyright Hogrefe, Amsterdam 2008).

Please be aware that the script saves the raw scores only. Consult your handbook to transform these scores into t-scores.

by David Wisniewski (david.wisniewski@ugent.be)

'''

def srs (win, subjectnumber,outdir):
    
    import random
    import csv
    import myFun
    from psychopy import visual, core, event
    
    leftKeys=[]; rightKeys=[]; acceptKeys=[]
    
    # Instructions
    myFun.showText(win, "Click voor iedere vraag het antwoord dat uw gedrag in de laatste 6 maanden het best beschrijft. Click space om te beginnen.")
    event.waitKeys(keyList=['space'])
    
    # Item presentation
    def ratingScreen (win, itemText='default item text'):
        bisbasRating = visual.RatingScale (win, pos=(0,-.30), low=0, high=3, markerStart=1, stretch=1.5, textSize=.5, marker='circle', markerColor='Red', showAccept=False, singleClick=True, respKeys=['a','s','d','f'], tickMarks=[0,1,2,3], labels=["niet waar","soms waar","vaak waar","bijna altijd waar"])
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
    
    
    
    i1, i1RT, i1Pos = ratingScreen (win, 'Ik voel me veel minder op mijn gemak in sociale situaties dan wanneer ik alleen ben.')
    
    i2, i2RT, i2Pos = ratingScreen (win, 'Mijn gelaatsexpressies komen niet overeen met wat ik zeg.')
    
    i3, i3RT, i3Pos = ratingScreen (win, 'Ik voel me zelfverzekerd in de omgang met anderen.')
    
    i4, i4RT, i4Pos = ratingScreen (win, 'Op stressvolle momenten vertoon ik rigide of weinig flexibele gedragspatronen die eigenaardig lijken.')
    
    i5, i5RT, i5Pos = ratingScreen (win, "Ik besef niet wanneer anderen misbruik van mij maken.")
    
    i6, i6RT, i6Pos = ratingScreen (win, "Ik ben liever alleen dan samen met anderen.")
    
    i7, i7RT, i7Pos = ratingScreen (win, 'Ik ben mij bewust van wat anderen denken of voelen.')
    
    i8, i8RT, i8Pos = ratingScreen (win, 'Ik gedraag mij op een manier die vreemd of bizar overkomt.')
    
    i9, i9RT, i9Pos = ratingScreen (win, 'Ik ben te afhankelijk van hulp van anderen om mijzelf in mijn basisbehoeften te voorzien.')
    
    i10, i10RT, i10Pos = ratingScreen (win, 'Ik neem dingen te letterlijk en vind het moeilijk de eigenlijke betekenis van een gesprek te vatten.')
    
    i11, i11RT, i11Pos = ratingScreen (win, "Ik heb een goed zelfvertrouwen.")
    
    i12, i12RT, i12Pos = ratingScreen (win, 'Ik ben in staat mijn gevoelens naar anderen te communiceren.')
    
    i13, i13RT, i13Pos = ratingScreen (win, 'Ik ben onhandig in wederzijdse interacties met anderen (bijv. Ik vind het moeilijk om in een gesprek uit te maken wanneer het aan mij is om iets te zeggen en wanneer de ander aan de beurt is).')
    
    i14, i14RT, i14Pos = ratingScreen (win, 'Ik heb geen goede coordinatie.')
    
    i15, i15RT, i15Pos = ratingScreen (win, 'Ik herken veranderingen in intonatie en gelaatsexpressies van anderen en reageer hier adequaat op.')
    
    i16, i16RT, i16Pos = ratingScreen (win, 'Ik vermijd oogcontact of maak ongewoon oogcontact.')
    
    i17, i17RT, i17Pos = ratingScreen (win, "Ik zie in wanneer iets onrechtvaardig is.")
    
    i18, i18RT, i18Pos = ratingScreen (win, 'Ik maak moeilijk vrienden, zelfs wanneer ik erg mijn best doe.')
    
    i19, i19RT, i19Pos = ratingScreen (win, 'Ik raak gefrustreerd als ik probeer mijn ideeen over te brengen in gesprekken.')
    
    i20, i20RT, i20Pos = ratingScreen (win, 'Ik vertoon ongewone zintuiglijke interesses (bijv. ik ruik vaak aan mijn vingers) of ik hanteer en manipuleer kleine voorwerpen binnen handbereik op een vreemde of repetitieve manier.')
    
    i21, i21RT, i21Pos = ratingScreen (win, 'Ik ben in staat handelingen en de manier van doen van anderen te imiteren wanneer het sociaal gepast is dit te doen.')
    
    i22, i22RT, i22Pos = ratingScreen (win, 'Ik ga gepast om met andere volwassenen.')
    
    i23, i23RT, i23Pos = ratingScreen (win, 'Ik neem niet deel aan groepsactiviteiten of sociale evenementen tenzij ik daartoe gedwongen word.')
    
    i24, i24RT, i24Pos = ratingScreen (win, 'Ik heb het moeilijker dan anderen met veranderingen in mijn routines.')
    
    i25, i25RT, i25Pos = ratingScreen (win, 'Ik bied troost aan anderen wanneer zij verdrietig zijn.')
    
    i26, i26RT, i26Pos = ratingScreen (win, 'Ik vermijd het aangaan van sociale interacties met andere volwassenen.')
    
    i27, i27RT, i27Pos = ratingScreen (win, 'Ik denk of praat telkens weer over hetzelfde.')
    
    i28, i28RT, i28Pos = ratingScreen (win, 'Anderen vinden mij eigenaardig of raar.')
    
    i29, i29RT, i29Pos = ratingScreen (win, 'Ik raak overstuur in situaties waarin veel dingen gaande zijn.')
    
    i30, i30RT, i30Pos = ratingScreen (win, 'Ik kan mijn gedachten niet van iets afbrengen als ik er eenmaal over begin te denken.')
    
    i31, i31RT, i31Pos = ratingScreen (win, 'Ik heb een goede persoonlijke hygiene.')
    
    i32, i32RT, i32Pos = ratingScreen (win, 'Ik ben sociaal onhandig, zelfs als ik beleefd probeer te zijn.')
    
    i33, i33RT, i33Pos = ratingScreen (win, 'Ik vermijd mensen die een emotionele band met mij willen.')
    
    i34, i34RT, i34Pos = ratingScreen (win, 'Ik heb moeite om het verloop van een gewoon gesprek te volgen.')
    
    i35, i35RT, i35Pos = ratingScreen (win, 'Ik heb moeite om voeling te krijgen met familieleden.')
    
    i36, i36RT, i36Pos = ratingScreen (win, 'Ik heb moeite om voeling te krijgen met andere volwassenen.')
    
    i37, i37RT, i37Pos = ratingScreen (win, 'Ik reageer gepast op stemmingsveranderingen van anderen (bijv. wanneer de stemming van een vriend omslaat van blij naar droevig).')
    
    i38, i38RT, i38Pos = ratingScreen (win, 'Ik heb een ongewoon beperkt interessegebied.')
    
    i39, i39RT, i39Pos = ratingScreen (win, 'Ik ben fantasierijk zonder voeling met de werkelijkheid te verliezen.')
    
    i40, i40RT, i40Pos = ratingScreen (win, 'Ik dwaal doelloos van de ene activiteit naar de andere.')
    
    i41, i41RT, i41Pos = ratingScreen (win, 'Ik ben overgevoelig voor geluiden, texturen of geuren.')
    
    i42, i42RT, i42Pos = ratingScreen (win, 'Ik vind het fijn "over koetjes en kalfjes" te praten en ben hier goed in (kletsen met anderen).')
    
    i43, i43RT, i43Pos = ratingScreen (win, 'Ik begrijp niet goed hoe verschillende gebeurtenissen met elkaar verband houden (oorzaak en gevolg) zoals andere volwassenen dat doen.')
    
    i44, i44RT, i44Pos = ratingScreen (win, 'Ik toon gewoonlijk interesse in datgene waaraan anderen aandacht schenken.')
    
    i45, i45RT, i45Pos = ratingScreen (win, 'Mijn gelaatsuitdrukking is overdreven ernstig.')
    
    i46, i46RT, i46Pos = ratingScreen (win, 'Ik lach op ongepaste momenten.')
    
    i47, i47RT, i47Pos = ratingScreen (win, 'Ik heb een gevoel voor humor, begrijp grappen.')
    
    i48, i48RT, i48Pos = ratingScreen (win, 'Ik ben extreem goed in sommige intellectuele taken of rekenkundige bewerkingen, maar doe het niet zo goed op de meeste andere taken.')
    
    i49, i49RT, i49Pos = ratingScreen (win, 'Ik vertoon repetitieve, eigenaardige gedragingen.')
    
    i50, i50RT, i50Pos = ratingScreen (win, 'Ik heb moeite om vragen rechtstreeks te beantwoorden en eindig met om het onderwerp heen te praten.')
    
    i51, i51RT, i51Pos = ratingScreen (win, 'Ik weet wanneer ik te luid praat of teveel lawaai maak.')
    
    i52, i52RT, i52Pos = ratingScreen (win, 'Ik praat tegen mensen op een ongewone toon (bijv. ik praat als een robot of alsof ik een lezing geef).')
    
    i53, i53RT, i53Pos = ratingScreen (win, 'Ik reageer op mensen alsof ze voorwerpen zijn.')
    
    i54, i54RT, i54Pos = ratingScreen (win, 'Ik weet wanneer ik te dicht in de buurt ben bij iemand of iemands persoonlijke ruimte binnendring.')
    
    i55, i55RT, i55Pos = ratingScreen (win, 'Ik loop tussen twee mensen door die met elkaar aan het praten zijn.')
    
    i56, i56RT, i56Pos = ratingScreen (win, 'Ik heb de neiging mij te isoleren, mijn huis niet te verlaten.')
    
    i57, i57RT, i57Pos = ratingScreen (win, 'Ik concentreer mij teveel op deelaspecten van dingen, eerder dan het geheel te zien.')
    
    i58, i58RT, i58Pos = ratingScreen (win, 'Ik ben overdreven achterdochtig.')
    
    i59, i59RT, i59Pos = ratingScreen (win, 'Ik ben emotioneel afstandelijk, toon mijn gevoelens niet.')
    
    i60, i60RT, i60Pos = ratingScreen (win, 'Ik ben niet flexibel, heb moeite om van mening te veranderen.')
    
    i61, i61RT, i61Pos = ratingScreen (win, 'Anderen vinden de reden die ik geef voor wat ik doe ongewoon of onlogisch.')
    
    i62, i62RT, i62Pos = ratingScreen (win, 'Ik raak anderen op een ongewone manier aan, groet anderen op een ongewone manier.')
    
    i63, i63RT, i63Pos = ratingScreen (win, 'Ik ben te gespannen in sociale situaties.')
    
    i64, i64RT, i64Pos = ratingScreen (win, 'Ik staar of mijn blik dwaalt af in het niets.')
    
    # calculate summary score
    
    # recode reverse coded items
    i3=3-i3
    i7=3-i7
    i11=3-i11
    i12=3-i12
    i15=3-i15
    i17=3-i17
    i21=3-i21
    i22=3-i22
    i25=3-i25
    i31=3-i31
    i37=3-i37
    i39=3-i39
    i42=3-i42
    i44=3-i44
    i47=3-i47
    i51=3-i51
    i54=3-i54
    
    
    # get the summary scores
    socialbewustzijn = i2+i5+i7+i10+i15+i17+i29+i31+i39+i41+i43+i44+i47+i51+i53+i55+i57+i58+i61
    socialecommunicatie = i12+i13+i16+i18+i19+i21+i22+i25+i32+i34+i35+i36+i37+i40+i45+i46+i50+i52+i54+i56+i59+i60
    socialemotivatie = i1+i3+i6+i9+i11+i23+i26+i33+i42+i63+i64
    rigiditeitrepetitviteit = i4+i8+i14+i20+i24+i27+i28+i30+i38+i48+i49+i62

    total = socialbewustzijn + socialecommunicatie + socialemotivatie + rigiditeitrepetitviteit


    #log responses
    datafile = myFun.openDataFile(subjectnumber,'srs',outdir)  # open data output file
    writer = csv.writer(datafile, delimiter=";")    # connect it with a csv writer
    writer.writerow([
        "subject",
        
        "total",
        "socialbewustzijn",
        "socialecommunicatie",
        "socialemotivatie",
        "rigiditeitrepetitviteit",
       
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
        "i31",
        "i32",
        "i33",
        "i34",
        "i35",
        "i36",
        "i37",
        "i38",
        "i39",
        "i40",
        "i41",
        "i42",
        "i43",
        "i44",
        "i45",
        "i46",
        "i47",
        "i48",
        "i49",
        "i50",
        "i51",
        "i52",
        "i53",
        "i54",
        "i55",
        "i56",
        "i57",
        "i58",
        "i59",
        "i60",
        "i61",
        "i62",
        "i63",
        "i64",
        
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
        "i31RT",
        "i32RT",
        "i33RT",
        "i34RT",
        "i35RT",
        "i36RT",
        "i37RT",
        "i38RT",
        "i39RT",
        "i40RT",
        "i41RT",
        "i42RT",
        "i43RT",
        "i44RT",
        "i45RT",
        "i46RT",
        "i47RT",
        "i48RT",
        "i49RT",
        "i50RT",
        "i51RT",
        "i52RT",
        "i53RT",
        "i54RT",
        "i55RT",
        "i56RT",
        "i57RT",
        "i58RT",
        "i59RT",
        "i60RT",
        "i61RT",
        "i62RT",
        "i63RT",
        "i64RT",
        
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
        "i30Pos",
        "i31Pos",
        "i32Pos",
        "i33Pos",
        "i34Pos",
        "i35Pos",
        "i36Pos",
        "i37Pos",
        "i38Pos",
        "i39Pos",
        "i40Pos",
        "i41Pos",
        "i42Pos",
        "i43Pos",
        "i44Pos",
        "i45Pos",
        "i46Pos",
        "i47Pos",
        "i48Pos",
        "i49Pos",
        "i50Pos",
        "i51Pos",
        "i52Pos",
        "i53Pos",
        "i54Pos",
        "i55Pos",
        "i56Pos",
        "i57Pos",
        "i58Pos",
        "i59Pos",
        "i60Pos",
        "i61Pos",
        "i62Pos",
        "i63Pos",
        "i64Pos"
        
        
        ])
        
    writer.writerow([
        subjectnumber,
        
        total,
        socialbewustzijn,
        socialecommunicatie,
        socialemotivatie,
        rigiditeitrepetitviteit,
       
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
        i31,
        i32,
        i33,
        i34,
        i35,
        i36,
        i37,
        i38,
        i39,
        i40,
        i41,
        i42,
        i43,
        i44,
        i45,
        i46,
        i47,
        i48,
        i49,
        i50,
        i51,
        i52,
        i53,
        i54,
        i55,
        i56,
        i57,
        i58,
        i59,
        i60,
        i61,
        i62,
        i63,
        i64,
        
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
        i31RT,
        i32RT,
        i33RT,
        i34RT,
        i35RT,
        i36RT,
        i37RT,
        i38RT,
        i39RT,
        i40RT,
        i41RT,
        i42RT,
        i43RT,
        i44RT,
        i45RT,
        i46RT,
        i47RT,
        i48RT,
        i49RT,
        i50RT,
        i51RT,
        i52RT,
        i53RT,
        i54RT,
        i55RT,
        i56RT,
        i57RT,
        i58RT,
        i59RT,
        i60RT,
        i61RT,
        i62RT,
        i63RT,
        i64RT,
        
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
        i31Pos,
        i32Pos,
        i33Pos,
        i34Pos,
        i35Pos,
        i36Pos,
        i37Pos,
        i38Pos,
        i39Pos,
        i40Pos,
        i41Pos,
        i42Pos,
        i43Pos,
        i44Pos,
        i45Pos,
        i46Pos,
        i47Pos,
        i48Pos,
        i49Pos,
        i50Pos,
        i51Pos,
        i52Pos,
        i53Pos,
        i54Pos,
        i55Pos,
        i56Pos,
        i57Pos,
        i58Pos,
        i59Pos,
        i60Pos,
        i61Pos,
        i62Pos,
        i63Pos,
        i64Pos
        
        
        ])
            
        
    