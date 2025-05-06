import pygame, sys, random
from pygame.math import Vector2

# from pathlib import Path

from pathlib import Path

# Path to the current file
current_file = Path(__file__)

# Directory containing the file
current_dir = current_file.parent

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load(
            current_dir / "Graphics/head_up.png"
        ).convert_alpha()
        self.head_down = pygame.image.load(
            current_dir / "Graphics/head_down.png"
        ).convert_alpha()
        self.head_right = pygame.image.load(
            current_dir / "Graphics/head_right.png"
        ).convert_alpha()
        self.head_left = pygame.image.load(
            current_dir / "Graphics/head_left.png"
        ).convert_alpha()

        self.tail_up = pygame.image.load(
            current_dir / "Graphics/tail_up.png"
        ).convert_alpha()
        self.tail_down = pygame.image.load(
            current_dir / "Graphics/tail_down.png"
        ).convert_alpha()
        self.tail_right = pygame.image.load(
            current_dir / "Graphics/tail_right.png"
        ).convert_alpha()
        self.tail_left = pygame.image.load(
            current_dir / "Graphics/tail_left.png"
        ).convert_alpha()

        self.body_vertical = pygame.image.load(
            current_dir / "Graphics/body_vertical.png"
        ).convert_alpha()
        self.body_horizontal = pygame.image.load(
            current_dir / "Graphics/body_horizontal.png"
        ).convert_alpha()

        self.body_tr = pygame.image.load(
            current_dir / "Graphics/body_tr.png"
        ).convert_alpha()
        self.body_tl = pygame.image.load(
            current_dir / "Graphics/body_tl.png"
        ).convert_alpha()
        self.body_br = pygame.image.load(
            current_dir / "Graphics/body_br.png"
        ).convert_alpha()
        self.body_bl = pygame.image.load(
            current_dir / "Graphics/body_bl.png"
        ).convert_alpha()
        self.crunch_sound = pygame.mixer.Sound(current_dir / "Sound/crunch.wav")

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size) + header_height
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if (
                        previous_block.x == -1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == -1
                    ):
                        screen.blit(self.body_tl, block_rect)
                    elif (
                        previous_block.x == -1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == -1
                    ):
                        screen.blit(self.body_bl, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == 1
                    ):
                        screen.blit(self.body_tr, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == 1
                    ):
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(0, 0)


class CODON:
    def __init__(self):
        self.types = ["r", "b", "g", "y"]  # Example codon types
        self.colors = {"r": "red", "b": "blue", "g": "green", "y": "yellow"}
        self.current_type = None
        self.pos = None
        self.spawn_time = pygame.time.get_ticks()  # Track spawn time
        self.randomize()

    @property
    def expired(self):
        return pygame.time.get_ticks() - self.spawn_time > 15000  # 10 seconds

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

        # Favor spawning the next needed codon
        if random.random() < 0.8:  # 80% chance
            self.current_type = current_recipe[recipe_index]
        else:
            # Pick a random codon that is *not* the next needed one
            other_codons = [c for c in self.types if c != current_recipe[recipe_index]]
            self.current_type = random.choice(other_codons)

    def draw_codon(self):
        shape_rect = pygame.Rect(
            int(self.pos.x * cell_size),
            int(self.pos.y * cell_size) + header_height,  # Offset by header
            cell_size,
            cell_size,
        )
        pygame.draw.circle(
            screen, self.colors[self.current_type], shape_rect.center, 15
        )


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.codons = [CODON() for _ in range(3)]  # 3 codons on screen
        self.last_codon_time = pygame.time.get_ticks()
        self.active = False  # Game starts paused

    def update(self):
        if not self.active:
            return
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.check_codon_spawn()
        self.remove_expired_codons()

    def draw_elements(self):
        self.draw_header()  # Draw header FIRST
        self.draw_grass()  # Then draw grass UNDERNEATH
        for codon in self.codons:
            codon.draw_codon()
        self.snake.draw_snake()

    def check_codon_spawn(self):
        # Spawn new codon every 5 seconds
        if pygame.time.get_ticks() - self.last_codon_time > 3000:
            self.codons.append(CODON())
            self.last_codon_time = pygame.time.get_ticks()

    def remove_expired_codons(self):
        current_time = pygame.time.get_ticks()
        self.codons = [c for c in self.codons if not c.expired]

    def check_collision(self):
        global recipe_index

        for codon in self.codons[:]:
            if codon.pos == self.snake.body[0]:
                if codon.current_type == current_recipe[recipe_index]:
                    self.snake.add_block()
                    recipe_index += 1
                    self.codons.remove(codon)
                    if recipe_index >= len(current_recipe):
                        self.protein_complete()
                # else:
                #     self.snake.body.pop()  # Penalty for wrong codon, removes 1 body length
                break

    def check_fail(self):
        if (
            not 0 <= self.snake.body[0].x < cell_number
            or not 0 <= self.snake.body[0].y < cell_number
        ):
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def reset_game(self):
        self.reset_recipe_progress()
        self.select_new_protein()
        self.snake.reset()
        self.codons = [CODON() for _ in range(2)]
        self.last_codon_time = pygame.time.get_ticks()
        self.draw_header()
        pygame.display.update()
        self.active = False

    def game_over(self):
        self.reset_game()

    def protein_complete(self):
        self.reset_game()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        # Add header_height offset to y position
                        grass_rect = pygame.Rect(
                            col * cell_size,
                            row * cell_size + header_height,  # THIS LINE CHANGED
                            cell_size,
                            cell_size,
                        )
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        # Add header_height offset to y position
                        grass_rect = pygame.Rect(
                            col * cell_size,
                            row * cell_size + header_height,  # THIS LINE CHANGED
                            cell_size,
                            cell_size,
                        )
                        pygame.draw.rect(screen, grass_color, grass_rect)

    # def protein_complete(self):
    #     self.reset_recipe_progress()
    #     self.select_new_protein()
    #     self.snake.reset()
    #     self.codons = [CODON() for _ in range(2)]
    #     self.last_codon_time = pygame.time.get_ticks()
    #     self.draw_header()  # Force immediate redraw
    #     pygame.display.update()  # Update display before next frame

    def reset_recipe_progress(self):
        global recipe_index
        recipe_index = 0
        print(f"Reset recipe index to: {recipe_index}")  # Debugging

    def select_new_protein(self):
        global current_protein, current_recipe
        available = list(PROTEIN_RECIPES.keys())
        current_protein = random.choice(available)
        current_recipe = PROTEIN_RECIPES[current_protein]

    def draw_header(self):
        header_rect = pygame.Rect(0, 0, screen_width, header_height)
        pygame.draw.rect(screen, (255, 255, 255), header_rect)  # Changed to white

        # Protein name
        title_text = f"Building: {current_protein}"
        title_surf = game_font.render(title_text, True, (0, 0, 0))
        screen.blit(title_surf, (20, 15))

        # Recipe progress
        recipe_text = "Recipe: " + " ".join(
            [
                f"[{codon}]" if i == recipe_index else codon
                for i, codon in enumerate(current_recipe)
            ]
        )
        recipe_surf = game_font.render(recipe_text, True, (0, 0, 0))
        screen.blit(recipe_surf, (20, 45))


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 30
cell_number = 20

PROTEIN_RECIPES = {
    "Hemoglobin": ["r", "r", "g", "b", "y"],
    "Insulin": ["g", "g", "y", "b"],
    "Collagen": ["b", "y", "r"],
}

current_protein = random.choice(list(PROTEIN_RECIPES.keys()))
current_recipe = PROTEIN_RECIPES[current_protein]
recipe_index = 0

header_height = 80  # Space for protein info
screen_width = cell_number * cell_size
screen_height = (cell_number * cell_size) + header_height
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
apple = pygame.image.load(current_dir / "Graphics/apple.png").convert_alpha()
game_font = pygame.font.Font(current_dir / "Font/PoetsenOne-Regular.ttf", 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
                    main_game.active = True
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
                    main_game.active = True
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
                    main_game.active = True
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                    main_game.active = True

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    game_area = pygame.Rect(
        0, header_height, screen_width, screen_height - header_height
    )
    pygame.draw.rect(screen, (0, 0, 0), game_area, 2)
    pygame.display.update()
    clock.tick(60)

# next things to do: make random codons not random but depend on composition of next codon that needs to appear
# show final message about the protein
# allow incorporation of wrong codons, if too high percent show message about misfolding
# make graphics look better
