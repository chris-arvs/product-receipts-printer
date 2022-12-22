input_list = [1,2,3,4]#users choice

def choice_1(fname,dc):
	f1 = False 
	nosynolo = 1
	sumrec = 0 #to check sum of recites
	count = 0 #if its 1 then it will check for AFM 
	error = [] #keeps record for products and prices so in case of an error to remove the error
	stuff = [] #extracts from the file the name and the prices 
	for line in fname:
		l = line.split() #splits every line of the input file
		f2 = str(l[0])
		if f2[-1:] != '-': #if its not the end of recite
			count += 1
			if f1 == False: #if an error occured it will be true
				try:
					l_up = l[0].upper()
					if count == 1 and l[0] != 'ΑΦΜ:':
						raise Exception
					if l_up == 'ΑΦΜ:':
						int(l[1])
						if len(l[1]) != 10:
							raise Exception#AFM needs to be an int with 10 digits
						afm = str(l[1])#AFM -> from int to str 
						if afm not in dc:
							dc.update({afm:[]})	#update dictionary			
					elif l_up == 'ΣΥΝΟΛΟ:':
						sumrec=round(sumrec,2)#round the second decimal digit
						if sumrec != float(l[1]):
							raise Exception
					else:
						name = str(l[0])
						name = name.replace(':','')
						name = name.upper()
						amount = int(l[1])
						cost = float(l[2])
						total_cost = float(l[3])
						if total_cost != cost*amount:
							raise Exception
						sumrec += cost*amount
						error = error + [name,total_cost]#a list to keep record of products so in case of mistake to remove it
						onoma kai synoliko kostos.Einai lista me ola ta proionta kai to kostos tous gia kathe afm
						stuff = [name,total_cost]
						#dictionary key is afm and values is a list of product names and its price
						tmp = dc.get(afm)
						if stuff[0] in tmp:#check if product is in list
							pos = tmp.index(stuff[0])#keep the position of it
							tmp[pos+1] = tmp[pos+1] + stuff[1]#add products cost in total cost
							dc[afm] = tmp
						else:
							stuff = tmp + stuff
							dc[afm] = stuff
				except:
					f1 = True
					if count>1:#if afm is on the list
						checkafm = dc.get(afm)#compare value(name,total cost) with afm that error occured
						for i in error[::2]:#find the error in the list(product name)
							posit = checkafm.index(i)#i keeps the afm that error occured
							if i in checkafm:
								posi = error.index(i)#error keeps all of the AFM right and wrong
								checkafm[posit+1] = checkafm[posit+1]-error[posi+1]#remove from total price the error
								if checkafm[posit+1] == 0:#an einai 0 peta to
									del checkafm[posit+1]
									del checkafm[posit]
						dc[afm] = checkafm
						if dc.get(afm) == []:#if AFM is an empty list the pop it from dic
							dc.pop(afm)
		else:#in case of a new recite refresh counters
			sumrec = 0			
			f1 = False
			count = 0
			name = None
			amount = None
			cost = None
			total_cost = None
			stuff = None
			error = []
	return dc

def in_order(lst):
	for x in range(0,len(lst)-1,2):
		for y in range(0,len(lst)-1,2):
			if lst[y] > lst[x]:
				tmp1 = lst[x]
				tmp2 = lst[x+1]
				lst[x] = lst[y]
				lst[x+1] = lst[y+1]
				lst[y] = tmp1
				lst[y+1] = tmp2
	return lst

def print_lists(ls):
	for j in range(len(ls)):
		try:
			int(ls[j])
			print(ls[j])
		except:
			print(ls[j],end=' ')
	print()

def print_3_choise(afm,dc):
	tmpdc = dc.copy()
	if afm in tmpdc:
		ls = tmpdc.get(afm)
		print(afm)
		ls = in_order(ls)
		print_lists(ls)
#takes as argument the name of product and the dictionary(key afm:product name , cost)
def print_2_choice(stuff,dc):
	tmpdc = dc.copy()
	l = []#an empty list to keep afm and total cost
	for i in tmpdc:
		ls = tmpdc.get(i)
		if stuff in ls:
			l = l + [i,ls[ls.index(stuff)+1]]#i is the afm and stuff+1 is total price
	l = in_order(l)
	for j in range(0,len(l)-1,2):
		print(l[j],l[j+1]) #prints afm and total cost for the stuff given

def print_Menu():
	print('1:read new input file.......................')
	print('2:print statistics for a specific product...')
	print('3:print statistics for a specific AFM.......')
	print('4:Exit the program..........................')

#checks if its int
def check_input_value(local_input,x):
	while True:
		try:
			if x == 0:
				local_input = int(input("Give your preference:"))
			elif x == 1:
				x = 2
				local_input = int(local_input)
			else:
				x == 1
				local_input = int(input("Give your preference:"))
		except ValueError:
			print("Wrong type of input please try again...",end=' ')
		else:
			break
	return local_input

#check users choice(1,2,3,4)
def check_input_number(lc):
	while lc not in input_list:
		lc = input("Wrong input number please try again:")
		lc = check_input_value(lc,1)
	return lc

user_input = 0
y=0
dc={}
#main
while user_input != input_list[3]: #while not exit
	print_Menu()
	user_input = check_input_value(user_input,0) 
	user_input = check_input_number(user_input)

	if user_input == input_list[0]:
		y=1
		file = input("Enter the file's name:")
		if file[-4:] != '.txt':
			name_file = file + '.txt'
		else:
			name_file = file	
		try:
			f = open(name_file,'r',encoding='utf-8') 
			dc = choice_1(f,dc)
		except FileNotFoundError:
			print('\nNo such file with that name...')
		
	elif user_input == input_list[1]:
		stuff = str(input("Enter the name of the product:"))
		stuff = stuff.upper()
		print_2_choice(stuff,dc)
	elif user_input == input_list[2]:
		afm = str(input("Enter afm:"))
		print_3_choise(afm,dc)
	else:
		if y == 1:#if file not found
			f.close()
			print('File closed!!!')

	print()

print('Bye and thank you!!!')