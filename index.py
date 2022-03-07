from KNeighborsIris import KNeighborsIris

iris = KNeighborsIris()

is_run = True
while(is_run):
  print('-----------------------------')
  print("KNeightbors Iris")
  print("[1] Prediksi iris")
  print("[2] Keluar program")

  menu = input('Masukkan menu : ')
  print('-----------------------------')
  if(menu == "1"):
    print('Masukkan data')
    sepalLength = input("- Sepal Length (cm)\t: ")
    sepalWidth = input("- Sepal Width (cm)\t: ")
    petalLength = input("- Petal Length (cm)\t: ")
    petalWidth = input("- Petal Width (cm)\t: ")
    data = [      
      int(sepalLength),
      int(sepalWidth),
      int(petalLength),
      int(petalWidth),
    ]
    result = iris.find(data)
    print("Hasil\t\t\t:", result)
  elif(menu == "2"):
    is_run = False
  else:
    print("Menu tidak ditemukan")
