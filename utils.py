import binascii
import base64
import math

def hex2base64(hexstr):
  '''Takes hex string - returns base64 encoded binary string'''
  return base64.b64encode(binascii.unhexlify(hexstr))
  
def xor_hexstr(hexstr1, hexstr2):
  '''Takes 2 hex strings and XORs them - returns hex binary string'''
  return ''.join(["%02x"%(x[0]^x[1]) for x in zip(binascii.unhexlify(hexstr1), binascii.unhexlify(hexstr2))]).encode("ascii")
  
def bruteforce_single_char(hexstr):
    '''Takes hex string - XORs it with all printable characters - returns dict char:plain-text-binary-string'''
    u = {}
    for i in range(32, 127):
        key = binascii.hexlify((chr(i)*len(hexstr)).encode("ascii"))
        u[chr(i)] = binascii.unhexlify(xor_hexstr(hexstr, k))
    return u
    
def calc_freq_distr(binstr):
    '''Takes binary string - returns dict letter:freq-percent'''
    freqs = {}
    procstr = ''.join([chr(l).lower() for l in binstr if chr(l) in string.ascii_letters])
    n = len(procstr)
    for i in procstr:
        if i not in freqs: freqs[i] = procstr.count(i)/n*100
    freqs["*"] = len(procstr)/len(binstr)*100 #ascii letters to non-ascii letters ratio
    return freqs
  
def process_freqs(freqs): #work in progress
  '''Process frequency dictionaries - calculate some indicators [?]'''
    devs = []    
    for i in freqs:
        if i=="*": continue
        curr = freqs[i]
        eng = eng_freqs[i]
        dev = abs(curr-eng)
        devs.append(dev)
    try:
        #some possible indicators
        mean_dev = sum(devs)/len(devs)
        mean_square_dev = sum([d**2 for d in devs])/len(devs)
        mean_square_root_dev = math.sqrt(mean_square_dev)
    except ZeroDivisionError:
        continue
    ...
    
