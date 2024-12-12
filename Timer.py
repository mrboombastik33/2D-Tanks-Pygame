import pygame as pg
class Timer:
    def __init__(self, time):
        pg.time.set_timer(pg.USEREVENT, 1000)
        self.time = time
        self.text = f'{self.time}'.rjust(3)
        self.timer_text = pg.font.SysFont('Arial', 30)

    def update_timer(self, event_type): # Зміна часу в таймері
        if not event_type == pg.USEREVENT:
            return False
        self.time -= 1
        if self.time <= 0:
            self.time = 0
            return False  # Закінчення таймера
        return True

    def render(self):
        text = str(self.time).rjust(3)
        return self.timer_text.render(text, True, (0, 0, 0))
