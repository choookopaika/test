import sys

elements_file = sys.argv[1]

nums = []
with open(elements_file, 'r') as elements_f:
    for line in elements_f:
        line = line.strip()
        if line:  
            nums.append(int(line))

def moves(nums):
    if not nums:
        return 0

    nums_sorted = sorted(nums)
    n = len(nums_sorted)

    if n % 2 == 1:
        target = nums_sorted[n // 2]
    else:
        target = nums_sorted[n // 2]
    moves = 0
    
    while any(x != target for x in nums_sorted):
        for i in range(n):
            if nums_sorted[i] < target:
                nums_sorted[i] += 1
                moves += 1
            elif nums_sorted[i] > target:
                nums_sorted[i] -= 1
                moves += 1

            if moves > 20:
                print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
                return

    print(f"Минимальное количество ходов: {moves}")

moves(nums)
