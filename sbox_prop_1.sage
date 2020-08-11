from sage.crypto.sbox import SBox


def get_ddt(sbox):
    return sbox.difference_distribution_table()


def max_probability_of_diff(ddt):
    return max(max(ddt[1:,1:]))/2**4
    

def find_num_of_value(ddt,value):
    count=0
    for x in ddt:
        for y in x:
            if y == value:
                count+=1
                
    return count

def find_max_abs_bias_inLAT(lat):
    max_ =0
    for x in lat[1:,1:]:
        for y in x:
            if abs(y) >max_:
                max_ =abs(y)
    return max_



def return_component_function(sbox):
    count =0
    for i in range(16):
        f = sbox.component_function(i).algebraic_normal_form()
        print(str(f))
        f_string = str(f)
        f_list = f_string.split('+')
        f_list = [ s.replace(" ","") for s in f_list]
        f_list = [s.replace("*",'') for s in f_list]
        max_ = max(map(len,f_list))
        print(" Boolean function has degree: ",int(max_/2))
        if max_/2 ==3:
            count+=1
    print("Total Non Zero Component Functions with degree 3: ",count)



def num_abs_values_lat(sbox,value=1/4):
    lat = sbox.linear_approximation_table(scale="bias")
    count =0
    for x in lat:
        for y in x:
            if abs(y) == value:
                count+=1
    return count


def properties(s):
    print("SBOX",s)
    ddt_s = s.difference_distribution_table()
    max_prob_diff = max_probability_of_diff(ddt_s)
    print("Maximum Probability of a differential is: ",max_prob_diff )
    print("Number of differentials with probability 1/4: ",find_num_of_value(s.difference_distribution_table(),4))
    mx_abs_bias = find_max_abs_bias_inLAT(s.linear_approximation_table())/2**4
    print("Maximum Absolute Bias for Sbox: ",mx_abs_bias)
    print("Number of values with absolute bias 1/4: ", num_abs_values_lat(s,0.25))
    print("Component Functions")
    return_component_function(s)
    print("\n\n\n")



def get_1_1_ddt(s):
	ddt = get_ddt(s)
	answer = [[0 for x in range(4)] for j in range(4)]
	list_ = [1,2,4,8]
	for i in range(4):
		for  j in range(4):
			if ddt[list_[i]][list_[j]] !=0:
				answer[i][j] =ddt[list_[i]][list_[j]]
	print("    1 2 4 8")
	for i in range(4):
		print(2**i,":", end=' ') 
		for  j in range(4):
			print(answer[i][j],end=" ")
		print("\n")

def get_1_1_lat(s):
	lat = s.linear_approximation_table(scale="bias")
	answer = [[0 for x in range(4)] for j in range(4)]
	list_ = [1,2,4,8]
	for i in range(4):
		for  j in range(4):
			if lat[list_[i]][list_[j]] !=0:
				answer[i][j] =lat[list_[i]][list_[j]]
	print("    1   2   4   8")
	for i in range(4):
		print(2**i,":", end=' ') 
		for  j in range(4):
			print(answer[i][j],end=" ")
		print("\n")

			

if __name__ == "__main__":
	#s1 = SBox(0,1,2,13,4,7,15,6,8,12,9,11,10,14,5,3)
	s0 = SBox(0,6,14,1,15,4,7,13,9,8,12,5,2,10,3,11)
	s1 = SBox(0,9,13,2,15,1,11,7,6,4,5,3,8,12,10,14)


	print("Properties SBOX 0")

	properties(s0)
	print("1-1 DDT")
	get_1_1_ddt(s0)
	print("1-1 LAT")
	get_1_1_lat(s0)
	
	print("Properties SBOX 1")

	properties(s1)
	print("1-1 DDT")
	get_1_1_ddt(s1)
	print("1-1 LAT")
	get_1_1_lat(s1)
