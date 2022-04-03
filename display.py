import pygame


class Display:
    def __init__(self, screen, stats):
        self.font = pygame.font.SysFont("Times", 35)
        self.white = (255, 255, 255)
        # Score
        self.current_score = self.font.render(str(stats.score), True, self.white)
        self.current_score_rect = self.current_score.get_rect()
        self.current_score_rect.centerx = screen.get_rect().centerx - 180
        self.current_score_rect.centery = screen.get_rect().top + 20
        # Level
        self.current_world = self.font.render("1-1", True, self.white)
        self.current_world_rect = self.current_world.get_rect()
        self.current_world_rect.centerx = screen.get_rect().centerx - 400
        self.current_world_rect.centery = screen.get_rect().top + 20
        # Remaining Time
        self.current_time = self.font.render(str(stats.time), True, self.white)
        self.current_time_rect = self.current_time.get_rect()
        self.current_time_rect.centerx = screen.get_rect().centerx + 40
        self.current_time_rect.centery = screen.get_rect().top + 20
        # Lives
        self.current_lives = self.font.render(str(stats.lives), True, self.white)
        self.current_lives_rect = self.current_lives.get_rect()
        self.current_lives_rect.centerx = screen.get_rect().centerx + 180
        self.current_lives_rect.centery = screen.get_rect().top + 20
        # High Score
        self.current_high = self.font.render("0", True, self.white)
        self.current_high_rect = self.current_high.get_rect()
        self.current_high_rect.centerx = screen.get_rect().centerx + 350
        self.current_high_rect.centery = screen.get_rect().top + 20
        # Game Over Text
        self.over = self.font.render("GAME OVER", True, self.white)
        self.over_rect = self.over.get_rect()
        self.over_rect.centerx = screen.get_rect().centerx
        self.over_rect.centery = screen.get_rect().centery
        # Default Score
        self.give = self.font.render("0", True, self.white)
        self.give_rect = self.give.get_rect()
        self.give_rect.centerx = screen.get_rect().centerx
        self.give_rect.centery = screen.get_rect().centery

    def gameStats(self, screen, stats):
        self.current_score = self.font.render(str(stats.score), True, self.white)
        self.current_time = self.font.render(str(stats.time), True, self.white)
        self.current_lives = self.font.render(str(stats.lives), True, self.white)
        self.current_high = self.font.render(str(stats.high_score), True, self.white)
        screen.blit(self.current_score, self.current_score_rect)
        screen.blit(self.current_world, self.current_world_rect)
        screen.blit(self.current_time, self.current_time_rect)
        screen.blit(self.current_lives, self.current_lives_rect)
        screen.blit(self.current_high, self.current_high_rect)

    def gameOver(self, screen):
        screen.blit(self.over, self.over_rect)

    def give_score(self, screen, stats, x, y, score):
        self.give = self.font.render(str(score), True, self.white)
        self.give_rect.centerx = x
        self.give_rect.centery = y
        stats.score += score
        screen.blit(self.give, self.give_rect)