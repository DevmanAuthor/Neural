class Scene():
    def __init__(self):
        self.nextscene = self

    def Handle_Events(self, events):
        raise NotImplementedError
    
    def Update():
        raise NotImplementedError

    def Draw(self, sheet):
        raise NotImplementedError

    def Change_Scene(self, scene):
        self.nextscene = scene
    
    def Kill(self):
        self.nextscene = None
    

class Scene_Manager(dict):
    def __init__(self, scene):
        self.current_scene = scene
    
    def load(self, *args):
        self.current_scene.load(*args)

    def run(self, *args):
        self.current_scene.run(*args)
    
    def draw(self, *args):
        self.current_scene.draw(*args)
    
    def change_scene(self, scene, *args):
        self.current_scene = scene
        self.current_scene.load(args)

