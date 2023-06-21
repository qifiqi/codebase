from captcha.image import ImageCaptcha
import random
import os


list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 定义验证码尺寸
width, height = 170, 80

if not os.path.exists('./yzm'):
    os.makedirs('./yzm')

#生成一万张验证码
for i in range(20000):
    generator = ImageCaptcha(width=width, height=height)


    # 从list中取出4个字符
    random_str = ''.join([random.choice(list) for j in range(4)])
    # 生成验证码
    img = generator.generate_image(random_str)
    # 在验证码上加干扰点
    generator.create_noise_dots(img, '#000000', 4, 40)

    # 在验证码上加干扰线
    generator.create_noise_curve(img, '#000000')

    # 将图片保存在目录yzm文件夹下
    file_name = './yzm/'+random_str+'_'+str(i)+'.jpg'
    print(file_name)
    img.save(file_name)
