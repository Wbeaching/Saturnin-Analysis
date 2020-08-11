sbox_1 = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
inv_sbox_1 = [5, 14, 15, 8, 12, 1, 2, 13, 11, 4, 6, 3, 0, 7, 9, 10]

bdt = {}

for j in range(16):
	bdt[j] = [[0 for i in range(16)] for i in range(16)]
def get_c_d0(x,d0,invd0):
    return inv_sbox_1[sbox_1[x] ^ invd0] ^ inv_sbox_1[sbox_1[x ^ d0] ^ invd0]

def get_c_d1(x,d0):
    return  sbox_1[x] ^ sbox_1[x ^ d0]

def do_assignment(d1,d0,invd0):
    bdt[d1][d0][invd0] += 1



[[[[do_assignment(d1,d0,invd0) for x in range(16) if get_c_d0(x,d0,invd0) == d0 and get_c_d1(x,d0) == d1] for invd0 in range(16)] for d0 in range(16)] for d1 in range(16)]





for i in bdt:
    print("*"*25, f" d1 = {i}", "*"*25)
    for i in bdt[i]:
        print(i)
    print("\n")
