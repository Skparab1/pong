#pong
movedirection = 'right'
name = input('enter your name ')
def printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    print(' '+('_'*100))
    print('|'+line18+'|'),print('|'+line17+'|'),print('|'+line16+'|'),print('|'+line15+'|'),print('|'+line14+'|'),print('|'+line13+'|'),print('|'+line12+'|'),print('|'+line11+'|'),print('|'+line10+'|'),print('|'+line9+'|'),print('|'+line8+'|'),print('|'+line7+'|'),print('|'+line6+'|'),print('|'+line5+'|'),print('|'+line4+'|'),print('|'+line3+'|'),print('|'+line2+'|'),print('|'+line1+'|')
    print(' '+('-'*100))
def redefineline(content,linecontent,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    line1 = content if linecontent == line1 else line1
    line2 = content if linecontent == line2 else line2
    line3 = content if linecontent == line3 else line3
    line4 = content if linecontent == line4 else line4
    line5 = content if linecontent == line5 else line5
    line6 = content if linecontent == line6 else line6
    line7 = content if linecontent == line7 else line7
    line8 = content if linecontent == line8 else line8
    line9 = content if linecontent == line9 else line9
    line10 = content if linecontent == line10 else line10
    line11 = content if linecontent == line11 else line11
    line12 = content if linecontent == line12 else line12
    line13 = content if linecontent == line13 else line13
    line14 = content if linecontent == line14 else line14
    line15 = content if linecontent == line15 else line15
    line16 = content if linecontent == line16 else line16
    line17 = content if linecontent == line17 else line17
    line18 = content if linecontent == line18 else line18
    return line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
def moveball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    global movedirection
    linecontent = line1 if ('o' in line1 ) else (line2 if ('o' in line2 ) else (line3 if ('o' in line3 ) else (line4 if ('o' in line4 ) else (line5 if ('o' in line5 ) else (line6 if ('o' in line6 ) else (line7 if ('o' in line7 ) else (line8 if ('o' in line8 ) else (line9 if ('o' in line9 ) else (line10 if ('o' in line10 ) else (line11 if ('o' in line11 ) else (line12 if ('o' in line12 ) else (line13 if ('o' in line13 ) else (line14 if ('o' in line14 ) else (line15 if ('o' in line15 ) else (line16 if ('o' in line16 ) else (line17 if ('o' in line17 ) else line18))))))))))))))))
    lineabove = line2 if linecontent == line1 else (line3 if (linecontent == line2) else (line4 if (linecontent == line3) else (line5 if (linecontent == line4) else (line6 if (linecontent == line5) else (line7 if (linecontent == line6) else (line8 if (linecontent == line7) else (line9 if (linecontent == line8) else (line10 if (linecontent == line9) else (line11 if (linecontent == line10) else (line12 if (linecontent == line11) else (line13 if linecontent == line12 else (line14 if linecontent == line13 else (line15 if linecontent == line14 else (line16 if linecontent == line15 else (line17 if linecontent == line16 else line18)))))))))))))))
    lineabove = line1 if linecontent == line2 else (line2 if linecontent == line3 else (line3 if (linecontent == line4) else (line4 if (linecontent == line5) else (line5 if (linecontent == line6) else (line6 if (linecontent == line7) else (line7 if (linecontent == line8) else (line8 if (linecontent == line9) else (line9 if (linecontent == line10) else (line10 if (linecontent == line11) else (line11 if (linecontent == line12) else (line12 if (linecontent == line13) else (line13 if linecontent == line14 else (line14 if linecontent == line15 else (line15 if linecontent == line16 else (line16 if linecontent == line17 else (line17 if linecontent == line18 else line18))))))))))))))))
    if movedirection == 'right':
        content = ' '+linecontent[:99]
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = redefineline(content,linecontent,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    if movedirection == 'left':
        content = linecontent[1:]+' '
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = redefineline(content,linecontent,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    if movedirection == 'rightup':
        
    if movedirection == 'leftup':
    if movedirection == 'rightdown':
    if movedirection == 'rightup':
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = ' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100
printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
