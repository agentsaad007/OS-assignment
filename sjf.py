arr = []
bt=[]
wtotal=0
temp=0
n = int(raw_input('Enter the total no of processes: '))
ind=[0]*n
wt=[0]*n
for i in xrange(n):
    arr.append([])
    arr[i].append(raw_input('Enter arrival time of process '+repr(i+1)+': '))
    arr[i].append(int(raw_input('Enter burst time of process '+repr(i+1)+': ')))
    arr[i].append(i+1)
j=1
arr.sort(key = lambda arr:arr[1])
j=0
for j in xrange(n)
	temp=arr[j][0]	
	for i in xrange(n):
		if temp>arr[i][0] and arr[i]!=0
			ind.append(i)
			temp=arr[i][0]	
wt[ind]=arr[ind][1]
wtotal+=wt[ind]
arr[ind][0]=0
print 'ProcessNumber\tArrivalTime\tBurstTime\tWaiting Time'
for i in xrange(n):
    print str(arr[i][2]), '\t\t', str(arr[i][0]), '\t\t', str(arr[i][1]), '\t\t', str(wt[i])
    
print 'Total waiting time: ',wtotal
print 'Average waiting time: ',(wtotal/n)
