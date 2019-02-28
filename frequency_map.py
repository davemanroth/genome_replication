#!/usr/local/bin/pyvenv-3.7 python3

def main():
  text = 'CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA'
  #text = 'CAGTATCAATACTGGACTAACG'
  words = frequencyWords(text, 3)
  print(words)

def frequencyWords(text, k):
  words = []
  freq = frequencyMap(text, k)
  largest = max( freq.values())
  for key in freq:
    if freq[key] == largest:
      words.append(key)
  return words

def frequencyMap(text, k):
  freq = {}
  n = len(text)
  for i in range(n-k+1):
    pattern = text[i:i+k]
    if pattern in freq:
      freq[pattern] += 1
    else:
      freq[pattern] = 1
  return freq


if __name__=='__main__' : main()
