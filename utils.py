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
  u = []
  for i in range(256):
    key = ''.join([str(hex(i))[2:] for j in range(len(hexstr))]).encode("ascii")
    u.append(binascii.unhexlify(xor_hexstr(hexstr, key)))
  return u
    
def calc_lett_ratio(binstr):
  '''Takes hex string - returns letter||whitespace to non letter||withespace ratio'''
  check = string.ascii_letters + ' '
  lettstr = ''.join([chr(c) for c in binstr if chr(c) in check])
  return len(lettstr)/len(binstr)
    
