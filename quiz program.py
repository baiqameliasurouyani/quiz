#diklarasi daftar
list_nilai=[1,2,3,4,5,6,7,8,9,10]
#tampilkan list
print("daftar nilai : \n" ,list_nilai)
#menggunakan len
print("\nJumlah Index list nilai (len): \n" ,(list_nilai))
#menggunakan count
print("\njumlah nilai 10 Dalam List (cout) : \n" , list_nilai.count(10))
#menggunakan append
print("Menambah elemen dalam list (append) : " )
list_nilai.append(4)
list_nilai.append(97)
list_nilai.append(5)
list_nilai.append(3)
print("list nilai : ",list_nilai)
#menggunakan hapus
list_nilai.remove(1)
list_nilai.remove(2)
print("\nlist nilai (hapus) :\n" , list_nilai)
#menggunakan extend
list_nilai = [7]
list_nilai.extend(list_nilai)
print("\nlist nilai (extend :\n" , list_nilai)



jawaban
daftar nilai : 
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Jumlah Index list nilai (len): 
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

jumlah nilai 10 Dalam List (cout) : 
 1
Menambah elemen dalam list (append) : 
list nilai :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4, 97, 5, 3]

list nilai (hapus) :
 [3, 4, 5, 6, 7, 8, 9, 10, 4, 97, 5, 3]

list nilai (extend :
 [7, 7]






