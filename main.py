#삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if(array[j] < array[j-1]):
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)

#퀵정렬
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
  if(start>=end):
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    #피벗보다 큰 데이터를 찾을 때가지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(array)

array = [5,7,9,0,3,1,6,2,4,8]
def quick(array):
  if(len(array) <= 1):
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
  #print(pivot)
  #print(left_side)
  #print(right_side)
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick(left_side) + [pivot] + quick(right_side)

print(quick(array))

















  

  