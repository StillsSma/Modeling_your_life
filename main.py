import time

class Instrument:
    def __init__(self):
        pass

    def make_noise(self):
        return self.make_noise

class Guitar(Instrument):
    def __init__(self):
        self.loudness = 10
        self.strings = 6
    def noise(self):
        return "WIDDILLEEEWIDDDILLEEEWAAAAAAAAAHHHHHHH"
    def __add__(self,other):
        return self.loudness + other.loudness

class Acoustic_Guitar(Guitar):
    def __init__(self):
        self.loudness = 4
    def noise(self):
        return "thwakathwakaTWAKAthwakathwakathwakaTHWAKAthwaka"
    def __add__(self,other):
        return self.loudness + other.loudness
class Bass_Guitar(Guitar):
    def __init__(self):
        self.strings = 4
        self.loudness = 8
    def noise(self):
        return "BOOOWBOOOOMBOOOW"
    def __add__(self,other):
        return self.loudness + other.loudness

class Drumset(Instrument):
    def __init__(self):
        self.loudness = 15
    def noise(self):
        return "BLATDADABLATDADABLATDADABLAT"
    def __add__(self,other):
        return self.loudness + other.loudness

class Band:
    def __init__(self):
        self.instruments = []
        self.loudness = 0
    def add_instrument(self,instrument):
        self.instruments.append(instrument)
    def volume(self):
        for instrument in self.instruments:
            self.loudness += instrument.loudness
        return self.loudness


rockband = Band()

rockband.add_instrument(Bass_Guitar())
rockband.add_instrument(Drumset())
rockband.add_instrument(Guitar())
rockband.add_instrument(Acoustic_Guitar())

print(rockband.volume())

for instrument in rockband.instruments:
    print(instrument.noise())
    time.sleep(1)
