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

while num > 0:
	min_arrival_time=0 #min_arrival_time
	for i in range(num):
		if(arrival[min_arrival_time] >= arrival[i]):
			min_arrival_time=i

	burst_time = burst[min_arrival_time] #getting burst time
	wait_time = cpu_time - arrival[min_arrival_time] #calculating wait
	wait.append(int(wait_time))

	for i in range(burst_time):
		cpu_time = cpu_time + 1

	print("process no ", int(min_arrival_time) , " terminates at " , int(cpu_time))
	print("WAIT TIME OF PROCESS NO " , int(min_arrival_time) , " is ",int(wait_time))
	proc_arr_to_rm = arrival[min_arrival_time]
	arrival.remove(proc_arr_to_rm)
	burst.remove(burst_time)
	num = num - 1

w_sum = 0 #sum of all waits
count_proc = w_num #number of process
for i in range(w_num):
	w_sum = int(w_sum) + int(wait[i])
avg_w8_time = int(w_sum) / int(count_proc) #average wait time
print("AVERAGE WAIT TIME IS " , int(avg_w8_time))
