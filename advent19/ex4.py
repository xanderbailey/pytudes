lower = 152085
upper = 670283
delta = upper - lower 


all_passwords = [str(i) for i in range(lower, upper + 1)] 
#find all that contain a double
tests = ["11","22","33","44","55","66","77","88","99","00"]

all_with_double = [p for p in all_passwords if any(test in p for test in tests)]

#make numbers increase
all_with_increase = []
for p in all_with_double:
	if (p[0] <= p[1]) and (p[1] <= p[2]) and (p[2] <= p[3]) and p[3] <= p[4] and p[4] <= p[5]: 
		all_with_increase.append(p)

trythis = [([test for test in tests if test[0] != str(i)],[f"{i}"*j for j in range(3,7)]) for i in range(1,10)]

bad_passes = []
for k in range(9):
	all_with_double_only = [p for p in all_with_increase if not any(test in p for test in trythis[k][0]) and any(test in p for test in trythis[k][1])]
	bad_passes.extend(all_with_double_only)
	#print(all_with_double_only)
fin_passes = [p for p in all_with_increase if p not in bad_passes]

moretests = [(f"{i}"*3,f"{j}"*3) for j in range(10) for i in range(10) if i !=j]
remove_these_too = []
for k in moretests:
	for p in fin_passes:
		if k[0] in p and k[1] in p:
			remove_these_too.append(p)
fin_passes2 = [p for p in fin_passes if p not in remove_these_too]
print(len(fin_passes2))

