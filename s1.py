import utils

def ch1():
  '''Challenge 1 - Convert hex to base64'''
  s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
  return utils.hex2base64(s)
  #>>> b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
  
def ch2():
  '''Challenge 2 - Fixed XOR
  Write a function that takes two equal-length buffers and produces their XOR combination'''
  s1 = "1c0111001f010100061a024b53535009181c"
  s2 = "686974207468652062756c6c277320657965"
  return utils.xor_hexstr(s1, s2)
  #>>> b'746865206b696420646f6e277420706c6179' 
  #unhexlified b"the kid don't play"
  
def ch3():
  '''Single-byte XOR cipher''''
  #Among all possible decrypted strings, returns the one that has all printable characters, contains 
  #at least one space and has the least variance from English letter frequency
  s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
  poss_decrypts = utils.bruteforce_single_char(s)
  variances = {}
  for d in poss_decrypts:
    variance = utils.process_freq(utils2.calc_freq_distr(poss_decrypts[d]))
    if variance >= 0: variances[variance] = poss_decrypts[d]
  return variances[sorted(variances)[0]]
  #>>> b"Cooking MC's like a pound of bacon"
