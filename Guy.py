
class Guy:
    def __init__(self):
        self.emotions = dict(shame=0, fear=0, pain=0, grief=0, joy=0, mood=0)

    def Run(self):
        self.emotions.mood = (self.emotions.griefa / self.emotions.joy)
