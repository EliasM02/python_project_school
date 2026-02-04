#Steg 4 
import csv
import kamratrespons_ändrad as steg1
import matplotlib.pyplot as plt
import numpy as np

mellanrum = ("-"*56)

def steg4():
    skattetabell = []
    with open("skattetabell.csv", "r", encoding = "utf-8") as file:       #utf-8 för tillgång till bokstäver som å,ä,ö
        k = csv.reader(file, delimiter = ";")      

        for rad in k:
            skattetabell.append(rad)
    while True:
        skatt = 0         
        kommun = input("\nVilken kommun tillhör du? ").upper() 
        fel = 0
        for i in range(len(skattetabell)):        
            if (skattetabell[i][2]) == kommun:        #Söker efter rätt kommun i colummn 3
                print(skattetabell[i][3])              #Printar ut församlingarna inom vald kommun
                fel+=1
        if fel == 0:                                        #Gör det möjligt att skriva fel och man kan göra ett nytt försök direkt i loopen
            print("Felaktig kommun")
        else:
            while True:
                forsamling = input("\nVilken församling tillhör du? ").upper()  
                for i in range(len(skattetabell)):
                    if (skattetabell[i][3]) == forsamling: 
                        skatt = float(skattetabell[i][4])                         #Vill hitta skattesatsen till vald församling i vald kommun
                        print(f"\nSkattesatsen för din församling är {skatt} %")
                        return skatt
                if skatt == 0:                              
                    print("Felaktig församling")           #Samma sak här, kunna skriva fel och få frågan om församling igen
                    continue   
                        

def steg5():
    arbtimmar = []
    with open("arbetstimmar.csv", "r", encoding = "utf-8") as file:
        fil = csv.reader(file, delimiter = ";")      
        for rad in fil:
            arbtimmar.append(rad)                    
    del arbtimmar[0]                                                        #Vill ta bort översta raden ur csv filen med "rubriker" med "del"
    print(f"""{"Månad":<10} {"100% Beläggning":<15}{"80% Beläggning":>15}
          """)
    for rad in arbtimmar[:-1]:
        print(f"""{rad[0]:<10} {round(timpris * int(rad[2])):<15} {round(timpris * int(rad[2]) * 0.8):<20}""")          #Skapar mellanrum mellan månader respektive 100/80% för lite snyggare utskrift

    print(f"""
    {mellanrum}
    Total intäkt för hela året (100%): {round(timpris * int(arbtimmar[12][2])):<30}
    Realistisk intäkt för hela året (80%): {round(timpris * int(arbtimmar[12][2]) * 0.8):<30}""")            #Använder mig av den sista raden i csv filen med total arbetstid för att räkna ut årliga intäkter. Index 12 pga borttagen första rad som kommenterats tidigare

def steg6():
    arbtimmar = []
    with open("arbetstimmar.csv", "r", encoding = "utf-8") as file:
        fil = csv.reader(file, delimiter = ";")      
        for rad in fil:
            arbtimmar.append(rad)                #Likt steg 4 och 5, söker igenom csv filen
    del arbtimmar[0]
    plot_manad = []
    plot_inkomst = []                  #Vill ha tomma listor för att kunna lagra det jag söker efter i filen  OBS används på flera ställen i koden, men samma sak gäller.
    plot_inkomst80 = []                    
    for rad in arbtimmar[:-1]:
        plot_manad.append(rad[0][:3])                          
        plot_inkomst.append(int(rad[2]) * timpris)
        plot_inkomst80.append(int(rad[2])* timpris * 0.8)        

    plt.title("Prognos")            #Vill ha en rubrik "prognos" för stapeldiagrammet

    xpoints = np.array(plot_manad)
    ypoints = np.array(plot_inkomst)
    ypoints2 = np.array(plot_inkomst80)                                   #Ny varibel y för att kunna göra den sträckade linjen
    plt.bar(xpoints,ypoints)
    plt.plot(xpoints, ypoints2, linestyle = 'dashed', color = 'darkblue')
    plt.show()

skatt = steg4()

del1 = steg1.räkning_steg1()
tot_pris_ex_moms = del1[0]
månad = del1[1]
arbetad_tid = del1[2]
timpris = del1[3]
moms = del1[4]
månadens_timmar = del1[5]
timmar_diff = del1[6]
semesterdagar = del1[7]        #Importerat från steg1

del2 = steg1.räkning_steg2(tot_pris_ex_moms)
bruttolön = del2[0]
total_lonekostnad = del2[1]
arbetsgivaravgift = del2[2]
tjänstepension = del2[3]
semesterersättning = del2[4]     #Importerat från steg2

del3 = steg1.räkning_netto(skatt,bruttolön,tot_pris_ex_moms,total_lonekostnad)
skatten = del3[0]
netto = del3[1]
kassa = del3[2]     #Importerat delar från steg3 

#2 - Meny
while True:
    meny = input(f"""
            1. Skapa en faktura
            2. Beräkna företagets kostnader
            3. Nettolön och semesterdagar
            4. Kvarvarande pengar i bolaget
            5. Prognos
            6. Avsluta programmet
            Välj ett alternativ: """)     
    if meny == '1':
        print("Du valde 1")
        steg1.faktura(månad,arbetad_tid,timpris,tot_pris_ex_moms,moms,månadens_timmar,timmar_diff)

    elif meny == '2':
        print("\nDu valde 2")
        steg1.för_kost(bruttolön,arbetsgivaravgift,tjänstepension,semesterersättning,total_lonekostnad)
       
    elif meny == '3':
        print("Du valde 3")
        steg1.netto(bruttolön,netto,semesterdagar)

    elif meny == '4':
        print("\nDu valde 4")
        steg1.kassa(kassa)

    elif meny == '5':
        print("Du valde 5")
        print(mellanrum)
        steg5()                             #Importerat alla olika steg och tilldelat till en siffra i menyn. (Gäller alla menyval ovan)
        print(mellanrum)                    
        steg6()
        
    elif meny == '6':
        print("Du valde 6, programmet avslutas.")
        break
    else:
        print("Felaktig input")               #Gör det möjligt att skriva en ej tilldelad siffra t.ex. "7" utan att programmet ska stoppas
        continue