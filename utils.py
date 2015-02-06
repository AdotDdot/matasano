import binascii
import base64

def hex2base64(hexstr):
  '''Takes hex string - returns base64 encoded binary string'''
  return base64.b64encode(binascii.unhexlify(hexstr))
  
def xor_hexstr(hexstr1, hexstr2):
  '''Takes 2 hex strings and XORs them - returns hex string'''
  return ''.join(["%02x"%(x[0]^x[1]) for x in zip(binascii.unhexlify(hexstr1), binascii.unhexlify(hexstr2))])
