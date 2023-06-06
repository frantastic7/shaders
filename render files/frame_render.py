import moderngl
import sys
import numpy as np
from PIL import Image


shader_file = sys.argv[1]
TIME  = float(sys.argv[2])
RESOLUTION_X = int(sys.argv[3])
RESOLUTION_Y = int(sys.argv[4])

output_name = shader_file + "_"+str(TIME)+".png"

# vertex shader in glsl
vertex_shader = """
#version 330
in vec2 in_vert;
void main() {
    gl_Position = vec4(in_vert, 0.0, 1.0);
}
"""

# reads glsl file
with open(shader_file, 'r') as file:
    fragment_shader = file.read()

# context create
context = moderngl.create_standalone_context()

# compiles the program
prog = context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

# creates vortex array objects
vertices = np.array([-1.0,  1.0, 1.0,  1.0, -1.0, -1.0, 1.0, -1.0], dtype='f4')
vbo = context.buffer(vertices)
vao = context.simple_vertex_array(prog, vbo, 'in_vert')

prog['iTime'].value = float(TIME)
prog['iResolution'].value = (RESOLUTION_X, RESOLUTION_Y)

# creates framebuffer
fbuffer = context.framebuffer(color_attachments=[context.texture((RESOLUTION_X, RESOLUTION_Y), 4)])

# uses the framebuffer
fbuffer.use()

# renders shader into framebuffer
context.clear()
vao.render(moderngl.TRIANGLE_STRIP)

# reads data and saves image
data = np.frombuffer(fbuffer.read(), dtype=np.dtype('u1')).reshape((fbuffer.height, fbuffer.width, 3))
Image.fromarray(data).save(output_name)
