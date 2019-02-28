def main():
  profile_1 = {
    "A": [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    "C": [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    "G": [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    "T": [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
  }

  profile_2 = {
    "A" : [0.2, 0.2, 0.3, 0.2, 0.3],
    "C" : [0.4, 0.3, 0.1, 0.5, 0.1],
    "G" : [0.3, 0.3, 0.5, 0.2, 0.4],
    "T" : [0.1, 0.2, 0.1, 0.1, 0.2]
  }

  text_1 = "ACGGGGATTACC"
  text_2 = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"

  prob = probability(text_1, profile_1)
  size = len(profile_2["A"])

  profile = profileMostProbablePattern(text_2, size, profile_2)
  print(profile)

def profileMostProbablePattern(text, size, profile):
  boundary = len(text) - size + 1
  probablePattern = ""
  currHighestProb = 0
  for i in range(boundary):
    pattern = text[i:i + size]
    prob = probability(pattern, profile)
    if prob > currHighestProb:
      probablePattern = pattern
      currHighestProb = prob 
  return probablePattern
'''
'''
  

def probability(text, profile):
  probability = 1
  length = len(text)
  for i in range(length):
    sym = text[i]
    probability *= profile[sym][i]
  return probability

if __name__ == "__main__": main()
