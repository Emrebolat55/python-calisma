import random
import time 

class Kumanda () :
    
    def _init_(self,tv_durumu = "kapalı",tv_ses = 0,kanal_listesi = ["trt"],kanal = "trt"):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses 
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        
    def tv_ac(self):
        if (self.tv_durumu == "açık"):
            print("televizyon zaten açık")
        else:
            print("televizyon açılıyor...")
    
    def tv_kapat(self):
        if (self.tv_durumu == "kapalı"):
            print("televizyon zaten kapalı...")
            
        else:
            print("televizyon kapatılıyor")
            self.tv_durumu = "kapalı"
    
    
    def ses_ayarları(self):
        
        while True:
            cevap = input("sesi azalt:'<' \n sesi arttır: '>' \n çıkış:çıkış" )
            
            if(cevap == "<"):
                if(self.tv_ses != 0 ):
                    self.tv_ses -=1
                    print("ses:",self.tv_ses)
            
            elif (cevap == ">"):
                if(self.tv_ses !=31 ):
                    self.tv_ses +=1 
                    print("ses:",self.tv_ses)
                    
                    
            else:
                print("ses güncellendi:",self.tv_ses)
                break
            
            
    def kanal_ekle(self,kanal_isimi):
        print("kanal ekleniyor...")
        time.sleep(1)
        
        self.kanal_listesi.append(kanal_isimi)
        print("kanal eklendi")
        
    def rastgele_kanal(self):
        
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        
        self.kanal = self.kanal_listesi(rastgele)  
        
        print("şu anki kanal:",self.kanal)
        
    def _len_(self):
        return len(self.kanal_listesi)
    
    def _str_(self):
        return "tv durumu: {} \n tv ses : {} \n şu anki kanal:{}\n".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)
    
kumada = Kumanda()
    
print("""
          Televizyon uygulaması
          
    1.tv aç
    
    2.tv kapat
    
    3.kanal ayarı
    
    4.kanal ekle
    
    5.kanal sayısını öğrenme
    
    6.rastgele kanal seçme
    
    7. televizyon bilgileri
    
    çıkamak için 'q' basın
          """)
    
while True:
        
        işlem = input("işlem seçiniz:")
        
        if (işlem == "q"):
            print("program sonlandırılır...")
            break
        elif (işlem == "1"):
            kumanda.tv_ac()
            
        elif(işlem == "2"):
            kumanda.tv_kapat()
            
        elif ( işlem == "3"):
            kumanda.ses_ayarları()
        
        elif ( işlem == "4"):
            kanal_isimleri = input("kanal isimlerini','ile ayırarak girin:")
            
            kanal_listesi = kanal_isimleri.split(",")
            
            for eklenecekler in kanal_listesi:
                kumanda.kanal_ekle(eklenecekler)
        
        elif (işlem == "5"):
            print("kanal sayısı:",len(kumanda))
            
        elif (işlem == "6"):
            kumanda.rastgele_kanal()

        elif(işlem == "7"):
            print(kumanda)
            
        else:
            print( "geçersiz işlem:")        
            
                        
                
            
               
                
                              