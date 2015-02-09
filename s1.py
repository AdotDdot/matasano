import utils

def ch1():
  '''Challenge 1 - Convert hex to base64'''
  s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
  return utils.hex2base64(s)
  #>>> b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
  
def ch2():
  '''Challenge 2 - Fixed XOR'''
  #"Write a function that takes two equal-length buffers and produces their XOR combination"
  s1 = "1c0111001f010100061a024b53535009181c"
  s2 = "686974207468652062756c6c277320657965"
  return utils.xor_hexstr(s1, s2)
  #>>> b'746865206b696420646f6e277420706c6179' 
  #unhexlified b"the kid don't play"
  
def ch3(s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"):
  '''Challenge 3 - Single-byte XOR cipher'''
  #Among all possible decryptions, choose the one with the best score
  poss_decrypts = utils.bruteforce_single_char(s)
  scores = {}
  for binstr in poss_decrypts:
    score = utils.calc_lett_ratio(binstr)
    if score > 0: scores[score] = binstr
  best_score = sorted(scores)[-1]
  text = scores[best_score]
  return (text, best_score)
  #>>> b"Cooking MC's like a pound of bacon"
  
def ch4():
  '''Detect single-character XOR'''
  #Apply ch3 to all strings. Among the best-scoring lines of each 
  #string, return the one with the best score (text and line number)
  lines = open("4.txt").readlines()
  score_line = {}
  line_text = {}
  line = 0
  for l in lines:
      text, score = ch3(l.strip())
      score_line[score] = line
      line_text[line] = text
      line += 1
  best_score_line = score_line[sorted(score_line)[-1]]
  return line_text[best_score_line], best_score_line
  #>>> b'Now that the party is jumping\n', 170

