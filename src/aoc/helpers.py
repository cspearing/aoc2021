def read_int_line(f):
    line = f.readline().rstrip()
    return int(line)

def parse_int_line(line):
    num_strings = line.split(' ')
    result = []
    for num_string in num_strings:
        try:
            result.append(int(num_string))
        except Exception:
            pass
    return result

def read_many_int_line(f):
    line = f.readline().rstrip()
    return parse_int_line(line)

def read_all_int_lines(f):
    lines = f.readlines()
    values = map(int, lines)
    return values