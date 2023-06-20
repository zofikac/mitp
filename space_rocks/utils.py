import random

#importuje kolor
from pygame import Color
#importuje ładowanie
from pygame.image import load
#żeby pojawiały się po przeciwnej stronie ekranu
from pygame.math import Vector2
#importuje dźwięki
from pygame.mixer import Sound


def load_sprite(name, with_alpha=True): #metoda konieczna do załadowania obrazka
    path = f"C:\\Users\\Użytkownik\\mitp_proj_ZK\\assets\\sprites\\{name}.png"
    loaded_sprite = load(path) #metoda ładuje powierzchnię,
    # obiekt używany przez pygamw reprezentujący obraz

    if with_alpha: #konwertuje obraz, żeby lepiej pasował do ekranu
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


def load_sound(name): #metoda konieczna do załadowania dźwięku
    path = f"C:\\Users\\Użytkownik\\mitp_proj_ZK\\assets\\sounds\\{name}.wav"
    return Sound(path)


def wrap_position(position, surface): #surface to powierzchnia ekranu
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h) #dzięki użyciu modulo, wiemy że nigdy nie opuści ekranu



def get_random_position(surface):
    #generuje randomowe współrzędne, zwraca wynik w wektorach
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )


def get_random_velocity(min_speed, max_speed):
    #generuje przypadkową wartosć z zakresu prędkości/stopni
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)


def print_text(surface, text, font, color=Color("tomato")): #deklaruję metodę; tomato to defaultowy kolor
    # tworzy powierzchnię z tekstem używając render()
    # true wygładza krawędzie tekstu
    text_surface = font.render(text, True, color)
    # pobiera kąt, który odzwierciedla powierzchnię tekstu
    rect = text_surface.get_rect()
    # oblicza środek, używając powierzchni ekranu/2
    rect.center = Vector2(surface.get_size()) / 2
    # rysuje tekst na ekranie; przekazuje kąt do funkcji
    surface.blit(text_surface, rect)
