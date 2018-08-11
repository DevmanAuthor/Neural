import pygame
import os


def load_image(pic):
    return pygame.image.load(os.path.join('gfx', pic))


class socket(object):
    def __init__(self, bodypart, point):
        self.pos = (bodypart.pos[0] + point[0], bodypart.pos[1] + point[1])


class BodyPart:
    def __init__(self, gfx, bodypart_socket=None, num=None, pos=(0, 0)):
        self.pos = pos
        self.gfx = load_image(gfx)
        self.sockets = list()
        if bodypart_socket is not None and num is not None:
            self.lock_to_socket(bodypart_socket, num)

    def add_socket(self, *pos):
        for x, y in pos:
            self.sockets.append(socket(self, (x, y)))

    def lock(self, pos):
        self.pos = pos

    def lock_to_socket(self, bodypart, socketnumber):
        self.pos = bodypart.sockets[socketnumber].pos

             
class Default_Entity:
    def __init__(self, head, torso, arm_l, arm_r, legs, pos, *bodyparts):
        self.pos = pos
        self.head = BodyPart(head, None, None, pos)
        self.head.add_socket((0, 8))

        self.torso = BodyPart(torso, self.head, 0)
        self.torso.add_socket((-8, 0), (8, 0), (0, 8))

        self.arm_l = BodyPart(arm_l, self.torso, 0)
        self.arm_r = BodyPart(arm_r, self.torso, 1)
        self.legs = BodyPart(legs, self.torso, 2)

        self.Body = list()
        self.add_bodypart(self.head, self.torso, self.arm_l, self.arm_r, self.legs)

    def draw_bodypart(self, bodypart, screen):
        screen.blit(bodypart.gfx, bodypart.pos)

    def add_bodypart(self, *bodyparts):
        for item in bodyparts:
            self.Body.append(item)

    def draw_Body(self, screen):
        for i in range(len(self.Body)):
                self.draw_bodypart(self.Body[i], screen)

    def Run(self, screen):

        self.draw_Body(screen)

        print("\n\n\n Entity base position: ", self.pos)
        print("Head position: ", self.head.pos)
        print("Torso position: ", self.torso.pos)
        print("Arm(L) position: ", self.arm_l.pos)
        print("Arm(R) position: ", self.arm_r.pos)
        print("Legs position: ", self.legs.pos)


class Guy(Default_Entity):
    def __init__(self):
        pass