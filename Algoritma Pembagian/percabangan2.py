#Algoritma Pembagian
#Menentukan akar-akar dari suatu pembagian, dengan memasukkan nilai a,b da c.



a =int( input("Masukkan nilai (a): "))
b =int( input("Masukkan nilai (b): "))
c =int( input("Masukkan nilai (c): "))
print("Rumus Deskriminan:")
print("D = b^2-4ac")
def rumus1 (a,b,c):
    rumus1 = (b**2)-(4*a*c)
    return rumus1 
D = rumus1 (a,b,c)
def rumus2 (b,a): #x1=x2=-b/2*a
    rumus2 = -b/2*a
    return rumus2
def rumus3 (b,rumus1,a): #x1=-b+D**(0.5)/2*a
    rumus3 = -b+D**(1/2)/2*a
    return rumus3
def rumus4 (b,rumus1,a): #x2=-b-D**(0.5)/2*a
    rumus4 = -b-D**(1/2)/2*a
    return rumus4


print ("Hasil Deskriminan: ", rumus1 (a,b,c))

#nilai Deskriminan yg diperoleh memiliki tiga kemungkinan
if ( D==0 ):
    print("maka nilai akarnya x1 dan x2 : ", rumus2 (b,a))
elif ( D > int(0)) :
    print("maka nilai akarnya x1 : ", rumus3 (b,rumus1,a))
    print("maka nilai akarnya x2 : ", rumus4 (b,rumus1,a))
else:
    print("maka 'Akar Imajiner'")
