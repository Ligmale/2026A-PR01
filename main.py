#!./venv/bin/python
# ======================== main.py ========================
import sys
import pygame

from config import FPS, doodle_dict
from game import (
    apply_gravity,
    check_game_over,
    check_platform_collisions,
    move_doodle,
    move_platforms,
    restart_game,
    scroll_camera,
)
from window import draw_window, generate_initial_platforms, show_game_over_message

# Initialisation de Pygame et de l'horloge
pygame.init()
clock = pygame.time.Clock()
running = True

# Génération initiale des plateformes avant de lancer la boucle
generate_initial_platforms()

# ======================== BOUCLE PRINCIPALE ========================
while running:
    clock.tick(FPS)

    # 1. Gestion des événements (clavier et fermeture de fenêtre)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if doodle_dict["lives"] <= 0 and event.key == pygame.K_r:
                restart_game()

    # 2. Gestion de l'état Game Over
    if doodle_dict["lives"] <= 0:
        show_game_over_message()
        continue

    # 3. Logique du jeu
    move_doodle()
    apply_gravity()
    move_platforms()
    check_platform_collisions()
    scroll_camera()
    check_game_over()

    # 4. Affichage graphique
    draw_window()

# Fermeture propre de Pygame
pygame.quit()
sys.exit()
