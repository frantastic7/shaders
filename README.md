# Shaders

Various random shaders I wrote for fun. 
 
![Snowflake](snowflake.png)

Use shadertoy.com or the VSC plug-in to check them out!

Also use the frame render script to render a specific frame. 
For the render script please use the "_for_render" versions since they require a different syntax than the VSC plugin ones.  
 
Please use the pip_reqs.txt for all the required Python libraries. And FFMPEG (For the video script)  

Usage :  
  
python3 frame_render.py "shader_file.glsl" iTime_value horizontal_resolution vertical_resolution  

iTime values are seconds (floats)  
resolutions are ints.  

Usage for video script :

python3 frame_render.py "shader_file.glsl" seconds horizontal_resolution vertical_resolution frames

Video script just runs the frame script on a loop and compiles with ffmpeg.  


-----
OpenGL windows coming soon.
-----
