
class Band:
    def __init__(self,name="unknown",members=None):
        self.name = name
        self.members = members or []

    def __str__(self):
        band_musicians = [str(musician) for musician in self.musicians]
        return " ".join(band_musicians)

    def __repr__(self):
        return f"Band({self.musicians})"

    def play_solos(self):
        solos=[]
        for member in self.members:
            solos.append(member.solo)
        return solos


class Musician:
    def __init__(self, name, instrument, playing, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo
        self.playing = playing

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.playing} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo}"


class Guitarist(Musician):
    def __init__(self, name="unknown"):
        super().__init__(name, "guitar", "Guitarist", "face melting guitar solo")

    # def __init__(self,name="unknown", instrument="guitar"):
    #     self.name = name
    #     self.instrument = instrument
    #
    # def __repr__(self):
    #     return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):

    def __init__(self, name="unknown"):
        super().__init__(name, "bass", "Bassist", "bom bom buh bom")
    #
    # def __repr__(self):
    #     return f"Bassist instance. Name = {self.name}"
    #
    # def play_solo(self):
    #     return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name="unknown"):
        super().__init__(name, "drums", "Drummer", "face melting guitar solo")
    #
    # def __repr__(self):
    #     return f"Drummer instance. Name = {self.name}"
    #
    # def play_solo(self):
    #     return "rattle boom crash"