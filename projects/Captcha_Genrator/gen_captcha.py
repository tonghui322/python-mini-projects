#图片验证码生成器，包含4个字符，字母大小写和数字随机组合，再对字符做验证码处理
import random
import string
from captcha.image import ImageCaptcha

all_chars = string.ascii_letters + string.digits
print(all_chars)

#step1 随机字符生成
def create_random_num(length):
    char_list = []
    # 循环length次
    for i in range(length):
        # 每次随机拿一个字符
        one_char = random.choice(all_chars)
        # 放进列表
        char_list.append(one_char)
    # 拼接列表所有字符
    code = ''.join(char_list)
    return code


#step2 字符图片处理
def str_to_captcha(text, save_path="captcha.png"):
    img_gen = ImageCaptcha(width=260, height=90)
    img_data = img_gen.generate(text)
    with open(save_path, "wb") as f:
        f.write(img_data.read())
    print(f"验证码图片已保存 ->{save_path}")


if __name__ == "__main__":
    code = create_random_num(6)
    print(code)
    str_to_captcha(code)