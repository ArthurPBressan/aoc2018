def _get_frequencies():
    with open('input.txt', 'r') as file:
        return [int(line) for line in file]

def pt1(frequencies):
    return sum(frequencies)

def pt2(frequencies, visited_frequencies, current_frequency=0):
    for frequency in frequencies:
        current_frequency += frequency
        if current_frequency in visited_frequencies:
            return current_frequency
        visited_frequencies.add(current_frequency)
    return pt2(frequencies, visited_frequencies, current_frequency)


if __name__ == '__main__':
    input_frequencies = _get_frequencies()
    final_frequency = pt1(input_frequencies)
    print("Final Frequency:", final_frequency)
    repeated_frequency = pt2(input_frequencies, set())
    print("First Repeated Frequency:", repeated_frequency)
