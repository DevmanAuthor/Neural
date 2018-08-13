import pygame
import os


def calc_abs_rect(x, y, w, h):
    return(x, y, x+w, y+h)


def offset_origin(pos1, pos2):
    return(pos1[0] + pos2[0], pos1[1] + pos2[1])


def load_image(picdir):
    return pygame.image.load(picdir)


class socket(object):
    def __init__(self, bodypart, point):
        self.pos = (bodypart.x + point[0], bodypart.y + point[1])


class BodyPart:
    def __init__(self, name, gfxpath, pos=(0, 0)):
        self.name = name
        self.pos = pos
        self.gfx = load_image(gfxpath)
        self.sockets = list()

    def add_socket(self, *pos):
        for x, y in pos:
            self.sockets.append(socket(self, (x, y)))

    def lock_socket(self, socket, pos):
        self.socket = pos

    def lock_to_socket(self, bodypart, socketnumber):
        self.pos = bodypart.sockets[socketnumber].pos

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]
        

class Default_Entity:
    def __init__(self, name, pos=(0, 0)):
        self.name = name
        self.pos = pos
        self.Body = list()
        
    def draw_bodypart(self, bodypart, screen):
        screen.blit(bodypart.gfx, bodypart.pos)

    def add_to_body(self, *bodyparts):
        for item in bodyparts:
            self.Body.append(item)

    def draw_Body(self, screen):
        for i in range(len(self.Body)):
                self.draw_bodypart(self.Body[i], screen)

    def debug_self_position(self):
        print("\n==================\n" + self.name + "'s position: ", self.pos, "\n-------------")
        for i in range(len(self.Body)):
                print(self.Body[i].name + "'s position: ", self.Body[i].pos)

    def Run(self, screen):
        self.draw_Body(screen)
        pygame.draw.rect(screen, (0, 0, 225), self.rect, 1)
        
    def update_rect(self):
        x, y, j, k = float("inf"), float("inf"), 0, 0
        for i in range(len(self.Body)):
            if (self.Body[i].x < x):
                x = self.Body[i].x
            if (self.Body[i].y < y):
                y = self.Body[i].y    # resolve x and y

        for i in range(len(self.Body)):
            xx = (self.Body[i].x + self.Body[i].gfx.get_width())
            yy = (self.Body[i].y + self.Body[i].gfx.get_height())
            if (j < xx):
                j = xx
            if (k < yy):
                k = yy    # resolve j and k
        w = j - x
        h = k - y                           # resolve w and h
        return (x, y, w, h)

    @property
    def x(self):
        return self.pos[0]
    
    @property
    def y(self):
        return self.pos[1]

    @property
    def rect(self):
        return self.update_rect()
        

class Guy(Default_Entity): 
    def Load(self, head, torso, arm_l, arm_r, leg_l, leg_r):
        self.head = BodyPart("Head", head, self.pos)
        self.head.add_socket((-2, 2))

        self.torso = BodyPart("Torso", torso, self.head.sockets[0].pos)
        self.torso.add_socket((self.torso.gfx.get_width()-3, -1), (-2, -1), ((self.torso.gfx.get_width()/2)+1, self.torso.gfx.get_height()), (1, self.torso.gfx.get_height()))

        self.arm_l = BodyPart("(L)Arm", arm_l, self.torso.sockets[0].pos)
        self.arm_r = BodyPart("(R)Arm", arm_r, self.torso.sockets[1].pos)
        self.leg_l = BodyPart("(L)Leg", leg_l, self.torso.sockets[2].pos)
        self.leg_r = BodyPart("(R)Leg", leg_r, self.torso.sockets[3].pos)
        self.add_to_body(self.leg_l, self.leg_r, self.arm_l, self.arm_r, self.torso, self.head)
        self.head.pos = (0, 0)