arrival = []			#list of arrival
burst = []			#list of brust
wait = []			#list of waiting time of every process
cpu_time = 0
num = int(input("ENTER THE NUMBER OF PROCESSORS ")) #num for number of processorss
w_num = num


for i in range(num):
	arrival_time = int(input("ENTER THE ARRIVAL TIME ")) #arrival_time
	burst_time = int(input("ENTER THE BURST TIME ")) #brust_time
	arrival.append(arrival_time)
	burst.append(burst_time)

min_arrival_time=0 #min_arrival_time
min_burst_time = -1
for i in range(num):
#	print(min_arrival_time)
#	print(min_burst_time)
	if(arrival[min_arrival_time] >= arrival[i]):
		min_arrival_time=i

min_burst_time = -1
cpu_time = arrival[min_arrival_time]
while num > 0:
	dic = {}
#	print(min_arrival_time)
#	print(min_burst_time)
	if(min_burst_time == -1):
		burst_time = burst[min_arrival_time] #getting burst time
	if(min_burst_time != -1):
		burst_time = burst[min_burst_time]

	for i in range(burst_time):
		cpu_time = cpu_time + 1

#	print(min_arrival_time)
#	print(min_burst_time)

	if(min_burst_time>-1):
                print("process having arrival time ", int(arrival[min_burst_time]) , " terminate at " , cpu_time)
                proc_arr_to_rm = arrival[min_burst_time]
                arrival.remove(proc_arr_to_rm)
                burst.remove(burst_time)
                num = num - 1

	if(min_burst_time == -1):
                print("process having arrival time ", int(arrival[min_arrival_time]) , " terminate at " , cpu_time)
                proc_arr_to_rm = arrival[min_arrival_time]
                arrival.remove(proc_arr_to_rm)
                burst.remove(burst_time)
                num = num - 1

#	print(min_arrival_time)
#	print(min_burst_time)


	n=0
	for i in range(int(num)):
#		print(min_arrival_time)
#		print(min_burst_time)

		if(arrival[i] < cpu_time):
			dic[n] = i
			n = int(n+1)
#	print(n)
	if(n>0):
		min_burst_time=dic[0] #min_burst_time
		for j in range(int(n)):
			num2 = dic[j]
			if(burst[min_burst_time] >= burst[num2]):
                        	min_burst_time=j
#		print("check" , int(min_burst_time))
	if(n==0):
		min_arrival_time=0 #min_arrival_time
		for i in range(num):
        		if(arrival[min_arrival_time] >= arrival[i]):
                		min_arrival_time=i

#	print(min_arrival_time)
#	print(min_burst_time)

