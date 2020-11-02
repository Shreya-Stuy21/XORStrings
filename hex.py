import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)
    
#Part 1: Human Readable Mode
if(mode = "human"):
    output = ""
    #loop the key string when the keyfile is shorter than the textfiles
    diff = len(inp) - len(key)
    while (diff > 0):
        key = key + key
        diff = len(inp) - len(key)
    key = key[0, len(inp)]
        
    #convert key and inp to Unicode numbers for XOR
    for n in (0, len(inp)):
        #ord returns an integer representing the Unicode code point of the character
        x = ord(inp[n])
        y = ord(key[n])
        #chr returns the Unicode object corresponding to the letter
        #the ^ operator uses moduli two addition, essentially decrypting the message by using the key
        output = output + chr(x^y)
    debug = True
    
#Part 2: Hexidecimal Mode
if(mode = "numOut"):
        output = ""
    #loop the key string when the keyfile is shorter than the textfiles
    diff = len(inp) - len(key)
    while (diff > 0):
        key = key + key
        diff = len(inp) - len(key)
    key = key[0, len(inp)]
        
    #convert key and inp to binary for XOR
    for n in (0, len(inp)):
        x = format(inp[n], 'b')
        y = format(key[n], 'b')
        bin = x ^ y
        hex = 
        output = output + hex + "\t"
        
    debug = True

    
    
