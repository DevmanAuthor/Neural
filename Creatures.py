import Entity
import Stats


BugBear = Entity.Organism("Some Guy", Stats.Being, (0, 0), "gfx/guy.png")

List = {BugBear: 5}


def load():
    BugBear.body.create("Head", "Torso", "Arm")


def draw(sheet):
    BugBear.draw(sheet)
