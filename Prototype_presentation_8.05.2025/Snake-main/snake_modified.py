import pygame, sys, random
import json
import time
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
        self.right_sound = pygame.mixer.Sound(f"{current_dir}/Sound/right_codon.mp3")
        self.wrong_sound = pygame.mixer.Sound(f"{current_dir}/Sound/wrong_codon.mp3")

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

    def play_right_sound(self):
        self.right_sound.play()
        
    def play_wrong_sound(self):
        self.wrong_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(0, 0)
        self.codon_history = []


class CODON:
    def __init__(self):
        self.types = ["c", "s", "q", "x", "f", "d"]
        self.shapes = {"c": "circle", "s": "star", "q": "square", "x": "cross", "f": "flower", "d": "diamond"}
        self.images = {
            codon: pygame.image.load(f"{current_dir}/Graphics/{self.shapes[codon]}.png").convert_alpha()
            for codon in self.shapes
        }
        self.current_type = None
        self.pos = None
        self.spawn_time = pygame.time.get_ticks()  # Track spawn time
        self.randomize()

    @property
    def expired(self):
        return pygame.time.get_ticks() - self.spawn_time > random.randint(5000, 10000)

    def randomize(self):
        self.x = random.randint(0, cell_number_x - 1)
        self.y = random.randint(0, cell_number_y - 1)
        self.pos = Vector2(self.x, self.y)

        # Favor spawning the next needed codon
        if random.random() < 0.55:  # 55% chance
            self.current_type = current_recipe[recipe_index]
        else:
            # Pick a random codon that is *not* the next needed one
            other_codons = [c for c in self.types if c != current_recipe[recipe_index]]
            self.current_type = random.choice(other_codons)

    def draw_codon(self):
        x_px = int(self.pos.x * cell_size)
        y_px = int(self.pos.y * cell_size) + header_height
        
        img = self.images[self.current_type]

        screen.blit(img, (x_px, y_px))


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.codons = [CODON() for _ in range(4)]  # 8 codons on screen
        self.last_codon_time = pygame.time.get_ticks()
        self.active = False  # Game starts paused
        self.game_over_reason = None
        self.snake_speed = 150  # Initial speed in ms
        self.level_up_every = 5  # Increase speed every 5 codons
        self.speed_floor = 50    # Fastest allowed speed
        self.codons_eaten = 0
        self.tutorial_shown = False

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
        if pygame.time.get_ticks() - self.last_codon_time >= random.randint(500, 1000):
            # Get occupied positions (by snake and existing codons)
            occupied_positions = set((int(codon.pos.x), int(codon.pos.y)) for codon in self.codons)
            occupied_positions.update((int(block.x), int(block.y)) for block in self.snake.body)

            # Try spawning at a free position (limit attempts to prevent infinite loop)
            max_attempts = 50
            for _ in range(max_attempts):
                new_codon = CODON()
                new_pos = (int(new_codon.pos.x), int(new_codon.pos.y))
                if new_pos not in occupied_positions:
                    self.codons.append(new_codon)
                    self.last_codon_time = pygame.time.get_ticks()
                    break
                
    def update_speed(self):
        new_speed = max(
            self.speed_floor,
            150 - (self.codons_eaten // self.level_up_every) * 10
        )
        if new_speed != self.snake_speed:
            self.snake_speed = new_speed
            pygame.time.set_timer(SCREEN_UPDATE, self.snake_speed)

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
                self.codons_eaten += 1
                self.update_speed()
                
                if actual_codon == expected_codon:
                    self.snake.play_right_sound()
                else:
                    self.snake.play_wrong_sound()
                
                self.codons.remove(codon)

                recipe_index += 1  # Always advance, even on errors

                if recipe_index >= len(current_recipe):
                    self.protein_complete()
                break

    def check_fail(self):
        if (
            not 0 <= self.snake.body[0].x < cell_number_x
            or not 0 <= self.snake.body[0].y < cell_number_y
        ):
            self.game_over_reason = "ooops... you hit the edge!"
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over_reason = "ooops... you tangled up!"
                self.game_over()

    def reset_game(self):
        self.reset_recipe_progress()
        self.select_new_protein()
        self.snake.reset()
        self.codons_eaten = 0
        self.snake_speed = 200  # Reset speed to starting value
        pygame.time.set_timer(SCREEN_UPDATE, self.snake_speed)  
        self.codons = [CODON() for _ in range(2)]
        self.last_codon_time = pygame.time.get_ticks()
        self.draw_header()
        pygame.display.update()
        self.active = False
        
    def game_over(self):
        if self.game_over_reason:
            failure.play()
            choice = self.show_popup(
                "Game Over :(",
                self.game_over_reason,
                emoji_img=emoji_cross
            )
            self.game_over_reason = None  # Clear for next round

            if choice == "tutorial":
                self.reset_game()
                self.show_tutorial()
                return  # Exit early so reset_game is NOT called

        self.reset_game()
    
    def protein_complete(self):
        errors = 0
        for i, (expected, actual) in enumerate(
            zip(current_recipe, self.snake.codon_history)
        ):
            if expected != actual:
                errors += 1
                if i in active_sites:
                    time.sleep(1)
                    failure.play()
                    self.show_popup(
                        "Oh no! Wrong codon in the active site!",
                        "The protein is inactive :(",
                        emoji_img=emoji_cross,
                    )
                    
                    self.game_over()
                    
                    return

        error_rate = errors / len(current_recipe)
        if error_rate > 0.3:
            time.sleep(1)
            failure.play()
            self.show_popup(
                "Oh no! Your protein is misfolded!",
                f"{errors} wrong codons in the sequence ({error_rate:.0%})! The protein cannot work :(",
                emoji_img=emoji_cross,
            )
            self.game_over()
            
            return

        description = current_protein_data.get(
            "description", "No description available."
        )
        time.sleep(1)
        success.play()
        self.show_popup(f"Congratulations! You correctly synthesised {current_protein_name.upper()}!", description, emoji_img=emoji_check)
        self.reset_game()

    def draw_grass(self):
        grass_color = (229,225,207)
        for row in range(cell_number_x):
            if row % 2 == 0:
                for col in range(cell_number_x):
                    if col % 2 == 0:
                        # Add header_height offset to y position
                        grass_rect = pygame.Rect(
                            col * cell_size,
                            row * cell_size + header_height,
                            cell_size,
                            cell_size,
                        )
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number_x):
                    if col % 2 != 0:
                        # Add header_height offset to y position
                        grass_rect = pygame.Rect(
                            col * cell_size,
                            row * cell_size + header_height,
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
        
    def show_tutorial(self):
        tutorial_text = (
            "Welcome to Codon Snake!"
            "🧬 Collect codons by moving the snake onto them."
            "✅ Follow the recipe shown at the top of the screen."
            "⚠️ Wrong codons may cause the protein to misfold."
            "🧠 Active site codons are especially important!"
            "🎮 Controls:"
            "Use arrow keys to move the snake."
            "🍎 The snake grows with each codon."
            "🚫 Avoid crashing into the wall or yourself."
            "Good luck making a functional protein!"
        )

        # Popup dimensions
        popup_width = 600
        popup_height = 500
        popup_x = (screen_width - popup_width) // 2
        popup_y = (screen_height - popup_height) // 2

        # Button
        button_width = 200
        button_height = 50
        button_x = popup_x + (popup_width - button_width) // 2
        button_y = popup_y + popup_height - button_height - 20
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        # Wrap text
        wrapped_lines = self.wrap_text(tutorial_text, game_font, popup_width - 40)

        while True:
            # Background
            screen.fill((223, 218, 196))

            # Popup box
            pygame.draw.rect(screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height))
            pygame.draw.rect(screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 4)

            # Title
            title_surf = game_font.render("Tutorial", True, (0, 0, 0))
            screen.blit(title_surf, (popup_x + 20, popup_y + 20))

            # Body text
            for i, line in enumerate(wrapped_lines):
                text_surface = game_font.render(line, True, (50, 50, 50))
                screen.blit(text_surface, (popup_x + 20, popup_y + 60 + i * 30))

            # Button
            pygame.draw.rect(screen, (100, 200, 100), button_rect)
            pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
            button_text = game_font.render("Start Game", True, (0, 0, 0))
            text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, text_rect)

            pygame.display.update()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        return


    def draw_header(self):
        global active_sites
        header_rect = pygame.Rect(0, 0, screen_width, header_height)
        pygame.draw.rect(screen, (255, 255, 255), header_rect)

        # 1. Title
        title_text = f"let's build {current_protein_name.upper()}"
        title_surf = game_font.render(title_text, True, (0, 0, 0))
        title_rect = title_surf.get_rect(centerx=screen_width // 2, y=10)
        screen.blit(title_surf, title_rect)

        # 2. Prefix + icons
        prefix = "follow this recipe:"
        prefix_surf = game_font.render(prefix, True, (0, 0, 0))
        prefix_width = prefix_surf.get_width()
        spacing = 4
        num = len(current_recipe)
        icons_width = num * header_icon_size + (num - 1) * spacing
        total_width = prefix_width + 10 + icons_width
        start_x = (screen_width - total_width) // 2
        icon_y = 50

        screen.blit(prefix_surf, (start_x, icon_y))
        prefix_end = start_x + prefix_width

        # 3. Precompute x‐positions for each codon icon
        icon_positions = []                             
        for i in range(num):
            x = prefix_end + 10 + i * (header_icon_size + spacing)
            icon_positions.append(x)                    

        # 4. Group contiguous active_sites into runs
        runs = []                                       
        for idx in sorted(active_sites):                
            if not runs or idx > runs[-1][-1] + 1:      
                runs.append([idx, idx])                 
            else:                                      
                runs[-1][-1] = idx                      

        # 5. Draw highlights for each run
        pad = 4                                        
        highlight_color = (167,0,0)
        highlight_shift = 3               
        for start_idx, end_idx in runs:                
            x_start = icon_positions[start_idx]       
            x_end   = icon_positions[end_idx]          
            run_width = (end_idx - start_idx) * (header_icon_size + spacing) + header_icon_size
            rect = pygame.Rect(
                x_start - pad + highlight_shift,                         
                icon_y - pad + 2,                          
                run_width + pad * 2,                   
                header_icon_size + pad * 2             
            )
            pygame.draw.rect(
                screen,
                highlight_color,
                rect,
                width=3,
                border_radius=7
            )

        # 6. Draw icons + progress
        for i, codon in enumerate(current_recipe):
            x = icon_positions[i]                      
            screen.blit(CODON_ICONS[codon], (x, icon_y))

            # progress square
            square_size = 25
            square_y = icon_y + header_icon_size + 10
            square_rect = pygame.Rect(
                x + (header_icon_size - square_size)//2,
                square_y,
                square_size,
                square_size
            )
            if i < len(self.snake.codon_history):
                emoji_img = emoji_check if self.snake.codon_history[i] == current_recipe[i] else emoji_cross
                emoji_rect = emoji_img.get_rect(center=square_rect.center)
                screen.blit(emoji_img, emoji_rect)
            else:
                pygame.draw.rect(screen, (180,180,180), square_rect, width=1)

    def wrap_text(self, text, font, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        if current_line:
            lines.append(current_line.strip())
        return lines
    
    def show_popup(self, message, submessage, emoji_img=None):
        popup_width = 500
        popup_height = 300
        popup_x = (screen_width - popup_width) // 2
        popup_y = (screen_height - popup_height) // 2

        # Button dimensions
        button_width = 180
        button_height = 50

        # "Play Again" button
        play_button_rect = pygame.Rect(
            popup_x + 40,
            popup_y + 220,
            button_width,
            button_height
        )

        # "Tutorial" button
        tutorial_button_rect = pygame.Rect(
            popup_x + popup_width - 40 - button_width,
            popup_y + 220,
            button_width,
            button_height
        )

        while True:
            # Draw popup background
            pygame.draw.rect(screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height))
            pygame.draw.rect(screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 4)

            # Emoji
            if emoji_img:
                emoji_rect = emoji_img.get_rect(topleft=(popup_x + 20, popup_y + 20))
                screen.blit(emoji_img, emoji_rect)

            # Title
            title_surf = game_font.render(message, True, (0, 0, 0))
            screen.blit(title_surf, (popup_x + 60, popup_y + 20))

            # Body text (wrapped)
            wrapped_lines = self.wrap_text(submessage, game_font, popup_width - 40)
            for i, line in enumerate(wrapped_lines):
                sub_surf = game_font.render(line, True, (50, 50, 50))
                screen.blit(sub_surf, (popup_x + 20, popup_y + 60 + i * 30))

            # Play Again button
            pygame.draw.rect(screen, (100, 200, 100), play_button_rect)
            pygame.draw.rect(screen, (0, 0, 0), play_button_rect, 2)
            play_text = game_font.render("Play Again", True, (0, 0, 0))
            screen.blit(play_text, play_text.get_rect(center=play_button_rect.center))

            # Tutorial button
            pygame.draw.rect(screen, (180, 180, 255), tutorial_button_rect)
            pygame.draw.rect(screen, (0, 0, 0), tutorial_button_rect, 2)
            tutorial_text = game_font.render("View Tutorial", True, (0, 0, 0))
            screen.blit(tutorial_text, tutorial_text.get_rect(center=tutorial_button_rect.center))

            pygame.display.update()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        return "play"
                    elif tutorial_button_rect.collidepoint(event.pos):
                        return "tutorial"


    # def show_popup(self, message, submessage, emoji_img=None):
    #     popup_width = 500
    #     popup_height = 250
    #     popup_x = (screen_width - popup_width) // 2
    #     popup_y = (screen_height - popup_height) // 2

    #     button_width = 200
    #     button_height = 50
    #     button_x = popup_x + (popup_width - button_width) // 2
    #     button_y = popup_y + 170
    #     button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    #     while True:
    #         # Draw popup box
    #         pygame.draw.rect(
    #             screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height)
    #         )
    #         pygame.draw.rect(
    #             screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 4
    #         )

    #         # Draw emoji at the top-left corner of the popup
    #         if emoji_img:
    #             emoji_rect = emoji_img.get_rect(
    #                 topleft=(popup_x + 20, popup_y + 20)
    #             )  # Position emoji at the top-left corner
    #             screen.blit(emoji_img, emoji_rect)

    #         # Draw message (title) text to the right of the emoji
    #         title_surf = game_font.render(message, True, (0, 0, 0))
    #         screen.blit(
    #             title_surf, (popup_x + 60, popup_y + 20)
    #         )  # Offset to make room for the emoji

    #         # Wrap and draw submessage (body text)
    #         wrapped_lines = self.wrap_text(submessage, game_font, popup_width - 40)
    #         for i, line in enumerate(wrapped_lines):
    #             sub_surf = game_font.render(line, True, (50, 50, 50))
    #             screen.blit(
    #                 sub_surf, (popup_x + 20, popup_y + 60 + i * 30)
    #             )  # Added extra spacing

    #         # Draw button
    #         pygame.draw.rect(screen, (100, 200, 100), button_rect)
    #         pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
    #         button_text = game_font.render("play again", True, (0, 0, 0))
    #         text_rect = button_text.get_rect(center=button_rect.center)
    #         screen.blit(button_text, text_rect)

    #         pygame.display.update()

    #         # Wait for button click or quit
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 if button_rect.collidepoint(event.pos):
    #                     return


with open(f"{current_dir}/proteins_db.json") as f:
    PROTEINS = json.load(f)

# Choose a random protein from the database
current_protein_data = random.choice(PROTEINS)
current_protein_name = current_protein_data["name"]
current_recipe = current_protein_data["sequence"]
active_sites = current_protein_data["active_sites"]
recipe_index = 0

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
infoObject = pygame.display.Info()
screen_width = infoObject.current_w - 5
header_height = 130  # Space for protein info
screen_height = infoObject.current_h - 115  # Leave space for taskbars etc.

cell_size = 30
cell_number_x = screen_width // cell_size
cell_number_y = (screen_height - header_height) // cell_size

screen_width = cell_number_x * cell_size
screen_height = (cell_number_y * cell_size) + header_height

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
game_font = pygame.font.Font(f"{current_dir}/Font/PoetsenOne-Regular.ttf", 25)
emoji_check = pygame.image.load(
    f"{current_dir}/Graphics/check_emoji.png"
).convert_alpha()
emoji_cross = pygame.image.load(
    f"{current_dir}/Graphics/cross_emoji.png"
).convert_alpha()

header_icon_size = 35
shapes = {"c": "circle", "s": "star", "q": "square", "x": "cross", "f": "flower", "d": "diamond"}
CODON_ICONS = {
    codon: pygame.image.load(f"{current_dir}/Graphics/{shapes[codon]}.png").convert_alpha()
            for codon in shapes
}

success = pygame.mixer.Sound(f"{current_dir}/Sound/you_won.wav")
failure = pygame.mixer.Sound(f"{current_dir}/Sound/you_lost.wav")

emoji_check = pygame.transform.scale(emoji_check, (30, 30))
emoji_cross = pygame.transform.scale(emoji_cross, (30, 30))

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    if not main_game.tutorial_shown:
        main_game.show_tutorial()
        main_game.tutorial_shown = True
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if not main_game.active and main_game.game_over_reason:
                main_game.reset_game()
                main_game.active = True
            else:
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

    screen.fill((223,218,196))
    main_game.draw_elements()
    game_area = pygame.Rect(
        0, header_height, screen_width, screen_height - header_height
    )
    pygame.draw.rect(screen, (0, 0, 0), game_area, 2)
    pygame.display.update()
    clock.tick(60)


# add short tutorial
# improve final message window + add protein drawing

# add proteins to db??
# add shapes added into snake body???
