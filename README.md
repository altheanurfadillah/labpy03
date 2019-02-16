# labpy03
### Alur Algoritma 
    Pengertian :
    Alur yaitu tahapan,sedangkan Algoritma adalah sekumpulan langkah-langkah terbatas untuk mencari solusi suatu masalah.
    Jadi, Disini saya akan membuat penjelasan tentang pemrograman terstruktur yang merupakan konsep dasar yang harus kita 
    pahami sebelum melakukan implementasi pada pembuatan program.

# LATIHAN 1 
            print (" Nama	  : Althea Nur Fadillah")
            print (" NIM  	: 311810110")
            print (" Kelas	: TI.18.A1 ")

            import random
            jumlah = int(input("Masukan Jumlah N:"))

            for i in range(jumlah):
              i=random.uniform(0.0,0.5)
              print("Data ke: =>",i)


            print("Selesai")
            

  ## ALGORITMA LATIHAN 1
    A. Input 
        Print :
            >>Print  : berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.
        Import random
            >>Import yaitu fungsi lanjut yang dipanggil oleh statement import.sedangankan random untuk menentukan suatu
            pilihan. yang berarti menggabungkan dua operasi.
    B. Proses 
        Jumlah = int(input("Masukan Jumlah N:"))
            >>merupakan fungsi untuk menghasilkan interger
        For i in range(jumlah):
            >>merupakan fungsi yang menghasilkan list. Fungsi ini akan menciptakan sebuah list baru dengan tentang nilai tertentu.
          i=random.uniform(0.0,0.5)
            >>digunakan untuk menampilkan bilangan float random dengan batas awal bilangan x, dan batas akhir bilangan y.
    C. Output
        print("Data ke: =>",i)
            >>Untuk Menampilkan Hasil dari sebuah proses yaitu dengan menampilkan i
        print("Selesai")
            >>Berfungsi untuk mencetak teks "Selesai" yang bertanda bahwa program sudah berakhir
     
   Dan ini Merupakan Hasil SreenShoot Program Latihan 1.
   ![5](https://user-images.githubusercontent.com/44330055/52686232-5b434c80-2f7f-11e9-962f-6859bd9a2e6a.png)


 # LATIHAN 2
  
    print (" Nama	  : Althea Nur Fadillah")
    print (" NIM  	: 311810110")
    print (" Kelas	: TI.18.A1 ")

    max = 0
    while True:
      a=int(input("Masukan bilangan :"))
      if max < int(a):
        max = int(a)
      if a == 0:
        break
    print("Bilangan Terbesar Adalah: ",max)
    
 ## ALGORITMA LATIHAN 2
    A. Input 
          Print
              >>berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.
          Max = 0
              >>fungsi bulid-in untuk mencari nilai tertinggi.Fungsi ini dapat diberikan sebuah parameter berupa angka.
    B. Proses
          while True:
            a=int(input("Masukan bilangan :"))
            if max < int(a):
              max = int(a)
            if a == 0:
              break
               
               ## "while"	: disebut uncounted loop (perulangan yang tak terhitung),
               ## "int"	: berfungsi mengkonversi bilangan maupun string angka menjadi bilangan bulat (integer).
               ## "if"	= Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan.
               ## "break"	: fungsi yang menghentikan operasi dibawahnya jika suatu kondisi yang ditentukan telah tercapai.
  
    C. Output
          print("Bilangan Terbesar Adalah: ",max)
              >>Untuk menampilkan Hasil dengan mencetak bilangan terbesar yaitu max
             
 
   Dan ini Merupakan Hasil SreenShoot Program Latihan 2.
   ![6](https://user-images.githubusercontent.com/44330055/52686276-87f76400-2f7f-11e9-8ebc-4702bb6ae510.png)
   
  # PROGRAM 1
        print (" Nama	  : Althea Nur Fadillah")
        print (" NIM  	: 311810110")
        print (" Kelas	: TI.18.A1 ")

        a = 100000000
        for x in range(1,9):
          if(x>=1 and x<=2):
            b=a*0
            print("Laba Bulan Ke-",x," :",b)
          if(x>=3 and x<=4):
            c=a*0.1
            print("Laba Bulan Ke-",x," :",c)
          if(x>=5 and x<=7):
            d=a*0.5
            print("Laba Bulan Ke-",x," :",d)
          if(x==8):
            e=a*0.2
            print("Laba Bulan Ke-",x," :",e)
        total = b+b+c+c+d+d+d+e
        print("\nTotal : ", total)

  ## ALGORITMA PROGRAM 1 
      A. Input 
          print (" Nama	  : Althea Nur Fadillah")
          print (" NIM  	: 311810110")
          print (" Kelas	: TI.18.A1 ")

            a = 100000000
                ##"print"	= Fungsi "print()" berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (Layar).
                ##"a" = adalah variable dimana 100000000 adalah modal awalnya.,
      B. Proses
          for x in range(1,9):
          if(x>=1 and x<=2):
            b=a*0
            print("Laba Bulan Ke-",x," :",b)
          if(x>=3 and x<=4):
            c=a*0.1
            print("Laba Bulan Ke-",x," :",c)
          if(x>=5 and x<=7):
            d=a*0.5
            print("Laba Bulan Ke-",x," :",d)
          if(x==8):
            e=a*0.2
            print("Laba Bulan Ke-",x," :",e)
          
            ##"for x in range" = "for" perulangan yang terhitung, dan "range" mengembalikan deret integer berurut pada range yang                       ditentukan dari start sampai stop.
            ##"if"= Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu                  perintah dalam kondisi tertentu. 
            ##"for"	= Perulangan yang terhitung.
            ##"range" = Mengembalikan deret integer berurut pada range yang ditentukan dari start sampai stop.
       C.Output
          total = b+b+c+c+d+d+d+e
            print("\nTotal : ", total)
              ##"\nTotal" = Membuat garis baru, dan menampilkan total hasil dari apa yang kita inginkan.
              
   Dan ini Merupakan Hasil SreenShoot Program 1
   ![8](https://user-images.githubusercontent.com/44330055/52686315-ae1d0400-2f7f-11e9-8e32-d4b94505a043.png)


Sekian tentang Pengertian dan Beberapa Program beserta Contoh Alur Algoritma yang telah saya buat., Jika ada kesalahan saya minta maaf,.


                                                        ALTHEA NUR FADILLAH
                                                          TUGAS PRAKUM 3 
                                                             TI.18.A1
                                                     
