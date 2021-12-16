import operator
from functools import reduce


with open('input') as infile:
    content = infile.read().strip()

binary = []
for char in content:
    num = int(char, 16)
    for idx in range(4):
        binary.append(int(bool(num & (1 << (3 - idx)))))

class countable:
    """Wrap *iterable* and keep a count of how many items have been consumed.

    The ``items_seen`` attribute starts at ``0`` and increments as the iterable
    is consumed:

        >>> iterable = map(str, range(10))
        >>> it = countable(iterable)
        >>> it.items_seen
        0
        >>> next(it), next(it)
        ('0', '1')
        >>> list(it)
        ['2', '3', '4', '5', '6', '7', '8', '9']
        >>> it.items_seen
        10
    """

    def __init__(self, iterable):
        self._it = iter(iterable)
        self.items_seen = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._it)
        self.items_seen += 1
        return item

def read_int(stream, bits):
    i = 0
    for _, r in zip(range(bits), stream):
        i = (i << 1) + r
    return i

def parse_literal(stream):
    retval = 0
    r = 0b10000
    while r & 0b10000:
        r = read_int(stream, 5)
        retval = (retval << 4) | (r & 0b1111)
    return retval

def parse_operator(stream):
    length_type_id = read_int(stream, 1)
    subpackets = []
    if length_type_id == 0:
        total_subpacket_bit_len = read_int(stream, 15)
        current_amount_read = stream.items_seen
        while stream.items_seen < current_amount_read + total_subpacket_bit_len:
            subpackets.append(parse_block(stream))
    elif length_type_id == 1:
        subpacket_amount = read_int(stream, 11)
        subpackets = [parse_block(stream) for _ in range(subpacket_amount)]
    return tuple(subpackets)


def parse_block(stream):
    version = read_int(stream, 3)
    type_id = read_int(stream, 3)
    if type_id == 4:
        return (version, 4, parse_literal(stream))
    else:
        return (version, type_id, parse_operator(stream))

stream = countable(iter(binary))
parsed = parse_block(stream)

def solve1(block):
    version, type_id, content = block
    if type_id == 4:
        return version
    else:
        return version + sum(solve1(b) for b in content)
print(solve1(parsed))

def solve2(block):
    version, type_id, content = block
    if type_id == 0:
        return sum(solve2(b) for b in content)
    elif type_id == 1:
        return reduce(operator.mul, (solve2(b) for b in content))
    elif type_id == 2:
        return min(solve2(b) for b in content)
    elif type_id == 3:
        return max(solve2(b) for b in content)
    elif type_id == 4:
        return content
    elif type_id == 5:
        return int(solve2(content[0]) > solve2(content[1]))
    elif type_id == 6:
        return int(solve2(content[0]) < solve2(content[1]))
    elif type_id == 7:
        return int(solve2(content[0]) == solve2(content[1]))

print(solve2(parsed))
