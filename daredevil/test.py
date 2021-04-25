import numpy as np
import sounddevice as sd
from scipy.io import wavfile


class SoundPrimitive:
    def __init__(self, file=None):
        self.samplerate, self.sound = wavfile.read('/home/vladyslav/Documents/Diploma/daredevil/test.wav')
        if file:
            self.sound = wave.open(file, 'r')

    def pitch_shift(self, semitones):
        sound_array = self.sound
        factor = 2**(1.0 * semitones / 12.0)
        indices = np.round( np.arange(0, len(sound_array), factor) )
        indices = indices[indices < len(sound_array)].astype(int)
        self.sound = sound_array[indices.astype(int)]
        return self

    def play(self):
        sd.play(self.sound, self.samplerate, blocking=True)
        return self

if __name__ == "__main__":
    sp = SoundPrimitive()

    sp.pitch_shift(2).play()
