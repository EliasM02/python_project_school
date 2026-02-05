"""
This file is based on an initial version written by another student.
The code has been modified, extended and integrated into the main program.
"""

# Företagsnamn
foretagsnamn = "Shaik.AB"

# Konstanter
mellanrum = ("-"*56)
blank = print()

#Steg 1 samt felhantering om användaren anger ett felaktigt värde

def räkning_steg1():
    while True:
        arbetstimmar_per_månad = [176,160,168,160,160,144,184,168,176,184,160,168]
        try:
            timpris = float(input("\nAnge företagets timpris (exklusive moms): "))
            arbetad_tid = float(input("\nAnge antal arbetade timmar som skall faktureras: "))
            break 
        except ValueError:
            print("Du har skrivit in ett felaktigt värde. Försök igen med siffror.")

    # Beräkna totala beloppet
    tot_pris_ex_moms = round(timpris * arbetad_tid)
    tot_pris_ink_moms = round(tot_pris_ex_moms * 1.25)
    moms = tot_pris_ink_moms - tot_pris_ex_moms
    arbetsdagar = arbetad_tid / 8 
    semesterdagar = arbetsdagar * 0.12
    
    # Fråga vilken månad fakturan avser
    while True:
        try:
            månad = int(input("\nVilken månad avser fakturan (t.ex. 1, 2, 3, etc.): "))
            if månad >0 and månad < 13:
                break
            else:
                print("Ogiltig månad. Försök igen.")
                continue
        except ValueError:
            print("Ogiltig månad. Försök igen.")

    # Hämta arbetstimmar för vald månad
    månadens_timmar = arbetstimmar_per_månad[månad-1]                                                      
    timmar_diff = round(arbetad_tid - månadens_timmar)                                   # Bytte plats på variablerna för att inte få negativa värden vid övertid
    list1 = [tot_pris_ex_moms , månad ,arbetad_tid,timpris,moms,månadens_timmar,timmar_diff,semesterdagar]
    return list1
"""del1 = räkning_steg1()
tot_pris_ex_moms = del1[0]
månad = del1[1]
arbetad_tid = del1[2]
timpris = del1[3]
moms = del1[4]
månadens_timmar = del1[5]
timmar_diff = del1[6]
semesterdagar = del1[7]
"""

#Steg 2 - Beräkna företagets kostnader
def räkning_steg2(tot_pris_ex_moms):
    while True:
        try:
            bruttolön = float(input("\nAnge din önskade bruttolön (före skatt): "))
            if bruttolön >0:
                
                arbetsgivaravgift = round(bruttolön * 0.3142)
                tjänstepension = round(bruttolön * 0.045)
                semesterersättning = round(bruttolön * 0.12)
                total_lonekostnad = round(bruttolön + arbetsgivaravgift + tjänstepension + semesterersättning)

                if bruttolön > tot_pris_ex_moms:
                    print("\nVarning: Bruttolönen är för hög jämfört med företagets totala intäkter!")
                    continue
                else:
                    print("\nBruttolönen är inom acceptabla gränser.")
                    list2 = [bruttolön,total_lonekostnad,arbetsgivaravgift,tjänstepension,semesterersättning,]
                    return list2
            else:
                print("Lönen måste vara större än 0")
                continue        
        except ValueError:
            print("Du har skrivit in ett felaktigt värde. Försök igen med siffror.")
        
    
    
    

# Kontrollera om bruttolönen är för hög jämfört med företagets intäkter
        
        
"""del2 = räkning_steg2()
bruttolön = del2[0]
total_lonekostnad = del2[1]
arbetsgivaravgift = del2[2]
tjänstepension = del2[3]
semesterersättning = del2[4]"""


#Steg 3 - Beräkna nettolön och kvarvarande pengar 
def räkning_netto(skatt,bruttolön,tot_pris_ex_moms,total_lonekostnad):
    skatten = round(bruttolön * (skatt/100))
    netto = round(bruttolön - skatten)
    kassa = tot_pris_ex_moms - total_lonekostnad
    list3 = [skatten,netto,kassa]
    return list3
"""del3 = räkning_netto()
skatten = del3[0]
netto = del3[1]
kassa = del3[2]"""

# Skriver ut en faktura med all information given
def faktura(månad,arbetad_tid,timpris,tot_pris_ex_moms,moms,månadens_timmar,timmar_diff):
    print(f"""
    {foretagsnamn}

    Månad {månad}
    {mellanrum}               
    Arbetade timmar: {arbetad_tid:>32} timmar
    Timpris: {timpris:>40} kr
    Totalt exkl. moms: {tot_pris_ex_moms:>30} kr
    Moms: {moms:>43} kr
    Totalt fakturerat: {tot_pris_ex_moms:>30} kr
    {mellanrum}

    Arbetstid snitt denna månad: {månadens_timmar} timmar
    Du har fakturerat {arbetad_tid} timmar
    Du skulle potentiellt kunna ha fakturerat {månadens_timmar} timmar om du varit
    frisk hela månaden.

    Skillnad (missade timmar om du varit sjuk): {timmar_diff} timmar
    Om du varit sjuk eller haft frånvaro, missade du {timmar_diff} timmar.
    Eventuella intäkter som du inte fick in: {timmar_diff * timpris:.1f} kr """)

def för_kost(bruttolön,arbetsgivaravgift,tjänstepension,semesterersättning,total_lonekostnad):
    print(f"""Företagets kostander
    {mellanrum}
    Bruttolön: {bruttolön:>39} kr
    Arbetsgivaravgift: {arbetsgivaravgift:>30.1f} kr
    Tjänstepension: {tjänstepension:>33} kr
    Semesterersättning: {semesterersättning:>29} kr
    Total lönekostnad: {total_lonekostnad:>30} kr """)

def netto(bruttolön,netto,semesterdagar):
    print(f"""
    Nettolön och semesterdagar
    {mellanrum}
    Nettolön: {netto:>39} kr
    Betald skatt: {bruttolön - netto:>35.1f} kr
    Semesterdagar: {semesterdagar:>34.1f} dagar
    {mellanrum}""")
    
def kassa(kassa):
    print(f"""
    {mellanrum}
    Pengar som kvar i företaget: {kassa:>20.1f} kr 
    {mellanrum}""")