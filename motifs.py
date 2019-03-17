def main():
  motifs_1 = [
    'AACGTA',
    'CCCGTT',
    'CACCTT',
    'GGATTA',
    'TTCCGG'
  ]
  motifs_2 = [
    'GTACAACTGT',
    'CAACTATGAA',
    'TCCTACAGGA',
    'AAGCAAGGGT',
    'GCGTACGACC',
    'TCGTCAGCGT',
    'AACAAGGTCA',
    'CTCAGGCGTC',
    'GGATCCAGGT',
    'GGCAAGTACC'
  ]
  count = motifCount(motifs_1)
  profile = motifProfile(count, len(motifs_1))
  consensus = motifConsensus(motifs_1)
  score = motifScore(motifs_1)
  print(profile)

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
