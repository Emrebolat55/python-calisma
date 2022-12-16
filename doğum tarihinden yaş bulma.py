import datetime

a=input("isminizi giriniz")
b=input("doğum yılınızı giriniz")
t=datetime.datetime.now();
yaş=t.year-int(b)
print("\nmerhaba"+""+"\nyaşınız:"+str(yaş))