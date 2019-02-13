print ("Nama	: Althea Nur Fadillah")
print ("NIM		: 311810110")
print ("Kelas	: TI.18.A1")

max = 0
while True:
	a=int(input("Masukan Bilangan :"))
	if max < int(a):
			max = int(a)
	if a == 0:
			break
print("Bilangan Terbesar adalah : ",max)