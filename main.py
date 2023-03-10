
from controllo import controllo
from stampa import stampa

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
    stampa(mm)
    #controllo partita
    while win == False:
        g1 = False
        g2 = False
        #giocatore 1 scelta
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
            #controllo scelta g1
            if(mm[xc-1][yr-1] == 0):
                mm[xc-1][yr-1] = 1
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
        #controllo vittoria g1
        if(controllo(mm,win) == True):
            stampa(mm)
            print('\n IL VINCITORE E GIOCATORE 1')
            break
        else:
            win = False    

        #stampa tabella    
        stampa(mm)
        #giocatore 2 scelta
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
            #controllo scelta g2 
            print(mm[xc-1][yr-1] )
            if(mm[xc-1][yr-1] == 0):
                mm[xc-1][yr-1] = 2
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

        #controllo vittoria g2           
        if(controllo(mm,win) == True):
            stampa(mm)
            print('\n IL VINCITORE E GIOCATORE 2')
            break
        else:
            win = False 

        #stampa tabella    
        stampa(mm)

    #nuova partita
    print('Vuoi rigiocare? y/n: ')
    r = input()
    while(r != 'y' and r != 'n'):
        print('Immetti un carattere corretto\nVuoi rigiocare? y/n: ')
        r = input()
    
    if(r == 'y'):
        main()
    else:
        print('fine')

#richiamo main
if __name__ == "__main__":
    main()