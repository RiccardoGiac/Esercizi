#Riccardo Giacalone
import random
#Dati
#Percorso: lista 70 quadrati
#Ogni azione avviene a intervalli di un secondo

#Tartaruga
# funzioni: Passo_veloce: (50% di prob): avanza 3 quadrati
#           Scivolata: (20% prob): arretra 6 quadrati(non sotto 1)
#           Passo lento: (30% prob): avanza 1 quadrato

#Lepre
#funzioni: Riposo(20%): non si muove
#          Grande balzo(20%): avanza di 9 quadrati
#          Grande scivolata(10%): arretra 12 quadrati
#          Piccolo balzo(30%): avanza 1 quadrato
#          Piccola scivolata(20%): arretra 2 quadrati    

percorso: list[str] = ["_" for i in range(1,71)]


lepre: int = 1
tartaruga: int = 1
tempo: int = 0
pioggia: bool = False
stamina_l: int = 100
stamina_t: int = 100
d_ostacoli: dict[int:int] = {percorso[6]:-9, percorso[15]:-4, percorso[32]:-16,
                             percorso[40]: -2, percorso[53]:-3, percorso[69]: -10}
d_bonus: dict[int:int] = {percorso[2]:7, percorso[16]:10, percorso[25]:4,
                          percorso[39]:3, percorso[55]:10,percorso[61]:7}


def movimento_tartaruga(tartaruga:int,pioggia: bool,stamina_t: int)-> int:
    mov: int = random.randint(1,10)
    if pioggia == False:
        if mov <= 5 and stamina_t >= 5:
            tartaruga += 3
            stamina_t -= 5
            print(f"Passo veloce! +3 quadrati ({tartaruga}, s={stamina_t})")
        elif mov <= 5 and stamina_t < 5:
            print(f"La tartaruga stanca si riposa +10 stamina s={stamina_t}")
            stamina_t += 10
        if mov >=6 and mov <= 7 and tartaruga > 6 and stamina_t >= 10:
            tartaruga -= 6
            stamina_t -= 10
            print(f"Scivolata! -6 quadrati ({tartaruga}, s={stamina_t})")
        elif mov >= 6 and mov <= 7 and tartaruga <= 6 and stamina_t >= 10:
            tartaruga = 1
            stamina_t -= 10
            print(f"Scivolata! torna al primo quadrato! s={stamina_t}")
        elif mov >= 6 and mov <= 7 and tartaruga <= 6 and stamina_t < 10:
            print(f"La tartaruga stanca si riposa +10 stamina s={stamina_t}")
            stamina_t += 10
        elif mov >= 6 and mov <= 7 and tartaruga > 6 and stamina_t < 10:
            print(f"La tartaruga stanca si riposa +10 stamina s={stamina_t}")
            stamina_t += 10
        if mov >= 8 and mov <= 10 and stamina_t >= 3:
            tartaruga += 1
            stamina_t -= 3
            print(f"Passo lento! +1 quadrato ({tartaruga} s={stamina_t})")
        elif mov >= 8 and mov <= 10 and stamina_t < 3:
            print(f"La tartaruga stanca si riposa +10 stamina s= {stamina_t}")
            stamina_t += 10
    else:
        if mov <= 5:
            tartaruga += 2
            stamina_t -= 5
            print(f"Passo veloce sotto la pioggia! +2 quadrati ({tartaruga} s={stamina_t})")
        elif mov <= 5 and stamina_t < 5:
            print(f"La tartaruga stanca si riposa +10 stamina s={stamina_t}")
            stamina_t += 10
        if mov >= 6 and mov <= 7 and tartaruga > 7 and stamina_t >= 10:
            tartaruga -= 7
            stamina_t -= 10
            print(f"Scivolata sotto la pioggia! -7 quadrati ({tartaruga} s={stamina_t})")    
        elif mov >= 6 and mov <= 7 and tartaruga > 7 and stamina_t < 10:
            print(f"La tartaruga stanca si riposa +10 stamina s={stamina_t}")
            stamina_t += 10
        elif mov >= 6 and mov <=7 and tartaruga <=7 and stamina_t >=10:
            tartaruga = 1
            stamina_t -= 10
            print(f"Scivolata sotto la pioggia! torna al primo quadrato! s={stamina_t}")
        elif mov>=6 and mov <= 7 and tartaruga <= 7 and stamina_t <10:
            print(f"La tartaruga stanca si riposa +10 stamina s={stamina_t}")
            stamina_t += 10
        if mov >= 8 and mov <= 10 and stamina_t >= 3:
            print("Con la pioggia la tartaruga è così lenta da restare nella stessa casella")
        elif mov >= 8 and mov <= 10 and stamina_t < 3:
            print(f"La tartaruga stanca si riposa +10 stamina s={stamina_t}")
            stamina_t += 10

    return tartaruga,stamina_t

def movimento_lepre(lepre: int,pioggia: bool,stamina_l: int):
    mov: int = random.randint(1,10)
    if  pioggia == False:
        if mov == 1 and lepre > 12 and stamina_l >= 20:
            lepre -= 12
            stamina_l -= 20
            print(f"Grande Scivolata! -12 quadrati ({lepre}) s= {stamina_l}")
        elif mov == 1 and lepre <= 12 and stamina_l >= 20:
            lepre = 1
            stamina_l -= 20
            print(f"Scivolata! Torna alla prima posizione s= {stamina_l}")
        elif mov == 1 and lepre <= 12 and stamina_l < 20:
            print(f"La lepre è stanca s= {stamina_l}")
        elif mov == 1 and lepre > 12 and stamina_l < 20:
            print(f"La lepre è stanca s= {stamina_l}")
        if mov > 1 and mov <= 3:
            stamina_l += 10
            if stamina_l > 100:
                stamina_l= 100
            print("Riposo! La lepre si mette a dormire e non avanza")
        if mov > 3 and mov <= 5 and stamina_l >= 15:
            lepre += 9
            stamina_l -= 15
            print(f"Grande balzo! +9 quadrati ({lepre} s={stamina_l})")
        elif mov > 3 and mov <= 5 and stamina_l < 15:
            print(f"La lepre è stanca s= {stamina_l}")
        if mov > 5 and mov <= 8 and stamina_l >= 5:
            stamina_l -= 5
            lepre += 1
            print(f"Piccolo balzo! +1 quadrato ({lepre} s= {stamina_l})")
        elif mov > 5 and mov <= 8 and stamina_l < 5:
            print(f"La lepre è stanca s= {stamina_l}")
        if mov > 8 and mov <= 10 and lepre > 1 and stamina_l >= 8:
            lepre -= 2
            stamina_l -= 8
            print(f"Piccola scivolata! -2 quadrati ({lepre}) s={stamina_l}")
        elif mov > 8 and mov <= 10 and lepre > 1 and stamina_l < 8:
            print(f"La lepre è stanca s= {stamina_l}")
        elif mov > 8 and mov <= 10 and lepre == 1 and stamina_l >= 8:
            stamina_l -= 8
            print(f"Piccola scivolata! Resta al primo quadrato!")
        elif mov > 8 and mov <= 10 and lepre == 1 and stamina_l < 8:    
            print(f"La lepre è stanca s= {stamina_l}")
    
    else:
        if mov == 1 and lepre > 14 and stamina_l >= 20:
            lepre -= 14
            stamina_l -= 20
            print(f"Grande Scivolata sotto la pioggia! -14 quadrati {lepre} s={stamina_l}")
        elif mov == 1 and lepre > 14 and stamina_l < 20:
            print(f"La lepre è stanca s={stamina_l}")
        elif mov == 1 and lepre <= 14 and stamina_l > 20:
            lepre = 1
            stamina_l -= 20
            print(f"Scivolata sotto la pioggia! Torna alla prima posizione s= {stamina_l}")
        elif mov == 1 and lepre <= 14 and stamina_l < 20:
            print(f"La lepre è stanca s={stamina_l}")    
        if mov > 1 and mov <= 3:
            stamina_l += 10
            if stamina_l > 100:
                stamina_l = 100
            print(f"Riposo! La lepre si mette a dormire e non avanza s={stamina_l}")
        if mov > 3 and mov <= 5 and stamina_l >= 15:
            lepre += 7
            stamina_l -= 15
            print(f"Grande balzo! +7 quadrati ({lepre}) s= {stamina_l}")
        elif mov > 3 and mov <= 5 and stamina_l < 15:
            print(f"La lepre è stanca s={stamina_l}")
        if mov > 5 and mov <= 8 and lepre > 1 and stamina_l >= 5:
            lepre -= 1
            stamina_l -= 5
            print(f"Piccolo balzo ma la tempesta spinge la lepre indietro! -1 quadrato ({lepre}) s={stamina_l}")
        elif mov > 5 and mov <= 8 and lepre > 1 and stamina_l < 5:
            print(f"La lepre è stanca s= {stamina_l}")
        elif mov > 5 and mov <= 8 and lepre == 1 and stamina_l >= 5:
            stamina_l -= 5
            print(f"Piccolo balzo! La lepre scivola sul posto a causa della pioggia({lepre}) s= {stamina_l}")
        elif mov > 5 and mov <= 8 and lepre == 1 and stamina_l < 5:
            print(f"La lepre è stanca s= {stamina_l}")
        if mov > 8 and mov <= 10 and lepre >= 4 and stamina_l >=8:
            lepre -= 4
            stamina_l -=8
            print(f"Piccola scivolata sotto la pioggia! -4 quadrati ({lepre}) s={stamina_l}")
        elif mov > 8 and mov <= 10 and lepre >= 4 and stamina_l < 8:
            print(f"La lepre è stanca s= {stamina_l}")
        elif mov > 8 and mov <= 10 and lepre < 4 and stamina_l >=8:
            stamina_l -=8
            print(f"Piccola scivolata! Resta al primo quadrato! s= {stamina_l}")
        elif mov > 8 and mov <= 10 and lepre < 4 and stamina_l < 8:
            print(f"La lepre è stanca s= {stamina_l}")
    
    return lepre, stamina_l





print("BANG!!!! AND THEY'RE OFF!!!")


while lepre <= len(percorso) and tartaruga <= len(percorso):

    
    
        
    
    print(f"Tempo: {tempo}\nLepre: ")
    lepre,stamina_l = movimento_lepre(lepre,pioggia,stamina_l)
    print(f"\nTartaruga: ")
    tartaruga,stamina_t = movimento_tartaruga(tartaruga,pioggia,stamina_t)

    
    if tempo % 10 == 0:

        if pioggia == False:
            print("INIZIA A PIOVERE...")
            
        else:
            print("C'E' IL SOLE...")
        pioggia = not pioggia
    
    tempo += 1
    if lepre < len(percorso) and tartaruga < len(percorso):
        if lepre == tartaruga:
            percorso[lepre] = "OUCH!!!"
        else:
            percorso[lepre] = "L"
            percorso[tartaruga] = "T"
        print(percorso)
        percorso[lepre] = "_"
        percorso[tartaruga] = "_"

if lepre > tartaruga:
    print("LA LEPRE HA VINTO!!!")
elif lepre < tartaruga:
    print("LA TARTARUGA HA VINTO!!!")
else:
    print("PAREGGIO!!!")



    