import System


class Scene():
    def __init__(self, active=False, layer=0):
        self.nextscene = self
        self.active = active

    def handle_events(self, events):
        raise NotImplementedError
    
    def update(self):
        pass

    def draw(self, sheet):
        raise NotImplementedError

    def show_scene(self, scene):
        if scene.active is False:
            scene.active = True
        else:
            pass
        
    def change_scene(self, scene):
        scene.active = True
        self.kill(self)
    
    def kill(self, scene):
        scene.active = False


class SceneManager(list, object):
    def __init__(self, scene_listing):
        self.scene_listing = scene_listing
        for i in scene_listing:
            self.append(i)

    def handle_events(self, event):
        for i in self:
                i.handle_events(event)  

    def check_active(self):
        for i in self:
            if i.active is False:
                self.remove(i)
        for i in self.scene_listing:
            if i.active is True and i not in self:
                self.append(i)

    def update(self):
        for i in self:
            i.update()

    def draw(self, sheet):
        for i in range(len(self)):
            self[i].draw(sheet)
            
        