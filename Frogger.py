import pygame
import os
import sys

os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

# PARAMETERS
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 812

BOX_WIDTH = 50
BOX_HEIGHT = 58

WINDOW_LEFT = 0
WINDOW_RIGHT = 700
WINDOW_TOP = 0
WINDOW_BOTTOM = 812

ROTATION_ANGLE = 90
PAVEMENT1_POS_Y = (int)(13.5*BOX_HEIGHT)
PAVEMENT2_POS_Y = (int)(7.5*BOX_HEIGHT)
GRASS_POS_Y = (int)(1.5*BOX_HEIGHT)

PLAY_TRACK_ONCE = 0
PLAY_TRACK_INDEFINIETLY = -1

# COLORS
RED_COLOR = (255, 64, 64)
GREEN_COLOR = (124, 252, 0)
YELLOW_COLOR = (255, 255, 51)
BLACK_COLOR = (0, 0, 0)

# SOUND EFFECTS
FROG_HOP_SOUND_FILE_NAME = "Resources/frogHop.wav"
FROG_PLONK_SOUND_FILE_NAME = "Resources/frogPlonk.wav"
FROG_SQUASH_SOUND_FILE_NAME = "Resources/frogSquash.wav"
WIN_SOUND_FILE_NAME = "Resources/win.wav"

FROG_HOP_SOUND_INDEX = 0
FROG_PLONK_SOUND_INDEX = 1
FROG_SQUASH_SOUND_INDEX = 2
WIN_SOUND_INDEX = 3

# GAME
BACKGROUND_IMAGE_NAME = "Resources/Background.png"

SCORE_VALUE_FONT_SIZE = 30
SCORE_FONT_SIZE = 20

GAME_TEXT_POS_Y = (int)(0.5*BOX_HEIGHT)
GAME_SCORE_TEXT_POS_X = (int)(1.5*BOX_WIDTH)
GAME_SCORE_VALUE_POS_X = (int)(3*BOX_WIDTH)
GAME_LIVES_TEXT_POS_X = (int)(5*BOX_WIDTH)
GAME_WINS_TEXT_POS_X = (int)(9.5*BOX_WIDTH)

NORMAL_DIFFICULTY = 0
HARD_DIFFICULTY = 1

FPS = 60
SCORE_CHANGE = 1
OBSTACLE_SPEED_SCALE = 1.0

# FROG
FROG_IDLE_IMAGE_NAME = "Resources/frogIdle.png"
FROG_JUMP_IMAGE_NAME = "Resources/frogJumping.png"

FROG_START_POS_X = (int)(7.5*BOX_WIDTH)
FROG_START_POS_Y = (int)(13.5*BOX_HEIGHT)

JUMP_HORIZONTAL = 50
JUMP_VERTICAL = 58

STARTING_DIRECTION = "up"
STARTING_SPRITE_COUNTER = 1
STARTING_LIVES = 3
STARTING_WINS = 0
STARTING_SCORE = 5000

# LIVES
LIFE3_IMAGE_NAME = "Resources/Life3.png"
LIFE2_IMAGE_NAME = "Resources/Life2.png"
LIFE1_IMAGE_NAME = "Resources/Life1.png"

LIVES_IMAGE_POS_X = (int)(5.5*BOX_WIDTH)
LIVES_IMAGE_POS_Y = 0

# WINS
WIN0_IMAGE_NAME = "Resources/win0.png"
WIN1_IMAGE_NAME = "Resources/win1.png"
WIN2_IMAGE_NAME = "Resources/win2.png"
WIN3_IMAGE_NAME = "Resources/win3.png"

WINS_IMAGE_POS_X = 10*BOX_WIDTH
WINS_IMAGE_POS_Y = 0

# DIFFICULTY
HARD_STARTING_SCORE = 10000
HARD_SCORE_CHANGE = 2
HARD_OBSTACLES_SPEED_SCALE = 1.2

# START GAME MENU
START_GAME_TITLE_FONT_SIZE = 60
START_GAME_OPTIONS_FONT_SIZE = 20

START_GAME_OPTIONS_NUMBER = 5
START_GAME_START_INDEX = 0
START_GAME_MUSIC_INDEX = 1
START_GAME_SOUND_EFFECTS_INDEX = 2
START_GAME_DIFFICULTY_INDEX = 3
START_GAME_EXIT_INDEX = 4

START_GAME_TEXT_POS_X = (int)(0.5*SCREEN_WIDTH)
START_GAME_TITLE_POS_Y = 3*BOX_HEIGHT
START_GAME_START_POS_Y = 5*BOX_HEIGHT 
START_GAME_MUSIC_POS_Y = 6*BOX_HEIGHT
START_GAME_SOUND_EFFECTS_POS_Y = 7*BOX_HEIGHT
START_GAME_DIFFICULTY_POS_Y = 8*BOX_HEIGHT
START_GAME_EXIT_POS_Y = 9*BOX_HEIGHT

# PAUSE MENU
PAUSE_BACKGROUND_IMAGE_NAME = "Resources/pauseBackground.png"

PAUSE_MESSAGE_FONT_SIZE = 50
PAUSE_OPTIONS_FONT_SIZE = 20

PAUSE_TEXT_POS_X = (int)(0.5*SCREEN_WIDTH)
PAUSE_MESSAGE_POS_Y = 3*BOX_HEIGHT
PAUSE_UNPAUSE_POS_Y = 5*BOX_HEIGHT
PAUSE_RESTART_POS_Y = 6*BOX_HEIGHT
PAUSE_MUSIC_POS_Y = 7*BOX_HEIGHT
PAUSE_SOUND_EFFECTS_POS_Y = 8*BOX_HEIGHT
PAUSE_EXIT_POS_Y = 9*BOX_HEIGHT

PAUSE_OPTIONS_NUMBER = 5
PAUSE_UNPAUSE_INDEX = 0
PAUSE_RESTART_INDEX = 1

PAUSE_MUSIC_INDEX = 2
PAUSE_SOUND_EFFECTS_INDEX = 3
PAUSE_EXIT_INDEX = 4

PAUSE_BACKGROUND_CENTER_POS_X = (int)(0.5*SCREEN_WIDTH)
PAUSE_BACKGROUND_CENTER_POS_Y = (int)(0.5*SCREEN_HEIGHT)

# GAME OVER MENU
GAME_OVER_MESSAGE_FONT_SIZE = 40
GAME_OVER_OPTIONS_FONT_SIZE = 20

GAME_OVER_TEXT_POS_X = (int)(0.5*SCREEN_WIDTH)
GAME_OVER_MESSAGE_POS_Y = 4*BOX_HEIGHT
GAME_OVER_RESTART_POS_Y = 6*BOX_HEIGHT
GAME_OVER_EXIT_POS_Y = 7*BOX_HEIGHT

GAME_OVER_OPTIONS_NUMBER = 2
GAME_OVER_RESTART_INDEX = 0
GAME_OVER_EXIT_INDEX = 1

# VEHICLES
CAR1_IMAGE_NAME = 'Resources/Car(1).png'
CAR2_IMAGE_NAME = 'Resources/Car(2).png'
CAR3_IMAGE_NAME = 'Resources/Car(3).png'
TRUCK_IMAGE_NAME = 'Resources/Truck.png'
DIGGER_IMAGE_NAME = 'Resources/Digger.png'

CAR1_POS_X = 6*BOX_WIDTH
CAR2_POS_X = 2*BOX_WIDTH
CAR3_POS_X = 12*BOX_WIDTH
TRUCK_POS_X = 4*BOX_WIDTH
DIGGER_POS_X = 8*BOX_WIDTH

CAR1_POS_Y = (int)(8.5*BOX_HEIGHT)
CAR2_POS_Y = (int)(10.5*BOX_HEIGHT)
CAR3_POS_Y = (int)(12.5*BOX_HEIGHT)
TRUCK_POS_Y = (int)(11.5*BOX_HEIGHT)
DIGGER_POS_Y = (int)(9.5*BOX_HEIGHT)

CAR1_SPEED = -5
CAR2_SPEED = -6
CAR3_SPEED = 4
TRUCK_SPEED = 3
DIGGER_SPEED = 2

# LOGS
LOG2_IMAGE_NAME = 'Resources/Log(2).png'
LOG3_1_IMAGE_NAME = 'Resources/Log(3).png'
LOG3_2_IMAGE_NAME = 'Resources/Log(3).png'
LOG5_IMAGE_NAME = 'Resources/Log(5).png'
LOG8_IMAGE_NAME = 'Resources/Log(8).png'

LOG2_POS_X = 7*BOX_WIDTH
LOG3_1_POS_X = 3*BOX_WIDTH
LOG3_2_POS_X = 5*BOX_WIDTH
LOG5_POS_X = 5*BOX_WIDTH
LOG8_POS_X = 7*BOX_WIDTH

LOG2_POS_Y = (int)(5.5*BOX_HEIGHT)
LOG3_1_POS_Y = (int)(6.5*BOX_HEIGHT)
LOG3_2_POS_Y = (int)(2.5*BOX_HEIGHT)
LOG5_POS_Y = (int)(3.5*BOX_HEIGHT)
LOG8_POS_Y = (int)(4.5*BOX_HEIGHT)

LOG2_SPEED = -3
LOG3_1_SPEED = 5
LOG3_2_SPEED = -4
LOG5_SPEED = 5
LOG8_SPEED = 3

def gameLoop():
    while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game.exitGame()
                    elif event.key == pygame.K_p:
                        game.pauseGame()
                elif event.type == pygame.QUIT:
                    game.exitGame()
                player.move(event)
            screen.blit(game.background, game.window.topleft)
            for thing in logs:
                thing.move()
            for thing in vehicles:
                thing.move()
            player.detectHit()
            player.detectDrowning()
            player.detectWin()
            player.changeSprite()
            game.displayScore()
            pygame.display.update()
            game.clock.tick(FPS)

class Game(object):
    def __init__(self):
        self.initVariables()
        self.displayStartGameScreen()
        self.initDifficulty()
        self.initObstacles()
        self.initSoundEffects()
        self.initLives()
        self.initWins()

    def initVariables(self):
        pygame.display.set_caption("Frogger")
        self.window = screen.get_rect()
        self.background = pygame.image.load(BACKGROUND_IMAGE_NAME).convert()
        self.clock = pygame.time.Clock()
        self.gameRunning = False
        self.playMusic = True
        self.playSoundEffects = True
        self.difficulty = NORMAL_DIFFICULTY

    def displayStartGameScreen(self):
        self.playTrack("Resources/stageStart.mp3", PLAY_TRACK_ONCE)
        self.gameRunning = False
        chosenOptionIndex = 0
        titleFont = pygame.font.Font("Resources/munro.ttf", START_GAME_TITLE_FONT_SIZE)
        optionsFont = pygame.font.Font("Resources/munro.ttf", START_GAME_OPTIONS_FONT_SIZE)
        optionsColors = [GREEN_COLOR, GREEN_COLOR, GREEN_COLOR, GREEN_COLOR, GREEN_COLOR]

        while self.gameRunning is False:
            screen.fill(BLACK_COLOR)

            for optionIndex in range(START_GAME_OPTIONS_NUMBER):
                if optionIndex == chosenOptionIndex:
                    optionsColors[optionIndex] = RED_COLOR
                else:
                    optionsColors[optionIndex] = GREEN_COLOR
            
            if self.playMusic:
                musicStatus = "ON"
            else:
                musicStatus = "OFF"
            if self.playSoundEffects:
                soundEffectsStatus = "ON"
            else:
                soundEffectsStatus = "OFF"
            if self.difficulty == NORMAL_DIFFICULTY:
                difficultyStatus = "NORMAL"
            else:
                difficultyStatus = "HARD"

            self.displayText(titleFont, "Frogger", GREEN_COLOR, START_GAME_TEXT_POS_X, START_GAME_TITLE_POS_Y)
            self.displayText(optionsFont, "START", optionsColors[START_GAME_START_INDEX], START_GAME_TEXT_POS_X, START_GAME_START_POS_Y)
            self.displayText(optionsFont, ("MUSIC:  "  + musicStatus), optionsColors[START_GAME_MUSIC_INDEX], START_GAME_TEXT_POS_X, START_GAME_MUSIC_POS_Y)
            self.displayText(optionsFont, ("SOUND EFFECTS:  " + soundEffectsStatus), optionsColors[START_GAME_SOUND_EFFECTS_INDEX], START_GAME_TEXT_POS_X, START_GAME_SOUND_EFFECTS_POS_Y)
            self.displayText(optionsFont, ("DIFFICULTY:  " + difficultyStatus), optionsColors[START_GAME_DIFFICULTY_INDEX], START_GAME_TEXT_POS_X, START_GAME_DIFFICULTY_POS_Y) 
            self.displayText(optionsFont, "EXIT", optionsColors[START_GAME_EXIT_INDEX], START_GAME_TEXT_POS_X, START_GAME_EXIT_POS_Y)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        chosenOptionIndex -= 1
                        if chosenOptionIndex < START_GAME_START_INDEX:
                            chosenOptionIndex = START_GAME_EXIT_INDEX
                    elif event.key == pygame.K_DOWN:
                        chosenOptionIndex += 1
                        if chosenOptionIndex > START_GAME_EXIT_INDEX:
                            chosenOptionIndex = START_GAME_START_INDEX
                    elif (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                        if chosenOptionIndex == START_GAME_START_INDEX:
                            self.playTrack("Resources/stageTheme.mp3", PLAY_TRACK_INDEFINIETLY)
                            self.gameRunning = True
                        elif chosenOptionIndex == START_GAME_MUSIC_INDEX:
                            self.playMusic = not self.playMusic
                        elif chosenOptionIndex == START_GAME_SOUND_EFFECTS_INDEX:
                            self.playSoundEffects = not self.playSoundEffects
                        elif chosenOptionIndex == START_GAME_DIFFICULTY_INDEX:
                            if self.difficulty == NORMAL_DIFFICULTY:
                                self.difficulty = HARD_DIFFICULTY
                            else:
                                self.difficulty = NORMAL_DIFFICULTY
                        elif chosenOptionIndex == START_GAME_EXIT_INDEX:
                            self.exitGame()
                    elif event.key == pygame.K_ESCAPE:
                        self.exitGame()
                elif event.type == pygame.QUIT:
                    game.exitGame()
        
            if not self.playMusic:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()

    def initDifficulty(self):
        if self.difficulty == HARD_DIFFICULTY:
            player.score = HARD_STARTING_SCORE
            SCORE_CHANGE = HARD_SCORE_CHANGE
            OBSTACLE_SPEED_SCALE = HARD_OBSTACLES_SPEED_SCALE

    def initObstacles(self):
        tempObstacle = Obstacle(CAR1_POS_X, CAR1_POS_Y, OBSTACLE_SPEED_SCALE*CAR1_SPEED, CAR1_IMAGE_NAME)
        vehicles.append(tempObstacle)
        tempObstacle = Obstacle(CAR2_POS_X, CAR2_POS_Y, OBSTACLE_SPEED_SCALE*CAR2_SPEED, CAR2_IMAGE_NAME)
        vehicles.append(tempObstacle)
        tempObstacle = Obstacle(CAR3_POS_X, CAR3_POS_Y, OBSTACLE_SPEED_SCALE*CAR3_SPEED, CAR3_IMAGE_NAME)
        vehicles.append(tempObstacle)
        tempObstacle = Obstacle(TRUCK_POS_X, TRUCK_POS_Y, OBSTACLE_SPEED_SCALE*TRUCK_SPEED, TRUCK_IMAGE_NAME)
        vehicles.append(tempObstacle)
        tempObstacle = Obstacle(DIGGER_POS_X, DIGGER_POS_Y, OBSTACLE_SPEED_SCALE*DIGGER_SPEED, DIGGER_IMAGE_NAME)
        vehicles.append(tempObstacle)

        tempObstacle = Obstacle(LOG2_POS_X, LOG2_POS_Y, OBSTACLE_SPEED_SCALE*LOG2_SPEED, LOG2_IMAGE_NAME)
        logs.append(tempObstacle)
        tempObstacle = Obstacle(LOG3_1_POS_X, LOG3_1_POS_Y, OBSTACLE_SPEED_SCALE*LOG3_1_SPEED, LOG3_1_IMAGE_NAME)
        logs.append(tempObstacle)
        tempObstacle = Obstacle(LOG3_2_POS_X, LOG3_2_POS_Y, OBSTACLE_SPEED_SCALE*LOG3_2_SPEED, LOG3_2_IMAGE_NAME)
        logs.append(tempObstacle)
        tempObstacle = Obstacle(LOG5_POS_X, LOG5_POS_Y, OBSTACLE_SPEED_SCALE*LOG5_SPEED, LOG5_IMAGE_NAME)
        logs.append(tempObstacle)
        tempObstacle = Obstacle(LOG8_POS_X, LOG8_POS_Y, OBSTACLE_SPEED_SCALE*LOG8_SPEED, LOG8_IMAGE_NAME)
        logs.append(tempObstacle)

    def initSoundEffects(self):
        self.soundEffects = []
        self.soundEffects.append(pygame.mixer.Sound(FROG_HOP_SOUND_FILE_NAME))
        self.soundEffects.append(pygame.mixer.Sound(FROG_PLONK_SOUND_FILE_NAME))
        self.soundEffects.append(pygame.mixer.Sound(FROG_SQUASH_SOUND_FILE_NAME))
        self.soundEffects.append(pygame.mixer.Sound(WIN_SOUND_FILE_NAME))

    def initLives(self):
        self.livesSprites = []
        self.livesSprites.append(pygame.image.load(LIFE1_IMAGE_NAME))
        self.livesSprites.append(pygame.image.load(LIFE2_IMAGE_NAME))
        self.livesSprites.append(pygame.image.load(LIFE3_IMAGE_NAME))
        self.livesSurface = self.livesSprites[2]
        self.livesRectangle = self.livesSurface.get_rect()
        self.livesRectangle.topleft = (LIVES_IMAGE_POS_X, LIVES_IMAGE_POS_Y)

    def initWins(self):
        self.winsSprites = []
        self.winsSprites.append(pygame.image.load(WIN0_IMAGE_NAME))
        self.winsSprites.append(pygame.image.load(WIN1_IMAGE_NAME))
        self.winsSprites.append(pygame.image.load(WIN2_IMAGE_NAME))
        self.winsSprites.append(pygame.image.load(WIN3_IMAGE_NAME))
        self.winsSurface = self.winsSprites[0]
        self.winsRectangle = self.winsSurface.get_rect()
        self.winsRectangle.topleft = (WINS_IMAGE_POS_X, WINS_IMAGE_POS_Y)

    def playTrack(self, trackName, trackPlayTime):
        pygame.mixer.music.load(trackName)
        pygame.mixer.music.play(trackPlayTime)
        if self.playMusic is False:
            pygame.mixer.music.pause()

    def playSoundEffect(self, soundEffectIndex):
        if self.playSoundEffects:
            self.soundEffects[soundEffectIndex].play()

    def displayScore(self):
        if player.score > 0:
            player.score -= SCORE_CHANGE

        scoreValueFont = pygame.font.Font("Resources/munro.ttf", SCORE_VALUE_FONT_SIZE)
        font = pygame.font.Font("Resources/munro.ttf", SCORE_FONT_SIZE)

        self.displayText(font, "SCORE: ", YELLOW_COLOR, GAME_SCORE_TEXT_POS_X, GAME_TEXT_POS_Y)
        self.displayText(scoreValueFont, str(player.score), YELLOW_COLOR, GAME_SCORE_VALUE_POS_X, GAME_TEXT_POS_Y)
        self.displayText(font, "LIVES: ", YELLOW_COLOR, GAME_LIVES_TEXT_POS_X, GAME_TEXT_POS_Y)
        self.displayText(font, "WINS: ", YELLOW_COLOR, GAME_WINS_TEXT_POS_X, GAME_TEXT_POS_Y)
        screen.blit(self.livesSurface, self.livesRectangle)
        screen.blit(self.winsSurface, self.winsRectangle)

    def pauseGame(self):
        pygame.mixer.music.pause()
        self.gameRunning = False
        chosenOptionIndex = 0
        messageFont = pygame.font.Font("Resources/munro.ttf", PAUSE_MESSAGE_FONT_SIZE)
        optionsFont = pygame.font.Font("Resources/munro.ttf", PAUSE_OPTIONS_FONT_SIZE)
        optionsColors = [GREEN_COLOR, GREEN_COLOR, GREEN_COLOR, GREEN_COLOR, GREEN_COLOR]

        while self.gameRunning is False:
            self.displayPauseBackground()

            for optionIndex in range(PAUSE_OPTIONS_NUMBER):
                if optionIndex == chosenOptionIndex:
                    optionsColors[optionIndex] = RED_COLOR
                else:
                    optionsColors[optionIndex] = GREEN_COLOR
            
            if self.playMusic:
                musicStatus = "ON"
            else:
                musicStatus = "OFF"
            if self.playSoundEffects:
                soundEffectsStatus = "ON"
            else:
                soundEffectsStatus = "OFF"

            self.displayText(messageFont, "PAUSED", YELLOW_COLOR, PAUSE_TEXT_POS_X, PAUSE_MESSAGE_POS_Y)
            self.displayText(optionsFont, "UNPAUSE", optionsColors[PAUSE_UNPAUSE_INDEX], PAUSE_TEXT_POS_X, PAUSE_UNPAUSE_POS_Y)
            self.displayText(optionsFont, "RESTART", optionsColors[PAUSE_RESTART_INDEX], PAUSE_TEXT_POS_X, PAUSE_RESTART_POS_Y)
            self.displayText(optionsFont, ("MUSIC:  "  + musicStatus), optionsColors[PAUSE_MUSIC_INDEX], PAUSE_TEXT_POS_X, PAUSE_MUSIC_POS_Y)
            self.displayText(optionsFont, ("SOUND EFFECTS:  " + soundEffectsStatus), optionsColors[PAUSE_SOUND_EFFECTS_INDEX], PAUSE_TEXT_POS_X, PAUSE_SOUND_EFFECTS_POS_Y)
            self.displayText(optionsFont, "EXIT", optionsColors[PAUSE_EXIT_INDEX], PAUSE_TEXT_POS_X, PAUSE_EXIT_POS_Y)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        chosenOptionIndex -= 1
                        if chosenOptionIndex < PAUSE_UNPAUSE_INDEX:
                            chosenOptionIndex = PAUSE_EXIT_INDEX
                    elif event.key == pygame.K_DOWN:
                        chosenOptionIndex += 1
                        if chosenOptionIndex > PAUSE_EXIT_INDEX:
                            chosenOptionIndex = PAUSE_UNPAUSE_INDEX
                    elif event.key == pygame.K_p:
                        self.unpauseGame()
                    elif (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                        if chosenOptionIndex == PAUSE_UNPAUSE_INDEX:
                            self.unpauseGame()
                        elif chosenOptionIndex == PAUSE_RESTART_INDEX:
                            self.unpauseGame()
                            self.gameRunning = False
                            self.restartGame()
                        elif chosenOptionIndex == PAUSE_MUSIC_INDEX:
                            self.playMusic = not self.playMusic
                        elif chosenOptionIndex == PAUSE_SOUND_EFFECTS_INDEX:
                            self.playSoundEffects = not self.playSoundEffects
                        elif chosenOptionIndex == PAUSE_EXIT_INDEX:
                            self.exitGame()
                    elif event.key == pygame.K_ESCAPE:
                        self.exitGame()
                elif event.type == pygame.QUIT:
                    game.exitGame()

    def unpauseGame(self):
        if self.playMusic is True:
            pygame.mixer.music.unpause()
        self.gameRunning = True

    def displayPauseBackground(self):
        backgroundSurface = pygame.image.load(PAUSE_BACKGROUND_IMAGE_NAME)
        backgroundRectangle = backgroundSurface.get_rect()
        backgroundRectangle.center = (PAUSE_BACKGROUND_CENTER_POS_X, PAUSE_BACKGROUND_CENTER_POS_Y)
        screen.blit(backgroundSurface, backgroundRectangle)

    def changeLivesSprite(self):
        if player.lives > 0 and player.lives <= 3:
            self.livesSurface = self.livesSprites[player.lives-1]

    def changeWinsSprite(self):
        if (player.wins >= 0 and player.wins <= 3):
            self.winsSurface = self.winsSprites[player.wins]

    def displayText(self, font, text, color, posX, posY):
        message = font.render(text, True, color)
        messageBox = message.get_rect()
        messageBox.center = (posX, posY)
        screen.blit(message, messageBox)

    def displayGameOverScreen(self):
        self.playTrack("Resources/gameOver.mp3", PLAY_TRACK_ONCE)
        self.gameRunning = False
        chosenOptionIndex = 0
        messageFont = pygame.font.Font("Resources/munro.ttf", GAME_OVER_MESSAGE_FONT_SIZE)
        optionsFont = pygame.font.Font("Resources/munro.ttf", GAME_OVER_OPTIONS_FONT_SIZE)
        optionsColors = [GREEN_COLOR, GREEN_COLOR]

        while self.gameRunning is False:
            screen.fill(BLACK_COLOR)

            if player.lives == 0:
                messageText = "You Lost :c"
            else:
                messageText = "You Won!"

            for optionIndex in range(GAME_OVER_OPTIONS_NUMBER):
                if optionIndex == chosenOptionIndex:
                    optionsColors[optionIndex] = RED_COLOR
                else:
                    optionsColors[optionIndex] = GREEN_COLOR

            self.displayText(messageFont, messageText, YELLOW_COLOR, GAME_OVER_TEXT_POS_X, GAME_OVER_MESSAGE_POS_Y)
            self.displayText(optionsFont, "RESTART", optionsColors[GAME_OVER_RESTART_INDEX], GAME_OVER_TEXT_POS_X, GAME_OVER_RESTART_POS_Y)
            self.displayText(optionsFont, "EXIT", optionsColors[GAME_OVER_EXIT_INDEX], GAME_OVER_TEXT_POS_X, GAME_OVER_EXIT_POS_Y)

            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        chosenOptionIndex -= 1
                        if chosenOptionIndex < GAME_OVER_RESTART_INDEX:
                            chosenOptionIndex = GAME_OVER_EXIT_INDEX
                    elif event.key == pygame.K_DOWN:
                        chosenOptionIndex += 1
                        if chosenOptionIndex > GAME_OVER_EXIT_INDEX:
                            chosenOptionIndex = GAME_OVER_RESTART_INDEX
                    elif (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                        if chosenOptionIndex == GAME_OVER_RESTART_INDEX:
                            self.restartGame()
                        elif chosenOptionIndex == GAME_OVER_EXIT_INDEX:
                            self.exitGame()
                    elif event.key == pygame.K_ESCAPE:
                        self.exitGame()
                elif event.type == pygame.QUIT:
                    game.exitGame()

    def restartGame(self):
        player.lives = STARTING_LIVES
        self.changeLivesSprite()
        player.score = STARTING_SCORE
        player.wins = STARTING_WINS
        self.changeWinsSprite()
        player.rectangle.center = (FROG_START_POS_X, FROG_START_POS_Y)
        self.displayStartGameScreen()

    def exitGame(self):
        pygame.quit()
        sys.exit()

class Obstacle(object):
    def __init__(self, posX, posY, speed, image):
        self.surface = pygame.image.load(image)
        self.rectangle = self.surface.get_rect()
        self.rectangle.center = (posX, posY)
        self.speed = speed

    def move(self):
        if (self.rectangle.left < WINDOW_LEFT or self.rectangle.right > WINDOW_RIGHT):
            self.surface = pygame.transform.flip(self.surface, True, False)
            self.speed = -self.speed
        self.rectangle = self.rectangle.move(self.speed, 0)
        screen.blit(self.surface, self.rectangle)

class Frog(object):
    def __init__(self):
        self.idleSprite = pygame.image.load(FROG_IDLE_IMAGE_NAME)
        self.jumpSprite = pygame.image.load(FROG_JUMP_IMAGE_NAME)
        self.surface = self.idleSprite
        self.rectangle = self.surface.get_rect()
        self.rectangle.center = (FROG_START_POS_X, FROG_START_POS_Y)
        self.direction = STARTING_DIRECTION
        self.counter = STARTING_SPRITE_COUNTER
        self.score = STARTING_SCORE
        self.lives = STARTING_LIVES
        self.wins = STARTING_WINS

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.playSoundEffect(FROG_HOP_SOUND_INDEX)
                self.direction = "left"
                self.counter = 2
                self.rectangle = self.rectangle.move(-JUMP_HORIZONTAL, 0)
            if event.key == pygame.K_RIGHT:
                game.playSoundEffect(FROG_HOP_SOUND_INDEX)
                self.direction = "right"
                self.counter = 2
                self.rectangle = self.rectangle.move(JUMP_HORIZONTAL, 0)
            if event.key == pygame.K_UP:
                game.playSoundEffect(FROG_HOP_SOUND_INDEX)
                self.direction = "up"
                self.counter = 2
                self.rectangle = self.rectangle.move(0, -JUMP_VERTICAL)
            if event.key == pygame.K_DOWN:
                game.playSoundEffect(FROG_HOP_SOUND_INDEX)
                self.direction = "down"
                self.counter = 2
                self.rectangle = self.rectangle.move(0, JUMP_VERTICAL)

    def detectWallCollision(self):
        if self.rectangle.right > WINDOW_RIGHT:
            self.rectangle.right = WINDOW_RIGHT
        if self.rectangle.left < WINDOW_LEFT:
            self.rectangle.left = WINDOW_LEFT
        if self.rectangle.top < BOX_HEIGHT:
            self.rectangle.top = BOX_HEIGHT
        if self.rectangle.bottom > WINDOW_BOTTOM:
            self.rectangle.bottom = WINDOW_BOTTOM

    def changeDirection(self, sprite):
        if self.direction == "up":
            self.surface = sprite
        elif self.direction == "down":
            self.surface = pygame.transform.flip(sprite, False, True)
        elif self.direction == "left":
            self.surface = pygame.transform.rotate(sprite, ROTATION_ANGLE)
        else:
            self.surface = pygame.transform.rotate(sprite, -ROTATION_ANGLE)

    def changeSprite(self):
        if self.counter == 7:
            self.counter = STARTING_SPRITE_COUNTER
            self.changeDirection(self.idleSprite)
        elif self.counter != STARTING_SPRITE_COUNTER:
            if self.counter == 2:
                self.changeDirection(self.jumpSprite)
            self.counter += 1
        self.detectWallCollision()
        screen.blit(self.surface, self.rectangle)

    def detectHit(self):
        if self.rectangle.centery > PAVEMENT2_POS_Y and self.rectangle.centery < PAVEMENT1_POS_Y:
            for thing in vehicles:
                if thing.rectangle.colliderect(self.rectangle):
                    game.playSoundEffect(FROG_SQUASH_SOUND_INDEX)
                    self.removeLife()

    def detectDrowning(self):
        if self.rectangle.centery < PAVEMENT2_POS_Y and self.rectangle.centery > GRASS_POS_Y:
            for thing in logs:
                if thing.rectangle.colliderect(self.rectangle):
                    self.rectangle = self.rectangle.move(thing.speed, 0)
                    return 0
            game.playSoundEffect(FROG_PLONK_SOUND_INDEX)
            self.removeLife()

    def detectWin(self):
        if self.rectangle.centery == GRASS_POS_Y:
            self.wins += 1
            game.changeWinsSprite()
            game.playSoundEffect(WIN_SOUND_INDEX)
            self.score += STARTING_SCORE
            self.rectangle.center = (FROG_START_POS_X, FROG_START_POS_Y)
            if self.wins == 3:
                game.displayGameOverScreen()

    def removeLife(self):
        self.lives -= 1
        game.changeLivesSprite()
        self.rectangle.center = (FROG_START_POS_X, FROG_START_POS_Y)
        if self.lives == 0:
            game.displayGameOverScreen()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
vehicles = []
logs = []
player = Frog()
game = Game()
gameLoop()

