cat = list(input().split())
ans = 0
symbols = ["*", "+", "/", "-"]
print (cat)
i = 0
memory = []
while cat != []:
    if cat[i] not in symbols:
        memory.append(cat[i])
        print ("BOO", memory)
        i += 1
    else:
        if cat[i] == "*":
            memory = [int(memory[0])*int(memory[1])]
        elif cat[i] == "+":
            memory = [int(memory[0])+int(memory[1])]
        elif cat[i] == "/":
            memory = [int(memory[0])/int(memory[1])]
        elif cat[i] == "-":
            memory = [int(memory[0])-int(memory[1])]
        print ("BOOO", "mem: ", memory, "line:", cat)
        del cat[0]
        del cat[0]
        try:
            del cat[0]
        except IndexError:
            i = i
        i = 0
    print ("memory:", memory, "string:", cat)
ans = memory[0]
print (ans)
