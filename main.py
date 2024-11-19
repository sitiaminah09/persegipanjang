#meminta input panjang dan lebar dari pengguna 
panjang = float(input("masukan panjang persegi panjang: "))
lebar = float(input("masukan lebar persegi panjang: "))
#menghitung luas
luas = panjang *  lebar
#menghitung keliling 
keliling = 2 * (panjang + lebar)
#menampilkan hasil luas dan keliling dengan format yang lebih jelas
print(f"luas persegi panjang adalah {luas} satuan persegi")
print(f"keliling persegi panjang adalah {keliling} satuan persegi")

