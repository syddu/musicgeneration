from music21 import *

bach_works = corpus.getComposer('bach')

works = corpus.search(composer = 'bach',timeSignature = '3/4')
bach_34_work = works[0]

parsed_partita = converter.parse('bach_partita_2.mxl')

#DFS substream traversal of all nested streams
recursed_partita = parsed_partita.recurse()

new_stream = stream.Stream()
for element in recursed_partita.notes:
    if element.duration == duration.Duration(.25):
        new_stream.append(element)

new_stream.show()