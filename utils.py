import binascii
import base64
import string

def hex2base64(hexstr):
  '''Takes hex string - returns base64 encoded binary string'''
  return base64.b64encode(binascii.unhexlify(hexstr))
  
def xor_hexstr(hexstr1, hexstr2):
  '''Takes 2 hex strings and XORs them - returns hex binary string'''
  return ''.join(["%02x"%(x[0]^x[1]) for x in zip(binascii.unhexlify(hexstr1), binascii.unhexlify(hexstr2))]).encode("ascii")
  
def bruteforce_single_char(hexstr):
  '''Takes hex string - XORs it with all printable characters incl. extended ascii- returns all possible decryptions'''
  u = {}
  for i in range(256):
    key = ''.join([str(hex(i))[2:] for j in range(len(hexstr))]).encode("ascii")
    u[chr(i)] = binascii.unhexlify(xor_hexstr(hexstr, key))
  return u
    
def calc_lett_ratio(binstr):
  '''Takes hex string - returns letter||whitespace to non letter||withespace ratio'''
  check = string.ascii_letters + ' '
  lettstr = ''.join([chr(c) for c in binstr if chr(c) in check])
  return len(lettstr)/len(binstr)
  
def rep_key_xor(binpt, binkey):
  '''Takes 2 binary strings (plaintext and key) - returns hex binary string'''
  exp_key = binkey * int(len(binpt)/len(binkey)) +  binkey[:len(binpt)%len(binkey)]
  return xor_hexstr(binascii.hexlify(binpt), binascii.hexlify(exp_key))
  
def hamming_distance(binstr1, binstr2):
  '''Takes 2 binary strings - returns hamming distance'''
  hd = 0
  for z in zip(binstr1, binstr2):
    hd += bin(z[0]^z[1]).count("1")
  return hd
  # hamming_distance(b'this is a test', b'wokka wokka!!!')
  #>>> 37
  
def find_ksizes(binstr):
  '''Takes binary string - returns 5 most likely key sizes'''
  dists = {}
  for k in range(2, 41):
    m = sum( [ hamming_distance(binstr[:n*k], binstr[n*k:2*n*k]) for n in range(1, 11)] )//10
    dists[k] = m
  return [v[1] for v in sorted(dists.items(), key=operator.itemgetter(1))[:5]]

def split_blocks(binstr, k):
  '''Takes hex string - returns blocks of length k'''
  blocks = []
  while binstr:
    block, binstr = binstr[:k], binstr[k:]
    blocks.append(block)
  return blocks

def transpose_blocks(blocks):
  '''Takes blocks of binary strings - returns transposed blocks'''
  newblocks = []
  for i in range(len(blocks[0])):
    newblock = []
    for block in blocks:
      try: newblock.append(block[i])
      except IndexError: continue
      newblocks.append(''.join(["%c"%n for n in newblock]).encode("ascii"))
  return newblocks
    
