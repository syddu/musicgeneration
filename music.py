from music21 import *
from music21 import note, stream, duration, instrument
import music21
import random
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()  # Loads variables from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 
client = OpenAI(api_key="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") 
# Create note variables for violin/cello octaves
# Octave 3
quarter_rest = note.Rest('quarter')
cf3 = note.Note('C-3')
c3  = note.Note('C3')
cs3 = note.Note('C#3')

df3 = note.Note('D-3')
d3  = note.Note('D3')
ds3 = note.Note('D#3')

ef3 = note.Note('E-3')
e3  = note.Note('E3')
es3 = note.Note('E#3')

ff3 = note.Note('F-3')
f3  = note.Note('F3')
fs3 = note.Note('F#3')

gf3 = note.Note('G-3')
g3  = note.Note('G3')
gs3 = note.Note('G#3')

af3 = note.Note('A-3')
a3  = note.Note('A3')
as3 = note.Note('A#3')

bf3 = note.Note('B-3')
b3  = note.Note('B3')
bs3 = note.Note('B#3')

# Octave 4
cf4 = note.Note('C-4')
c4  = note.Note('C4')
cs4 = note.Note('C#4')

df4 = note.Note('D-4')
d4  = note.Note('D4')
ds4 = note.Note('D#4')

ef4 = note.Note('E-4')
e4  = note.Note('E4')
es4 = note.Note('E#4')

ff4 = note.Note('F-4')
f4  = note.Note('F4')
fs4 = note.Note('F#4')

gf4 = note.Note('G-4')
g4  = note.Note('G4')
gs4 = note.Note('G#4')

af4 = note.Note('A-4')
a4  = note.Note('A4')
as4 = note.Note('A#4')

bf4 = note.Note('B-4')
b4  = note.Note('B4')
bs4 = note.Note('B#4')

# Octave 5
cf5 = note.Note('C-5')
c5  = note.Note('C5')
cs5 = note.Note('C#5')

df5 = note.Note('D-5')
d5  = note.Note('D5')
ds5 = note.Note('D#5')

ef5 = note.Note('E-5')
e5  = note.Note('E5')
es5 = note.Note('E#5')

ff5 = note.Note('F-5')
f5  = note.Note('F5')
fs5 = note.Note('F#5')

gf5 = note.Note('G-5')
g5  = note.Note('G5')
gs5 = note.Note('G#5')

af5 = note.Note('A-5')
a5  = note.Note('A5')
as5 = note.Note('A#5')

bf5 = note.Note('B-5')
b5  = note.Note('B5')
bs5 = note.Note('B#5')

# Eighth-note versions for Octave 3
cf3_eighth = note.Note('C-3', duration=duration.Duration('eighth'))
c3_eighth  = note.Note('C3', duration=duration.Duration('eighth'))
cs3_eighth = note.Note('C#3', duration=duration.Duration('eighth'))

df3_eighth = note.Note('D-3', duration=duration.Duration('eighth'))
d3_eighth  = note.Note('D3', duration=duration.Duration('eighth'))
ds3_eighth = note.Note('D#3', duration=duration.Duration('eighth'))

ef3_eighth = note.Note('E-3', duration=duration.Duration('eighth'))
e3_eighth  = note.Note('E3', duration=duration.Duration('eighth'))
es3_eighth = note.Note('E#3', duration=duration.Duration('eighth'))

ff3_eighth = note.Note('F-3', duration=duration.Duration('eighth'))
f3_eighth  = note.Note('F3', duration=duration.Duration('eighth'))
fs3_eighth = note.Note('F#3', duration=duration.Duration('eighth'))

gf3_eighth = note.Note('G-3', duration=duration.Duration('eighth'))
g3_eighth  = note.Note('G3', duration=duration.Duration('eighth'))
gs3_eighth = note.Note('G#3', duration=duration.Duration('eighth'))

af3_eighth = note.Note('A-3', duration=duration.Duration('eighth'))
a3_eighth  = note.Note('A3', duration=duration.Duration('eighth'))
as3_eighth = note.Note('A#3', duration=duration.Duration('eighth'))

bf3_eighth = note.Note('B-3', duration=duration.Duration('eighth'))
b3_eighth  = note.Note('B3', duration=duration.Duration('eighth'))
bs3_eighth = note.Note('B#3', duration=duration.Duration('eighth'))

# Eighth-note versions for Octave 4
cf4_eighth = note.Note('C-4', duration=duration.Duration('eighth'))
c4_eighth  = note.Note('C4', duration=duration.Duration('eighth'))
cs4_eighth = note.Note('C#4', duration=duration.Duration('eighth'))

df4_eighth = note.Note('D-4', duration=duration.Duration('eighth'))
d4_eighth  = note.Note('D4', duration=duration.Duration('eighth'))
ds4_eighth = note.Note('D#4', duration=duration.Duration('eighth'))

ef4_eighth = note.Note('E-4', duration=duration.Duration('eighth'))
e4_eighth  = note.Note('E4', duration=duration.Duration('eighth'))
es4_eighth = note.Note('E#4', duration=duration.Duration('eighth'))

ff4_eighth = note.Note('F-4', duration=duration.Duration('eighth'))
f4_eighth  = note.Note('F4', duration=duration.Duration('eighth'))
fs4_eighth = note.Note('F#4', duration=duration.Duration('eighth'))

gf4_eighth = note.Note('G-4', duration=duration.Duration('eighth'))
g4_eighth  = note.Note('G4', duration=duration.Duration('eighth'))
gs4_eighth = note.Note('G#4', duration=duration.Duration('eighth'))

af4_eighth = note.Note('A-4', duration=duration.Duration('eighth'))
a4_eighth  = note.Note('A4', duration=duration.Duration('eighth'))
as4_eighth = note.Note('A#4', duration=duration.Duration('eighth'))

bf4_eighth = note.Note('B-4', duration=duration.Duration('eighth'))
b4_eighth  = note.Note('B4', duration=duration.Duration('eighth'))
bs4_eighth = note.Note('B#4', duration=duration.Duration('eighth'))

# Eighth-note versions for Octave 5
cf5_eighth = note.Note('C-5', duration=duration.Duration('eighth'))
c5_eighth  = note.Note('C5', duration=duration.Duration('eighth'))
cs5_eighth = note.Note('C#5', duration=duration.Duration('eighth'))

df5_eighth = note.Note('D-5', duration=duration.Duration('eighth'))
d5_eighth  = note.Note('D5', duration=duration.Duration('eighth'))
ds5_eighth = note.Note('D#5', duration=duration.Duration('eighth'))

ef5_eighth = note.Note('E-5', duration=duration.Duration('eighth'))
e5_eighth  = note.Note('E5', duration=duration.Duration('eighth'))
es5_eighth = note.Note('E#5', duration=duration.Duration('eighth'))

ff5_eighth = note.Note('F-5', duration=duration.Duration('eighth'))
f5_eighth  = note.Note('F5', duration=duration.Duration('eighth'))
fs5_eighth = note.Note('F#5', duration=duration.Duration('eighth'))

gf5_eighth = note.Note('G-5', duration=duration.Duration('eighth'))
g5_eighth  = note.Note('G5', duration=duration.Duration('eighth'))
gs5_eighth = note.Note('G#5', duration=duration.Duration('eighth'))

af5_eighth = note.Note('A-5', duration=duration.Duration('eighth'))
a5_eighth  = note.Note('A5', duration=duration.Duration('eighth'))
as5_eighth = note.Note('A#5', duration=duration.Duration('eighth'))

bf5_eighth = note.Note('B-5', duration=duration.Duration('eighth'))
b5_eighth  = note.Note('B5', duration=duration.Duration('eighth'))
bs5_eighth = note.Note('B#5', duration=duration.Duration('eighth'))

c_maj = {c4, d4, e4, f4, g4, a4, b4, c5, d5, e5, f5, g5, a5, b5}
g_maj = {c4, d4, e4, fs4, g4, a4, b4, c5, d5, e5, fs5, g5, a5, b5}
d_maj = {cs4, d4, e4, fs4, g4, a4, b4, cs5, d5, e5, fs5, g5, a5, b5}
a_maj = {cs4, d4, e4, fs4, gs4, a4, b4, cs5, d5, e5, fs5, gs5, a5, b5}
f_maj = {c4, d4, e4, f4, g4, a4, bf4, c5, d5, e5, f5, g5, a5, bf5}
bf_maj = {c4, d4, ef4, f4, g4, a4, bf4, c5, d5, ef5, f5, g5, a5, bf5}
ef_maj = {c4, d4, ef4, f4, g4, af4, bf4, c5, d5, ef5, f5, g5, af5, bf5}

#testing
def bach():
    s = corpus.parse('bach/bwv65.2.xml')
    s.analyze('key')
    s.show('midi')
    fVoices = stream.Part((s.parts['Soprano'], s.parts['Alto'])).chordify()
    mVoices = stream.Part((s.parts['Tenor'], s.parts['Bass'])).chordify()
    chorale2p = stream.Score((fVoices, mVoices))
    chorale2p.show()
def streamtest():
    s1 = stream.Stream()
    s1.append([cf3, c3, cs3])
    s1.append(d3)
    s1.show()
def rhythmtest():
    rhalfDuration = duration.Duration('half')
    rquarterDuration = duration.Duration('quarter')
    newNote = note.Note('C4')
    #newNote.quarterLength = rhalfDuration
    newNote.duration = duration.Duration(.25)
    newNote.show()
def attributes(n):
    print(n.pitch)
    print(n.duration)
    print(n.octave)
    print(n.pitch.spanish)
def simpleMelody():
    s = stream.Stream()
    # Hot Cross Buns in G major:
    # Phrase 1: G4, G4, G4, E4
    # Phrase 2: G4, G4, G4, E4
    # Phrase 3: F4, F4, E4, E4
    # Phrase 4: D4, D4, C4, C4
    c_eighth = note.Note('C5', duration = duration.Duration('eighth'))

    #c_eighth.duration = duration.Duration('eighth')
    d_eighth = note.Note('D5')
    d_eighth.duration = duration.Duration('eighth')
    melody = [
        e5, d5, c5, quarter_rest,
        e5, d5, c5, quarter_rest,
        c_eighth,c_eighth,c_eighth,c_eighth,d_eighth,d_eighth,d_eighth,d_eighth,
        e5, d5, c5, quarter_rest,
    ]
    for n in melody:
        s.repeatAppend(n,1)
    s.show()
    #s.show('midi')
def random_melody_in_key(key):
    s = stream.Stream()
    notes = list(key)
    for i in range(16):
        n = random.choice(notes)
        s.repeatAppend(n,1)
    s.show()
    s.show('midi')
    
def create_score(piano_stream: stream.Part, violin_stream: stream.Part) -> stream.Score:
    """
    Takes two music21 streams and returns a score with Piano and Violin parts.

    Parameters:
        piano_stream (music21.stream.Stream): The stream to assign as Piano part
        violin_stream (music21.stream.Stream): The stream to assign as Violin part

    Returns:
        music21.stream.Score: Combined score with piano and violin parts
    """
    # Assign instruments
    piano_part = piano_stream
    piano_part.insert(0, instrument.Piano())

    violin_part = violin_stream
    violin_part.insert(0, instrument.Violin())

    # Create the score
    full_score = stream.Score()
    full_score.insert(0, piano_part)
    full_score.insert(0, violin_part)

    full_score.show()
    return full_score

sample_response1 = """C4 eighth,E4 eighth,G4 quarter,E4 eighth,F4 16th,G4 16th,A4 eighth,G4 eighth,
E4 quarter,rest eighth,C4 eighth,E4 eighth,F4 eighth,G4 eighth,E4 eighth,D4 eighth,
C4 quarter,rest eighth,C5 eighth,A4 eighth,F4 quarter,E4 eighth,C4 half"""

sample_response2 = """C4 eighth,G4 eighth,E4 eighth,A4 quarter,rest eighth,F4 eighth,G4 eighth,B4 eighth,
C5 quarter,rest eighth,E4 eighth,G4 quarter,F4 eighth,E4 eighth,
D4 quarter,C4 eighth,E4 eighth,D4 quarter,C4 half"""

sample_response_sad_aminor = """A4 quarter,C5 eighth,B4 16th,A4 16th,F4 eighth,E4 eighth,
G4 quarter,rest eighth,A4 eighth,C5 eighth,E5 eighth,D5 eighth,C5 eighth,
B4 quarter,rest eighth,A4 eighth,E5 eighth,C5 eighth,D5 quarter,A4 quarter"""

sample_response_sad_dminor = """D4 quarter,F4 eighth,D5 quarter,B-4 eighth,G4 eighth,A4 quarter,
rest eighth,C5 eighth,B-4 eighth,A4 eighth,F4 quarter,E4 quarter,D4 quarter"""

sample_response_exciting_emajor = """E4 quarter,F#4 eighth,G#4 eighth,A4 quarter,G#4 eighth,F#4 eighth,
E4 quarter,rest 16th,E4 16th,F#4 16th,G#4 16th,A4 16th,B4 16th,C#5 16th,D#5 16th,
E5 quarter,rest eighth,B4 eighth,E5 quarter,E4 quarter"""

sample_response_varied = """E4 eighth,G#4 16th,F#4 16th,E4 eighth,rest 16th,C#4 eighth,D#4 eighth,
E4 quarter,B3 eighth,C#4 eighth,D#4 eighth,E4 eighth,F#4 quarter,rest eighth,
G#4 quarter,E4 half"""

def generate_response(mood_description):
    prompt = (
    f"Compose a melody using note-duration pairs in this format: "
    f"E4 quarter,rest eighth,E4 eighth,F4 eighth,G4 eighth,A4 eighth,B4 eighth,C5 eighth,D5 quarter. "
    f"Write a melody that captures the following mood: '{mood_description}'. Use a variety of rhythms, intervals (not just scalar motion), and phrasing. The melody should sound natural and musically expressive."
    f"Use a comma-separated string of note-duration pairs with no space after commas. "
    f"Every pitch must have a duration, and the melody must start and end on the tonic pitch. "
    f"The melody must be syntactically complete (no dangling notes) and follow consistent formatting."
)
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": (
        "You are a music composition assistant that writes single-line melodies using a comma-separated string of note-duration pairs. "
        "Each note must follow the format 'NOTE DURATION' with no space after the comma (e.g., E4 quarter,F#4 eighth). "
        "Durations must be valid values from the music21 library (e.g., quarter, half, eighth, 16th, etc.). "
        "Every pitch must include a duration, and no pitch should appear without a corresponding duration. "
        "If a key is specified, the melody must start and end on the tonic (e.g., C4 in C major, A4 in A minor). "
        "Avoid trailing commas or incomplete phrases. The melody should be syntactically complete and musically satisfying."
        )},
        {"role": "user", "content": "Write a joyful melody with syncopation and leaps, E major"},
        {"role": "assistant", "content": sample_response_varied},
        {"role": "user", "content": "Write a long melody in a happy mood, C major, imitating Bach’s style, meaning stepwise motion, sequences, motivic repetition, and some implied harmonic progressions"},
        {"role": "assistant", "content": sample_response1},
        {"role": "user", "content": "Write a melody in a happy mood, C major, imitating Bach’s style"},
        {"role": "assistant", "content": sample_response2},
        {"role": "user", "content": "Write a melody in a sad mood, A minor"},
        {"role": "assistant", "content": sample_response_sad_aminor},
        {"role": "user", "content": "Write a melody in a sad, expressive, mood, D minor"},
        {"role": "assistant", "content": sample_response_sad_dminor},
        {"role": "user", "content": "Write a melody in an exciting mood, E major"},
        {"role": "assistant", "content": sample_response_exciting_emajor},
        {"role": "user", "content": prompt}
    ],
    max_tokens=120)
    return response.choices[0].message.content
def parse_response(response):
    print("melody:" + response)
    res = []
    note_sequence = response.split(",")
    for pair in note_sequence:
        note_duration_pair = pair.split(" ")
        if len(note_duration_pair) < 2:
            print("RESPONSE NOT PARSEABLE")
            continue
        res.append((note_duration_pair[0], note_duration_pair[1]))
    return res
def compose_from_notes(note_duration_pairs):
    s = stream.Stream()
    for n, d in note_duration_pairs:
        if n == 'rest':
            s.append(note.Rest(d))
        else:
            s.append(note.Note(n, duration=duration.Duration(d)))
    # s.show()
    # s.show('midi')
    return s
def compose_with_llm(mood_description):
    return compose_from_notes(parse_response(generate_response(mood_description))
)
def test_sample_response(response):
    return compose_from_notes(parse_response(response))
    
    
def melody_in_key(key, mood_description):
    s = stream.Stream()
    # Get a note sequence from the LLM
    #note_sequence_str = compose_with_llm(mood_description)
    #note_sequence_str = "c4 e4 g4 c5 quarter_rest e4 g4 a4 quarter_rest d5 b4 c5 quarter_rest g4 a4 f4 quarter_rest e4 g4 c5"
    #note_sequence_str = "c4_eighth e4_eighth g4 quarter_rest g4_eighth a4_eighth b4 quarter_rest c5_eighth d5_eighth e5 quarter_rest e4_eighth f4_eighth g4 quarter_rest g4_eighth a4_eighth c5 quarter_rest"
#     note_sequence_str = """c4_eighth e4_eighth g4 quarter_rest g4_eighth a4_eighth b4 quarter_rest c5_eighth d5_eighth e5 quarter_rest 
# e4_eighth f4_eighth g4 quarter_rest g4_eighth a4_eighth c5 quarter_rest 

# e4_eighth g4_eighth a4_eighth b4_eighth c5 quarter_rest d5_eighth e5_eighth f5_eighth g5_eighth a5 quarter_rest 
# g5_eighth f5_eighth e5_eighth d5_eighth c5 quarter_rest 

# b4_eighth g4_eighth a4 quarter_rest e4_eighth g4_eighth c5 quarter_rest 
# d5_eighth b4_eighth c5_eighth a4_eighth g4_eighth e4_eighth f4 quarter_rest 

# e4_eighth f4_eighth g4 quarter_rest a4_eighth b4_eighth c5 quarter_rest d5_eighth e5_eighth f5 quarter_rest 
# g5_eighth f5_eighth d5_eighth b4_eighth c5_eighth a4_eighth g4 quarter_rest"""
    note_sequence_str = """c4_eighth d4_eighth e4_eighth f4_eighth g4_eighth f4_eighth e4_eighth d4_eighth 
c4 quarter_rest e4_eighth f4_eighth g4_eighth a4_eighth b4_eighth c5_eighth d5_eighth 
e5 quarter_rest g4_eighth a4_eighth b4_eighth c5_eighth d5_eighth b4_eighth c5_eighth a4_eighth 

g4 quarter_rest e4_eighth f4_eighth g4_eighth a4_eighth f4_eighth g4_eighth e4_eighth d4 quarter_rest 
f4_eighth g4_eighth a4_eighth b4_eighth g4_eighth a4_eighth f4_eighth g4 quarter_rest 

c4_eighth d4_eighth e4_eighth c4_eighth f4_eighth e4_eighth d4_eighth b3_eighth 
c4 quarter_rest e4_eighth d4_eighth f4_eighth e4_eighth g4_eighth f4_eighth a4_eighth g4_eighth 

b4 quarter_rest c5_eighth a4_eighth b4_eighth g4_eighth a4_eighth f4_eighth g4_eighth e4 quarter_rest 
d4_eighth e4_eighth f4_eighth g4_eighth a4_eighth b4_eighth c5_eighth d5_eighth 

e5 quarter_rest d5_eighth b4_eighth c5_eighth a4_eighth g4_eighth f4_eighth e4 quarter_rest
"""
    # paragraphs = note_sequence_str.strip().split('\n\n')

    # substreams = []

    # for para in paragraphs:
    #     s = stream.Stream()
    #     note_names = para.strip().split()
    #     for name in note_names:
    #         try:
    #             note_obj = globals()[name]
    #             s.repeatAppend(note_obj, 1)
    #         except KeyError:
    #             print(f"Warning: Note variable '{name}' is not defined.")
    #     substreams.append(s)

    # # Create a stream of streams
    # main_stream = stream.Stream()
    # for sub in substreams:
    #     main_stream.append(sub)
    # main_stream.show()
    # main_stream.show('midi')
    note_names = note_sequence_str.split()
    for name in note_names:
        try:
            note_obj = globals()[name]
            s.repeatAppend(note_obj,1)
        except KeyError:
            print(f"Warning: Note variable '{name}' is not defined.")
    s.show()
    s.show('midi')

if __name__ == '__main__':
    # random_melody_in_key(c_maj)
    # melody_in_key(c_maj, 'happy')
    # response = generate_response('happy')
    # print(compose_with_llm("long melody, happy, exciting, D Major"))
    violin_stream = test_sample_response(sample_response1)
    piano_stream = test_sample_response(sample_response1)
    full_score = create_score(piano_stream, violin_stream)