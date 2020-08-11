



BN = 5
def objective_function(r  = 2):
    number_active_sboxs = r*64
    print("Minimize")
    for i in range(number_active_sboxs):
        if i == number_active_sboxs-1:
            print(f"x_{i}",end=" ")
        else:
            print(f"x_{i} +", end = " ")


def linear_layer(num_rounds =2):
    # Intial State
    init_state  = [f'x_{j}' for j in range(64) ]
    for i in range(num_rounds):

        #Subs Layer -- No Change
        #print(f"ROUND NUMBER {i}")
        # Shift Row
        sr_state = perm_layer(init_state,r =i)
        # Linear Layer
        curr_ll = [f"x_{(i+1)*64 + j}" for j in range(64)]
#         print("SR_STATE,", sr_state)
#         print("LL_LAYER,", curr_ll)
        init_state = curr_ll
        for column in range(16):
            a = column*4
            b = column*4+1
            c = column*4+2
            d = column*4+3
            col_index = [a,b,c,d]
            for elem in range(4):
                print(f"{sr_state[col_index[elem]]} ",end =" ")
                print(" + ",end=" ")
                print(f"{curr_ll[col_index[elem]]} ",end =" ")
                if elem != 3:
                    print(" + ",end = " ")
            # Dummy Variables


            print(f"- {BN} d{i*16+column} >= 0")
            for elem in range(4):
                print(f" d{i*16+column}  - {sr_state[col_index[elem]]} >= 0")
                print(f" d{i*16+column}  - {curr_ll[col_index[elem]]} >= 0")

    print("\n\n")


def setting_type(num_rounds =1):
    print("\n\n")
    print("Binary")
    num_active_sboxs = (num_rounds+1)*64
    for i in range(num_active_sboxs):
        print(f"x_{i}")
    for column in range((num_rounds)*16):
        print(f"d{column}")
    print("End")

def perm_layer(state,r=1):
    new_state = [0 for i in range(64)]
    if r%4 == 1:
        for i in range(64):
            z = int(i/16)
            x = int(i/4) % 4
            y = int(i%4)

            x_dash = (x+y)%4
            y_dash = y
            z_dash = z

            new_index = z_dash*16 + x_dash*4 +y_dash

            new_state[new_index] = state[i]
    if r%4 == 3:
        for i in range(64):
            z = int(i/16)
            x = int(i/4) % 4
            y = int(i%4)

            x_dash = x
            y_dash = y
            z_dash = (y+z)%4

            new_index = z_dash*16 + x_dash*4 +y_dash

            new_state[new_index] = state[i]
    if r%2 ==0:
        new_state = [state[index] for index in range(64)]

    return new_state

def atleast_one_active(r):
    number_active_sboxs = r*64
    for i in range(number_active_sboxs):
        if i == number_active_sboxs-1:
            print(f"x_{i}",end=" ")
        else:
            print(f"x_{i} +", end = " ")
    print(" >= 1 ")

if __name__ == "__main__":
    ROUNDS =2
    objective_function(ROUNDS)
    print("\n\nSubject To")
    linear_layer(ROUNDS)
    atleast_one_active(ROUNDS)
    setting_type(ROUNDS)



