def build_arr(size, length):
  A = [i+1 for i in range(size)]
  intervals = []
  index = 0
  while True:

      interval = []
      for i in range(length):
          interval.append(A[(index + i) % size])
      intervals.append(interval)

      index = (index + length-1) % size
      if index == 0:
          break
  path = "".join(str(interval[0]) for interval in intervals) 
  #print("При длине обхода ", length, " получаем интервалы:", intervals)
  #print("Полученный путь:", path)
  return path  
    
size1, length1 = map(int, input("Введите размер первого массива и длину обхода через пробел: ").split())
size2, length2 = map(int, input("Введите размер второго массива и длину обхода через пробел: ").split())

path1 = build_arr(size1, length1)
path2 = build_arr(size2, length2)

print("Общий путь:", path1 + path2)
