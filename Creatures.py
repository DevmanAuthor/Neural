import Object
import Entity


BugBear = Entity.Organism("Some Guy", {1: 2}, (50, 50), "gfx/guy.png")

Creatures = (BugBear)


def Load():
    BugBear.body.create("Head", "Torso", "Arm")


Load()