
'''
  profile_3 = {
    "A" : [],
    "C" : [],
    "G" : [],
    "T" : []
  }
'''

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

  profile_3 = {
    "A" : [0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1],
    "C" : [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6],
    "G" : [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2],
    "T" : [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1]
  }

  profile_4 = {
    "A" : [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5],
    "C" : [0.3, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.4, 0.3, 0.2, 0.2, 0.1],
    "G" : [0.2, 0.1, 0.4, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
    "T" : [0.3, 0.4, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.4, 0.4, 0.2, 0.3]
  }

  profile_5 = {
    "A" : [1.0, 1.0, 1.0],
    "C" : [0.0, 0.0, 0.0],
    "G" : [0.0, 0.0, 0.0],
    "T" : [0.0, 0.0, 0.0]
  }

  profile_6 = {
    "A" : [0.2, 0.2, 0.3, 0.2, 0.3],
    "C" : [0.4, 0.3, 0.1, 0.5, 0.1],
    "G" : [0.3, 0.3, 0.5, 0.2, 0.4],
    "T" : [0.1, 0.2, 0.1, 0.1, 0.2]
  }

  text_1 = "ACGGGGATTACC"
  text_2 = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
  text_3 = "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT"
  text_4 = "TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA"
  text_5 = "AACCGGTT"
  text_6 = "TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA"

  prob = probability(text_1, profile_1)
  size = len(profile_6["A"])

  profile = profileMostProbablePattern(text_6, size, profile_6)
  print(profile)

def profileMostProbablePattern(text, size, profile):
  boundary = len(text) - size + 1
  probablePattern = text[0:size]
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
