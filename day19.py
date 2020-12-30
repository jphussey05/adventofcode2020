
from pyformlang.cfg import Production, Variable, Terminal, CFG


if __name__ == "__main__":
    with open('day19.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]

    terminals = set()
    variables = set()
    productions = set()
    strings = []
    cnt = 0
    
    for line in contents:
        if not line:
            continue
        elif ':' in line:
            var, production = line.split(': ')
            
            variables.add(Variable(var))

            if "|" in production:
                # create multiple productions
                part1, part2 = production.split(' | ')
                
                tmp_p1 = [Variable(p1) for p1 in part1.split()]
                productions.add(Production(Variable(var), tmp_p1))

                tmp_p2 = [Variable(p2) for p2 in part2.split()]
                productions.add(Production(Variable(var), tmp_p2))

            elif '"' in production:
                # create a terminal
                t = production[1]

                terminals.add(Terminal(t))
                productions.add(Production(Variable(var), [Terminal(t)]))
            else:
                # just a normal production
                tmp_p = [Variable(p) for p in production.split()]
                productions.add(Production(Variable(var), tmp_p))
        else:
            strings.append(line)


    cfg = CFG(variables, terminals, Variable("0"), productions)
    print(f'[INFO] CFG is built')
    for string in strings:
        if cfg.contains(string):
            cnt += 1
    
    print(f'Total strings in grammar is ** {cnt} **')