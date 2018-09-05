class Scene():
    def __init__(self, active):
        self.nextscene = self
        self.active = active

    def Handle_Events(self, events):
        raise NotImplementedError
    
    def Update():
        raise NotImplementedError

    def Draw(self, sheet):
        raise NotImplementedError

    def Birth_Scene(self, scene):
        scene.active = True
        
    def Change_Scene(self, scene):
        scene.active = True
        self.Kill(self)
    
    def Kill(self, scene):
        scene.active = False


class SceneManager(list, object):
    def __init__(self, scene_listing):
        self.scene_listing = scene_listing
        for i in scene_listing:
            self.append(i)

    def Handle_Scene_Events(self, event):
        for i in self:
                i.Handle_Events(event)  

    def check_active(self):
        for i in self:
            if i.active is False:
                self.remove(i)
        for i in self.scene_listing:
            if i.active is True and i not in self:
                self.append(i)
  
    def Draw(self, sheet):
        for i in range(len(self)):
            self[i].Draw(sheet)
            
        