arr = []
twait = 0
n = int(raw_input('Enter the total no of processes: '))
for i in xrange(n):
    arr.append([])
    arr[i].append(int(raw_input('Enter arrival time of process '+repr(i+1)+': ')))
    arr[i].append(int(raw_input('Enter bust time of process '+repr(i+1)+': ')))
    twait += arr[i][1]

arr.sort(key = lambda arr:arr[0])

print 'P_Number\tArrivalTime\tBurstTime'
for i in xrange(n):
    print i+1,'\t',arr[i][0],'\t',arr[i][1]
    
print 'Total waiting time = ',twait
print 'Average waiting time = ',(twait/n)
