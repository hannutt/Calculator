from tkinter import *
from tkinter import messagebox #tuodaan messagebox kirjasto, jonka avulla voidaan näyttää ilmoituksia
                               #erillisissä ikkunoissa.

#luodaan funktiot laskutoimituksille. jokaisessa funktiossa arvojen tietotyyppinä
#käytetään liukulukuja, että laskutoimitukset onnistuvat myös desimaaliluvuilla.

def plussaa():                      #funktio yhteenlaskuun.
    arvo1 = float(Entry.get(luku1)) #tallennetaan muuttujiin arvo1 ja arvo2
    arvo2 = float(Entry.get(luku2)) #kenttiin luku1 ja luku2 syötetyt luvut.
    summa = arvo1 + arvo2           #summa muuttujaan tallennetaan laskutoimituksen tulos.
    Entry.insert(tulos, 0 , summa)  #tulostetaan tulos kenttään muuttujan summa arvo.
    

def jaa():                          #funktio jakolaskuihin
    arvo1 = float(Entry.get(luku1)) 
    arvo2 = float(Entry.get(luku2))
    jakotulos = arvo1 / arvo2
    Entry.insert(tulos, 0 ,jakotulos)

def kerro():                       #funktio kertolaskuihin
    arvo1 = float(Entry.get(luku1))
    arvo2 = float(Entry.get(luku2))
    kertotulos = arvo1 * arvo2
    Entry.insert(tulos, 0 ,kertotulos)

def vahenna():                    #funktio vähennyslaskuihin
    arvo1 = float(Entry.get(luku1))
    arvo2 = float(Entry.get(luku2))
    erotus = arvo1 - arvo2
    Entry.insert(tulos, 0 ,erotus)

def potenssi():                 #funktio potenssilaskuihin
    arvo1 = int(Entry.get(luku1))
    arvo2 = int(Entry.get(luku2))
    potenssitulos = pow(arvo1,arvo2) #käytetään "built-in" funktiota pow potenssin
    Entry.insert(tulos, 0, potenssitulos) #laskemiseen.

def prosentti():                  #funktio prosenttilaskuihin
    arvo1 = float(Entry.get(luku1))
    arvo2 = float(Entry.get(luku2))
    prosenttitulos = arvo1 * arvo2 / 100
    Entry.insert(tulos, 0, prosenttitulos)
                

def tyhjenna(): #luodaan funktio, joka poistaa luku1,luku2 ja tulos kentissä
    luku1.delete(0,END) #olevat arvot
    luku2.delete(0,END)
    tulos.delete(0,END)

def kysymys(): #funktio näyttää kysymysmerkin klikkaamisen jälkeen allaolevan tekstin.
    messagebox.showinfo('?','Jos haluat laskea kuinka paljon X määrä prosentteja on luvusta, kirjoita luku1 kenttään'
                        ' prosettiluku ja luku2 kenttään luku, josta prosentit lasketaan.')

    
    
    
    
                  

ikkuna = Tk() #luodaan pohjakomponentti
ikkuna.geometry('250x250') #avataan ohjelma 250x250 pikselin koossa.
ikkuna.configure(background = 'LightSteelBlue3')#asetetaan pohjakomponentin taustaväri.
ikkuna.title('Nelilaskin')

frame1 = Frame(ikkuna) #painikkeiden, kenttien jne asettelu toteutetaan frame-komponenttien avulla.
frame1.configure(background = 'gray49')
frame2 = Frame(ikkuna)
frame3 = Frame(ikkuna)
frame3.configure(background = 'gray49')

#luodaan entry komennolla syötekentät,width komennolla kerrotaan niiden koko.

luku1 = Entry(frame1, width=5, borderwidth = 2)
luku2 = Entry(frame1, width=5, borderwidth = 2)
tulos = Entry(frame3, width=5, borderwidth = 2)

#luodaan button komennolla painikkeet, command komennolla kerrotaan funktio
#joka suoritetaan kun painiketta painetaan, fg komennolla kerrottaan painikkeessa
#käytettävän fontin väri.

plus = Button(frame2, text='+', command = plussaa, relief= 'groove', fg = 'blue')
miinus = Button(frame2, text='-', command = vahenna, relief = 'groove', fg = 'blue')
kerto = Button(frame2, text='*', command = kerro, relief = 'groove', fg = 'blue')
jako = Button(frame2, text='/', command = jaa, relief = 'groove', fg = 'blue')
potpainike = Button(frame2, text = 'pow', command = potenssi, relief = 'groove', fg = 'blue')
prospainike = Button(frame2, text = '%', command = prosentti, relief = 'groove',fg = 'blue') 
tyhjennys = Button(frame2, text = 'C', command = tyhjenna, relief = 'groove', fg = 'blue')
kysymysmerkki = Button (frame1, text = '?', command = kysymys, background = 'gray49')

#luodaan label komennolla tekstikomponentit, background komennolla kerrotaan niiden taustaväri.

luku1txt = Label(frame1, text = 'Number 1 or %: ', background = 'gray49')
luku2txt = Label(frame1, text = 'Number 2:', background = 'gray49')
tulostxt = Label(frame1, text = 'Result:', background = 'gray49')
tyhja = Label(ikkuna, background = 'LightSteelBlue3')              
ohjelmannimi = Label(ikkuna, text='Nelilaskin', background = 'LightSteelBlue3')



#pakataan komponentit, että ne toimivat ohjelmassa, side komennolla asemoidaan komponentteja.
ohjelmannimi.pack()
frame1.pack()
frame3.pack()
luku1txt.pack()
luku1.pack()
kysymysmerkki.pack()
luku2txt.pack()
luku2.pack()

tyhja.pack()
tulostxt.pack(side=BOTTOM)
tulos.pack(side=BOTTOM)
frame2.pack()
plus.pack(side=LEFT)
miinus.pack(side=LEFT)
kerto.pack(side=LEFT)
jako.pack(side=LEFT)
potpainike.pack(side=LEFT)
prospainike.pack(side=LEFT)
tyhjennys.pack()
mainloop()
