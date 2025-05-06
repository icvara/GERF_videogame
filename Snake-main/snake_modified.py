import pygame, sys, random
import json
from pygame.math import Vector2
from pathlib import Path

# Path to the current file
current_file = Path(__file__)

# Directory containing the file
current_dir = current_file.parent


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(0, 0)
        self.codon_history = []
        self.new_block = False

        self.head_up = pygame.image.load(
            f"{current_dir}/Graphics/head_up.png"
        ).convert_alpha()
        self.head_down = pygame.image.load(
            f"{current_dir}/Graphics/head_down.png"
        ).convert_alpha()
        self.head_right = pygame.image.load(
            f"{current_dir}/Graphics/head_right.png"
        ).convert_alpha()
        self.head_left = pygame.image.load(
            f"{current_dir}/Graphics/head_left.png"
        ).convert_alpha()

        self.tail_up = pygame.image.load(
            f"{current_dir}/Graphics/tail_up.png"
        ).convert_alpha()
        self.tail_down = pygame.image.load(
            f"{current_dir}/Graphics/tail_down.png"
        ).convert_alpha()
        self.tail_right = pygame.image.load(
            f"{current_dir}/Graphics/tail_right.png"
        ).convert_alpha()
        self.tail_left = pygame.image.load(
            f"{current_dir}/Graphics/tail_left.png"
        ).convert_alpha()

        self.body_vertical = pygame.image.load(
            f"{current_dir}/Graphics/body_vertical.png"
        ).convert_alpha()
        self.body_horizontal = pygame.image.load(
            f"{current_dir}/Graphics/body_horizontal.png"
        ).convert_alpha()

        self.body_tr = pygame.image.load(
            f"{current_dir}/Graphics/body_tr.png"
        ).convert_alpha()
        self.body_tl = pygame.image.load(
            f"{current_dir}/Graphics/body_tl.png"
        ).convert_alpha()
        self.body_br = pygame.image.load(
            f"{current_dir}/Graphics/body_br.png"
        ).convert_alpha()
        self.body_bl = pygame.image.load(
            f"{current_dir}/Graphics/body_bl.png"
        ).convert_alpha()
        self.crunch_sound = pygame.mixer.Sound(f"{current_dir}/Sound/crunch.wav")

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
        self.codon_history = []


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
        if random.random() < 0.75:  # 75% chance
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
                actual_codon = codon.current_type
                expected_codon = current_recipe[recipe_index]

                self.snake.codon_history.append(actual_codon)
                self.snake.add_block()
                self.codons.remove(codon)

                recipe_index += 1  # Always advance, even on errors

                if recipe_index >= len(current_recipe):
                    self.protein_complete()
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
        errors = 0
        for i, (expected, actual) in enumerate(zip(current_recipe, self.snake.codon_history)):
            if expected != actual:
                errors += 1
                if i in active_sites:
                    self.show_popup("❌ Misfolded Protein", "Error in active site!")
                    self.game_over()
                    return

        error_rate = errors / len(current_recipe)
        if error_rate > 0.3:
            self.show_popup("❌ Misfolded Protein", f"{errors} errors ({error_rate:.0%})")
            self.game_over()
            return

        description = current_protein_data.get("description", "No description available.")
        self.show_popup("✅ Protein Synthesized!", description)
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

    def reset_recipe_progress(self):
        global recipe_index
        recipe_index = 0

    def select_new_protein(self):
        global current_protein_data, current_protein_name, current_recipe, active_sites, recipe_index
        current_protein_data = random.choice(PROTEINS)
        current_protein_name = current_protein_data["name"]
        current_recipe = current_protein_data["sequence"]
        active_sites = current_protein_data["active_sites"]
        recipe_index = 0

    def draw_header(self):
        header_rect = pygame.Rect(0, 0, screen_width, header_height)
        pygame.draw.rect(screen, (255, 255, 255), header_rect)  # Changed to white

        # Protein name
        title_text = f"Building: {current_protein_name}"
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
        
    def show_popup(self, message, submessage):
        popup_width = 500
        popup_height = 250
        popup_x = (screen_width - popup_width) // 2
        popup_y = (screen_height - popup_height) // 2

        button_width = 200
        button_height = 50
        button_x = popup_x + (popup_width - button_width) // 2
        button_y = popup_y + 170
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        while True:
            # Draw popup box
            pygame.draw.rect(screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height))
            pygame.draw.rect(screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 4)

            # Draw text
            title_surf = game_font.render(message, True, (0, 0, 0))
            sub_surf = game_font.render(submessage, True, (50, 50, 50))
            screen.blit(title_surf, (popup_x + 20, popup_y + 20))
            screen.blit(sub_surf, (popup_x + 20, popup_y + 80))

            # Draw button
            pygame.draw.rect(screen, (100, 200, 100), button_rect)
            pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
            button_text = game_font.render("Play Again", True, (0, 0, 0))
            text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, text_rect)

            pygame.display.update()

            # Wait for button click or quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        return

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 30
cell_number = 20

with open(f"{current_dir}/proteins_db.json") as f:
    PROTEINS = json.load(f)

# Choose a random protein from the database
current_protein_data = random.choice(PROTEINS)
current_protein_name = current_protein_data["name"]
current_recipe = current_protein_data["sequence"]
active_sites = current_protein_data["active_sites"]
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

# make graphics look better
# add different visual / sound for wrong codon incorporation
