import pygame
import sys, time
import strings

# 初始化窗口
pygame.init()
# 设置窗口大小,设置全屏pygame.FULLSCREEN
# screen_image = pygame.display.set_mode((800, 600))
screen_image = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# 查看窗口的像素（坐标）信息
screen_rect = screen_image.get_rect()
screen_image.fill(strings.bg_color1)

# 设置窗口的标题
pygame.display.set_caption('打怪兽小游戏')
'飞机'
# 加载飞机图片
ship_image = pygame.image.load('./static_resources/ship.bmp')
# 获得小飞机图片的像素信息
ship_rect = ship_image.get_rect()
# 设置小飞机的坐标中心点=窗口的画面中心点
ship_rect.midbottom = screen_rect.midbottom
# 飞机次数
ships_frequency = 0
screen_image.blit(ship_image, ship_rect)

moving_lift = False
moving_right = False

'''子弹'''
bullets = pygame.sprite.Group()

'''科学计算敌人位置'''
an_alien_image = pygame.image.load('./static_resources/alien.bmp')
an_alien_image_rect = an_alien_image.get_rect()
an_alien_width = an_alien_image_rect.width  # 敌人宽
an_alien_height = an_alien_image_rect.right  # 敌人高
screen_width, screen_height = screen_rect.size  # 飞船的大小
ship_width, ship_height = ship_rect.size  # 子弹的大小
space_x = screen_width - 2 * an_alien_width  # 设置宽度以及空隙
space_y = screen_height - ship_height - 3 * an_alien_height  # 设置高度以及空隙
column_number = space_x // (2 * an_alien_width)
line_number = space_y // (2 * an_alien_height)

'''敌人代码'''
aliens = pygame.sprite.Group()
for y_number in range(line_number):
    for x_number in range(column_number):
        alien_sprite = pygame.sprite.Sprite()
        alien_sprite.image = pygame.image.load("./static_resources/alien.bmp")
        alien_sprite.rect = alien_sprite.image.get_rect()
        alien_sprite.rect.x = an_alien_width + 2 * an_alien_width * x_number
        alien_sprite.rect.y = an_alien_height + 2 * an_alien_height * y_number
        aliens.add(alien_sprite)
aliens.draw(screen_image)
alien_direction = 1

'按钮'
button_rect = pygame.Rect(0, 0, 200, 50)
button_rect.center = screen_rect.center
play_font = pygame.font.SysFont(None, 48)
play_image = play_font.render('Play', True, strings.bg_color2, strings.bg_color3)
play_rect = play_image.get_rect()
play_rect.center = button_rect.center

'显示信息'
score = 0
high_score = 0
level = 1
alien_points = 50
'显示分数'
score_str = str(score)
score_font = pygame.font.SysFont(None, 48)
score_image = score_font.render(score_str, True, strings.bg_color4, strings.bg_color3)
score_rect = score_image.get_rect()
score_rect.right = screen_rect.right - 20
score_rect.top = 20
screen_image.blit(score_image, score_rect)

'最高分记录'
high_score_str = str(high_score)
high_score_font = pygame.font.SysFont(None, 48)
high_score_image = high_score_font.render(high_score_str, True, strings.bg_color4, strings.bg_color3)
high_score_rect = high_score_image.get_rect()
high_score_rect.right = screen_rect.centerx
high_score_rect.top = score_rect.top
screen_image.blit(high_score_image, high_score_rect)

'级别'
level_str = str(level)
level_font = pygame.font.SysFont(None, 48)
level_image = level_font.render(level_str, True, strings.bg_color4, strings.bg_color3)
level_rect = level_image.get_rect()
level_rect.right = score_rect.right
level_rect.top = score_rect.top + 50
screen_image.blit(level_image, level_rect)

'可用飞船数量'
ship_group = pygame.sprite.Group()
for ships_number in range(strings.ship_limit - 1):
    ship = pygame.sprite.Sprite()
    ship.image = pygame.image.load('./static_resources/ship.bmp')
    ship.rect = ship.image.get_rect()
    ship.rect.x = 10 + (ship.rect.width + 10) * ships_number
    ship.rect.y = 10
    ship_group.add(ship)
# 绘制显示生命
ship_group.draw(screen_image)

"""死循环让窗口一直显示"""
while True:
    # 循环遍历窗口的所有事件
    for event in pygame.event.get():
        # 判断当前事件是不是点击了关闭按钮
        if event.type == pygame.QUIT:
            sys.exit()  # 关闭
        # 添加了一个键盘按下事件
        elif event.type == pygame.KEYDOWN:
            # 设置按esc关闭
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_LEFT:
                moving_lift = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                # Sprite精灵：有image属性和rect属性的对象,但是绝对不是图像文件
                if len(bullets) < strings.bullets_allowed:
                    new_bullet = pygame.sprite.Sprite()
                    new_bullet.rect = pygame.Rect(0, 0, 3, 15)
                    new_bullet.rect.midbottom = ship_rect.midbottom
                    bullets.add(new_bullet)
        # 添加了一个键盘松开事件
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_lift = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 设置鼠标点击事件
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                ships_frequency = strings.ship_limit
                pygame.mouse.set_visible(False)  # 在玩游戏是关闭鼠标，让他不显示
                bullets.empty()

    if ships_frequency > 0:
        # 设置小飞机左右移动,按下一直移动
        if moving_lift and ship_rect.left > 0:
            # 设置船速
            ship_rect.x -= strings.ship_speed
        if moving_right and ship_rect.right < screen_rect.right:
            ship_rect.x += strings.ship_speed
        ship_sprite = pygame.sprite.Sprite()
        ship_sprite.image = ship_image
        ship_sprite.rect = ship_rect

        # 设置窗口的颜色
        screen_image.fill(strings.bg_color1)
        # 在窗口中添加小飞机图片，并设置位置
        screen_image.blit(ship_image, ship_rect)

        for bullet in bullets:
            # 设置子弹输出，窗口，颜色，子弹的位置
            pygame.draw.rect(screen_image, strings.bg_color2, bullet.rect)
            # 子弹移动
            bullet.rect.y -= strings.bullets_speed
            # 档子弹出到窗口以外的时候删除
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        # 设置敌人的边界
        for alien in aliens:
            if alien.rect.right >= screen_rect.right or alien.rect.left <= 0:
                alien_direction *= -1
                for alien in aliens:
                    alien.rect.y += strings.alien_y_speed
                break

        # 设置让他动起来
        for alien in aliens:
            alien.rect.x += strings.alien_x_speed * alien_direction

        # 绘制敌人
        aliens.draw(screen_image)
        # 碰撞小时效果，两个都是true的话就是碰撞都消失，
        # 第一个true代表第一个群组的值消失，第二个true代表第二个群组的值消失
        duang = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if duang:
            for item in duang.values():
                score += alien_points * len(item)
        if score > high_score:
            high_score = score

        '统计信息'
        '显示分数'
        score_str = '{:,}'.format(score)
        score_font = pygame.font.SysFont(None, 48)
        score_image = score_font.render(score_str, True, strings.bg_color4, strings.bg_color3)
        score_rect = score_image.get_rect()
        score_rect.right = screen_rect.right - 20
        score_rect.top = 20
        screen_image.blit(score_image, score_rect)

        '最高分记录'
        high_score_str = '{:,}'.format(high_score)
        high_score_font = pygame.font.SysFont(None, 48)
        high_score_image = high_score_font.render(high_score_str, True, strings.bg_color4, strings.bg_color3)
        high_score_rect = high_score_image.get_rect()
        high_score_rect.right = screen_rect.centerx
        high_score_rect.top = score_rect.top
        screen_image.blit(high_score_image, high_score_rect)

        '级别'
        level_str = str(level)
        level_font = pygame.font.SysFont(None, 48)
        level_image = level_font.render(level_str, True, strings.bg_color4, strings.bg_color3)
        level_rect = level_image.get_rect()
        level_rect.right = score_rect.right
        level_rect.top = score_rect.top + 50
        screen_image.blit(level_image, level_rect)

        '可用飞船数量'
        ship_group = pygame.sprite.Group()
        for ships_number in range(ships_frequency - 1):
            ship = pygame.sprite.Sprite()
            ship.image = pygame.image.load('./static_resources/ship.bmp')
            ship.rect = ship.image.get_rect()
            ship.rect.x = 10 + (ship.rect.width + 10) * ships_number
            ship.rect.y = 10
            ship_group.add(ship)
        # 绘制显示生命
        ship_group.draw(screen_image)

        '打完敌人后'
        if not aliens:
            bullets.empty()
            for y_number in range(line_number):
                for x_number in range(column_number):
                    alien_sprite = pygame.sprite.Sprite()
                    alien_sprite.image = pygame.image.load("./static_resources/alien.bmp")
                    alien_sprite.rect = alien_sprite.image.get_rect()
                    alien_sprite.rect.x = an_alien_width + 2 * an_alien_width * x_number
                    alien_sprite.rect.y = an_alien_height + 2 * an_alien_height * y_number
                    aliens.add(alien_sprite)
            strings.ship_speed *= strings.speedup_scale
            strings.bullets_speed *= strings.speedup_scale
            strings.alien_x_speed *= strings.speedup_scale
            level += 1

        '敌人打到我了怎么办'
        if pygame.sprite.spritecollideany(ship_sprite, aliens):
            ships_frequency -= 1
            # 清空所有的敌人的子弹
            aliens.empty()
            bullets.empty()
            # 重新生成敌人
            for y_number in range(line_number):
                for x_number in range(column_number):
                    alien_sprite = pygame.sprite.Sprite()
                    alien_sprite.image = pygame.image.load("./static_resources/alien.bmp")
                    alien_sprite.rect = alien_sprite.image.get_rect()
                    alien_sprite.rect.x = an_alien_width + 2 * an_alien_width * x_number
                    alien_sprite.rect.y = an_alien_height + 2 * an_alien_height * y_number
                    aliens.add(alien_sprite)

            # 刷新飞船的位置
            ship_rect.midbottom = screen_rect.midbottom
            time.sleep(2)

        '敌人到底部了怎么办'
        for alien in aliens:
            if alien.rect.bottom >= screen_rect.bottom:
                ships_frequency -= 1
                aliens.empty()
                bullets.empty()
                # 重新生成敌人
                for y_number in range(line_number):
                    for x_number in range(column_number):
                        alien_sprite = pygame.sprite.Sprite()
                        alien_sprite.image = pygame.image.load("./static_resources/alien.bmp")
                        alien_sprite.rect = alien_sprite.image.get_rect()
                        alien_sprite.rect.x = an_alien_width + 2 * an_alien_width * x_number
                        alien_sprite.rect.y = an_alien_height + 2 * an_alien_height * y_number
                        aliens.add(alien_sprite)
                # 刷新飞船的位置
                ship_rect.midbottom = screen_rect.midbottom
                time.sleep(2)
                break
    else:
        # 显示play按钮
        pygame.draw.rect(screen_image, strings.bg_color4, button_rect)
        screen_image.blit(play_image, play_rect)
        pygame.mouse.set_visible(True)
        # 重置游戏速度
        strings.ship_speed, strings.bullets_speed, strings.alien_x_speed = strings.speedup_list
        score = 0
        level = 1
    # 基于现有条件刷新
    pygame.display.flip()
