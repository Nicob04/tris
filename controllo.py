def controllo(mm,win):
    win = False
    if(mm[0][0] == mm[0][1] and mm[0][1] == mm[0][2] 
        and mm[0][0] != 0 and mm[0][1] != 0 and mm[0][2] != 0 or 
        mm[1][0] == mm[1][1] and mm[1][1] == mm[1][2] 
        and mm[1][0] != 0 and mm[1][1] != 0 and mm[1][2] != 0 or 
        mm[2][0] == mm[2][1] and mm[2][1] == mm[2][2] 
        and mm[2][0] != 0 and mm[2][1] != 0 and mm[2][2] != 0 or 
        mm[0][0] == mm[1][1] and mm[1][1] == mm[2][2] 
        and mm[0][0] != 0 and mm[1][1] != 0 and mm[2][2] != 0 or 
        mm[0][2] == mm[1][1] and mm[1][1] == mm[2][0] 
        and mm[0][2] != 0 and mm[1][1] != 0 and mm[2][0] != 0 or 
        mm[0][0] == mm[1][0] and mm[1][0] == mm[2][0] 
        and mm[0][0] != 0 and mm[1][0] != 0 and mm[2][0] != 0 or 
        mm[0][1] == mm[1][1] and mm[1][1] == mm[2][1] 
        and mm[0][1] != 0 and mm[1][1] != 0 and mm[2][1] != 0 or 
        mm[0][2] == mm[1][2] and mm[1][2] == mm[2][2]
        and mm[0][2] != 0 and mm[1][2] != 0 and mm[2][2] != 0):
        win = True
    else:
        win = False

    return win        