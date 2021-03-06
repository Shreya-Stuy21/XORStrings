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

output = ""
#loop the key string when the keyfile is shorter than the textfiles
diff = len(inp) - len(key)
while (diff > 0):
    key = key + key
    diff = len(inp) - len(key)
key = key[0: len(inp)]
    
#Part 1: Human Readable Mode
if(mode == "human"):
    #convert key and inp to Unicode numbers for XOR
    for n in range(0, len(inp)):
        #ord returns an integer representing the Unicode code point of the character
        x = ord(inp[n])
        y = ord(key[n])
        #chr returns the Unicode object corresponding to the letter
        #the ^ operator uses moduli two addition, essentially decrypting the message by using the key
        output = output + chr(x^y)
    debug = True
    
#Part 2: Hexidecimal Mode
if(mode == "numOut"):
    for n in range(0, len(inp)):
        a = ord(inp[n])
        b = ord(key[n])
        bitwise_xor = a^b
        hexadecimal = hex(bitwise_xor)
        hexadecimal = hexadecimal[2:len(hexadecimal)]
        #adds the hexadecimal value to the output with a tab for space
        output = output + hexadecimal + "   "
        
    debug = True
print(output)

    
    
