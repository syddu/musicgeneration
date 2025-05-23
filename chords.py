from music21 import *

chord1 = chord.Chord(['C', 'E', 'G'])
chord2 = chord.Chord([0,4, 7])

note1, note2, note3 = note.Note('C'), note.Note('E'), note.Note('G')
chord3 = chord.Chord([note1, note2, note3])

print(chord1.commonName)

#list of the number of [semitones, whole-tones, minor-thirds/augmented-seconds, major-thirds, perfect fourths, and tritones] in the chord or inversion
print(chord1.intervalVector)


chord4 = chord.Chord([1, 5, 8])
s = stream.Stream()
s.append([chord1,chord2,chord3])
# s.show()


works = corpus.search(composer = 'bach',timeSignature = '3/4')

bach_34_work = works[0]
bach_34_work = converter.parse(bach_34_work)
bach_34_work.show()
# bach_34_work = bach_34_work.recurse().notes
# bach_34_work.show()
bach_34_work_chordified = bach_34_work.chordify()
bach_34_work_chordified.show()