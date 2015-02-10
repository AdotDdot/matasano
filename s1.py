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
  map_keys = {}
  for d in poss_decrypts:
    binstr = poss_decrypts[d]
    score = utils.calc_lett_ratio(binstr)
    if score > 0: 
      scores[score] = binstr
      map_keys[score] = d
  best_score = sorted(scores)[-1]
  text = scores[best_score]
  return {"text": text, "score": best_score, "key": map_keys[best_score]}
  #>>> b"Cooking MC's like a pound of bacon"
  
def ch4():
  '''Challenge 4 - Detect single-character XOR'''
  #Apply ch3 to all strings. Among the best-scoring lines of each 
  #string, return the one with the best score (text and line number)
  lines = open("4.txt").readlines()
  score_line = {}
  line_text = {}
  line = 0
  for l in lines:
      results = ch3(l.strip())
      text, score = results["text"], results["score"]
      score_line[score] = line
      line_text[line] = text
      line += 1
  best_score_line = score_line[sorted(score_line)[-1]]
  return line_text[best_score_line], best_score_line
  #>>> b'Now that the party is jumping\n', 170

def ch5():
  '''Challenge 5 - Implement repeating-key XOR'''
  pt = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
  k = "ICE"
  return utils.rep_key_xor(pt.encode("ascii"), k.encode("ascii"))
  #>>> b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f2044490c69242a69203728393c69342d2c2d6500632d2c22376922652a3a282b2229'
