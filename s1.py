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
  #>>>b'746865206b696420646f6e277420706c6179' 
  #unhexlified b"the kid don't play"
