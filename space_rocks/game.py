import pygame
#importuje bezpośrednie klasy, które reprezentują obiekty w grze
from models import Asteroid, Spaceship
#importuje metody związane z pozycją, obrazkiem, tekstem
from utils import get_random_position, load_sprite, print_text


class SpaceRocks:
    # definiuję przestzeń, jaka ma zostać pusta dla kalmana
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        self._init_pygame() #metoda inicjująca pygame
        self.screen = pygame.display.set_mode((800, 600)) #tworzy ekran
        #w tej metodzie przekazuje szerokość i wysokość jego
        self.background = load_sprite("space", False)
        #clock prędkosci będą te same niezależnie od komputera/procesor
        self.clock = pygame.time.Clock()
        #tworzę czcionkę
        self.font = pygame.font.Font(None, 64)
        #przechowuję wiadomość
        self.message = ""
        #definiuję obiekty
        self.asteroids = []
        self.bullets = []
        #dodaję pociski
        self.spaceship = Spaceship((400, 300), self.bullets.append)

        #pętla sprawdza, czy pozycja asteroidy jest dalsza, niż ta określona
        #jeśli nie - ponownie pętla
        #tworzymy 6 asteroid
        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break

            self.asteroids.append(Asteroid(position, self.asteroids.append))

    # metoda, która zwraca mi obiekty wszystkie
    # dzięki temu używać będziemy rysowania + poruszania obiektu
    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init() #inicjacja gry
        pygame.display.set_caption("Space Rocks") #wyświetla nazwę gry

    def _handle_input(self):
        # metoda, która pozwala na wyjście użytkownikowi, używając Close albo ALT+F4, albo ESC
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            # pozwala na strzelanie pocisków
            elif (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()

        is_key_pressed = pygame.key.get_pressed()

        #pozwala na poruszanie
        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def _process_game_logic(self): #logika gry
        #uaktalnia pozycję
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship: #sprawdzamy, czy istnieje; jeśli nie isitneje, pętla nie miałaby sensu
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    #jeśli kolizja - nie będzie obiektu
                    self.spaceship = None
                    self.message = "Przegrałeś!"
                    break

        #niszczę statek
        #kiedy wykruje kolizję, usuwa je z gry
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    break

        #usuwa pociski poza ekranem
        for bullet in self.bullets[:]: #używam kopii listy, bo bez tego
            #usuwanie elementów podczas przebiegania przez nią może wywołać error
            #powierzchnia w Pygame ma metodę get_rect(), która zwraca kąt reprezentujacy obszar
            #ten kąt zwraca true, jeśli punkt jest w tym kącie i false, jeśli jest poza
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

        if not self.asteroids and self.spaceship:
            self.message = "Zwycięstwo!"

    def _draw(self): #rysuje rzeczy na ekranie
        #by coś wyświetlić na jednym ekranie, używa metody blit(to na czym chcę rysować, punkty gdzie chcę rysować)
        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        if self.message: #umieszcza wiadomość na ekranie
            print_text(self.screen, self.message, self.font)

        pygame.display.flip() #updateuje zwartość ekranu; obiekty się ruszają, wiec wywoływany by je uaktualnić
        self.clock.tick(60)

    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_objects.append(self.spaceship)

        return game_objects
