data =[1,2,3,5,6,2,9,10,4]
min = 9999
max = 1
avg = 0
sum = 0
total = 0
count = 0
data[0] = 17


for x in data:
    if x <= min:
        min = x
print('min = ',min)

for x in data:
    if x >= max:
        max = x
print('max = ',max)

for x in data:
    total += x
    count += 1
avg = total / count
print('sum = ',total)
print('Avg =  %.2f'%(avg))



