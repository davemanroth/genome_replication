def main():
  input = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
  print( minimumSkew(input))

def minimumSkew(genome):
  positions = []
  skewArr = skewArray(genome)
  minVal = min(skewArr)
  for i in range(len(skewArr)):
    if skewArr[i] == minVal:
      positions.append(i)
  return positions


def skewArray(input):
  skew = [0] * (len(input) + 1)
  skew[0] = 0
  skewPos = 0
  for i in range(len(input)):
    skewPos += 1
    if input[i] == 'G':
      skew[skewPos] = skew[i] + 1
    elif input[i] == 'C':
      skew[skewPos] = skew[i] - 1
    else:
      skew[skewPos] = skew[i]
  return skew

if __name__ == '__main__': main()
