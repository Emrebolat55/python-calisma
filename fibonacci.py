a = 1
b = 1

fibonacci = [a,b]
for i in range(20):#20tane terim olması için
    a,b = b,a+b # a değerine b yi, b değerine a+b yi atatdık
    fibonacci.append(b) #listeye b değerini ekledik
    print(fibonacci)