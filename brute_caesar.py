def bruteforce(text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = ''.join([t for t in text.upper() if t in alphabet])
    for i in range(len(alphabet)-1,0,-1):
        otvet = ''
        for t in text:
            x = (alphabet.index(t) + i)%len(alphabet)
            otvet += alphabet[x]
        print(otvet)
