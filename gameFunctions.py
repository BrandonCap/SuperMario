import sys
import pygame


def update_screen(screen, mario, settings, level, pipes, display, stats, bricks, upgrades, enemies, flags, poles, radio, sounds, fireballs, secret_bricks, secret_pipes):
    screen.fill(settings.bg_color)
    if stats.flag_reach_bot and stats.timer <= 100:
        mario.move_right()
        stats.timer += 1
    if stats.timer >= 100:
        mario.move_stop()
    mario.update(stats, level, sounds)
    fireballs.update()
    check_fire_enemy_collisions(enemies, fireballs, stats, sounds)
    flags.update()
    upgrades.update()
    for enemy in enemies:
        enemy.update(mario)
    bricks.update()
    mario.check_collision(screen, stats, display)
    if not stats.secret_level:
        level.blitme()
        enemies.draw(screen)
        bricks.draw(screen)
        pipes.draw(screen)
        poles.draw(screen)
        flags.draw(screen)

    # Draws only if in underground level
    if stats.secret_level:
        secret_bricks.draw(screen)
        secret_pipes.draw(screen)
    fireballs.draw(screen)
    mario.blitme()
    upgrades.draw(screen)
    display.gameStats(screen, stats)
    stats.update_time(radio, sounds)
    stats.update_txt()

    if stats.game_over is True:
        screen.fill((0, 0, 0))
        display.gameOver(screen)

    pygame.display.flip()


def check_events(mario, stats, sounds, fireballs):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_a:
                if not stats.reached_pole:
                    if mario.rect.left >= 20:
                        mario.move_left()
            elif event.key == pygame.K_d:
                if not stats.reached_pole:
                    mario.move_right()
            elif event.key == pygame.K_s:
                mario.crouch = True
            elif event.key == pygame.K_w:
                if not stats.reached_pole:
                    if mario.y_change == 0:
                        sounds[7].play()
                        mario.move_jump()
            elif event.key == pygame.K_SPACE:
                if not stats.reached_pole and mario.fired and len(fireballs) <= 1:
                    mario.fire()
                    sounds[6].play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mario.move_stop()
            elif event.key == pygame.K_d:
                mario.move_stop()


def check_fire_enemy_collisions(enemies, fireballs, stats, sounds):
    if pygame.sprite.groupcollide(enemies, fireballs, True, True):
        stats.score += 100
        sounds[8].play()