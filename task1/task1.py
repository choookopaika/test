import sys

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
    
size1, length1, size2, length2 = map(int, sys.argv[1:5])

path1 = build_arr(size1, length1)
path2 = build_arr(size2, length2)

print("Общий путь:", path1 + path2)
