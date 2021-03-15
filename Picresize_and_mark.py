import os , glob
from PIL import Image , ImageDraw , ImageFont
os.chdir('C:\\Users\\USER\\OneDrive\\endoscope_review\\figures')
ttfont = ImageFont.truetype('C:\\Windows\\Fonts\\Arial\\arial.ttf',100)
ims=glob.glob('8*.jpg')
width_pixel=1024
for i in ims:
    images = Image.open(i)
    short_pixel = int(images.height*(width_pixel/images.width))
    images = images.resize((width_pixel,short_pixel))
    draw = ImageDraw.Draw(images)
    draw.text((50,50),i[0:2],font=ttfont,fill=(255,255,255,255))
    images.save('{}_{}'.format('new',i),dpi=(300,300))