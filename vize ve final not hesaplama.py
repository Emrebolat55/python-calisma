# vize ve final puanı ile not hesaplama
vize = input("vize notunuzu giriniz")
final = input("final notunu gir ")
ortalama = (float(vize) * 0.3 + float(final) * 0.7)
if ("ortalama<50"):
    print("kaldınız")
else:
    print("geçtiniz")
