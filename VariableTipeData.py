print("\n")
print("Contoh Menampilkan Nilai Variable")
print("=================================")
# membuat variable untuk menyimpan angka
x = 5
print("Nilai variabel x: ",x) # output : 5

# membuat variable untuk menyimpan teks
nama = "Salman"
print("Nilai dari variabel nama: ",nama) # output: Salman
print("\n")
print("Contoh Memanggil Type Data")
print("==========================")

# Menampilkan berbagai tipe data pada python

# type data integer
usia = 40 # integer
print("Tipe data dari variabel usia: ",type(usia)) # output: <class 'int'>

# type data float/desimal
tinggi = 1.75 # float
print("Tipe data dari variable tinggi: ",type(tinggi)) # output: <class 'float'>

# type data string
sapa = "Hallo Salman" # ini variabel string
print("Tipe data dari variabel sapa: ",type(sapa)) # output: <class 'str'>

# type data boolean
isActive = True
print("Tipe data dari variabel isActive",type(isActive)) # output: <class 'bool'>

# type data complex
DataComplex = 2 + 3j
print("Tipe data dari variabel DataComplex",type(DataComplex)) # output: <class 'complex'>

# type data squence/ urutan: ini akan menyimpan beberapa nilai dalam urutan tertentu
# list dan tuple
print("\n")
print("Ini type data skuensial/urutan")
print("==============================")
# 1. List Koleksi elemen yang dapat berubah (mutable), ditulis dalam []
data_list= [1,2,3,"python", True]
print("Tipe data dari variabel data_list: ",type(data_list)) # output: <class 'list>

# 2. Tuple Koleksi elemen yang tidak dapat diubah (immutable), ditulis dalam ().

data_tuple= (10,2,16,"Data")
print("Tipe data dari variabel data_tuple: ",type(data_tuple)) # output: <class 'tuple'>

print("\n")
# Tipe data set: koleksi unik tanpa urutan, ditulis dalam {}
data_set = {1,2,3,4,4,4,5}
print("Tipe data dari variabel data_set: ",type(data_set)) # output: <class 'set'>

# Tipe data dictionary/dict
# menyimpan pasangan key-value, ditulis dalam {}
# dengan format {key:value}

data_dict = {nama:"Salman", usia:45}
print("Tipe data dari variabel data_dict: ",type(data_dict)) # output: <class 'dict'>

# tipe data NoneType
# ini untuk mewakili nilai kosong atau tidak ada

kosong = None
print("Tipe data dari variable kosong: ",type(kosong)) # output: <class 'NoneType'>