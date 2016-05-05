arr = []
wt=[]
wtotal=0
temp=k=ind=c=0;
n = int(raw_input('Enter the total no of processes: '))
wt=[0]*n
for i in xrange(n):
    arr.append([])
    arr[i].append(raw_input('Enter arrival time of process '+repr(i+1)+': '))
    arr[i].append(int(raw_input('Enter burst time of process '+repr(i+1)+': ')))
    arr[i].append(i+1)
    arr[i].append(0)
arr.sort(key = lambda arr:arr[0])
i=0
while i<n and c != n:
	if arr[i][3] != -1:
		temp=arr[i][1]
		k=arr[i][0]
		j=0
		ind=i
		for j in xrange(n):
			if temp>arr[j][1] and arr[j][0]==k and arr[j][3] != -1:				
				temp=arr[j][1]
				ind=j
		wt[ind]=wtotal		
		wtotal=wtotal+arr[ind][1]
		arr[ind][3]=-1
		if ind==i:
			i+=1
		n+=1	
print 'ProcessNumber\tArrivalTime\tBurstTime\tWaiting Time'
for i in xrange(n):
    print str(arr[i][2]), '\t\t', str(arr[i][0]), '\t\t', str(arr[i][1]), '\t\t', str(wt[i])
    
print 'Total waiting time: ',wtotal
print 'Average waiting time: ',(wtotal/n)
