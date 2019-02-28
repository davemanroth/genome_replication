#!/usr/loca/bin/pyvenv-3.7 python3

def main():
  print( symbolArray('AAAAGGGG', 'A'))

def symbolArray(genome, symbol):
  tally = {}
  extendedGenome = genome + genome[0:len(genome)//2]
  for i in range(len(genome)):
    tally[i] = patternCount(symbol, extendedGenome[i:i + (len(genome)//2)])
  return tally
  
def patternCount(symbol, genome):
  count = 0
  for i in range(len(genome)):
    if (genome[i:i + len(symbol)] == symbol):
      count += 1
  return count

if __name__ == '__main__': main()
