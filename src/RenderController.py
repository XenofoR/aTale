import arcade

class RenderController():
    render_components = []

    def draw(self):
        for c in self.render_components:
            c.draw()

    def addComponent(self, component):
        self.render_components.append(component)

    def update(self):
        for c in self.render_components:
            c.update()
