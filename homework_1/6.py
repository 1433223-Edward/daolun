def reverse_with_for(sequence):
    reversed_sequence = []
    for i in range(len(sequence) - 1, -1, -1):
        reversed_sequence.append(sequence[i])
    return reversed_sequence

def reverse_with_while(sequence):
    reversed_sequence = []
    i = len(sequence) - 1
    while i >= 0:
        reversed_sequence.append(sequence[i])
        i -= 1
    return reversed_sequence

sequence = [1, 2, 3, 4, 5]

reversed_sequence_for = reverse_with_for(sequence)
print("Reversed sequence using for loop:", reversed_sequence_for)

reversed_sequence_while = reverse_with_while(sequence)
print("Reversed sequence using while loop:", reversed_sequence_while)