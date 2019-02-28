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
  print(profile)

def profile(counts):
  return motifStats(motifs)

def motifCount(motifs):
  count = initializeMatrix(motifs[0])
  for i in range(len(motifs)):
    motif = motifs[i]
    for j in range(len(motif)):
      symbol = motif[j]
      count[symbol][j] += 1
  return count

def motifProfile(count, numRows):
  profile = count
  for key, row in count.items(): 
    for i in range(len(row)):
      profile[key][i] = count[key][i] / numRows
  return profile
      

'''
def count(motifs):
  matrix = initializeMatrix(motifs[0])
  for i in range(len(motifs)):
    motif = motifs[i]
    for j in range(len(motif)):
      symbol = motif[j]
      matrix[symbol][j] += 1
  return matrix
'''

def initializeMatrix(motif):
  matrix = {}
  keys = 'ACGT'
  for i in range(len(keys)):
    symbol = keys[i]
    matrix[symbol] = [0] * len(motif)
  return matrix

if __name__ == '__main__': main()
