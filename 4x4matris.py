import numpy as np


a = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for i in range(np.size(a[0:4])):
        for j in range(np.size(a[0:4])):
            eleman = int(input(" İlk matris elemanlarını giriniz"))
            a = np.append(a, eleman)

a = np.delete(a, np.s_[:16])       #Burası 0 olarak girdiğimiz yerleri listeden atacak
a = np.reshape(a, (4,4))             #Burası da 4x4 matrix olarak listeyi şekillendirecek

print ("---------------------------------")

b = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for i in range(np.size(b[0:4])):
        for j in range(np.size(b[0:4])):
            eleman = int(input(" ikinci matris elemanlarını giriniz"))
            b = np.append(b, eleman)

b = np.delete(b, np.s_[:16])      
b = np.reshape(b, (4,4)) 

sonuc = np.add(a,b)


print("birinci matris" , a)
print ("---------------------------------")
print("ikinci matris" , b)
print ("---------------------------------")
print("toplamı" ,sonuc)
print("---------------------------")
print("determinantı" , np.linalg.det(sonuc))