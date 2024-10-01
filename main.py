import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 510)) #flags=pygame.NOFRAME
pygame.display.set_caption('Игра века')
icon = pygame.image.load('images/icon_pygame.png.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png').convert_alpha()
player = pygame.image.load('images/player/player_right.png').convert_alpha()
player2 = pygame.image.load('images/player_2/player_right1.png').convert_alpha()
brick_block = pygame.image.load('images/brick_block.png').convert_alpha()
gun_pistolet = pygame.image.load('images/gun_pistolet.png')
shot = pygame.image.load('images/shot.png')

'''Списки картинок персонажа'''
walk_left = [
    pygame.image.load('images/player/player_left.png').convert_alpha(),
    pygame.image.load('images/player/player_left_go.png').convert_alpha(),
    pygame.image.load('images/player/player_left_run.png').convert_alpha(),
    pygame.image.load('images/player/player_left.png').convert_alpha(),
]
walk_right = [
    pygame.image.load('images/player/player_right.png').convert_alpha(),
    pygame.image.load('images/player/player_right_go.png').convert_alpha(),
    pygame.image.load('images/player/player_right_run.png').convert_alpha(),
    pygame.image.load('images/player/player_right.png').convert_alpha(),
]

walk_left2 = [
    pygame.image.load('images/player_2/player_left1.png').convert_alpha(),
    pygame.image.load('images/player_2/player_left2.png').convert_alpha(),
    pygame.image.load('images/player_2/player_left1.png').convert_alpha(),
]
walk_right2 = [
    pygame.image.load('images/player_2/player_right1.png').convert_alpha(),
    pygame.image.load('images/player_2/player_right2.png').convert_alpha(),
    pygame.image.load('images/player_2/player_right1.png').convert_alpha(),
]

'''Картинка призрака'''
ghost = pygame.image.load('images/ghost.png')
ghost_list_in_game = []

'''Характеристики персонажа'''
player_anim_count = 0
player_anim_count2 = 0
bg_x = 0
walk = [walk_right[0], walk_left[0]]
walk2 = [walk_right2[0], walk_left2[0]]
smotrit_na_pravo = True
smotrit_na_pravo2 = False

player_speed = 15
player_x = 150     #}
player_y = -500   #}Координаты игрока

player_x2 = 850     #}
player_y2 = -500


is_jump = False
is_fly = False
is_fly_end = False
jump_count = 10
jump_count3 = -2    #Прыжок1

is2_jump = False
is2_fly = False
is2_fly_end = False
jump2_count = 10
jump2_count3 = -2    #Прыжок2

is_padenie = False  #Падение1
is2_padenie = False  #Падение1

shot_x = []
shot_quantity = 7 #Выстрел
shot2_x = []
shot2_quantity = 7 #Выстрел

'''Фоновая музыка'''
bg_sound = pygame.mixer.Sound('sounds/bg_sound_classic.mp3') #Звуковой фон
sound_shot = pygame.mixer.Sound('sounds/sound_shot.mp3') #Звук выстрела
bg_sound.play()

'''Текст на экране'''
my_font = pygame.font.Font('fonts/Roboto-Black.ttf', 25) #Количество патронов

'''Таймер, счетчик событий'''
ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3000)

'''Характеристики отлета игроков от попаданий пуль'''
popadania_po_1 = False
popadania_po_2 = False
shot_count_1 = 10
shot_count_2 = 10

'''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@__Функции__@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
work_rects = []
def landshaft(stroi_material):
    scheme = [
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    x_0 = 220
    y_0 = 130
    width = 32
    height = 32
    x0 = x_0
    y0 = y_0
    for element in scheme:
        for el in element:
            if el == 1:
                screen.blit(stroi_material, (x0, y0))
                work_rects.append(pygame.Rect((x0, y0 + 10, 32, 5)))
            x0 += width
        x0 = x_0
        y0 += height
'''@@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@'''
'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@__ЦИКЛ__ИГРЫ__@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
'''@@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@ @@@ @@@@'''
running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x - 1000, 0))
    screen.blit(bg, (bg_x + 1000, 0))
    generate_landshaft = landshaft(brick_block)

    text_quantity_shots = my_font.render( f"{shot_quantity} / 7", False, 'grey')
    screen.blit(text_quantity_shots, (50, 440))
    text_quantity2_shots = my_font.render(f"{shot2_quantity} / 7", False, 'grey')
    screen.blit(text_quantity2_shots, (900, 440))

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    player_sole_rect = pygame.Rect((player_x + 15, player_y + 56, 10, 5))#15--> для середины персонажа, 56--> рост персонажа

    player2_rect = walk_left2[0].get_rect(topleft=(player_x2, player_y2))
    player2_sole_rect = pygame.Rect((player_x2 + 15, player_y2 + 45, 10, 10)) #для второго игрока

    terrene_rect = pygame.Rect((0, 431, 1000, 1000))#431--> 375 + 56(рост персонажа)
    if terrene_rect not in work_rects:
        work_rects.append(terrene_rect)

    '''Приведение, буу'''
    if ghost_list_in_game:
        for el in ghost_list_in_game:
            screen.blit(ghost, el)
            el.x -= 10

            if player_rect.colliderect(el):
                YOU_LOSE = 'YOU_LoSE'
                #print("YOU LOSE")

    keys = pygame.key.get_pressed()  #Поключение вроде бы клавишь

    '''Ходьба1'''
    if keys[pygame.K_a] and player_x > 0:
        walk = walk_left
        screen.blit(pygame.transform.flip(gun_pistolet, True, False), (player_x - 4, player_y + 28))
        screen.blit(walk[player_anim_count], (player_x, player_y))
        player_x -= player_speed
        smotrit_na_pravo = False
        #bg_x += 5
    elif keys[pygame.K_d] and player_x < 960:
        walk = walk_right
        screen.blit(gun_pistolet, (player_x + 33, player_y + 28))
        screen.blit(walk[player_anim_count], (player_x, player_y))
        player_x += player_speed
        smotrit_na_pravo = True
        #bg_x -= 5
    else:
        if smotrit_na_pravo:
            screen.blit(gun_pistolet, (player_x + 30, player_y + 32))
            screen.blit(walk[0], (player_x, player_y))
        else:
            screen.blit(pygame.transform.flip(gun_pistolet, True, False), (player_x , player_y + 32))
            screen.blit(walk[1], (player_x, player_y))

    if player_anim_count == 3:# Анимация ходьбы
        player_anim_count = 0
    else:
        player_anim_count += 1

    '''Ходьба2'''
    if keys[pygame.K_LEFT] and player_x2 > 0:
        walk2 = walk_left2
        screen.blit(pygame.transform.flip(gun_pistolet, True, False), (player_x2 - 9, player_y2 + 21))
        screen.blit(walk2[player_anim_count2], (player_x2, player_y2))
        player_x2 -= player_speed
        smotrit_na_pravo2 = False
        # bg_x += 5
    elif keys[pygame.K_RIGHT] and player_x2 < 960:
        walk2 = walk_right2
        screen.blit(gun_pistolet, (player_x2 + 25 , player_y2 + 21))
        screen.blit(walk2[player_anim_count2], (player_x2, player_y2))
        player_x2 += player_speed
        smotrit_na_pravo2 = True
        # bg_x -= 5
    else:
        if smotrit_na_pravo2:
            screen.blit(gun_pistolet, (player_x2 + 25, player_y2 + 21))
            screen.blit(walk2[0], (player_x2, player_y2))
        else:
            screen.blit(pygame.transform.flip(gun_pistolet, True, False), (player_x2 - 9, player_y2 + 21))
            screen.blit(walk2[1], (player_x2, player_y2))

    if player_anim_count2 == 1:# Анимация ходьбы
        player_anim_count2 = 0
    else:
        player_anim_count2 += 1

    if bg_x == -1000 or bg_x == 1000: #Продолжение экрана
        bg_x = 0



    '''Прыжок и гравитация '''
    if not is_jump:
        if player_sole_rect.collidelist(work_rects) == -1:
            is_padenie = True
        if is_padenie == True:

            '''Падение'''
            if is_fly_end == False:
                player_y += (jump_count3 ** 2) // 2

                if jump_count3 > -10:  # проверка, что нужно телепортировать_________
                    jump_count2 = jump_count3 - 2
                player1_y2 = player_y + (jump_count2 ** 2) // 2
                player_rect2 = pygame.Rect((player_x + 15, player1_y2 + 56, 10, 40 ))

                if player_rect2.collidelist(work_rects) != -1:
                    is_fly_end = True
                jump_count3 -= 2
                # _____END__________________________________________________________
            else:
                if player_sole_rect.collidelist(work_rects):  # Сам телепорт
                    player_y = work_rects[player_rect2.collidelist(work_rects)].top - 56
                    is_fly = False
                    is_fly_end = False
                    jump_count3 = -2
                    is_padenie = False
        ################################################################################################################
        if keys[pygame.K_w]:
            is_jump = True
            is_fly = True
    else:
        if is_fly == True:
            if jump_count > 0:
                player_y -= (jump_count ** 2 )//2
                '''Набор высоты'''
            else:
                '''Падение'''
                if is_fly_end == False:
                    player_y += (jump_count ** 2 )//2

                    if jump_count > -10:  # проверка, что нужно телепортировать_________
                        jump_count2 = jump_count - 2
                    player1_y2 = player_y + (jump_count2 ** 2) // 2
                    player_rect2 = pygame.Rect((player_x + 15, player1_y2 + 46, 10, 40 ))

                    if player_rect2.collidelist(work_rects) != -1:
                        is_fly_end = True
                else:
                    if player_sole_rect.collidelist(work_rects):#Сам телепорт
                        is_fly = False
                        player_y = work_rects[player_rect2.collidelist(work_rects)].top - 56
            if jump_count > -10:
                jump_count -= 2
        else:
            is_jump = False
            is_fly_end = False
            jump_count = 10

    if not is2_jump:
        if player2_sole_rect.collidelist(work_rects) == -1:
            is2_padenie = True
        if is2_padenie == True:

            '''Падение'''
            if is2_fly_end == False:
                player_y2 += (jump2_count3 ** 2) // 2

                if jump2_count3 > -10:  # проверка, что нужно телепортировать_________
                    jump2_count2 = jump2_count3 - 2
                player2_y2 = player_y2 + (jump2_count2 ** 2) // 2
                player2_rect2 = pygame.Rect((player_x2 + 15, player2_y2 + 45, 10, 50 ))

                if player2_rect2.collidelist(work_rects) != -1:
                    is2_fly_end = True
                jump2_count3 -= 2
                # _____END__________________________________________________________
            else:
                if player2_sole_rect.collidelist(work_rects):  # Сам телепорт
                    player_y2 = work_rects[player2_rect2.collidelist(work_rects)].top - 45
                    is2_fly = False
                    is2_fly_end = False
                    jump2_count3 = -2
                    is2_padenie = False
        ################################################################################################################
        if keys[pygame.K_UP]:
            is2_jump = True
            is2_fly = True
    else:
        if is2_fly == True:
            if jump2_count > 0:
                player_y2 -= (jump2_count ** 2 )//2
                '''Набор высоты'''
            else:
                '''Падение'''
                if is2_fly_end == False:
                    player_y2 += (jump2_count ** 2 )//2

                    if jump2_count > -10:  # проверка, что нужно телепортировать_________
                        jump2_count2 = jump2_count - 2
                    player2_y2 = player_y2 + (jump2_count2 ** 2) // 2
                    player2_rect2 = pygame.Rect((player_x2 + 15, player2_y2 + 45, 10, 50 ))

                    if player2_rect2.collidelist(work_rects) != -1:
                        is2_fly_end = True
                else:
                    if player2_sole_rect.collidelist(work_rects):#Сам телепорт
                        is2_fly = False
                        player_y2 = work_rects[player2_rect2.collidelist(work_rects)].top - 45
            if jump2_count > -10:
                jump2_count -= 2
        else:
            is2_jump = False
            is2_fly_end = False
            jump2_count = 10

    '''функция выстрела, пиф-паф'''
    body_rects = [player_rect, player2_rect]
    #Для первого игрока
    if len(shot_x) != 0:
        for i in range(len(shot_x)):
            if shot_x[i][2] == 'right':
                screen.blit(shot, ( shot_x[i][0], shot_x[i][1]))
                shot_x[i][0] += 125
                patron_rect = pygame.Rect((shot_x[i][0] + 10, shot_x[i][1], 125, 10))
                if patron_rect.collidelist(body_rects) != -1:
                    popadania_po_1 = True
                    shot_count_1 = 10
                    popadanie_storona_1 = True
            else:
                screen.blit(pygame.transform.flip(shot, True, False), (shot_x[i][0] - 10, shot_x[i][1] - 4))
                shot_x[i][0] -= 125
                patron_rect = pygame.Rect((shot_x[i][0] + 10, shot_x[i][1], -125, 10))
                if patron_rect.collidelist(body_rects) != -1:
                    popadania_po_1 = True
                    shot_count_1 = 10
                    popadanie_storona_1 = False
        if shot_x[0][0] > 1000 or shot_x[0][0] < 0 :
            shot_x = shot_x[1:]
    if popadania_po_1 == True:
        if shot_count_1 > 0:
            if popadanie_storona_1 == True:
                player_x2 += (shot_count_1 ** 2) // 2
                shot_count_1 -= 2
            else:
                player_x2 -= (shot_count_1 ** 2) // 2
                shot_count_1 -= 2

    #Для второго игрока
    if len(shot2_x) != 0:
        for i in range(len(shot2_x)):
            if shot2_x[i][2] == 'right':
                screen.blit(shot, ( shot2_x[i][0], shot2_x[i][1]))
                shot2_x[i][0] += 125
                patron_rect = pygame.Rect((shot2_x[i][0] + 10, shot2_x[i][1], 125, 10))
                if patron_rect.collidelist(body_rects) != -1:
                    popadania_po_2 = True
                    shot_count_2 = 10
                    popadanie_storona_2 = True
            else:
                screen.blit(pygame.transform.flip(shot, True, False), (shot2_x[i][0]-10, shot2_x[i][1]-4))
                shot2_x[i][0] -= 125
                patron_rect = pygame.Rect((shot2_x[i][0] + 10, shot2_x[i][1], -125, 10))
                if patron_rect.collidelist(body_rects) != -1:
                    popadania_po_2 = True
                    shot_count_2 = 10
                    popadanie_storona_2 = False
        if shot2_x[0][0] > 1000 or shot2_x[0][0] < 0 :
            shot2_x = shot2_x[1:]
    if popadania_po_2 == True:
        if shot_count_2 > 0:
            if popadanie_storona_2 == True:
                player_x += (shot_count_2 ** 2) // 2
                shot_count_2 -= 2
            else:
                player_x -= (shot_count_2 ** 2) // 2
                shot_count_2 -= 2

    '''Перераспавн игрока если он вылетел за пределы арены'''
    if player_x < -10 or player_x > 1000 or player_y > 550:
        player_x = 150
        player_y = -600
        
    if player_x2 < -10 or player_x2 > 1000 or player_y2 > 550:
        player_x2 = 850
        player_y2 = -600



    work_rects = []
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1000, 380)))
        if event.type == pygame.KEYUP and event.key == pygame.K_v and shot_quantity > 0:
            shot_quantity -= 1
            if smotrit_na_pravo:
                shot_x.append([player_x + 40, player_y + 28, 'right'])
            else:
                shot_x.append([player_x, player_y + 32, 'left'])
            sound_shot.play()
        if event.type == pygame.KEYUP and event.key == pygame.K_b:
            shot_quantity = 7

        if event.type == pygame.KEYUP and event.key == pygame.K_o and shot2_quantity > 0:
            shot2_quantity -= 1
            if smotrit_na_pravo2:
                shot2_x.append([player_x2 + 40, player_y2 + 17, 'right'])
            else:
                shot2_x.append([player_x2 - 10, player_y2 + 22, 'left'])
            sound_shot.play()
        if event.type == pygame.KEYUP and event.key == pygame.K_p:
            shot2_quantity = 7
    clock.tick(15)



def proverka():
    print("GGGGOOOOOOODDDD")