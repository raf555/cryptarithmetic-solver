'''
Library time digunakan untuk menghasilkan waktu sekarang
lib_tugas2 tempat fungsi-fungsi bantuan
'''
from time import time
from lib_tugas2 import permutations, stringtonum, makeliststringnum, filterliststring, filltoten, isfirstnotzero, sumallin, print_output

'''
DISCLAIMER:

Fail = File
Fail merupakan File dalam Bahasa Indonesia menurut KBBI
'''

def intro():
  '''
  Intro
  '''
  print("-----------------------------------------------------------------------")
  print("| Selamat datang di Tucil 1 Stima 2020/2021                           |")
  print("| Penerapan Algoritma Brute Force untuk menyelesaikan CryptArithmetic |")
  print("| Oleh: Rezda A.F | 13519194 | K4                                     |")
  print("-----------------------------------------------------------------------")
  print("\n")

def parse(file):
  '''
  Parsing isi fail input dan error handler
  Output berupa boolean, list of letter, dan list of lines
  
  Asumsi: Spasi pada fail tidak dihiraukan, dianggap selalu rata kanan setiap baris
  (asumsi format penulisan selalu benar tanpa mempedulikan posisi kata).
  '''

  line = file.readlines()
  line_total = len(line)

  if (line_total < 4):
    print("Format isi fail salah! (Minimal empat baris)")
    return False, [], []
  
  for i in range(line_total):
    line[i] = line[i].replace(" ", "").replace("\n","")
  
  if(line[line_total-2]!="------"):
    print("Format isi fail salah! (Baris kedua dari akhir harus memuat string ------)")
    return False, [], []
  
  if(line[line_total-3][len(line[line_total-3])-1]!="+"):
    print("Format isi fail salah! (Baris ketiga dari akhir harus memuat tanda tambah (+) pada akhir kata)")
    return False, [], []
  
  # Menghapus tanda tambah
  line[line_total-3] = line[line_total-3][:-1]

  # Pengecekan karakter lain selain alfabet
  huruf_valid = True
  huruf = []
  for data in line:
    if(data == "------"): continue
    if(not data.isalpha()): 
      huruf_valid = False
      break
    for letter in data:
      try:
        huruf.index(letter)
      except:
        huruf.append(letter)
  
  if(not huruf_valid):
    print("Format isi fail salah! (Terdapat karakter lain selain alfabet --> "+data+")")
    return False, [], []

  if(len(huruf)>10):
    print("Format isi fail salah! (Jumlah alfabet unik lebih dari 10)")
    return False, [], []

  return True, huruf, line

def start(sort=True):
  '''
  Memulai program
  '''
  intro()

  nama_file = input("Masukkan nama fail dengan ekstensinya: ")
  err = False

  try:
    file = open(nama_file, "r")
  except:
    err = True

  # Mengecek apakah ada error pada pembacaan fail
  if (err):
    return print("Terjadi galat! (Fail tidak ditemukan atau lainnya)")
  
  print("Mohon tunggu..")

  # Waktu sebelum memulai brute force
  timebefore = time()

  # Parsing fail
  check = parse(file)
  if(not check[0]):
    return

  # Assign data yang diterima dari fungsi parse
  # line = list of lines (fitlered)
  # permutasi = list of permutations of list of letter
  # ^^^^^^^^^-> filltoten: mengisi list of letter sehingga berjumlah 10, 
  #             permutations : menghasilkan permutasi dari list, 
  #             set: menghapus permutasi yang menghasilkan list duplikat
  #             sorted: mengurutkan isi list

  line = filterliststring(check[2])
  permutasi = set(permutations(filltoten(check[1])))
  if sort:
    permutasi = sorted(permutasi)

  # assign jumlah tes yang akan dihitung, penanda hasil yg ditemukan, dan hasil permutasi yang benar
  tes = 0
  ada = False
  outnum = []

  # proses pencarian dengan metode brute force
  for data in permutasi:
    listnum = makeliststringnum(line, data) # menghasilkan list of num (string)
    tes += 1
    if(isfirstnotzero(listnum)): # mengecek apakah dimulai dengan 0 atau tidak, jika tidak maka lanjut
      penjumlah = sumallin(listnum)
      hasil = int(listnum[len(listnum)-1])
      if penjumlah == hasil: # mengecek hasil penjumlah dengan hasilnya, apabila ada maka loop langsung dihentikan
        ada = True
        outnum = data
        break

  # membuka kembali fail untuk diambil bentuk penjumlahannya utk ditampilkan ke layar
  file =  open(nama_file, "r")
  unedited_lines = file.readlines()
  file.close()

  # penampilan hasil ke layar
  print("\nInput:")
  print_output(unedited_lines)
  print("\n\nOutput:")

  if(not ada):
    print("Tidak ditemukan hasil untuk input tersebut..")
    return
  else:
    print_output(unedited_lines, True, outnum)
    # menghitung selisih waktu
    deltatime = time()-timebefore
    print("\n\nWaktu yang dihabiskan: %.2f"%deltatime+" detik")
    print("Jumlah tes:", tes, "kali")
    return