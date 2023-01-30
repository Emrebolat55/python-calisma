print("""
************************     
Kulanıcı Giriş Programı

************************    
      """)

syn_kulanıcı_adı = "emre"
syn_parola = "123"
giriş_hakkı = 3

while True:
    kulanıcı_adı = input("Kulanıcı adını giriniz:")
    parola = input("Parolanızı giriniz:")
    if (syn_kulanıcı_adı != kulanıcı_adı and syn_parola != parola):
        print("Kulanıcı adı ve parola hatalı")
        giriş_hakkı -= 1
    elif (syn_kulanıcı_adı != kulanıcı_adı and syn_parola == parola):
        print("kulanıcı adı yanlış")
        giriş_hakkı -= 1
    elif (syn_kulanıcı_adı == kulanıcı_adı and syn_parola != parola):
        print("Parola yanlış")
    else:
        print("sisteme giriş yapılıyor...")
        break
    if (giriş_hakkı == 0):
        print("Giriş hakkınız bitti")
        break
