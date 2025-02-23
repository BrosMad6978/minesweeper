import pygame


def draw_text(
    surface: pygame.Surface,
    text: str,
    size: int,
    x: int,
    y: int,
    color: tuple[int, int, int] = (255, 255, 255),
):
    """
    Draw text on the screen

    Args:
        surface: pygame surface to draw on
        text: string to display
        size: font size
        x, y: position on screen
        color: RGB tuple, default is white
    """
    font = pygame.font.Font(None, size)  # None uses default system font
    text_surface = font.render(text, True, color)  # True enables anti-aliasing
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)  # Centers text at given position
    surface.blit(text_surface, text_rect)


def draw_rect(
    surface: pygame.Surface,
    color_with_alpha: tuple[int, int, int, int],
    rect: pygame.Rect | tuple[int, int, int, int],
):
    """
    Draw a transparent rectangle with borders
    surface: pygame surface to draw on
    color: border color (RGB tuple)
    rect: pygame.Rect or tuple of (x, y, width, height)
    border_width: thickness of the border
    """
    # Create a surface with alpha channel
    rect_surface = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    pygame.draw.rect(
        rect_surface,
        color_with_alpha,
        (
            0,
            0,
            rect[2],
            rect[3],
        ),
    )

    # Blit the transparent rectangle onto the main surface
    surface.blit(rect_surface, (rect[0], rect[1]))
