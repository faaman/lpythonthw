class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Adventure(Scene):

    def enter(self):
        pass

class HQ(Scene):

    def enter(self):
        pass

class Library(Scene):

    def enter(self):
        pass

class Chute(Scene):

    def enter(self):
        pass

class LaunchBay(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('head_quarters')
a_game = Engine(a_map)
a_game.play()
