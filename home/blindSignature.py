from math import ceil
def getblock(N):
    blocks=0
    while(N>0):
        N//=2
        blocks+=1
    return blocks//8

def splitCount(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]
def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    #print(decimal) 
    return decimal  

def combine(sample):
    answer = ""
    for i in sample:
        temp = bin(ord(i))[2:]
        while (len(temp)<8):
            temp = '0' + temp
        answer = answer + temp
    #print(answer)

    return binaryToDecimal(int(answer))

def signPrivate(m1, d, n):
    #return ( m1**d ) % n
    return pow(m1,d,n)
def sign(m, r, e, n):
    x = r**e
    #print("x",x)
    y = x * m
    #print("y",y)
    #print("final",y%n)
    return ((r ** e) * m) % n

def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 
    return x 

 

def blindAttack(plainText,p,q,r,e):
    print("Running blind Attack")
    # plainText = input("Enter Plain text\n")
    # p = int(input("Enter p\n"))
    # q = int(input("Enter q\n"))
    # r = int(input("Enter r\n"))
    # e = int(input("Enter e\n"))
    #r = 37
    #plainText = "NITK"
    # for i in plainText:
    #     print(bin(ord(i)))
    # p = 11
    # q = 13
    n1 = (p - 1) * (q - 1)
    n = p * q
    blockSize = 0
    temp = 1

    while temp < n:
        temp = temp * 256
        blockSize = blockSize + 1
    #print("blockSize is",blockSize)

    blockSize = getblock(n)
    if blockSize == 0:
        blockSize = 1
    #blockSize = 1
    #print(n)



    count = 0
    while count < 3:
        try:
            rInv = modInverse(r,n)
            break
        except:
            return 1
            r = int(input("Enter the value of r again"))
            count = count + 1
    try:
        d = modInverse(e,n1)
    except:
        return 2
        print("E value is wrong")
        e = int(input("Enter e\n"))
        d = modInverse(e,n1)

    print("D value",d)

    print("R inverse exhist", rInv)
    li=[]
    sample = ""
    for i in plainText:
        if len(sample) < blockSize:
            sample = sample + i
            continue
        if len(sample) == blockSize:
            output = combine(sample)
            sample = ""
            sample = sample + i
        m = int(output)
        #print(i)
        print("Message",m)
        signature = sign(m,r,e,n)
        print("Signature",signature)
        private = signPrivate(signature,d,n)
        print("Private",private)
        print("Blind Signature", (rInv * private) % n )
        li.append((rInv * private) % n)
    #print(li)
    if sample:
        output = combine(sample)
        m = int(output)
        #print(i)
        print("Message",m)
        signature = sign(m,r,e,n)
        print("Signature",signature)
        private = signPrivate(signature,d,n)
        print("Private",private)
        print( (rInv * private) % n )
        li.append((rInv * private) % n)

    print("Signatures:")
    print(li)
    message = ""
    for i in li:
        #print("i is",i)
        #print(chr((i**e)%n))
        st = bin(pow(i,e,n))[2:]
        #print(len(st))
        zero = 8 - (len(st) % 8)
        st = zero * "0" + st
        #print(st,len(st))
        output = splitCount(st,8)

        #print(output)
        for i in output:
            #print(chr(int(i,2)))
            message = message +  chr(int(i,2))

    print("Original message:",message)
    li.append(message)
    return({'li':li,'d':d,'rInv':rInv})

