import moderngl_window as mglw

class App(mglw.WindowConfig):
    window_size = (1600, 900)
    resource_dir = 'programs'

    def __init__(self, **kwargs):
        # create screen-aligned quad
        super().__init__(**kwargs)
        self.quad=mglw.geometry.quad_fs()
        #Load shader program
        self.prog = self.load_program(vertex_shader='vertex_shader.glsl',
                                      fragment_shader='fragment_shader.glsl')

    def on_render(self, time: float, frametime: float):
        # This method is called every frame
        self.ctx.clear()
        self.quad.render(self.prog)

if __name__ == '__main__':
    mglw.run_window_config(App)
