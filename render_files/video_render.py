import moderngl
import sys
import numpy as np
from PIL import Image
import subprocess

shader_file = sys.argv[1]
TIME  = float(sys.argv[2])
RESOLUTION_X = int(sys.argv[3])
RESOLUTION_Y = int(sys.argv[4])
frames = int(sys.argv[5])

# vertex shader in glsl
vertex_shader = """
#version 330
in vec2 in_vert;
void main() {
    gl_Position = vec4(in_vert, 0.0, 1.0);
}
"""

with open(shader_file, 'r') as file:
    fragment_shader = file.read()

context = moderngl.create_standalone_context()

prog = context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

vertices = np.array([-1.0,  1.0, 1.0,  1.0, -1.0, -1.0, 1.0, -1.0], dtype='f4')
vbo = context.buffer(vertices)
vao = context.simple_vertex_array(prog, vbo, 'in_vert')

subprocess.run(['mkdir','tmp'])

for i in np.arange(0, TIME*frames):

    output_name = "./tmp/"+shader_file[:8] + "_"+str(int(i))+".png"
    prog['iTime'].value = float(i/frames)
    prog['iResolution'].value = (RESOLUTION_X, RESOLUTION_Y)
    fbuffer = context.framebuffer(color_attachments=[context.texture((RESOLUTION_X, RESOLUTION_Y), 4)])
    fbuffer.use()
    context.clear()
    vao.render(moderngl.TRIANGLE_STRIP)
    data = np.frombuffer(fbuffer.read(), dtype=np.dtype('u1')).reshape((fbuffer.height, fbuffer.width, 3))
    Image.fromarray(data).save(output_name)


subprocess.run(['ffmpeg','-r',str(frames),'-i',f'./tmp/{shader_file[:8]}_%d.png','-vcodec','mpeg4','-b','5000k','-y',f'movie_{shader_file[:8]}.mp4'])


subprocess.run(['rm','-rf','./tmp'])
subprocess.run(['open',f'movie_{shader_file[:8]}.mp4'])