import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
WIDTH = 16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.2
FRAMES_PER_FFT = 16
SAMPLES_PER_FFT = CHUNK * FRAMES_PER_FFT
FREQ_STEP = float(RATE) / SAMPLES_PER_FFT

NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()

NOTE_MIN = 40
NOTE_MAX = 100



def freq_to_number(f): return 69 + 12 * np.log2(f / 440.0)


def number_to_freq(n): return 440 * 2.0 ** ((n - 69) / 12.0)


def note_name(n): return NOTE_NAMES[n % 12] + str(n / 12 - 1)


def note_to_fftbin(n): return number_to_freq(n) / FREQ_STEP


imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN - 1))))
imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX + 1))))

buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)





def record():

        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paInt16,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK)


        window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, SAMPLES_PER_FFT, False)))

        binFqs = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            buf[:-CHUNK] = buf[CHUNK:]
            data = stream.read(CHUNK)
            stream.write(data, CHUNK)
            buf[-CHUNK:] = np.frombuffer(stream.read(CHUNK), np.int32)

            fft = np.fft.rfft(buf * window)

            freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

            n = freq_to_number(freq)
            n0 = int(round(n))
            binFqs.append(n0)

        res = max(set(binFqs), key=binFqs.count)
        return note_name(res)
