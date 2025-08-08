import pygame
from constants import *
from players import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    """
    Main game loop for the Asteroids game.
    Initializes pygame, creates the game window, and runs the main game loop.
    The function sets up a player object at the center of the screen and handles
    the core game mechanics including:
    - Event handling (quit events)
    - Screen clearing and rendering
    - Player updates and drawing
    - Frame rate control at 60 FPS
    - Delta time calculation for smooth movement
    The loop continues indefinitely until the user closes the window.
    """
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    updateable.add(player)
    drawable.add(player)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting Asteroids!")
                return

        
        screen.fill(color=(0, 0, 0))
        updateable.update(dt)

        #Collision detection
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for item in drawable:
            item.draw(screen)

        dt = clock.tick(60) / 1000
        
        player.shoot_cooldown -= dt
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
