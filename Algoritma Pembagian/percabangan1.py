#Algoritma Pembagian
#Menentukan jumlah pembayaran telepon jika ada jam tertentu diberikan diskon, jika di hari minggu atau antara jam 10 malam sampai jam 7 pagi


print("contoh:")
print("hari : 1                      (1:senin,2:selasa,3:rabu,4:kamis,5:jumat,6:sabtu,7:minggu)")
print("jam mulai menelepon : 1       (0 sampai 23)")
print("berapa jam menelepon : 1      (0 sampai n)")
print("berapa menit menelepon : 11   (0 sampai 60)")
print("berapa detik menelepon : 34   (0 sampai 60)")
print('')
 
a =( input("Masukkan hari : "))
b =int( input("Masukkan jam mulai menelepon : "))
c =int( input("berapa jam menelepon  : "))
d =int( input("berapa menit menelepon : "))
e =int( input("berapa detik menelepon : "))
 
def lmbcr (c,d,e):
    lmbcr = (c*3600)+(d*60)+e
    return lmbcr
L = lmbcr (c,d,e)
def diskon (L):
    diskon = 0.3*(((L)/ int(20))*200)
    return diskon
D = diskon (L)
def bayar1 (L,D):
    bayar1 =  int(((L)/ int(20))*200)- (D)
    return bayar1
def bayar2 (L):
    bayar2 =  int(((L)/ int(20))*200)
    return bayar2
#nilai pembayaran ada dua kemungkinan
if ( a ==int(7) ) or (b >= 22) or (b <= 7):
    print("Lama Bicara (detik): ", lmbcr (c,d,e))
    print("Diskon yg didapat :Rp.", diskon (L))
    print("Biaya: tiap 20 detik : Rp.200")
    print('')
    print("Maka Biaya yg harus dibayarkan :Rp.", bayar1 (L,D))

else :
    print("Lama Bicara (detik): ", lmbcr (c,d,e))
    print("Biaya: tiap 20 detik : Rp. 200")
    print('')
    print("Maka Biaya yg harus dibayarkan :Rp.", bayar2 (L))
