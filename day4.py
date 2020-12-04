def byr_valid(byr):
    return True if byr in range(1920, 2002+1) else False

def iyr_valid(iyr):
    return True if iyr in range(2010, 2020+1) else False

def eyr_valid(eyr):
    return True if eyr in range(2020, 2030+1) else False

def hgt_valid(hgt):
    if hgt[-2:] == 'cm':
        return True if int(hgt[:-2]) in range(150, 193+1) else False
    elif hgt[-2:] == 'in':
        return True if int(hgt[:-2]) in range(59, 76+1) else False
    else:
        return False

def hcl_valid(hcl):
    valids = list(map(chr, range(97, 103))) + list(map(str, range(0,10)))
    if hcl[0] != '#':
        return False # didn't lead with the #
    
    if len(hcl[1:]) == 6:
        for c in hcl[1:]:
            if c not in valids:
                return False # right length but had invalid char
        
        return True # everything checked out
    else:
        return False # wasn't the right length

def ecl_valid(ecl):
    valids = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return True if ecl in valids else False

def pid_valid(pid):
    return True if pid.isdigit() and len(pid) == 9 else False

def validate(item):
    if len(item) == 7 and 'cid' in item.keys():
        return 0
    elif byr_valid(int(item['byr'])) and \
         iyr_valid(int(item['iyr'])) and \
         eyr_valid(int(item['eyr'])) and \
         hgt_valid(item['hgt']) and \
         hcl_valid(item['hcl']) and \
         ecl_valid(item['ecl']) and \
         pid_valid(item['pid']):
         return 1
    else:
        return 0
    

if __name__ == "__main__":
    
    with open('day4.txt') as fin:
        contents = fin.readlines()

    contents = [line.strip() for line in contents]

    print(contents.count('') + 1)
    passports = []
    passport = {}
    for line in contents:
        if line == '':
            passports.append(passport)
            passport = {}
            
        else:
            fields = line.split()
            for field in fields:
                name, value = field.split(':')
                passport[name] = value 

    passports.append(passport)

    valids = 0
    for item in passports:
        if len(item) >= 7:
            valids += validate(item)

    print(valids)