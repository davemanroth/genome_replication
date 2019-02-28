def main():
  p = 'CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA'
  q = 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'
  print( hammingDistance(p, q))
  #pattern = 'ATTCTGGA'
  #genome = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
  #d = 3
  #print( appxPatternMatching(pattern, genome, d))

def appxPatternMatching(pattern, genome, threshold):
  positions = []
  for i in range(len(genome)):
    appxPattern = genome[i:i+len(pattern)]
    if len(appxPattern) != len(pattern):
      break
    hammingDist = hammingDistance(pattern, appxPattern)
    if hammingDist <= threshold:
      positions.append(i)
  return positions

def hammingDistance(p, q):
  distance = 0
  for i in range(len(p)):
    if p[i] != q[i]:
      distance += 1
  return distance
    
#def appxPatternCount():


if __name__ == '__main__': main()
