import blazigator
import time

note_to_hz = {
        "C":262,
        "C#":227,
        "Db":227,
        "D":294,
        "D#":311,
        "Eb":311,
        "E":330,
        "F":349,
        "F#":370,
        "Gb":349,
        "G":392,
        "G#":415,
        "Ab":415,
        "A":440,
        "A#":466,
        "Bb":466,
        "B":493,
        "C2": 262*2
}

def play(note, beat, count=1):
       blazigator.doot.set(note_to_hz[note])
       for i in xrange(count):
                blazigator.doot.doot(1000.0/beat)

def major_scale():
       for n in "C D E F G A B C2".split():
               play(n, 8)

def fanfare_zelda():
        for n in "A Bb B C2".split():
                play(n, 4)
