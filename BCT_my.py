sbox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
inv_sbox = [5, 14, 15, 8, 12, 1, 2, 13, 11, 4, 6, 3, 0, 7, 9, 10]

bct = [[0 for i in range(16)] for i in range(16)]

  # for del1 in range(16):
  #         for del0 in range(16):
  #                 for x in range(16):
  #                         bct_val = Invsbox[sbox[x] ^ del0] ^ Invsbox[sbox[x ^ del1] ^ del0]
  #                         if bct_val == del1:
  #                                 bct_table[del1][del0] += 1





def get_val_bct(x,d0,d1):
    return inv_sbox[sbox[x] ^ d0] ^ inv_sbox[sbox[x ^ d1] ^ d0]



def do_assignment(d1,d0):
    bct[d1][d0]+=1

[[[ do_assignment(d1,d0)  for x in range(16) if get_val_bct(x,d0,d1) == d1] for d0 in range(16)] for d1 in range(16)]

for i in bct:
	print(i)


