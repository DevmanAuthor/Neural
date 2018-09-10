import Entity
import Stats
import System

BugBear = Entity.Walkable("Some Guy", Stats.Being, (System.width/2, System.height/2))

List = {BugBear: 5}


def load():
    BugBear.body.create("Head", "Torso", "Arm")


def draw(sheet):
    for i in List:
        i.draw(sheet)


def run():
    for i in List:
        i.run()