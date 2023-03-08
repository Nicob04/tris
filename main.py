#t4ris game

def main():  
    win = False
    mm = [
        [0  ,  0 ,  0],
        [0  ,  0 ,  0],
        [0  ,  0 ,  0]
    ]
    c = 0
    p = False
    print('INIZIAMO IL GIOCO \n')
    print(mm[0],'\n')
    print(mm[1],'\n')
    print(mm[2],'\n')
    
    while win == False:
        g1 = False
        g2 = False
        #giocatore 1 
        while g1 == False:
            print('tocca a te giocatore 1: \n')
            x = input('inserisci un valore riga: ')
            xc = int(x)
            while(xc < 0 or xc > 3):
                x = input('inserisci un valore riga: ')
                xc = int(x)
            y = input('inserisci un valore colonna: ')
            yr = int(y)
            while(yr < 0 or yr > 3):
                y = input('inserisci un valore colonna: ')
                yr = int(y)
            #controllo g1
            if(mm[xc-1][yr-1] == 0):
                mm[xc-1][yr-1] = 'X'
                g1 = True
                c+= 1
                if(c == 9):
                    p = True
                    break
            else:
                print('gia occupato cambia posizione')    
                g1 = False
        if(p == True):
            print('PAREGGIO FINE PARTITA')
            break
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
                
            print('\n IL VINCITORE E GIOCATORE 1')
            break
        else:
            win = False    
        print(mm[0],'\n')
        print(mm[1],'\n')
        print(mm[2],'\n')
        #giocatore 2
        while g2 == False:
            print('tocca a te giocatore 2: \n')
            x = input('inserisci un valore riga: ')
            xc = int(x)
            print(xc)
            while(xc < 0 or xc > 3):
                x = input('inserisci un valore riga: ')
                xc = int(x)
            y = input('inserisci un valore colonna: ')
            yr = int(y)
            while(yr < 0 or yr > 3):
                y = input('inserisci un valore colonna: ')
                yr = int(y)
            #controllo g2
            print(mm[xc-1][yr-1] )
            if(mm[xc-1][yr-1] == 0):
                mm[xc-1][yr-1] = 'O'
                g2 = True
                c+= 1
                if(c == 9):
                    p = True
            else:
                print('gia occupato cambia posizione')    
                g2 = False

        if(p == True):
            print('PAREGGIO FINE PARTITA')
            break

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
            print(mm[0] ,'\n',mm[1],'\n',mm[2])
            print('\n IL VINCITORE E GIOCATORE 1')
            break
        else:
            win = False       
        print(mm[0],'\n')
        print(mm[1],'\n')
        print(mm[2],'\n')


    print('vuoi rigiocare? y/n: ')
    r = input()
    if(r == 'y'):
        main()
    else:
        print('fine')


if __name__ == "__main__":
    main()