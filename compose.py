from dotenv import load_dotenv
import os
load_dotenv()

from music21 import *
from music21 import note, stream, duration, instrument

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

sample_response1 = """C4 eighth,E4 eighth,G4 quarter,E4 eighth,F4 16th,G4 16th,A4 eighth,G4 eighth,E4 quarter,rest eighth,C4 eighth,E4 eighth,F4 eighth,G4 eighth,E4 eighth,D4 eighth,C4 quarter,rest eighth,C5 eighth,A4 eighth,F4 quarter,E4 eighth,C4 half"""

sample_response2 = """C4 eighth,G4 eighth,E4 eighth,A4 quarter,rest eighth,F4 eighth,G4 eighth,B4 eighth,C5 quarter,rest eighth,E4 eighth,G4 quarter,F4 eighth,E4 eighth,D4 quarter,C4 eighth,E4 eighth,D4 quarter,C4 half"""

sample_response_sad_aminor = """A4 quarter,C5 eighth,B4 16th,A4 16th,F4 eighth,E4 eighth,G4 quarter,rest eighth,A4 eighth,C5 eighth,E5 eighth,D5 eighth,C5 eighth,B4 quarter,rest eighth,A4 eighth,E5 eighth,C5 eighth,D5 quarter,A4 quarter"""

sample_response_sad_dminor = """D4 quarter,F4 eighth,D5 quarter,B-4 eighth,G4 eighth,A4 quarter,rest eighth,C5 eighth,B-4 eighth,A4 eighth,F4 quarter,E4 quarter,D4 quarter"""

sample_response_exciting_emajor = """E4 quarter,F#4 eighth,G#4 eighth,A4 quarter,G#4 eighth,F#4 eighth,E4 quarter,rest 16th,E4 16th,F#4 16th,G#4 16th,A4 16th,B4 16th,C#5 16th,D#5 16th,E5 quarter,rest eighth,B4 eighth,E5 quarter,E4 quarter"""

sample_response_varied = """E4 eighth,G#4 16th,F#4 16th,E4 eighth,rest 16th,C#4 eighth,D#4 eighth,E4 quarter,B3 eighth,C#4 eighth,D#4 eighth,E4 eighth,F#4 quarter,rest eighth,G#4 quarter,E4 half"""

tokyo_walk_emajor = """E4 eighth,F#4 16th,G#4 16th,A4 eighth,rest 16th,C#5 16th,B4 16th,A4 16th,
G#4 quarter,rest eighth,E4 eighth,G#4 eighth,F#4 eighth,A4 quarter,
B4 eighth,C#5 16th,D#5 16th,E5 eighth,rest 16th,F#5 16th,E5 16th,D#5 16th,
C#5 quarter,B4 eighth,G#4 eighth,A4 quarter,E4 quarter,
rest eighth,B3 eighth,E4 eighth,F#4 eighth,G#4 eighth,F#4 16th,E4 16th,
C#4 quarter,E4 quarter
"""

def generate_response(mood_description):
    #prompt = mood_description
    prompt = (
    f"Compose a melody using note-duration pairs in this format: "
    f"E4 quarter,rest eighth,E4 eighth,F4 eighth,G4 eighth,A4 eighth,B4 eighth,C5 eighth,D5 quarter"
    f"Write a melody that captures the following mood: '{mood_description}'. Use a variety of rhythms, intervals (not just scalar motion), and phrasing. The melody should sound natural and musically expressive."
    f"Use a comma-separated string of note-duration pairs with no space after commas. "
    f"Every pitch must have a duration, and the melody must start and end on the tonic pitch. "
    f"The melody must be syntactically complete (no dangling notes) and follow consistent formatting."
)
    response = client.chat.completions.create(model="gpt-4.1",
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
        {"role": "user", "content": "Write a melody like I am walking down a sunny street in Boston, C major"},
        {"role": "assistant", "content": sample_response2},
        {"role": "user", "content": "Write a melody in a sad mood, A minor"},
        {"role": "assistant", "content": sample_response_sad_aminor},
        {"role": "user", "content": "Write a melody in a sad, expressive, mood, D minor"},
        {"role": "assistant", "content": sample_response_sad_dminor},
        {"role": "user", "content": "Write a melody in an exciting mood, E major"},
        {"role": "assistant", "content": sample_response_exciting_emajor},
        {"role": "user", "content": "Write a melody that feels like I'm walking down a sunny street in Tokyo, E major"},
        {"role": "assistant", "content": tokyo_walk_emajor},
        {"role": "user", "content": prompt}
    ],
    max_tokens=120)
    return response.choices[0].message.content
def parse_response(response):
    print("Melody: " + response)
    res = []
    note_sequence = response.split(",")
    for pair in note_sequence:
        note_duration_pair = pair.split(" ")
        if len(note_duration_pair) < 2:
            print("RESPONSE NOT PARSEABLE")
            continue
        res.append((note_duration_pair[0], note_duration_pair[1]))
    return res
def compose_from_notes(note_duration_pairs, play=False):
    s = stream.Stream()
    for n, d in note_duration_pairs:
        if n == 'rest':
            s.append(note.Rest(d))
        else:
            s.append(note.Note(n, duration=duration.Duration(d)))
    s.show()
    if play:
        s.show('midi')
    return s

def compose_part_from_notes(note_duration_pairs):
    s = stream.Part()
    for n, d in note_duration_pairs:
        if n == 'rest':
            s.append(note.Rest(d))
        else:
            s.append(note.Note(n, duration=duration.Duration(d)))
    return s

def make_score(part1, part2, part3, play=False):
    score = stream.Score()
    score.insert(meter.TimeSignature("4/4"))
    score.append(part1)
    score.insert(0, part2)
    score.insert(0, part3)
    score.show()
    if play:
        score.show('midi')
    return score

def compose_with_llm(mood_description, play=False):
    return compose_from_notes(parse_response(generate_response(mood_description)), play)
def test_sample_response(response):
    return compose_from_notes(parse_response(response))
def compose_part_with_llm(mood_description):
    return compose_part_from_notes(parse_response(generate_response(mood_description)))
def part_from_response(response):
    return compose_part_from_notes(parse_response(response))

if __name__ == '__main__':
    # prompt = "Write a melody that feels like I'm happily walking down the streets of Boston, E major"
    # compose_with_llm(prompt, True)
    
    
    part1 = compose_part_with_llm("Happy melody, D major")
    part2 = compose_part_with_llm("Energetic melody, D major")
    part3 = compose_part_with_llm("Sad melody, D major")
    full_score = make_score(part1, part2, part3, False)