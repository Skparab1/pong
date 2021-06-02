#pong
import time, random, shelve
from random import randint, randrange
movedirection = 'right'
autoplay = False
print('Pong')
print('How to play: press contol + c to move your paddle up')
name = input('enter your name ')
if name == 'autoplay':
    autoplay = True
pos = 49
angle = 2
score = 0
waittime = 0.1
def printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18
    print(' '+('_'*100))
    print(s18+line18+p18),print(s17+line17+p17),print(s16+line16+p16),print(s15+line15+p15),print(s14+line14+p14),print(s13+line13+p13),print(s12+line12+p12),print(s11+line11+p11),print(s10+line10+p10),print(s9+line9+p9),print(s8+line8+p8),print(s7+line7+p7),print(s6+line6+p6),print(s5+line5+p5),print(s4+line4+p4),print(s3+line3+p3),print(s2+line2+p2),print(s1+line1+p1)
    print(' '+('-'*100))
def removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('o',' '),line2.replace('o',' '),line3.replace('o',' '),line4.replace('o',' '),line5.replace('o',' '),line6.replace('o',' '),line7.replace('o',' '),line8.replace('o',' '),line9.replace('o',' '),line10.replace('o',' '),line11.replace('o',' '),line12.replace('o',' '),line13.replace('o',' '),line14.replace('o',' '),line15.replace('o',' '),line16.replace('o',' '),line17.replace('o',' '),line18.replace('o',' ')
    return line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
def addball(pos,line):
    linepart1 = line[:pos-1]
    linepart2 = line[pos+1:]
    line = linepart1 + 'o ' + linepart2
    return line
def moveball(movedirection,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    global pos, angle
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    numtomove = angle
    if movedirection == 'right':
        pos += numtomove
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 1 else line1),(addball(pos,line2) if linenum == 2 else line2),(addball(pos,line3) if linenum == 3 else line3),(addball(pos,line4) if linenum == 4 else line4),(addball(pos,line5) if linenum == 5 else line5),(addball(pos,line6) if linenum == 6 else line6),(addball(pos,line7) if linenum == 7 else line7),(addball(pos,line8) if linenum == 8 else line8),(addball(pos,line9) if linenum == 9 else line9),(addball(pos,line10) if linenum == 10 else line10),(addball(pos,line11) if linenum == 11 else line11),(addball(pos,line12) if linenum == 12 else line12),(addball(pos,line13) if linenum == 13 else line13),(addball(pos,line14) if linenum == 14 else line14),(addball(pos,line15) if linenum == 15 else line15),(addball(pos,line16) if linenum == 16 else line16),(addball(pos,line17) if linenum == 17 else line17),(addball(pos,line18) if linenum == 18 else line18)
    if movedirection == 'left':
        pos -= numtomove
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 1 else line1),(addball(pos,line2) if linenum == 2 else line2),(addball(pos,line3) if linenum == 3 else line3),(addball(pos,line4) if linenum == 4 else line4),(addball(pos,line5) if linenum == 5 else line5),(addball(pos,line6) if linenum == 6 else line6),(addball(pos,line7) if linenum == 7 else line7),(addball(pos,line8) if linenum == 8 else line8),(addball(pos,line9) if linenum == 9 else line9),(addball(pos,line10) if linenum == 10 else line10),(addball(pos,line11) if linenum == 11 else line11),(addball(pos,line12) if linenum == 12 else line12),(addball(pos,line13) if linenum == 13 else line13),(addball(pos,line14) if linenum == 14 else line14),(addball(pos,line15) if linenum == 15 else line15),(addball(pos,line16) if linenum == 16 else line16),(addball(pos,line17) if linenum == 17 else line17),(addball(pos,line18) if linenum == 18 else line18)
    if movedirection == 'rightup':
        pos = pos + numtomove                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line2) if linenum == 1 else line2),(addball(pos,line3) if linenum == 2 else line3),(addball(pos,line4) if linenum == 3 else line4),(addball(pos,line5) if linenum == 4 else line5),(addball(pos,line6) if linenum == 5 else line6),(addball(pos,line7) if linenum == 6 else line7),(addball(pos,line8) if linenum == 7 else line8),(addball(pos,line9) if linenum == 8 else line9),(addball(pos,line10) if linenum == 9 else line10),(addball(pos,line11) if linenum == 10 else line11),(addball(pos,line12) if linenum == 11 else line12),(addball(pos,line13) if linenum == 12 else line13),(addball(pos,line14) if linenum == 13 else line14),(addball(pos,line15) if linenum == 14 else line15),(addball(pos,line16) if linenum == 15 else line16),(addball(pos,line17) if linenum == 16 else line17),(addball(pos,line18) if linenum == 17 else line18)
    if movedirection== 'leftup':
        pos = pos - numtomove                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line2) if linenum == 1 else line2),(addball(pos,line3) if linenum == 2 else line3),(addball(pos,line4) if linenum == 3 else line4),(addball(pos,line5) if linenum == 4 else line5),(addball(pos,line6) if linenum == 5 else line6),(addball(pos,line7) if linenum == 6 else line7),(addball(pos,line8) if linenum == 7 else line8),(addball(pos,line9) if linenum == 8 else line9),(addball(pos,line10) if linenum == 9 else line10),(addball(pos,line11) if linenum == 10 else line11),(addball(pos,line12) if linenum == 11 else line12),(addball(pos,line13) if linenum == 12 else line13),(addball(pos,line14) if linenum == 13 else line14),(addball(pos,line15) if linenum == 14 else line15),(addball(pos,line16) if linenum == 15 else line16),(addball(pos,line17) if linenum == 16 else line17),(addball(pos,line18) if linenum == 17 else line18)
    if movedirection == 'rightdown':
        pos = pos + numtomove                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 2 else line1),(addball(pos,line2) if linenum == 3 else line2),(addball(pos,line3) if linenum == 4 else line3),(addball(pos,line4) if linenum == 5 else line4),(addball(pos,line5) if linenum == 6 else line5),(addball(pos,line6) if linenum == 7 else line6),(addball(pos,line7) if linenum == 8 else line7),(addball(pos,line8) if linenum == 9 else line8),(addball(pos,line9) if linenum == 10 else line9),(addball(pos,line10) if linenum == 11 else line10),(addball(pos,line11) if linenum == 12 else line11),(addball(pos,line12) if linenum == 13 else line12),(addball(pos,line13) if linenum == 14 else line13),(addball(pos,line14) if linenum == 15 else line14),(addball(pos,line15) if linenum == 16 else line15),(addball(pos,line16) if linenum == 17 else line16),(addball(pos,line17) if linenum == 18 else line17),(addball(pos,line18) if linenum == False else line18)
    if movedirection == 'leftdown':
        pos = pos - numtomove                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 2 else line1),(addball(pos,line2) if linenum == 3 else line2),(addball(pos,line3) if linenum == 4 else line3),(addball(pos,line4) if linenum == 5 else line4),(addball(pos,line5) if linenum == 6 else line5),(addball(pos,line6) if linenum == 7 else line6),(addball(pos,line7) if linenum == 8 else line7),(addball(pos,line8) if linenum == 9 else line8),(addball(pos,line9) if linenum == 10 else line9),(addball(pos,line10) if linenum == 11 else line10),(addball(pos,line11) if linenum == 12 else line11),(addball(pos,line12) if linenum == 13 else line12),(addball(pos,line13) if linenum == 14 else line13),(addball(pos,line14) if linenum == 15 else line14),(addball(pos,line15) if linenum == 16 else line15),(addball(pos,line16) if linenum == 17 else line16),(addball(pos,line17) if linenum == 18 else line17),(addball(pos,line18) if linenum == False else line18)
    return line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
padpos = 8
spos = 8
apos = 8
p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18 = '','','','','','','','|','|','|','|','','','','','','',''
s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = ' ',' ',' ',' ',' ',' ',' ','|','|','|','|',' ',' ',' ',' ',' ',' ',' '
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = ' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,((' '*50)+'o'+(' '*49)),' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100
printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
lost = 10
while True:
    try:
        time.sleep(waittime)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = moveball(movedirection,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        if ((pos >= 98 and angle > 2) or pos >= 98) and lost > 9:
            ln = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
            if (ln == 1 and '|' in p1) or (ln == 2 and '|' in p2) or (ln == 3 and '|' in p3) or (ln == 4 and '|' in p4) or (ln == 5 and '|' in p5) or (ln == 6 and '|' in p6) or (ln == 7 and '|' in p7) or (ln == 8 and '|' in p8) or (ln == 9 and '|' in p9) or (ln == 10 and '|' in p10) or (ln == 11 and '|' in p11) or (ln == 12 and '|' in p12) or (ln == 13 and '|' in p13) or (ln == 14 and '|' in p14) or (ln == 15 and '|' in p15) or (ln == 16 and '|' in p16) or (ln == 17 and '|' in p17) or (ln == 18 and '|' in p18):
                rand = randint(1,7)
                if rand == 1 or rand == 2 or rand == 3:
                    movedirection = 'leftup'
                    angle = randint(2,4)
                elif rand == 4 or rand == 5 or rand == 6:
                    movedirection = 'leftdown'
                    angle = randint(2,4)
                else:
                    movedirection = 'left'
                    angle = 3
            elif autoplay == False:
                lost = 0
            score += 1
        if pos <= 3:
            rand = randint(1,5)
            if rand == 1 or rand == 2 or rand == 3:
                movedirection = 'rightup'
                angle = randint(2,4)
            elif rand == 4 or rand == 5 or rand == 6:
                movedirection = 'rightdown'
                angle = randint(2,4)
            else:
                movedirection = 'right'
                angle = 3
        if 'o' in line1:
            if movedirection == 'leftdown':
                movedirection = 'leftup'
            else:
                movedirection = 'rightup'
        if 'o' in line18:
            if movedirection == 'leftup':
                movedirection = 'leftdown'
            else:
                movedirection = 'rightdown'
        lost += 1
        if lost == 2:
            print('you have lost')
            break
        linein = 1 if ('o' in line1 ) else (1 if ('o' in line2 ) else (2 if ('o' in line3 ) else (2 if ('o' in line4 ) else (3 if ('o' in line5 ) else (4 if ('o' in line6 ) else (5 if ('o' in line7 ) else (6 if ('o' in line8 ) else (7 if ('o' in line9 ) else (8 if ('o' in line10 ) else (9 if ('o' in line11 ) else (10 if ('o' in line12 ) else (11 if ('o' in line13 ) else (12 if ('o' in line14 ) else (13 if ('o' in line15 ) else (14 if ('o' in line16 ) else (15 if ('o' in line17 ) else 16))))))))))))))))
        padstorer = padpos
        padpos = round(padpos)
        if ((pos <= 40 and angle >= 3) or (pos <= 25 and angle == 2) or pos <= 20) and (movedirection == 'left' or movedirection == 'leftup' or movedirection == 'leftdown'):
            if spos > linein:
                spos -= 1
            if spos <= linein:
                spos += 1   
            s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = '|' if spos == 1 else ' ','|' if spos == 1 or spos == 2 else ' ','|' if spos == 1 or spos == 2 or spos == 3 else ' ','|' if spos == 1 or spos == 2 or spos == 3 or spos == 4 else ' ','|' if spos == 2 or spos == 3 or spos == 4 or spos == 5 else ' ','|' if spos == 3 or spos == 4 or spos == 5 or spos == 6 else ' ','|' if spos == 4 or spos == 5 or spos == 6 or spos == 7 else ' ','|' if spos == 5 or spos == 6 or spos == 7 or spos == 8 else ' ','|' if spos == 6 or spos == 7 or spos == 8 or spos == 9 else ' ','|' if spos == 7 or spos == 8 or spos == 9 or spos == 10 else ' ','|' if spos == 8 or spos == 9 or spos == 10 or spos == 11 else ' ','|' if spos == 9 or spos == 10 or spos == 11 or spos == 12 else ' ','|' if spos == 10 or spos == 11 or spos == 12 or spos == 12 else ' ','|' if spos == 11 or spos == 12 or spos == 13 or spos == 14 else ' ','|' if spos == 12 or spos == 13 or spos == 14 or spos == 15 else ' ','|' if spos == 13 or spos == 14 or spos == 15 or spos == 16 else ' ','|' if spos == 14 or spos == 15 or spos == 16 or spos == 17 else ' ','|' if spos == 15 or spos == 16 or spos == 17 or spos == 18 else ' '
        if (((pos >= 60 and angle >= 3) or (pos >= 75 and angle == 2) or pos >= 85) and (movedirection == 'right' or movedirection == 'rightup' or movedirection == 'rightdown')) and autoplay == True:
            if apos > linein:
                apos -= 1
            if apos <= linein:
                apos += 1
            padpos = apos
        p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18 = '|' if padpos == 1  or padpos == 2 else '','|' if padpos == 1 or padpos == 2 or padpos == 3 else '','|' if padpos == 1 or padpos == 2 or padpos == 3  or padpos == 4 else '','|' if padpos == 1 or padpos == 2 or padpos == 3 or padpos == 4 or padpos == 5 else '','|' if padpos == 2 or padpos == 3 or padpos == 4 or padpos == 5 or padpos == 6 else '','|' if padpos == 3 or padpos == 4 or padpos == 5 or padpos == 6  or padpos == 7 else '','|' if padpos == 4 or padpos == 5 or padpos == 6 or padpos == 7  or padpos == 8 else '','|' if padpos == 5 or padpos == 6 or padpos == 7 or padpos == 8  or padpos == 9 else '','|' if padpos == 6 or padpos == 7 or padpos == 8 or padpos == 9  or padpos == 10 else '','|' if padpos == 7 or padpos == 8 or padpos == 9 or padpos == 10  or padpos == 11 else '','|' if padpos == 8 or padpos == 9 or padpos == 10 or padpos == 11 or padpos == 12 else '','|' if padpos == 9 or padpos == 10 or padpos == 11 or padpos == 12  or padpos == 13 else '','|' if padpos == 10 or padpos == 11 or padpos == 12 or padpos == 13 or padpos == 14 else '','|' if padpos == 11 or padpos == 12 or padpos == 13 or padpos == 14 or padpos == 15 else '','|' if padpos == 12 or padpos == 13 or padpos == 14 or padpos == 15  or padpos == 16 else '','|' if padpos == 13 or padpos == 14 or padpos == 15 or padpos == 16  or padpos == 17 else '','|' if padpos == 14 or padpos == 15 or padpos == 16 or padpos == 17  or padpos == 18 else '','|' if padpos == 14 or padpos == 15 or padpos == 16 or padpos == 17 or padpos == 18 else ''
        print('Score: ',score,'    ',movedirection)
        if padpos > 1 and autoplay == False:
            padpos = padstorer
            padpos -= 0.3
    except:
        if padpos <= 17 and autoplay == False:
            padpos += 2
print('your score was ',score)