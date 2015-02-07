import binascii
import base64
import math

eng_freqs = { 'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015,
          'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
          'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074 }

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
    #discard strings that containunprintable characters or don't cointain spaces
    if not (all([i >= 32 and i < 127 for i in binstr]) and 32 in binstr): return {} 
    freqs = {}
    procstr = ''.join([chr(l).lower() for l in binstr if chr(l) in string.ascii_letters])
    n = len(procstr)
    for i in procstr:
        if i not in freqs: freqs[i] = procstr.count(i)/n*100
    freqs["*"] = len(procstr)/len(binstr)*100 #ascii letters to non-ascii letters ratio
    return freqs
  
def process_freqs(freqs): #work in progress
    '''Process frequency dictionaries - calculate some indicators [?]'''
    if not freqs: return 0 #check needed?
    devs = []    
    for i in freqs:
        if i=="*": continue
        curr = freqs[i]
        eng = eng_freqs[i]
        dev = abs(curr-eng)
        devs.append(dev)
        variance = sum([d**2 for d in devs])/len(devs)
     ...
    
