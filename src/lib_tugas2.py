'''
Berisi fungsi-fungsi yang membantu proses brute force
Bikin ini biar ga menuh2in fail satunya aja hehe
'''

def swap(arr, i, j):
    '''
    swap array
    '''
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def permutations(arr):
    '''
    Mencari permutasi pada array dengan Algoritma Heap's
    Referensi: https://en.wikipedia.org/wiki/Heap%27s_algorithm#Details_of_the_algorithm
    output berupa set (agar tidak ada duplikat dari hasil permutasi)
    '''
    l = len(arr)
    out = set()
    out.add(tuple(arr))
    c = []
    for i in range(l):
        c.append(0)
    i = 0
    while i < l:
        if(c[i]<i):
            if(i%2==0):
                swap(arr, 0, i)
            else:
                swap(arr, c[i], i)
            out.add(tuple(arr))
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i+=1
    return out

def stringtonum(string, listnum):
  '''
  Mengubah string input menjadi angka sesuai listnum (dalam bentuk integer dan string)
  Contoh listnum = ["b", "c"] yang berarti "b" bernilai 0 dan "c" bernilai 1.
  '''
  out = ""
  for letter in string:
    if(letter == "-"): continue
    out += str(listnum.index(letter))
  return int(out), out

def makeliststringnum(liststring, listnum):
  '''
  Membuat list of string yang berisi nilai dari masing-masing string pada liststring
  '''
  out = []
  for data in liststring:
    out.append(stringtonum(data, listnum)[1])
  return out

def filterliststring(listnya):
  '''
  Menghapus "------" dari list of string
  '''
  out = []
  for data in listnya:
    if data == "------": continue
    out.append(data)
  return out

def filltoten(listnya):
  '''
  Mengisi list sampai berjumlah 10 (diisi dengan simbol -, dianggap kosong)
  '''
  arr2 = listnya
  pjg = len(listnya)
  minus = 10-pjg
  for i in range(minus):
    arr2.append("-")
  return arr2

def isfirstnotzero(listnum):
  '''
  Mengecek letter pertama pada string dari listnum apakah merupakan 0 atau bukan
  '''
  for num in listnum:
    if int(num[0]) == 0:
      return False
  return True

def sumallin(listnum):
  '''
  Menjumlahkan seluruh penjumlah kecuali hasil (nilai terakhir) dari listnum
  '''
  out = 0
  for i in range(len(listnum)):
    if i < len(listnum)-1:
      out += int(listnum[i])
  return out

def print_output(lines, replace=False, listnum=[]):
  '''
  Menulis bentuk penjumlahan pada layar
  '''
  for i in range(len(lines)):
    if (replace):
      for letter in lines[i]:
        if (letter.isalpha()):
          lines[i] = lines[i].replace(letter, str(listnum.index(letter)))
    print(lines[i],end="")