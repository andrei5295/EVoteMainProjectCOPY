class Candidate:

    voteCount = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def addVoteCount(self):
        self.voteCount += 1