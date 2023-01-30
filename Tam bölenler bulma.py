print("""
*************************************
Tam sayı bölenlerine ayırma programı

*************************************      
      
      """)


def tambolenleribulma(sayı):
    tam_bolenler = []
    
    for i in range(2,sayı):
        if (sayı % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayı = input("sayı:")
    
    if (sayı == "q"):
        print("Program sonlandırılıyor...")
        break
    
    else:
        sayı = int(sayı)
        print("Tam sayı bölenleri",tambolenleribulma(sayı))