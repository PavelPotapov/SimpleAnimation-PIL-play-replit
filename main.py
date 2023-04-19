from PIL import Image
import play
import os

def create_images():
    step = 192//24
    x1 = 0
    y1 = 0

    x2 = step
    y2 = 8

    img = Image.open('GoldCoinSpinning.png')
    images = []

    if not os.path.exists('coins'):
        os.makedirs('coins')
    for i in range(24):
        img_crop = img.crop([x1,y1,x2,y2])
        img_crop.save('coins/coin' + str(i) + '.png')
        images.append('coins/coin' + str(i) + '.png')
        x1 += step
        x2 += step

    return images


images = create_images()
coin = play.new_image(image = images[0], size=500)

coin.speedx = 5
coin.speedy = 5

@play.repeat_forever
async def do():
    
    for i in range(len(images)):
        coin.image = images[i]

        coin.x += coin.speedx
        coin.y += coin.speedy
        if coin.x > 300 or coin.x < -300:
            coin.speedx *= -1
        if coin.y > 200 or coin.y < -200:
            coin.speedy *= -1
    
        await play.timer(seconds=1/60)



play.start_program()



