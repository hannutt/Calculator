from tkinter import * #tuodaan tkinter-kirjasto.

from tkinter import messagebox #tuodaan messagebox kirjasto, jonka avulla voidaan näyttää ilmoituksia
                               #erillisissä ikkunoissa.

from tkinter.font import Font #Tuodaan fonttikirjasto ohjelmaan

#luodaan funktiot laskutoimituksille. jokaisessa funktiossa arvojen tietotyyppinä
#käytetään liukulukuja, että laskutoimitukset onnistuvat myös desimaaliluvuilla.

def plus():                      #funktio yhteenlaskuun.
    value1 = float(Entry.get(numb1)) #tallennetaan muuttujiin  value1 ja value2
    value2 = float(Entry.get(numb2)) #kenttiin numb1 ja numb2 syötetyt luvut.
    Sum = value1 + value2           #sum muuttujaan tallennetaan laskutoimituksen tulos.
    Entry.insert(result, 0 , Sum)  #tulostetaan result kenttään muuttujan sum  sisältämä arvo.
    

def div():                          #funktio jakolaskuihin
    value1 = float(Entry.get(numb1)) 
    value2 = float(Entry.get(numb2))
    division = value1 / value2
    Entry.insert(result, 0 ,division)

def multi():                       #funktio kertolaskuihin
    value1 = float(Entry.get(numb1))
    value2 = float(Entry.get(numb2))
    multip = value1 * value2
    Entry.insert(result, 0 ,multip)

def minus():                    #funktio vähennyslaskuihin
    value1 = float(Entry.get(numb1))
    value2 = float(Entry.get(numb2))
    subtraction = value1 - value2
    Entry.insert(result, 0 ,subtraction)

def powre():                 #funktio potenssilaskuihin
    value1 = int(Entry.get(numb1))
    value2 = int(Entry.get(numb2))
    powerreduction = pow(value1,value2) #käytetään "built-in" funktiota pow potenssin
    Entry.insert(result, 0, powerreduction) #laskemiseen.

def per():                  #funktio prosenttilaskuihin
    value1 = float(Entry.get(numb1))
    value2 = float(Entry.get(numb2))
    perresult = value1 * value2 / 100
    Entry.insert(result, 0, perresult)
                

def empty(): #luodaan funktio, joka poistaa luku1,luku2 ja tulos kentissä
    numb1.delete(0,END) #olevat arvot
    numb2.delete(0,END)
    result.delete(0,END)

def question(): #funktio näyttää kysymysmerkin klikkaamisen jälkeen allaolevan tekstin.
    messagebox.showinfo('?','Percentage calculations: Enter a percentage in the Number 1 field'
                        ' and integer to the number 2 field. After that click % button. Convert: Enter number'
                         ' in the number 1 field and choose convert operation from the drop-down menu')

#funktiot gallona, unssi maili ja solmumuuntoihin.
def gallons():
    gallon = float(Entry.get(numb1))
    litre = 3.785
    gal = gallon * litre
    Entry.insert(result,0,gal)

def oztogram():
    oz = float(Entry.get(numb1))
    gram = 28.34
    gramresult = oz * gram
    Entry.insert(result,0,gramresult)


def miles():
    mile = float(Entry.get(numb1))
    km = 1.60
    kmresult = mile * km
    Entry.insert(result,0,kmresult)

def knots():
    knot = float(Entry.get(numb1))
    km = 1.85
    knotresult = knot * km
    Entry.insert(result,0,knotresult)
    
    
    
                  

root = Tk() #luodaan pohjakomponentti
root.geometry('250x250') #annetaan pohjakomponentin kooksi 250x250 pikseliä.
root.configure(background = 'LightSteelBlue3')#annetaan pohjakomponentin taustaväri.
root.title('Calculator')

#luodaan alasvetovalikko.
menubar = Menu(root)
root.config(menu=menubar)
convert = Menu(menubar)
menubar.add_cascade(label = 'Convert', menu = convert)

#lisätään alasvetovalikkoon toimintoja, label komennolla lisätään teksti ja command komennolla
#kerrotaan mikä funktio suoritetaan.
convert.add_command(label = 'US liquid gallons to litres',command = gallons)
convert.add_command(label = 'Oz to grams',command = oztogram)
convert.add_command(label = 'Miles to kilometers',command = miles)
convert.add_command(label = 'Knots to kilometers', command = knots)

#tallennetaan Britannic Bold fontti muuttujaan, jota käytetään ohjelman otsikossa.
titlefont = Font (family = 'Britannic Bold')

frame1 = Frame(root) #painikkeiden, kenttien jne asettelu toteutetaan frame-komponenttien avulla.
frame1.configure(background = 'gray49')
frame2 = Frame(root)
frame2.configure(background = 'LightSteelBlue3')
frame3 = Frame(root)
frame3.configure(background = 'gray49')

#luodaan entry komennolla syötekentät,width komennolla kerrotaan niiden koko.

numb1 = Entry(frame1, width=5)
numb2 = Entry(frame1, width=5)
result = Entry(frame3, width=5)

#luodaan button komennolla painikkeet, command komennolla kerrotaan funktio
#joka suoritetaan kun painiketta painetaan, fg komennolla kerrottaan painikkeessa
#käytettävän tekstin väri.

plusbtn = Button(frame2, text='+', command = plus, relief= 'groove', fg = 'blue')
minusbtn = Button(frame2, text='-', command = minus, relief = 'groove', fg = 'blue')
multibtn = Button(frame2, text='*', command = multi, relief = 'groove', fg = 'blue')
divbtn = Button(frame2, text='/', command = div, relief = 'groove', fg = 'blue')
powbtn = Button(frame2, text = 'pow', command = powre, relief = 'groove', fg = 'blue')
perbtn = Button(frame2, text = '%', command = per, relief = 'groove',fg = 'blue') 
emptybtn = Button(frame2, text = 'C', command = empty, relief = 'groove', fg = 'blue')
questionbtn = Button (frame1, text = '?', command = question, background = 'gray49',fg = 'white')

#luodaan label komennolla tekstikomponentit, background komennolla kerrotaan niiden taustaväri.
#fg komennolla annetaan tekstin väri.

numb1txt = Label(frame1, text = 'Number 1 or %: ', background = 'gray49',fg = 'white')
numb2txt = Label(frame1, text = 'Number 2:', background = 'gray49',fg = 'white')
resulttxt = Label(frame1, text = 'Result:', background = 'gray49', fg = 'white')
  
programtitle = Label(root, text='Calculator & converter', background = 'LightSteelBlue3', font = titlefont)



#pakataan komponentit, että ne toimivat ohjelmassa, side komennolla asemoidaan komponentteja.
#pady ja padx komennoila lisätään tyhjää tilaa komponenttien ympärille.
programtitle.pack()
frame1.pack()
frame3.pack()
numb1txt.pack()
numb1.pack()
questionbtn.pack(pady=4)
numb2txt.pack()
numb2.pack()


resulttxt.pack(side=BOTTOM)
result.pack(side=BOTTOM,pady=4)
frame2.pack()
plusbtn.pack(side=LEFT,padx=2)
minusbtn.pack(side=LEFT,padx=2)
multibtn.pack(side=LEFT,padx=2)
divbtn.pack(side=LEFT,padx=2)
powbtn.pack(side=LEFT,padx=2)
perbtn.pack(side=LEFT,padx=2)
emptybtn.pack()
mainloop()
