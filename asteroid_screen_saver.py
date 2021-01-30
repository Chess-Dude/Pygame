# Importing Modules
import pygame
import random

# Instantiating Asteroid Class
class AsteroidObject:
    # Constructor Method
    def __init__(self, image, x_coord, y_coord, speed):
        self.image = image
        self.pos = image.get_rect().move(x_coord, y_coord)
        self.speedx = speed[0]
        self.speedy = speed[1]
        
    # Methods
    def adjust_trajectory(self):
        """
        Updating the position of the asteroid
        """
        self.pos = self.pos.move(self.speedx, self.speedy)

        if self.pos.left < 0 or self.pos.right > 1650: 
            self.speedx = -self.speedx

        if self.pos.top < 0 or self.pos.bottom > 1050: 
            self.speedy = -self.speedy

# Collision Detector Program (Prints if Any Asteroids Collided)        
def collision_detector(all_asteroids):
    """
    To Detect if any asteroids collided
    """
    # For Loop 
    for i in range(0, len(all_asteroids) -1):
        # For Loop 
        for j in range(i + 1, len(all_asteroids)):
            # Checking If any asteroids collided
            if (all_asteroids[i].pos.colliderect(all_asteroids[j].pos)):
                # Do this stuff if they collided
                print("Asteroid %d collided with %d" % (i, j))
                return True
            
            # Do this stuff if they didnt collide
            else: return False

# Deflects/Bounces Any asteroids that overlap/collide off of eachother
def asteroid_deflector(all_asteroids):
    """
    To Reflect any colliding asteroids
    """
    # For loop
    for i in range(0, len(all_asteroids) -1):
        # For Loop
        for j in range(i + 1, len(all_asteroids)):
            # Checking if any asteroids collided
            if (all_asteroids[i].pos.colliderect(all_asteroids[j].pos)):
                # If true, do this stuff.
                # Printing that this asteroid collided with this asteroid
                print("Asteroid %d collided with %d",i, j)
                
                # Changing the Speed values on both asteroids that collided to negative
                all_asteroids[i].speedx = -all_asteroids[i].speedx
                all_asteroids[i].speedy = -all_asteroids[i].speedy

                all_asteroids[j].speedx = -all_asteroids[j].speedx
                all_asteroids[j].speedy = -all_asteroids[j].speedy


# All Code needed to Instantiate the Asteroid
def asteroid_initializer(all_asteroids):
    """
    Makes sure that there is no overlap once asteroids are instantiated
    """
    
    while True:
        x_coord = random.randint(0, 1650-224)
        y_coord = random.randint(0, 1050-126)

        # Checking if there is 0 asteroids, and returning the coords if there are
        # Otherwise Perform a Full check
        if len(all_asteroids) == 0: return (x_coord, y_coord)

        else:

            for asteroid in all_asteroids:
                if ((x_coord < asteroid.pos.left or x_coord > asteroid.pos.right) and (y_coord < asteroid.pos.top or y_coord > asteroid.pos.bottom)):

                    return (x_coord, y_coord)


                else: 
                    print("Breaking")
                    print(x_coord, y_coord)
                    print(asteroid.pos.left, "Left", asteroid.pos.top, "top")
                    break

# Run All Code (Functions)
def main_program():
    """
    Calls all functions to Run the program
    """
    # Setting Variables
    screen_size = (1680, 1050)
    screen = pygame.display.set_mode(screen_size)
    Asteroid_img = pygame.image.load('C:\\Users\\GEMS\\OneDrive - Peel District School Board\\Desktop\\Python\\pygame_practice\\asteroid.png')
    print(type(Asteroid_img))
    Asteroid_img = Asteroid_img.convert()
    print(type(Asteroid_img))
    background = pygame.image.load('C:\\Users\\GEMS\\OneDrive - Peel District School Board\\Desktop\\Python\\pygame_practice\\Cosmos Background.jpg').convert()
    screen.blit(background, (0, 0))
    all_asteroids = []

    # For loop instantiating 3 asteroids, Increase # in bracket for more asteroids.
    for x in range(3):                    #create 3 objects
        # Instantiating the speed & position of each asteroid
        print("the value of x is", x)
       
        (x_coord, y_coord) = asteroid_initializer(all_asteroids)
        speed_x = random.randint(1, 5)
        if random.randint(0, 1) == 0:
            speed_x = -speed_x
        
        speed_y = random.randint(1, 5)
        if random.randint(0, 1) == 0:
            speed_y = -speed_y

        speed = (speed_x, speed_y)

        asteroid = AsteroidObject(Asteroid_img, x_coord, y_coord, speed)
        
        # Add all the new instantiate asteroids to the asteroid list
        all_asteroids.append(asteroid)

    print(all_asteroids)
    # Infinite While Loop
    while 1:

        # Checking If game crashed/quit
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                sys.exit()

        # Blitting the Background Image
        for asteroid in all_asteroids:
            screen.blit(background, asteroid.pos, asteroid.pos)
            # Figure out Why We need Both "asteroid.pos"

        # Blitting the Asteroid Image
        for asteroid in all_asteroids:
            asteroid.adjust_trajectory()
            screen.blit(asteroid.image, asteroid.pos)

        #collision_detector(all_asteroids)   
        asteroid_deflector(all_asteroids)

        # Updating the Display for anything new
        pygame.display.update()
        pygame.time.delay(10)


# Call All the Code
main_program()