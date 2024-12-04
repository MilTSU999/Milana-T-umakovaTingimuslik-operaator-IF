print("Tere")

nimi=input("Mis on sinu nimi?")
if nimi.isalpha() and nimi.isupper():
    if nimi=="JUKU":
        print("Lähme kinno")
        try:
            vanus=int(input(f"Kui vana sa oled {nimi}?"))
            if vanus<0: 
                print("Viga!")
            elif vanus<=6:
                print("Tasuta")
            elif vanus<15:
                print("Lastepilet")
            elif vanus<65:
                print("Täispilet")
            elif vanus<100:
                print("Sooduspilet")
            else:print("Nii palju!!!")         
        except:
            print("Täiarv oli vaja sisestada")
        else:
            print("Suured tähed")
    else:
        print("Segatud sõne")

        #Ül 2
        #Ül 2
    nimi1=input("1. Mis on sinu nimi? ")
    nimi2=input("2. Mis on sinu nimi? ")

    #1. variant
    nimi1=input("1. Mis on sinu nimi? ")
    nimi2=input("2. Mis on sinu nimi? ")
    nimed=["Kirill", "Gleb"]
    if nimi.isalpha() and nimi2.isalpha():
        if (nimi1 in nimed) and (nimi2 in nimed):
            print("Nad on pinginaabrid")
        else:
            print("Nad ei oli naabrid")
    else:
        print("Viga") 

        #2. variant
        if (nimi=="Kirill" and nimi2== "Gleb") or (nimi2=="Kirill" and nimi1=="Gleb"):
           print("Nad on pinginaabrid")
        else:
            print("Nad ei oli naabrid")

         #Ül 3
try:
    a=float(input("Pikkus:"))
    b=float(input("Toa laius:"))
    S=a*b
    print(f"Põranda pindala on {S} m**2")
    vastus=input("Kas tahad remondi teha? (Jah-1/Ei-0)") #Jah/ei
    if vastus. upper()=="JAH" or vastus=="1":
        print("Remont")
        hind=float(input("Ühe meetri hind: "))
        summa=hind*S
        print(f"Remondi kulud: {summa} eur")
    elif vastus.upper()=="EI" or vastus=="0":
        print("-")
    else:
        print("Ei saa aru")
except:
    print("Numbrid!!!!")

    #Ül 4    

