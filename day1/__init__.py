def _process_input(fn):
    with open('input.txt', 'r') as _file:
        return fn(_file)

def pt1(_file):
    freq = 0
    for line in _file:
        freq += int(line)
    return freq

def pt2(_file, frequencies=None, current_frequency=0):
    if not frequencies:
        frequencies = {0}
    print(current_frequency)
    for line in _file:
        freq = int(line)
        current_frequency += freq
        if current_frequency in frequencies:
            return current_frequency
        frequencies.add(current_frequency)
    return pt2(_file, frequencies, current_frequency)


if __name__ == '__main__':
    final_frequency = _process_input(pt1)
    print("Final Frequency:", final_frequency)
    repeated_frequency = _process_input(pt2)
    print("First Repeated Frequency:", repeated_frequency)
