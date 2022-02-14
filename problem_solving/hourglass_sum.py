def hourglassSum(arr):
    max = float('-inf')
    for i in range(1, 5):
        for j in range(1, 5):
            tmp_sum = sum(arr[i-1][j-1:j+2]) + arr[i][j] + sum(arr[i+1][j-1:j+2])
            if tmp_sum > max:
                max = tmp_sum
    return max


arr = [[1, 1, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [1, 1, 1, 0, 0, 0],
      [0, 0, 2, 4, 4, 0],
      [0, 0, 0, 2, 0, 0],
      [0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))
