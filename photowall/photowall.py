import os
import argparse
from PIL import Image

''' 将图片制作为520照片墙 '''

'''一些超参'''
CELLSIZE = 256

target_path = r'F:\tools\photowall\images'

'''图片重命名'''
def rename_image(target_path):
    for idx, each in enumerate(os.listdir(target_path)):
        os.rename(os.path.join(target_path, each), os.path.join(target_path, 'image%s.jpg' % idx))

'''图片读取'''
def read_image(img_path, target_size=(256, 256)):
    img = Image.open(img_path)
    image = img.resize(target_size)
    return image

'''图片生成器'''
def yield_image(target_dir, idx, target_size):
    img_paths = sorted([os.path.join(target_dir, imgname) for imgname in os.listdir(target_dir)])
    idx = (idx + 1) % len(img_paths)
    return read_image(img_paths[idx], target_size), idx

'''解析模板'''
def parse_template(template_path):
    template = []
    with open(template_path, 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            template.append(line.strip('\n').split(','))
    return template

'''主函数'''
def main(pictures_dir, template_path):
    template = parse_template(template_path)
    w = len(template[0])
    h = len(template)
    image_new = Image.new('RGBA', (CELLSIZE*w, CELLSIZE*h))
    img_idx = -1
    for y in range(h):
        for x in range(w):
            if template[y][x] == '1':
                img, img_idx = yield_image(pictures_dir, img_idx, (CELLSIZE, CELLSIZE))
                image_new.paste(img, (x*CELLSIZE, y*CELLSIZE))
    image_new.show()
    image_new.save('picturewall.png')

if __name__ == '__main__':
    # rename_image(target_path)
    parser = argparse.ArgumentParser(description="Picture Wall Generator.")
    parser.add_argument('-t', dest='template_path', help='Template path.', default='templates/template.txt')
    parser.add_argument('-p', dest='pictures_dir', help='Pictures dir.', default='images')
    args = parser.parse_args()
    template_path = args.template_path
    pictures_dir = args.pictures_dir
    main(pictures_dir, template_path)
