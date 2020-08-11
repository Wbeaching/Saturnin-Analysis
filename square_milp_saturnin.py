def objective_function(r  = 1):
    number_active_sboxs = r*16
    print("Minimize")
    for i in range(number_active_sboxs):
        if i == number_active_sboxs-1:
            print(f"x_{i}",end=" ")
        else:
            print(f"x_{i} +", end = " ")



def perm_layer_transpose(state):
    new_state = [0 for x in range(16)]
    
    for i in range(16):
        x = int(i/4)
        y = i%4
        
        y_dash = x
        x_dash = y
        
        new_index = x_dash*4 + y_dash
        new_state[new_index] = state[i]
    return new_state

def linear_layer_milp(num_rounds =2):
# Intial State
    init_state  = [f'x_{j}' for j in range(64) ]
    for i in range(num_rounds):
        
        #Subs Layer -- No Change
        #print(f"ROUND NUMBER {i}")
        # Shift Row
       
        # Linear Layer
        curr_ll = [f"x_{(i+1)*16 + j}" for j in range(16)]
    #         print("SR_STATE,", sr_state)
    #         print("LL_LAYER,", curr_ll)
    #         if (i-1)%2==0
    #             init_state = curr_ll
        if i>=1:
            init_state = sr_state
        for column in range(4):
            a = column*4
            b = column*4+1
            c = column*4+2
            d = column*4+3
            col_index = [a,b,c,d]
            for elem in range(4):
                print(f"{init_state[col_index[elem]]} ",end =" ")
                print(" + ",end=" ")
                print(f"{curr_ll[col_index[elem]]} ",end =" ")
                if elem != 3:
                    print(" + ",end = " ")
            # Dummy Variables


            print(f"- {BN} d{i*4+column} >= 0")
            for elem in range(4):
                print(f" d{i*4+column}  - {init_state[col_index[elem]]} >= 0")
                print(f" d{i*4+column}  - {curr_ll[col_index[elem]]} >= 0")
        sr_state = perm_layer_transpose(curr_ll)


print("\n\n")                 


BN = 5

def setting_type(num_rounds =2):
    print("\n\n")
    print("Binary")
    num_active_sboxs = (num_rounds+1)*16
    for i in range(num_active_sboxs):
        print(f"x_{i}")
    for column in range((num_rounds)*4):
        print(f"d{column}")
    print("End")


def atleast_one_active(r):
    number_active_sboxs = r*16
    for i in range(number_active_sboxs):
        if i == number_active_sboxs-1:
            print(f"x_{i}",end=" ")
        else:
            print(f"x_{i} +", end = " ")
    print(" >= 1 ")


BN = 5

if __name__ =="__main__":

    ROUNDS =12

    objective_function(ROUNDS)
    print("\n\nSubject To")
    linear_layer_milp(ROUNDS)
    atleast_one_active(ROUNDS)
    setting_type(ROUNDS)
