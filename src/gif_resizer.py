import sys
import os
from PIL import Image

path = sys.argv[1]

gif = Image.open(path)
# scale down gif by 50%
scale = (gif.size[0] // 2, gif.size[1] // 2)

gif_info = ['loop', 'duration', 'background', 'extension', 'transparency']
original_info = { info:gif.info.get(info) for info in gif_info }

new_frames = []
for frame in range(gif.n_frames):
    # seeks a given frame
    gif.seek(frame)
    # creates a new frame
    new_frame = Image.new('RGBA', gif.size)
    # pastes the current frame of the gif into new_frame
    new_frame.paste(gif)
    # create a thumbnail using the given scale and append it to the new frames
    new_frame.thumbnail(scale, Image.BICUBIC)
    new_frames.append(new_frame)

# need to save like this to avoid black frame at start of gif
new_frames[0].save(
    "new.gif",
    save_all=True,
    append_images=new_frames[1:],
    loop=original_info['loop'],
    duration=original_info['duration'],
    background=original_info['background'],
    extension=original_info['extension'],
    transparency=original_info['transparency'],
)

print(f"Scaled down gif successfuly")



