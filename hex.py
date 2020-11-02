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
        
    #convert key and inp to binary for XOR
    for n in (0, len(inp)):
        p = format(inp[n], 'b')
        q = format(inp[n], 'b')
        r = 
        
            
    
    
