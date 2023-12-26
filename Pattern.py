size = int(raw_input("Enter the size: ")) #Instead of input,
#convert it to integer!

print
char = raw_input("Enter the character to draw: ")

print
for i in range(1, size+1):
    print char*i #on the first iteration, prints 1 'x'
    #on the second iteration, prints 2 'x', and so on






num = int(raw_input("\nEnter num: "));

for i in range(1,(num+1)):
 for j in range(1,(i+1)):
  print " ",j,;
 print "\n";






side = int(input("Enter the length of the diamond pattern : "))

print
for x in list(range(side)) + list(reversed(range(side-1))):
    print('{: <{w1}}{:*<{w2}}'.format('', '', w1=side-x-1, w2=x*2+1))






num = int(raw_input("\nEnter n: "));

for i in range(1,(num+1)): 
 for j in range(0,i): 
  print " ",((i+j)%2),;
 print "\n";






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