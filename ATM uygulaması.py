print("""
****************************      
ATM programına Hoş Geldiniz  

İşlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

programdan çıkmak için "q" ya basın

****************************      
      """)
bakiye = 1000

while True:
    işlem = input("İşlem Giriniz:")
    
    if(işlem == "q"):
        print("Tekrar Bekleriz")
        break
    
    if(işlem == "1"):
        print("Bakiyeniz {}'tl dir".format(bakiye))
    
    elif(işlem == "2"):
        miktar = int(input("miktar giriniz:"))
        bakiye += miktar
        
    elif(işlem == "3"):
        miktar = int(input("miktar giriniz:"))
        if(bakiye - miktar < 0):
            print("Yetersiz Bakiye...")
            continue
        bakiye -= miktar
else:
    print("Geçersiz işlem")       