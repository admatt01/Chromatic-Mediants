#!/usr/bin/python

chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
major_intervals = [2, 2, 1, 2, 2, 2, 1]
minor_intervals = [2, 1, 2, 2, 1, 2, 2]
major_chord_names = ['Major', 'Minor', 'Minor', 'Major', 'Major', 'Minor', 'Diminished']
minor_chord_names = ['Minor', 'Diminished', 'Major', 'Minor', 'Minor', 'Major', 'Major']

# Get user input for scale type (major or minor)
scale_type = input("Enter the scale type (major or minor): ").lower()

# Check if the scale type is valid
if scale_type != 'major' and scale_type != 'minor':
    print("Invalid scale type!")
    exit()

# Get user input for the root note of the scale
root_note = input("Enter the root note of the scale: ").capitalize()

# Check if the root note is valid
if root_note not in chromatic_scale:
    print("Invalid root note!")
    exit()

# Determine the intervals and chord names based on the scale type
intervals = major_intervals if scale_type == 'major' else minor_intervals
chord_names = major_chord_names if scale_type == 'major' else minor_chord_names[:len(intervals)]

# Calculate the scale notes
root_index = chromatic_scale.index(root_note)
scale_notes = [chromatic_scale[root_index]]
for interval in intervals:
    root_index = (root_index + interval) % len(chromatic_scale)
    note = chromatic_scale[root_index]
    scale_notes.append(note)

# Calculate the triads
triads = []
for i in range(len(scale_notes)):
    root = scale_notes[i]
    third = scale_notes[(i + 2) % 7]
    fifth = scale_notes[(i + 4) % 7]
    chord_name = chord_names[i % len(chord_names)]
    triad_name = f"{root} {third} {fifth} ({root} {chord_name})"
    triads.append(triad_name)

# Calculate the mediant triad
mediant_triad = triads[2]

# Calculate the submediant triad
submediant_triad = triads[5]

# Calculate the first chromatic mediant
root, third, fifth, chord_name = mediant_triad.split(maxsplit=3)
if scale_type == 'major':
    raised_third = chromatic_scale[(chromatic_scale.index(third) + 1) % len(chromatic_scale)]
    chord_name = chord_names[3]
    chromatic_mediant_1 = f"{root} {raised_third} {fifth} ({root} {chord_name})"
else:
    lowered_third = chromatic_scale[(chromatic_scale.index(third) - 1) % len(chromatic_scale)]
    chord_name = chord_names[3]
    chromatic_mediant_1 = f"{root} {lowered_third} {fifth} ({root} {chord_name})"

# Calculate the second chromatic mediant
root, third, fifth, chord_name = mediant_triad.split(maxsplit=3)
if scale_type == 'major':
    lowered_first = chromatic_scale[(chromatic_scale.index(root) - 1) % len(chromatic_scale)]
    lowered_fifth = chromatic_scale[(chromatic_scale.index(fifth) - 1) % len(chromatic_scale)]
    chord_name = chord_names[3]
    chromatic_mediant_2 = f"{lowered_first} {third} {lowered_fifth} ({lowered_first} {chord_name})"
else:
    raised_first = chromatic_scale[(chromatic_scale.index(root) + 1) % len(chromatic_scale)]
    raised_fifth = chromatic_scale[(chromatic_scale.index(fifth) + 1) % len(chromatic_scale)]
    chord_name = chord_names[3]
    chromatic_mediant_2 = f"{raised_first} {third} {raised_fifth} ({raised_first} {chord_name})"

# Calculate the first chromatic submediant
root, third, fifth, chord_name = submediant_triad.split(maxsplit=3)
if scale_type == 'major':
    raised_third = chromatic_scale[(chromatic_scale.index(third) + 1) % len(chromatic_scale)]
    chord_name = chord_names[3]
    chromatic_submediant_1 = f"{root} {raised_third} {fifth} ({root} {chord_name})"
else:
    lowered_third = chromatic_scale[(chromatic_scale.index(third) - 1) % len(chromatic_scale)]
    chord_name = chord_names[3]
    chromatic_submediant_1 = f"{root} {lowered_third} {fifth} ({root} {chord_name})"

# Calculate the second chromatic submediant
root, third, fifth, chord_name = submediant_triad.split(maxsplit=3)
if scale_type == 'major':
    lowered_first = chromatic_scale[(chromatic_scale.index(root) - 1) % len(chromatic_scale)]
    lowered_fifth = chromatic_scale[(chromatic_scale.index(fifth) - 1) % len(chromatic_scale)]
    chord_name = chord_names[3]
    chromatic_submediant_2 = f"{lowered_first} {third} {lowered_fifth} ({lowered_first} {chord_name})"
else:
    raised_first = chromatic_scale[(chromatic_scale.index(root) + 1) % len(chromatic_scale)]
    raised_fifth = chromatic_scale[(chromatic_scale.index(fifth) + 1) % len(chromatic_scale)]
    chord_name = chord_names[3]
    chromatic_submediant_2 = f"{raised_first} {third} {raised_fifth} ({raised_first} {chord_name})"

# Print the results
print("Original Triads:")
for triad in triads:
    print(triad)

print("Mediant Triad:")
print(mediant_triad)

print("Submediant Triad:")
print(submediant_triad)

print("Chromatic Mediants:")
print(chromatic_mediant_1)
print(chromatic_mediant_2)

print("Chromatic Submediants:")
print(chromatic_submediant_1)
print(chromatic_submediant_2)
