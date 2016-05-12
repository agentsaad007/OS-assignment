#in SJF, we have to assume that all processes enter at same time. i.e. 0. As mentioned in slides as well.
arr = []
wtotal=0
temp=0
n = int(raw_input('Enter the total no of processes: '))
wt=[0]*n
for i in xrange(n):
    arr.append([])
    arr[i].append(int(raw_input('Enter burst time of process '+repr(i+1)+': ')))
    arr[i].append(i+1)
arr.sort(key = lambda arr:arr[0])
j=0
for i in xrange(n):
	wt[i]=wt[i]+wtotal
	wtotal+=arr[i][0]
print 'ProcessNumber\tBurstTime\tWaiting Time'
for i in xrange(n):
    print str(arr[i][1]), '\t\t', str(arr[i][0]), '\t\t', str(wt[i])
    
print 'Total waiting time: ',wtotal
print 'Average waiting time: ',(wtotal/n)
