import numpy as np
import matplotlib.pyplot as plt

def loadText(filepath):
    f = open(filepath,'r')
    t = f.read()
    f.close()
    
    return preprocess(t)

def preprocess(text):
    return ''.join([i for i in text if i.isalpha()]).upper()

def lettersToNumbers(text):
    text = preprocess(text)
    return np.array([ord(letter) - 65 for letter in text])

def numbersToLetters(numbers):
    if len(np.shape(numbers)) == 1:
        out = ''.join([chr(number + 65) for number in numbers])
    else:
        out = ''
        for i in range(np.shape(numbers)[0]):
            out += ''.join([str(chr(number + 65)) for number in numbers[i,:]])
            out += '\n'
    print(out)
    return out
    
def frequency(incoming):
    import numpy as np
    if type(incoming) == str:
        text = preprocess(incoming)
        numbers = lettersToNumbers(text)
    else:
        numbers = incoming

    freq = np.zeros(26)
    for i in range(26):
        freq[i] = np.sum(numbers == i)/len(numbers)
        
    plt.plot(freq)
    plt.xlabel('Character Number')
    plt.ylabel('Relative Frequency')
    
def friedman(incoming, N = 50):    
    coincidences = np.zeros(N)
    for shift in range(N):
        line1 = incoming[:-shift]
        line2 = incoming[shift:]
        
        coincidences[shift] = np.sum(line1 == line2)/(len(incoming)-1)
        
    plt.plot(coincidences)
    plt.xlabel('Shift')
    plt.ylabel('Coincidences [%]')
    
    
def isPrime(n):
    if n <= 0: return False
    elif n == 1: return False
    elif n == 2: return True
    else:
        for i in np.arange(2,np.sqrt(n) + 1):
            if n%i == 0: return False
        return True
    
def totient(n):
    prime_divisors = [d for d in np.arange(2,n+1) if n % d == 0 and isPrime(d)]
    return int(np.round(n*np.prod([1 - 1./d for d in prime_divisors])))
      
def gcd(a,b):
    while b != 0:
        t = b
        b = a % b 
        a = t 
    return a   
        
def modInv(x,n):
    if gcd(x,n) != 1: 
        print(x,'has no inverse modulo',n)
        return None
    return x**(totient(n) - 1) % n

def order(x,n):
    for i in range(1,n):
        if x**i%n == 1:
            return i
    return None

def powMod(base, exponent, modulus):
    out = base
    for i in range(exponent-1):
        out *= base
        out = out%modulus
    return out
    
    
def sha0(text):
    import hashlib
    hasher = hashlib.sha1()
    text = str(text)
    text = text.encode("utf-8")
    hasher.update(text)
    digest = hasher.hexdigest()
    sliced = digest[:4]
    return int(sliced,16)
