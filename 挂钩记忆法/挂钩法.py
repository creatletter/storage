import random
f = open ("memory.txt")
number = []
hint = []
for line in f:
	elemen = line.split()
	number.append(elemen[0])
	hint.append(elemen[1])
	
nhdic = {}#dictionary for number to hint
hndic = {}#dictionary for hint to number

for i in range (len(number)):
	nhdic[number[i]] = hint[i]
	hndic[hint[i]] = number[i]

print ("输入q退出")


	
	
							
def num_hint():
	wrong = []#wrong要放在外面，不然每次都会重置
	num = []
	num1 = [] #已答对的就不再答
	count = [n for n in range(0,len(number),1)]
	while count:
		i = random.randrange (0,len(number))#randint右边也是开的，在后面就会报错；但randrange右边是闭的，就不会报错
		num.append(i)
		answer = nhdic[number[i]]#input(f"{number[i]} 对应的是：\t ")
		if num == count:
			print ("你已经答完了1-100，请输入wrong或者Wrong来进入错题集")
		elif i in num1:
			pass
		else:
			if answer == nhdic[number[i]]:
				print (f"{number[i]} 对应的是：\t{nhdic[number[i]]} ")
				num.append(i)
				num1.append(i)
				print (num)
				continue
			elif answer == "q" or answer == 'Q':
				break
						
			elif answer == 'w' or answer == 'W':
				answer_wrong = True
				while answer_wrong:
					try:
						print(wrong)
						m = random.choice(wrong)
						answer_wrong = input(f"{number[m]}对应的是：\t")
									
						if answer_wrong == nhdic[number[m]]:
							wrong.remove(m)
						elif answer == "q" or answer == 'Q':
							answer_wrong = False
						else:
							print (f"{number[m]} ： {nhdic[number[m]]}")
							continue
					except IndexError:
						print("错误的答案已经复习完了")
						answer_wrong = False
			else:
				print (f"{number[i]} ： {nhdic[number[i]]}")
				wrong.append(i)
				print(wrong)
							
			
def hint_num():
	
	while True:
		i = random.randrange (0,len(number))
		answer = input(f"{hint[i]} 对应的是：\t ")
		if answer == hndic[hint[i]]:
						continue
		elif answer == "q" or answer == 'Q':
			break
		else:
			print (f"{hint[i]} ： {hndic[hint[i]]}")
			
		
	
train = input("练习什么？数字对提示输入nh,提示对数字输入hn,学习输入learn,随机测验输入random\n")
if train == "nh":
	num_hint()
elif train == "hn":
	hint_num()
elif train == "learn":
	for i in range (len(number)):
		print (f"{number[i]} : {hint[i]}")
elif train == "random":
	length = input("你想记多长的东西？输入正整数\n")
	number_string = ''
	hint_string = ''
	for i in range (int(length)):
		num = int(random.randrange(0,len(number)))
		number_string += number[num]
		hint_string += " "+nhdic[number[num]]
	print (number_string)
	quiry = input("需要答案吗？Y/N\n")
	if quiry == "Y" or quiry == 'y':
		print(hint_string)
		
		
else:
	print ("输入错误")
	
