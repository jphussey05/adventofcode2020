
from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon
from itertools import product

# Creation of variables
var_0 = Variable("0")
var_4 = Variable("4")

# Creation of terminals
ter_a = Terminal("a")


# Creation of productions
p0 = Production(var_0, [var_4])
p1 = Production(var_4, [ter_a])

# Creation of the CFG
cfg1 = CFG({var_0, var_4}, {ter_a}, var_0, {p0, p1})

# Check for containment






if __name__ == "__main__":
    with open('day19.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]

    terminals = []
    variables = []
    productions = []

  
    for line in contents:
        rule, derivations = line.split(': ')
        rule = int(rule) + 64
        print(f'Processing {rule} -> {derivations}')
        if '"' in derivations:
            term = str(derivations[1])
            print(f'Creating terminal {term} of type {type(term)}')
            terminals.append(Terminal(term))
            variables.append(Variable(chr(rule)))
            print(f'Creating variable {rule}')
            productions.append(Production(variables[-1], [terminals[-1]]))
            print(f' Added one production')
            print(f'-- {productions[-1].head} -> {productions[-1].body}')

        elif '|' in derivations:
            
            p1, p2 = derivations.split('|')
            variables.append(Variable(chr(rule)))
            print(f'Creating variable {rule}')
            productions.append(Production(variables[-1], list(p1.split())))
            productions.append(Production(variables[-1], list(p2.split())))
            print(f' Added two productions')
            print(f'-- {productions[-1].head} -> {productions[-1].body}')
            print(f'-- {productions[-2].head} -> {productions[-2].body}')
        else:
            print(f'Creating variable {rule}')
            variables.append(Variable(chr(rule)))
            print(f' Added one production')
            productions.append(Production(variables[-1], list(derivations.split())))
            print(f'-- {productions[-1].head} -> {productions[-1].body}')
            if rule == '0':
                print(f'Creating Rule 0!!!!')
                var_0 = variables[-1]
  

    productions = set(productions)
    variables = set(variables)
    terminals = set(terminals)

    cfg = CFG(
        variables=variables,
        terminals=terminals,
        start_symbol=var_0,
        productions=productions)

    print(productions)

    strings = [
        'a',
        'ababbb',
        'bababa',
        'abbbab',
        'aaabbb',
        'aaaabbb']

    # for string in strings:
        # print(f"{string} is {cfg.contains(string)}")

    print(cfg.productions)
    print(cfg1.productions)

    print(cfg.terminals)
    print(cfg1.terminals)

    print(cfg.variables)
    print(cfg1.variables)

    print(cfg.start_symbol)
    print(cfg1.start_symbol)

    print(cfg.contains('a'))
    print(cfg1.contains('a'))
# {S -> USELESS, USELESS -> , S -> Terminal(a) S B, B -> Terminal(b), USELESS -> Terminal(a) S B}
# {Terminal(a), Terminal(b)}
# {Variable(S), Variable(USELESS), Variable(B)}
# S



#### MINE

# {4 -> Terminal(a), 0 -> 4}
# {Terminal(a)}
# {Variable(0), Variable(4)}
# 0