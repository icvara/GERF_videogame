import pygame, sys, random, os
import json
import time
from pygame.math import Vector2
from pathlib import Path
from screeninfo import get_monitors

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

        self.head_up = SNAKE_PARTS["head"]["up"]
        self.head_down = SNAKE_PARTS["head"]["down"]
        self.head_right = SNAKE_PARTS["head"]["right"]
        self.head_left = SNAKE_PARTS["head"]["left"]

        self.tail_up = SNAKE_PARTS["tail"]["up"]
        self.tail_down = SNAKE_PARTS["tail"]["down"]
        self.tail_right = SNAKE_PARTS["tail"]["right"]
        self.tail_left = SNAKE_PARTS["tail"]["left"]

        self.body_vertical = SNAKE_PARTS["body"]["vertical"]
        self.body_horizontal = SNAKE_PARTS["body"]["horizontal"]

        self.body_tr = SNAKE_PARTS["body"]["tr"]
        self.body_tl = SNAKE_PARTS["body"]["tl"]
        self.body_br = SNAKE_PARTS["body"]["br"]
        self.body_bl = SNAKE_PARTS["body"]["bl"]

        self.right_sound = right_sound
        self.wrong_sound = wrong_sound

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
                    turn_lookup = {
                        ((-1, 0), (0, -1)): self.body_tl,
                        ((0, -1), (-1, 0)): self.body_tl,
                        ((-1, 0), (0, 1)): self.body_bl,
                        ((0, 1), (-1, 0)): self.body_bl,
                        ((1, 0), (0, -1)): self.body_tr,
                        ((0, -1), (1, 0)): self.body_tr,
                        ((1, 0), (0, 1)): self.body_br,
                        ((0, 1), (1, 0)): self.body_br,
                    }
                    key = (previous_block.x, previous_block.y), (
                        next_block.x,
                        next_block.y,
                    )
                    sprite = turn_lookup.get(key)
                    if sprite:
                        screen.blit(sprite, block_rect)

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
        if self.new_block:
            new_head = self.body[0] + self.direction
            self.body.insert(0, new_head)
            if not self.new_block:
                self.body.pop()
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
        self.current_type = None
        self.images = CODON_ICONS
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

        self.x_px = int(self.pos.x * cell_size)
        self.y_px = int(self.pos.y * cell_size) + header_height

        # Favor spawning the next needed codon
        if random.random() < 0.55:  # 55% chance
            self.current_type = current_recipe[recipe_index]
        else:
            # Pick a random codon that is *not* the next needed one
            other_codons = [c for c in self.types if c != current_recipe[recipe_index]]
            self.current_type = random.choice(other_codons)

        self.img = self.images[self.current_type]

    def draw_codon(self):
        screen.blit(self.img, (self.x_px, self.y_px))


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.codons = [CODON() for _ in range(1)]  # 0 codons on screen
        self.last_codon_time = pygame.time.get_ticks()
        self.active = False  # Game starts paused
        self.game_over_reason = None
        self.snake_speed = 150  # Initial speed in ms
        self.level_up_every = 5  # Increase speed every 5 codons
        self.speed_floor = 50  # Fastest allowed speed
        self.codons_eaten = 0
        self.tutorial_shown = False
        self.protein_correct = protein_correct
        self.protein_misfolded = protein_misfolded
        self.protein_inactive = protein_inactive

    def update(self):
        if not self.active:
            return
        current_time = pygame.time.get_ticks()
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.check_codon_spawn(current_time)
        self.remove_expired_codons(current_time)

    def draw_elements(self):
        self.draw_header()  # Draw header FIRST
        self.draw_grass()  # Then draw grass UNDERNEATH
        for codon in self.codons:
            codon.draw_codon()
        self.snake.draw_snake()

    def check_codon_spawn(self, current_time):
        if current_time - self.last_codon_time >= random.randint(500, 1000):
            # Get occupied positions (by snake and existing codons)
            occupied_positions = set(
                (int(codon.pos.x), int(codon.pos.y)) for codon in self.codons
            )
            occupied_positions.update(
                (int(block.x), int(block.y)) for block in self.snake.body
            )

            # Try spawning at a free position (limit attempts to prevent infinite loop)
            max_attempts = 50
            for _ in range(max_attempts):
                new_codon = CODON()
                new_pos = (int(new_codon.pos.x), int(new_codon.pos.y))
                if new_pos not in occupied_positions:
                    self.codons.append(new_codon)
                    self.last_codon_time = current_time
                    break

    def update_speed(self):
        new_speed = max(
            self.speed_floor, 150 - (self.codons_eaten // self.level_up_every) * 10
        )
        if new_speed != self.snake_speed:
            self.snake_speed = new_speed
            pygame.time.set_timer(SCREEN_UPDATE, self.snake_speed)

    def remove_expired_codons(self, current_time):
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
        self.snake = SNAKE()
        self.reset_recipe_progress()
        self.select_new_protein()
        self.snake.reset()
        self.codons_eaten = 0
        self.snake_speed = 150  # Reset speed to starting value
        pygame.time.set_timer(SCREEN_UPDATE, self.snake_speed)
        self.codons = [CODON() for _ in range(5)]
        self.last_codon_time = pygame.time.get_ticks()
        self.draw_header()
        pygame.display.update()
        self.active = False

    def game_over(self):
        if self.game_over_reason:
            failure.play()
            choice = self.show_gameover_popup(
                "GAME OVER", self.game_over_reason, emoji_img=emoji_gameover
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
                    self.last_description = (
                        "One or more wrong codons found in the active site."
                    )
                    choice = self.show_final_popup(
                        message="Oh no!",
                        submessage="Your protein is inactive!",
                        emoji_img=emoji_sadface,
                        figure_img=self.protein_inactive,
                    )

                    if choice == "tutorial":
                        self.reset_game()
                        self.show_tutorial()
                        return

                    self.reset_game()
                    return

        error_rate = errors / len(current_recipe)
        if error_rate > 0.3:
            time.sleep(1)
            failure.play()
            self.last_description = (
                "Your protein cannot hold its shape and is misfolded!",
            )
            choice = self.show_final_popup(
                message="Oh no!",
                submessage=f"{errors} wrong codons in the sequence ({error_rate:.0%} error rate).",
                emoji_img=emoji_sadface,
                figure_img=self.protein_misfolded,
            )

            if choice == "tutorial":
                self.reset_game()
                self.show_tutorial()
                return

            self.reset_game()
            return

        description = current_protein_data.get(
            "description", "No description available."
        )
        time.sleep(1)
        success.play()
        self.last_description = description
        choice = self.show_final_popup(
            message="Congratulations!",
            submessage=f"You correctly synthesised {current_protein_name.upper()}!",
            emoji_img=emoji_trophy,
            figure_img=self.protein_correct,
        )

        if choice == "tutorial":
            self.reset_game()
            self.show_tutorial()
            return

        self.reset_game()

    def draw_grass(self):
        grass_color = (229, 225, 207)
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
        tutorial_lines = [
            ("", None),
            ("Collect codons by guiding the snake over them.", emoji_snake),
            ("Follow the recipe displayed at the top carefully.", emoji_memo),
            (
                "Incorrect codons can cause the protein to misfold and be inactive.",
                emoji_warning,
            ),
            (
                "Codons in the active site (highlighted by a red rectangle) are the most important!",
                emoji_hollowsquare,
            ),
            (
                "Each codon collected makes the snake grow longer and move faster.",
                emoji_rocket,
            ),
            ("Avoid crashing into walls or running into yourself.", emoji_stop),
            ("", None),
            ("Good luck building a functional food protein!", emoji_dna),
        ]

        # Popup dimensions
        popup_width = 1030
        popup_height = 550
        popup_x = (screen_width - popup_width) // 2
        popup_y = (screen_height - popup_height) // 2

        # Button
        button_width = 200
        button_height = 50
        button_x = popup_x + (popup_width - button_width) // 2
        button_y = popup_y + popup_height - button_height - 20
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        while True:
            # Background
            screen.fill((223, 218, 196))

            # Popup box
            pygame.draw.rect(
                screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height)
            )
            pygame.draw.rect(
                screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 4
            )

            # Title
            title_surf = title_font.render("Welcome to PROTEIN SNAKE!", True, (0, 0, 0))
            title_rect = title_surf.get_rect(
                center=(popup_x + popup_width // 2, popup_y + 40)
            )
            screen.blit(title_surf, title_rect)

            # Body text
            for i, (line, emoji_img) in enumerate(tutorial_lines):
                y = popup_y + 80 + i * 40  # Slightly lower for spacing under title

                # Check if it's the last line
                is_final = i == len(tutorial_lines) - 1

                font_to_use = highlight_font if is_final else game_font
                text_color = (0, 0, 0) if is_final else (50, 50, 50)

                if is_final:
                    text_surface = font_to_use.render(line, True, text_color)
                    total_width = text_surface.get_width()
                    if emoji_img:
                        total_width += emoji_img.get_width() + 10

                    text_x = popup_x + (popup_width - total_width) // 2
                    if emoji_img:
                        screen.blit(emoji_img, (text_x, y))
                        text_x += emoji_img.get_width() + 10

                    screen.blit(text_surface, (text_x, y))
                else:
                    if emoji_img:
                        screen.blit(emoji_img, (popup_x + 20, y))
                        text_x = popup_x + 20 + emoji_img.get_width() + 10
                    else:
                        text_x = popup_x + 20

                    text_surface = font_to_use.render(line, True, text_color)
                    screen.blit(text_surface, (text_x, y))

            # Button
            pygame.draw.rect(screen, (100, 200, 100), button_rect)
            pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
            button_text = game_font.render("start game", True, (0, 0, 0))
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:  # Pressing 'A' on the keyboard
                        return
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:  # Usually A button on gamepads
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
        highlight_color = (167, 0, 0)
        highlight_shift = 3
        for start_idx, end_idx in runs:
            x_start = icon_positions[start_idx]
            x_end = icon_positions[end_idx]
            run_width = (end_idx - start_idx) * (
                header_icon_size + spacing
            ) + header_icon_size
            rect = pygame.Rect(
                x_start - pad + highlight_shift,
                icon_y - pad + 2,
                run_width + pad * 2,
                header_icon_size + pad * 2,
            )
            pygame.draw.rect(screen, highlight_color, rect, width=3, border_radius=7)

        # 6. Draw icons + progress
        for i, codon in enumerate(current_recipe):
            x = icon_positions[i]
            screen.blit(CODON_ICONS[codon], (x, icon_y))

            # progress square
            square_size = 25
            square_y = icon_y + header_icon_size + 10
            square_rect = pygame.Rect(
                x + (header_icon_size - square_size) // 2,
                square_y,
                square_size,
                square_size,
            )
            if i < len(self.snake.codon_history):
                emoji_img = (
                    emoji_check
                    if self.snake.codon_history[i] == current_recipe[i]
                    else emoji_cross
                )
                emoji_rect = emoji_img.get_rect(center=square_rect.center)
                screen.blit(emoji_img, emoji_rect)
            else:
                pygame.draw.rect(screen, (180, 180, 180), square_rect, width=1)

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

    def show_final_popup(self, message, submessage, emoji_img=None, figure_img=None):
        popup_width = 800
        popup_height = 480
        popup_x = (screen_width - popup_width) // 2
        popup_y = (screen_height - popup_height) // 2

        # Button dimensions
        button_width = 200
        button_height = 50
        button_spacing = 40
        button_y = popup_y + popup_height - 70

        # Button positions
        play_button_rect = pygame.Rect(
            popup_x + popup_width // 2 - button_width - button_spacing // 2,
            button_y,
            button_width,
            button_height,
        )

        tutorial_button_rect = pygame.Rect(
            popup_x + popup_width // 2 + button_spacing // 2,
            button_y,
            button_width,
            button_height,
        )

        while True:
            # Draw popup background
            pygame.draw.rect(
                screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height)
            )
            pygame.draw.rect(
                screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 4
            )

            # Title row: emoji + message (centered as a line)
            title_surf = title_font.render(message, True, (0, 0, 0))

            if emoji_img:
                emoji_rect = emoji_img.get_rect()
                total_width = emoji_rect.width + 10 + title_surf.get_width()
                start_x = popup_x + (popup_width - total_width) // 2

                emoji_rect.topleft = (start_x, popup_y + 30)
                title_rect = title_surf.get_rect(
                    midleft=(emoji_rect.right + 10, emoji_rect.centery)
                )
                screen.blit(emoji_img, emoji_rect)
                screen.blit(title_surf, title_rect)
            else:
                title_rect = title_surf.get_rect(
                    center=(popup_x + popup_width // 2, popup_y + 40)
                )
                screen.blit(title_surf, title_rect)

            # Second line: subheadline (centered)
            sub_surf = highlight_font.render(submessage, True, (80, 80, 80))
            sub_rect = sub_surf.get_rect(
                center=(popup_x + popup_width // 2, title_rect.bottom + 30)
            )
            screen.blit(sub_surf, sub_rect)

            # Image and description area
            text_top = sub_rect.bottom + 20
            padding = 30

            if figure_img:
                original_width, original_height = figure_img.get_size()
                if figure_img == self.protein_misfolded:
                    scale_factor = 0.25  # 25% of original size
                else:
                    scale_factor = 0.20  # 20% of original size
                new_size = (
                    int(original_width * scale_factor),
                    int(original_height * scale_factor),
                )
                fig_scaled = pygame.transform.smoothscale(figure_img, new_size)
                fig_rect = fig_scaled.get_rect(topleft=(popup_x + padding, text_top))
                screen.blit(fig_scaled, fig_rect)
                text_x = fig_rect.right + padding
            else:
                text_x = popup_x + padding

            # Wrapped description (to the right of figure, vertically centered)
            wrap_width = popup_width - 320 if figure_img else popup_width - 60
            wrapped_lines = self.wrap_text(self.last_description, game_font, wrap_width)

            text_block_height = len(wrapped_lines) * 30
            start_y = popup_y + (popup_height // 2) - (text_block_height // 2)

            for i, line in enumerate(wrapped_lines):
                text_surf = game_font.render(line, True, (50, 50, 50))
                text_x = popup_x + 300 if figure_img else popup_x + 30
                text_y = start_y + i * 30
                screen.blit(text_surf, (text_x, text_y))

            # Play Again button
            pygame.draw.rect(screen, (100, 200, 100), play_button_rect)
            pygame.draw.rect(screen, (0, 0, 0), play_button_rect, 2)
            play_text = game_font.render("play again", True, (0, 0, 0))
            screen.blit(play_text, play_text.get_rect(center=play_button_rect.center))

            # Tutorial button
            pygame.draw.rect(screen, (180, 180, 255), tutorial_button_rect)
            pygame.draw.rect(screen, (0, 0, 0), tutorial_button_rect, 2)
            tutorial_text = game_font.render("view tutorial", True, (0, 0, 0))
            screen.blit(
                tutorial_text,
                tutorial_text.get_rect(center=tutorial_button_rect.center),
            )

            pygame.display.update()

            # ----- Event handling -----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        return "play"
                    elif tutorial_button_rect.collidepoint(event.pos):
                        return "tutorial"

                # Keyboard input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:  # 'B' key for Play
                        return "play"
                    elif event.key == pygame.K_a:  # 'A' key for Tutorial
                        return "tutorial"

                # Gamepad input
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1:  # Usually 'B' on Xbox-style controllers
                        return "play"
                    elif event.button == 0:  # Usually 'A' on Xbox-style controllers
                        return "tutorial"

    def show_gameover_popup(self, message, submessage, emoji_img=None):
        popup_width = 500
        popup_height = 250
        popup_x = (screen_width - popup_width) // 2
        popup_y = (screen_height - popup_height) // 2

        # Button dimensions
        button_width = 180
        button_height = 50
        button_y = popup_y + popup_height - 70

        # "Play Again" button
        play_button_rect = pygame.Rect(
            popup_x + 40, button_y, button_width, button_height
        )

        # "Tutorial" button
        tutorial_button_rect = pygame.Rect(
            popup_x + popup_width - 40 - button_width,
            button_y,
            button_width,
            button_height,
        )

        while True:
            # Draw popup background
            pygame.draw.rect(
                screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height)
            )
            pygame.draw.rect(
                screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 4
            )

            # ----- Title line with emoji -----
            title_surf = title_font.render(message, True, (0, 0, 0))
            y_header = popup_y + 30

            if emoji_img:
                gap = 10
                pair_width = emoji_img.get_width() + gap + title_surf.get_width()
                x_start = popup_x + (popup_width - pair_width) // 2

                # Draw emoji and title text side-by-side
                emoji_rect = emoji_img.get_rect(topleft=(x_start, y_header))
                screen.blit(emoji_img, emoji_rect)
                screen.blit(
                    title_surf, (x_start + emoji_img.get_width() + gap, y_header)
                )
            else:
                title_rect = title_surf.get_rect(
                    center=(popup_x + popup_width // 2, y_header)
                )
                screen.blit(title_surf, title_rect)

            # ----- Submessage (reason), centered -----
            y_offset = (
                y_header + title_surf.get_height() + 50
            )  # Extra spacing below title
            wrapped_lines = self.wrap_text(submessage, game_font, popup_width - 80)

            for i, line in enumerate(wrapped_lines):
                line_surf = game_font.render(line, True, (50, 50, 50))
                line_rect = line_surf.get_rect(
                    center=(popup_x + popup_width // 2, y_offset + i * 30)
                )
                screen.blit(line_surf, line_rect)

            # ----- Buttons -----
            pygame.draw.rect(screen, (100, 200, 100), play_button_rect)
            pygame.draw.rect(screen, (0, 0, 0), play_button_rect, 2)
            play_text = game_font.render("play again", True, (0, 0, 0))
            screen.blit(play_text, play_text.get_rect(center=play_button_rect.center))

            pygame.draw.rect(screen, (180, 180, 255), tutorial_button_rect)
            pygame.draw.rect(screen, (0, 0, 0), tutorial_button_rect, 2)
            tutorial_text = game_font.render("view tutorial", True, (0, 0, 0))
            screen.blit(
                tutorial_text,
                tutorial_text.get_rect(center=tutorial_button_rect.center),
            )

            pygame.display.update()

            # ----- Event handling -----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        return "play"
                    elif tutorial_button_rect.collidepoint(event.pos):
                        return "tutorial"

                # Keyboard input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:  # 'B' key for Play
                        return "play"
                    elif event.key == pygame.K_a:  # 'A' key for Tutorial
                        return "tutorial"

                # Gamepad input
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1:  # Usually 'B' on Xbox-style controllers
                        return "play"
                    elif event.button == 0:  # Usually 'A' on Xbox-style controllers
                        return "tutorial"



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
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None
    
    
monitors = get_monitors()
for i, m in enumerate(monitors):
    print(f"Monitor {i}: {m.width}x{m.height} at ({m.x}, {m.y})")

# Use the second monitor if available
if len(monitors) > 1:
    screen_width = monitors[1].width
    screen_height = monitors[1].height - 10
    screen_x = monitors[1].x
    screen_y = monitors[1].y
else:
    screen_width = monitors[0].width
    screen_height = monitors[0].height - 10
    screen_x = monitors[0].x
    screen_y = monitors[0].y
    
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{screen_x},{screen_y}"
screen = pygame.display.set_mode((screen_width, screen_height))

header_height = 130  # Space for protein info

cell_size = 30
cell_number_x = screen_width // cell_size
cell_number_y = (screen_height - header_height) // cell_size

screen_width = cell_number_x * cell_size
screen_height = (cell_number_y * cell_size) + header_height

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
game_font = pygame.font.Font(f"{current_dir}/Font/PoetsenOne-Regular.ttf", 25)
title_font = pygame.font.Font(f"{current_dir}/Font/PoetsenOne-Regular.ttf", 30)
highlight_font = pygame.font.Font(f"{current_dir}/Font/PoetsenOne-Regular.ttf", 28)


def load_scaled(path, size=(30, 30)):
    return pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), size)


emoji_check = load_scaled(f"{current_dir}/Graphics/check_emoji.png")
emoji_cross = load_scaled(f"{current_dir}/Graphics/cross_emoji.png")
emoji_trophy = load_scaled(f"{current_dir}/Graphics/trophy.png")
emoji_sadface = load_scaled(f"{current_dir}/Graphics/sadface.png")
emoji_snake = load_scaled(f"{current_dir}/Graphics/snake.png")
emoji_memo = load_scaled(f"{current_dir}/Graphics/memo.png")
emoji_warning = load_scaled(f"{current_dir}/Graphics/warning.png")
emoji_hollowsquare = load_scaled(f"{current_dir}/Graphics/hollow_square.png")
emoji_dna = load_scaled(f"{current_dir}/Graphics/dna.png")
emoji_stop = load_scaled(f"{current_dir}/Graphics/prohibited.png")
emoji_rocket = load_scaled(f"{current_dir}/Graphics/rocket.png")
emoji_gameover = load_scaled(f"{current_dir}/Graphics/game_over.png")

protein_correct = pygame.image.load(f"{current_dir}/Graphics/protein_correct.png")
protein_misfolded = pygame.image.load(f"{current_dir}/Graphics/protein_misfolded.png")
protein_inactive = pygame.image.load(f"{current_dir}/Graphics/protein_inactive.png")

header_icon_size = 40

CODON_ICONS = {
    codon: pygame.image.load(f"{current_dir}/Graphics/{shape}.png").convert_alpha()
    for codon, shape in {
        "c": "circle",
        "s": "star",
        "q": "square",
        "x": "cross",
        "f": "flower",
        "d": "diamond",
    }.items()
}

SNAKE_PARTS = {
    "head": {
        "up": pygame.image.load(f"{current_dir}/Graphics/head_up.png").convert_alpha(),
        "down": pygame.image.load(
            f"{current_dir}/Graphics/head_down.png"
        ).convert_alpha(),
        "right": pygame.image.load(
            f"{current_dir}/Graphics/head_right.png"
        ).convert_alpha(),
        "left": pygame.image.load(
            f"{current_dir}/Graphics/head_left.png"
        ).convert_alpha(),
    },
    "tail": {
        "up": pygame.image.load(f"{current_dir}/Graphics/tail_up.png").convert_alpha(),
        "down": pygame.image.load(
            f"{current_dir}/Graphics/tail_down.png"
        ).convert_alpha(),
        "right": pygame.image.load(
            f"{current_dir}/Graphics/tail_right.png"
        ).convert_alpha(),
        "left": pygame.image.load(
            f"{current_dir}/Graphics/tail_left.png"
        ).convert_alpha(),
    },
    "body": {
        "vertical": pygame.image.load(
            f"{current_dir}/Graphics/body_vertical.png"
        ).convert_alpha(),
        "horizontal": pygame.image.load(
            f"{current_dir}/Graphics/body_horizontal.png"
        ).convert_alpha(),
        "tr": pygame.image.load(f"{current_dir}/Graphics/body_tr.png").convert_alpha(),
        "tl": pygame.image.load(f"{current_dir}/Graphics/body_tl.png").convert_alpha(),
        "br": pygame.image.load(f"{current_dir}/Graphics/body_br.png").convert_alpha(),
        "bl": pygame.image.load(f"{current_dir}/Graphics/body_bl.png").convert_alpha(),
    },
}

right_sound = pygame.mixer.Sound(f"{current_dir}/Sound/right_codon.mp3")
wrong_sound = pygame.mixer.Sound(f"{current_dir}/Sound/wrong_codon.mp3")
success = pygame.mixer.Sound(f"{current_dir}/Sound/you_won.wav")
failure = pygame.mixer.Sound(f"{current_dir}/Sound/you_lost.wav")

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

key_to_direction = {
    pygame.K_UP: Vector2(0, -1),
    pygame.K_DOWN: Vector2(0, 1),
    pygame.K_LEFT: Vector2(-1, 0),
    pygame.K_RIGHT: Vector2(1, 0),
}

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
                if event.key in key_to_direction:
                    new_dir = key_to_direction[event.key]
                    if new_dir + main_game.snake.direction != Vector2(
                        0, 0
                    ):  # Prevent reversal
                        main_game.snake.direction = new_dir
                        main_game.active = True
                        
        # Joystick hat/dpad
        if event.type == pygame.JOYHATMOTION:
            hat_x, hat_y = event.value
            new_dir = Vector2(hat_x, -hat_y)  # Note: y is inverted
            if new_dir.length() > 0 and new_dir + main_game.snake.direction != Vector2(0, 0):
                main_game.snake.direction = new_dir
                main_game.active = True

        # Optional: Joystick analog stick
        if event.type == pygame.JOYAXISMOTION:
            axis_x = joystick.get_axis(0)
            axis_y = joystick.get_axis(1)
            threshold = 0.5  # Deadzone threshold
            if abs(axis_x) > abs(axis_y):
                if axis_x > threshold:
                    new_dir = Vector2(1, 0)
                elif axis_x < -threshold:
                    new_dir = Vector2(-1, 0)
                else:
                    new_dir = Vector2(0, 0)
            else:
                if axis_y > threshold:
                    new_dir = Vector2(0, 1)
                elif axis_y < -threshold:
                    new_dir = Vector2(0, -1)
                else:
                    new_dir = Vector2(0, 0)
            if new_dir.length() > 0 and new_dir + main_game.snake.direction != Vector2(0, 0):
                main_game.snake.direction = new_dir
                main_game.active = True

    screen.fill((223, 218, 196))
    main_game.draw_elements()
    game_area = pygame.Rect(
        0, header_height, screen_width, screen_height - header_height
    )
    pygame.draw.rect(screen, (0, 0, 0), game_area, 2)
    pygame.display.update()
    clock.tick(60)



# buttons color? and text
# add pause (and add tutorial line about it)
# add start and play again/tutorial with buttons from joystick
# colorblind palette
