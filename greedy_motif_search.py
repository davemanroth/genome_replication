
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

  dna_1 = [
    "GGCGTTCAGGCA",
    "AAGAATCAGTCA",
    "CAAGGAGTTCGC",
    "CACGTCAATCAC",
    "CAATAATATTCG"
  ]

  prob = probability(text_1, profile_1)
  size = len(profile_6["A"])

  profile = profileMostProbablePattern(text_6, size, profile_6)
  result = greedyMotifSearch(dna_1, 3, 5)
  print(result)
  
# Given set of DNA strands, finds most closely related kmers 
def greedyMotifSearch(dna, k, t):
  bestMotifs = initializeBestMotifs(dna, k)
  firstStrand = dna[0]
  strandLength = len(firstStrand)
  for i in range(strandLength - k + 1):
    motifs = []
    motifs.append(firstStrand[i:k + i])
    for j in range(1, t):
      count = motifCount(motifs)
      profile = motifProfile(count, len(motifs))
      bestMatch = profileMostProbablePattern(dna[j], k, profile)
      motifs.append(bestMatch)
    if motifScore(motifs) < motifScore(bestMotifs):
      bestMotifs = motifs
  return bestMotifs
      
# Initializing best motifs list simply to the first kmer in each DNA strand
def initializeBestMotifs(dna, k):
  bestMotifs = []
  for i in range(len(dna)):
    currStrand = dna[i]
    bestMotifs.append(currStrand[0: k])
  return bestMotifs

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
  
def probability(text, profile):
  probability = 1
  length = len(text)
  for i in range(length):
    sym = text[i]
    probability *= profile[sym][i]
  return probability

def motifScore(motifs):
  consensus = motifConsensus(motifs)
  length = len(motifs[0])
  score = 0
  for i in range(length):
    for motif in motifs:
      if motif[i] != consensus[i]:
        score += 1
  return score

def motifConsensus(motifs):
  count = motifCount(motifs)
  length = len(motifs[0])
  consensus = ""
  for i in range(length):
    freqLet = ""
    highestNum = 0
    for sym in "ACGT":
      if count[sym][i] > highestNum:
        highestNum = count[sym][i]
        freqLet = sym
    consensus += freqLet
  return consensus

# Assembles counts for each nucleotide
def motifCount(motifs):
  count = initializeMatrix(motifs[0])
  for i in range(len(motifs)):
    motif = motifs[i]
    for j in range(len(motif)):
      symbol = motif[j]
      count[symbol][j] += 1
  return count

# Computes count ratios of each nucleotide
def motifProfile(count, numRows):
  profile = count
  for key, row in count.items(): 
    for i in range(len(row)):
      profile[key][i] = count[key][i] / numRows
  return profile
      
def initializeMatrix(motif):
  matrix = {}
  keys = 'ACGT'
  for i in range(len(keys)):
    symbol = keys[i]
    matrix[symbol] = [0] * len(motif)
  return matrix

if __name__ == '__main__': main()
