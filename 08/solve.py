import itertools
from collections import defaultdict

with open('input') as infile:
    parts = [((spl := line.strip().split(' | '))[0].split(' '), spl[1].split(' ')) for line in infile]

# 1
print(sum(1 for elem in itertools.chain.from_iterable(p[1] for p in parts) if (len(elem) in (2, 3, 4, 7))))

# 2
def segment_to_number(segment):
    return {
        frozenset('abcefg'): 0,
        frozenset('cf'): 1,
        frozenset('acdeg'): 2,
        frozenset('acdfg'): 3,
        frozenset('bdcf'): 4,
        frozenset('abdfg'): 5,
        frozenset('abdefg'): 6,
        frozenset('acf'): 7,
        frozenset('abcdefg'): 8,
        frozenset('abcdfg'): 9
    }[segment]

def deduce(part):
    len_mapped = defaultdict(list)
    for p in part[0]:
        len_mapped[len(p)].append(frozenset(p))
    one = len_mapped[2][0]
    seven = len_mapped[3][0]
    four = len_mapped[4][0]
    eight = len_mapped[7][0]
    a_segment = seven - one
    f_segment = [(s & one) for s in len_mapped[6] if len(s & one) == 1][0] # this uses the '6'
    c_segment = one - f_segment
    adg_segment = [(s - one) for s in len_mapped[5] if len(s & one) == 2][0] # this uses the '3'
    d_segment = (adg_segment & four) - one
    g_segment = ((adg_segment - four) - seven)
    b_segment = four - (d_segment | c_segment | f_segment)
    e_segment = eight - (a_segment | b_segment | c_segment | d_segment | f_segment | g_segment)

    mapper = {next(iter(k)): v for k,v in {
        a_segment: 'a',
        b_segment: 'b',
        c_segment: 'c',
        d_segment: 'd',
        e_segment: 'e',
        f_segment: 'f',
        g_segment: 'g'
    }.items()}
    return [frozenset(mapper[l] for l in p) for p in part[1]]

total = 0
for part in parts:
    result = deduce(part)
    translated = [segment_to_number(n) for n in result] # [1, 2, 3, 4]
    output_value = int(''.join(str(p) for p in translated))
    total += output_value
print(total)
