import Entity
import Stats


BugBear = Entity.Organism("Some Guy", Stats.Being, (51, 51), "gfx/guy.png")

List = {BugBear: 5}


def load():
    BugBear.body.create("Head", "Torso", "Arm")


def draw(sheet):
    for i in List:
        i.draw(sheet)
