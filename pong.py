#pong
import time, random, shelve
from random import randint
movedirection = 'right'
name = input('enter your name ')
pos = 50
def printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18
    print(' '+('_'*100))
    print('|'+line18+p18),print('|'+line17+p17),print('|'+line16+p16),print('|'+line15+p15),print('|'+line14+p14),print('|'+line13+p13),print('|'+line12+p12),print('|'+line11+p11),print('|'+line10+p10),print('|'+line9+p9),print('|'+line8+p8),print('|'+line7+p7),print('|'+line6+p16),print('|'+line5+p5),print('|'+line4+p4),print('|'+line3+p3),print('|'+line2+p2),print('|'+line1+p1)
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
    global pos
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    #lineabove = line2 if linenum == 1 else (line3 if (linenum == 2) else (line4 if (linenum == 3) else (line5 if (linenum == 4) else (line6 if (linenum == 5) else (line7 if (linenum == 6) else (line8 if (linenum == 7) else (line9 if (linenum == 8) else (line10 if (linenum == 9) else (line11 if (linenum == 10) else (line12 if (linenum == 11) else (line13 if linenum == 12 else (line14 if linenum == 13 else (line15 if linenum == 14 else (line16 if linenum == 15 else (line17 if linenum == 16 else line18)))))))))))))))
    #lineabove = line1 if linenum == 2 else (line2 if linenum == 3 else (line3 if (linenum == 4) else (line4 if (linenum == 5) else (line5 if (linenum == 6) else (line6 if (linenum == 7) else (line7 if (linenum == 8) else (line8 if (linenum == 9) else (line9 if (linenum == 10) else (line10 if (linenum == 11) else (line11 if (linenum == 12) else (line12 if (linenum == 13) else (line13 if linenum == 14 else (line14 if linenum == 15 else (line15 if linenum == 16 else (line16 if linenum == 17 else (line17 if linenum == 18 else line18))))))))))))))))
    numtomove = 2
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
padpos  = 8
p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18 = '','','','','','','','|','|','|','|','','','','','','',''
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = ' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,((' '*50)+'o'+(' '*49)),' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100
printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
while True:
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = moveball(movedirection,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    if pos >= 98:
        rand = randint(1,3)
        if rand == 1:
            movedirection = 'leftup'
        elif rand == 2:
            movedirection = 'left'
        else:
            movedirection = 'leftdown'
    if pos <= 2:
        rand = randint(1,3)
        if rand == 1:
            movedirection = 'rightup'
        elif rand == 2:
            movedirection = 'right'
        else:
            movedirection = 'rightdown'
    if 'o' in line1:
        if movedirection == 'leftdown':
            movedirection = 'leftup'
        if movedirection == 'rightdown':
            movedirection = 'rightup'
    if 'o' in line18:
        if movedirection == 'leftup':
            movedirection = 'leftdown'
        if movedirection == 'rightup':
            movedirection = 'rightdown'
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18 = '','','','','','','','|','|','|','|','','','','','','','',
    print(movedirection)
    time.sleep(0.1)