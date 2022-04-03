import pygame
from pygame.sprite import Group
from metaData import Stats, Settings
import gameFunctions
from mario import Mario
from mapElements import Pipe, Flag, Pole
from display import Display
from map import Map, Level


def game():
    music = pygame.mixer
    music.init()
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Super Mario")
    sounds = [music.Sound('resources/bgMusic.wav'), music.Sound('resources/blockBump.wav'),
              music.Sound('resources/brickBreak.wav'),
              music.Sound('resources/coin.wav'), music.Sound('resources/death.wav'),
              music.Sound('resources/extraLife.wav'),
              music.Sound('resources/fireball.wav'), music.Sound('resources/jump.wav'),
              music.Sound('resources/kill.wav'),
              music.Sound('resources/pipe.wav'), music.Sound('resources/power_spawn.wav'),
              music.Sound('resources/powerup.wav'),
              music.Sound('resources/stage_clear.wav'), music.Sound('resources/star.wav')]
    bricks = Group()
    secret_bricks = Group()
    flags = Group()
    ground = Group()
    upgrades = Group()
    pipes = Group()
    secret_pipes = Group()
    enemies = Group()
    poles = Group()
    fireballs = Group()
    stats = Stats()

    for i in range(6, 8):
        pipe = Pipe(screen, settings, i)
        secret_pipes.add(pipe)

    flag = Flag(screen, settings, stats)
    flags.add(flag)
    pole = Pole(screen, settings)
    poles.add(pole)
    mario = Mario(screen, settings, pipes, bricks, upgrades, stats, enemies, poles, music, sounds,
                  fireballs, secret_bricks, secret_pipes, ground)
    lvl_map = None
    level = Level(screen, settings, pipes, lvl_map, bricks, upgrades, enemies, flags, poles)
    display = Display(screen, stats)

    sounds[0].play(-1)
    while True:
        if stats.activate_main_lvl:
            lvl_map = Map(screen, settings, bricks, pipes, mario, enemies, ground, upgrades, stats, secret_bricks)
            lvl_map.build_brick()
            for i in range(0, 6):
                pipe = Pipe(screen, settings, i)
                pipes.add(pipe)
            flag = Flag(screen, settings, stats)
            flags.add(flag)
            pole = Pole(screen, settings)
            poles.add(pole)
            stats.activate_main_lvl = False

        if stats.activate_secret:
            pipes.empty()
            bricks.empty()
            enemies.empty()
            poles.empty()
            flags.empty()
            lvl_map = Map(screen, settings, bricks, pipes, mario, enemies, ground, upgrades, stats, secret_bricks)
            lvl_map.build_brick()
            stats.activate_secret = False
            stats.main_level = False

        if stats.game_active:
            gameFunctions.check_events(mario, stats, sounds, fireballs)
            if mario.rect.right >= 600 and stats.main_level:
                diff = mario.rect.right - 600
                mario.rect.right = 600
                level.shifting_world(-diff)
            gameFunctions.update_screen(screen, mario, settings, level, pipes, display, stats, bricks, upgrades,
                                        enemies, flags, poles, music, sounds, fireballs, secret_bricks, secret_pipes)
            pygame.display.flip()


game()
