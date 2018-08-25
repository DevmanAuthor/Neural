import Entity
import Stats


BugBear = Entity.Organism("Some Guy", Stats.Being, (51, 51), "gfx/guy.png")

List = {BugBear: 5}


def Load():
    BugBear.body.create("Head", "Torso", "Arm")


