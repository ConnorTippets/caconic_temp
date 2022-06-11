def handle_input(inp):
    inp = inp.split(" ")
    reserve = parse_input(inp)
    return reserve

def parse_input(inp):
    care = True
    inpe = []
    try:
        firstorig = inp[0]
    except:
        return
    first = firstorig
    if first in ('str', 'int', 'float', 'list', 'dict'):
        inpe.append("")
        first = ""
        care = True
    elif first in 'func':
        inpe.append("def")
        first = "def"
    else:
        inpe.append(first)
        first = firstorig
    for idx, x in enumerate(inp):
#        if first == 'func' and idx == 2:
#            args = []
#            for idxx, xx in enumerate(inp[2:]):
#                if not xx.endswith(":"):
#                    args.append(xx)
#                else:
#                    args.append(xx.split(":")[0])
#            inpe[inpe.index(first)] = inpe[inpe.index(first)] + f" {inp[1]}" + '\(' + f"{','.join(args)}" + '\):'
#            return
#        else:
        print(inpe)
        if firstorig == "func":
            if 'def '+inp[2] in inpe:
                splitter = ":\n"
                inpe[inpe.index(first + f" {inp[1]}")] = inpe[inpe.index(first + f" {inp[1]}")] + (f"({x.split(splitter)[0]}):" if not x == firstorig else "")
            elif 'def' in inpe:
                inpe[inpe.index(first)] = inpe[inpe.index(first)] + (f" {x}" if not x == firstorig else "")
        else:
            if first != "":
                inpe[inpe.index(first)] = inpe[inpe.index(first)] + (f" {x}" if not x == firstorig else "")
            else:
                if care:
                    inpe[inpe.index(f" {inp[1]}")] = inpe[inpe.index(f" {inp[1]}")] + (f" {x}" if not x == firstorig else "")
                    care = False
                else:
                    inpe[inpe.index(first)] = inpe[inpe.index(first)] + (f" {x}" if not x == firstorig else "")
                    care = True
                    
    print(inpe)
    return inpe
