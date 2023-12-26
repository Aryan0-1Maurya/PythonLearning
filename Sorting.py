#Shell Sort

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        
      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print "After increments of size",sublistcount,"The list is",alist

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue


#User input
sort_list = list()
count = raw_input("Enter number of elements : ")

print
print 'Enter '+str(count) +' numbers : '

print
for i in range(int(count)):
    n = raw_input("number"+str(i+1)+": ")
    sort_list.append(int(n))

print
shellSort(sort_list)

print
print "Elements in sorted order :"
print(sort_list)






def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst

num_array = list()
num = raw_input("Enter number of elements : ")

print 'Enter '+str(num) +' numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))
    
print "Sorted list in ascending order : "+str(selection_sort(num_array))







#Radix Sort Program

def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for i in aList:
      tmp = int(i / placement)
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX
    
#User input
sort_list = list()
count = raw_input("Enter number of elements : ")

print
print 'Enter '+str(count) +' numbers : '

print
for i in range(int(count)):
    n = raw_input("number"+str(i+1)+": ")
    sort_list.append(int(n))

radixsort(sort_list)

print
print "Elements in sorted order :"
print(sort_list)







def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

#recursive function
def quickSortHelper(alist,first,last):
   if first<last:

       #partition the list
       splitpoint = partition(alist,first,last)

       # sort both halves
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           # swap places
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   # swap start with alist[first]
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark


num_array = list()
num = raw_input("Enter number of elements : ")

print 'Enter '+str(num) +' numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))

quickSort(num_array)
print "Sorted list in ascending order : "+str(num_array)






from heapq import merge

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

num_array = list()
num = raw_input("Enter number of elements : ")

print 'Enter '+str(num) +' numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))
    
print "Sorted list in ascending order : "+str(merge_sort(num_array))






def InsertionSort(list):  
    for index in range(1,len(list)):  
        curr = list[index]  
        position = index  

        while position > 0 and list[position-1] > curr:  
            list[position] = list[position-1]  
            position = position - 1  

        list[position] = curr  
    return list 

num_array = list()
num = raw_input("Enter number of elements : ")

print 'Enter '+str(num) +' numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))
    
print "Sorted list in ascending order : "+str(InsertionSort(num_array))






#Heap Sort Program

def heapsort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = int(length / 2)
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )
 
  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      swap( aList, 0, i )
      moveDown( aList, 0, i - 1 )
 
 
def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1
 
    # right child is larger than parent
    if aList[largest] > aList[first]:
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit
 
 
def swap( A, x, y ):
  A[x],A[y] = A[y],A[x]


#User input
sort_list = list()
count = raw_input("Enter number of elements : ")

print
print 'Enter '+str(count) +' numbers : '

print
for i in range(int(count)):
    n = raw_input("number"+str(i+1)+": ")
    sort_list.append(int(n))

heapsort(sort_list)

print
print "Elements in sorted order :"
print(sort_list)





#Bucket Sort Program

def bucketsort( A ):
  # get hash codes
  code = hashing( A )
  buckets = [list() for _ in range( code[1] )]
  # distribute data into buckets: O(n)
  for i in A:
    x = re_hashing( i, code )
    buck = buckets[x]
    buck.append( i )

  for bucket in buckets:
    insertionsort( bucket )
    ndx = 0
  # merge the buckets: O(n)
  for b in range( len( buckets ) ):
    for v in buckets[b]:
      A[ndx] = v
      ndx += 1
 
import math
 
def hashing( A ):
  m = A[0]
  for i in range( 1, len( A ) ):
    if ( m < A[i] ):
      m = A[i]
  result = [m, int( math.sqrt( len( A ) ) )]
  return result
 
def re_hashing( i, code ):
  return int( i / code[0] * ( code[1] - 1 ) )

def insertionsort( aList ):
  for i in range( 1, len( aList ) ):
    tmp = aList[i]
    k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    aList[k] = tmp


#User input
sort_list = list()
count = raw_input("Enter number of elements : ")

print
print 'Enter '+str(count) +' numbers : '

print
for i in range(int(count)):
    n = raw_input("number"+str(i+1)+": ")
    sort_list.append(int(n))
    
bucketsort(sort_list)

print
print "Elements in sorted order :"
print(sort_list)






def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i];
                alist[i] = alist[i+1];
                alist[i+1] = temp;

alist = list();
num = input("\nEnter number of elements: ");

for i in range(int(num)):
 n = input("num: ");
 alist.append(int(n));

print("\nThe unsorted array: ");
print(alist);

bubbleSort(alist);

print("\nThe Sorted array: ");
print(alist);






def floyd(rowcount):
 rows = [[1]]
 while len(rows) < rowcount:
  n = rows[-1][-1] + 1
  rows.append(list(range(n, n + len(rows[-1]) + 1)))
 return rows

def pfloyd(rows):
 colspace = [len(str(n)) for n in rows[-1]]
 for row in rows:
  print( ' '.join('%*i' % space_n for space_n in zip(colspace, row)))

input = int(raw_input("Enter the number of rows of floyd's triangle : "))
pfloyd(floyd(input))