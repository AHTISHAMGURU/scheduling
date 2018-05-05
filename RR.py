num = int(input("ENTER NUMBER OF PROCESS: "))
time_slice = int(input("\nENTER TIME SLICE: "))
io_time = int(input("\nENTER I/O TIME IF NO I/O ENTER 0: "))
io_wait = int(input("ENTER I/O WAIT IF NO I/O ENTER 0: "))
ready ={}
old = {}
old_i = -1
new = {}
new_i = -1
trac = []
cpu_time = 0
min_arr = 1
total_proc =int(num)

#size_of_list = 2
for i in range(num):
	info=[]
	print("\nENTER ARRIVAL TIME OF PROCESS NO: ", int(i+1))
	arrival_time = int(input())
	info.append(int(arrival_time))

	print("ENTER BURST TIME OF PROCESS NO: " , int(i+1))
	burst_time = int(input())
	info.append(int(burst_time))
	ready[i+1] = info
	print(ready)

print("total proc ",total_proc )
for i in range(int(total_proc)):
	if(ready[min_arr][0] > ready[i+1][0]):
		min_arr = i+1

print(ready[min_arr][0])
cpu_time = ready[min_arr][0]
if(io_time == 0 and io_wait == 0):
	print(ready[min_arr][0])
	ready[min_arr][1] = ready[min_arr][1] - time_slice
	cpu_time = cpu_time + time_slice
	if(ready[min_arr][1] == 0):
		print("\nPROCESS HAVING ARRIVAL TIME " , ready[min_arr][0] , "TERMINATE AT " , cpu_time)
#		while min_arr < int(total_proc - 1)
#			c = min_arr + 1
#			delete = {}
#			delete[0] = ready[min_arr]
#			ready[min_arr] = ready[c]
#			ready[c] = delete[0]
		del ready[min_arr]
		total_proc = total_proc - 1
	else:
		old[old_i+1] = ready[min_arr]
		old_i = old_i + 1
		print("\nPROCESS HAVING ARRIVAL TIME " , ready[min_arr][0] , " GOES TO LAST AT " , cpu_time)
		del ready[min_arr]
		total_proc = total_proc - 1

	while total_proc>0:
		for i in range(int(total_proc)):
			if(ready[i][0] <= cpu_time):
				new[new_i+1] = ready[i+1]
				new_i = new_i + 1
				trac.append(i+1)
		if(new_i > -1):
			track = 0
			min_arr = 0
			for i in range(int(new_i+1)):
				if(new[min_arr][0] > new[i][0]):
					min_arr = i
					track = trac[i]
			del ready[track]
			total_proc = total_proc - 1
			new[min_arr][1] = new[min_arr][1] - time_slice
			cpu_time = cpu_time + time_slice
			if(new[min_arr][1] > 0):
				old[old_i+1] = new[min_arr]
				old_i = old_i + 1
				print("\nPROCESS HAVINNG ARRIVAL TIME ", new[min_arr][0] , " GOES TO LAST AT " , cpu_time)
			else:
				print("\nPROCESS HAVING ARRIVAL TIME " , new[min_arr][0] , " TERMINATED AT " , cpu_time)
			new = {}

		if(new_i == -1):
			if(old_i > -1):
				old[0][1] = old[0][1] - time_slice
				cpu_time = cpu_time + time_slice
				if(old[0][1] > 0):
					print("\nPROCESS HAVING ARRIVAL TIME " , old[0][0] , " GOES AGAIN TO LAST AT " , cpu_time)
					new[0] = old[0]
					del old[0]
					old_i = old_i - 1
					old[old_i+1] = new[0]
					old_i = old_i + 1
				else:
					print("PROCESS HAVING ARRIVAL TIME " , old[0][0] , " TERMINATED AT " , cpu_time )
					del old[0]
					old_i = old_i - 1
			else:
				cpu_time = cpu_time + 1
	while(old_i > -1):
		old[0][1] = old[0][1] - time_slice
		cpu_time = cpu_time + time_slice
		if(old[0][1] > 0):
			print("PROCESS HAVIN ARRIVAL TIME " , old[0][0] , " AGAIN GOES TO LAST AT " , cpu_time)
			new[0] = old[0]
			del old[0]
			old_i = old_i - 1
			old[old_i+1] = new[0]
			old_i = old_i + 1
		else:
			print("PROCESS HAVING TIME ARRIVAL TIME " , old[0][0] , " TERMINATED AT " , cpu_time)
			del old[0]
			old_i = old_i - 1
			new = {}
