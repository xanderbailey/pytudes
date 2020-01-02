import csv

def split_progs(data,n=4):
	codes = [data[i:i + n] for i in range(0, len(data), n)] 
	return codes

def compute(i, total,n=4):
	prog = split_progs(total,n)[i]
	flag = 0
	if prog[0] == 1:
		total[prog[3]] = total[prog[1]] + total[prog[2]]
	elif prog[0] == 2:
		total[prog[3]] = total[prog[1]] * total[prog[2]]
	elif prog[0] == 99:
		flag = 99
	return total, flag


with open('ex2.csv' ,'r') as f:
	data = [line for line in csv.reader(f)]

flag = 0
n=4
total = [int(d) for d in data[0]]

def run_int_prog(noun,verb,memory):
	memory = list(memory)
	memory[1] = noun 
	memory[2] = verb	 

	for i in range(len(memory)//4):
		memory, flag  =	compute(i,memory)
		if flag == 99:
#			print("flag reached")
			break
	return memory[0]

output = run_int_prog(12,2,tuple(total))
print()
print(output)

print(total)
for verb in range(100):
	for noun in range(100):
		output = run_int_prog(noun,verb,tuple(total))
		if output == 19690720:
			print(f"verb: {verb}, noun: {noun}")
