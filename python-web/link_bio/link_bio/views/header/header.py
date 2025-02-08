import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

import datetime
from link_bio import constants as const


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Abraham Flores", 
                src="graduated.jpg",
                fallback="AF",
                radius="full",
                size="7",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px solid #007BFF",
                box_shadow="0 0 8px #007BFF",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Abraham Flores",
                    size="5"
                    ),
                rx.text(
                    "@abrahamdev",
                    margin_top=Size.ZERO.value,
                    color=TextColor.HEADER.value
                ),
                rx.hstack(
                    link_icon(
                    "icons/x-twitter.svg",
                    const.TWITTER_X_URL
                ),
                    link_icon(
                    "icons/instagram.svg",
                    const.INSTAGRAM_URL
                    ),
                    spacing="3"
                ),
                align_items="start",
                
            ),
            spacing="2"
        
        ),
        rx.flex(
            info_text("+4", "años de experiencia"),
            rx.spacer(),
            width="100%"
            
        ),
        rx.text(
            f"""Acabo de descubrir que tengo un superpoder💻
            Amo el código,
            Me encanta viajar,
            Soy estudiante de Data Analyst & Data Science desde hace más de {experience()} años.
            Aquí podrás encontrar todos los enlaces de mis proyectos hasta el momento.
            Bienvenid@!
            #NuncaParesDeAprender📖""",
                
            font_size= Size.MEDIUM.value,
            color=TextColor.BODY.value,
        ),
        spacing="4",
        align_items="start"
        
    )
    
def experience() -> int:
    return datetime.date.today().year - 2021