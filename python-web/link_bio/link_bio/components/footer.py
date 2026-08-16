import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.jpg",
            height=Size.VERY_BIG.value,
            weight=Size.VERY_BIG.value,
            alt="Logotipo de Abrahamdev. \"AF\" entre llaves"
            ),
        rx.link(
            f"© 2020-{datetime.date.today().year} Abrahamdev by Abraham Flores",
                href=const.ABRAHAMDEV_URL,
                is_external=True,
                font_size=Size.MEDIUM.value,
                text_align="center"
                ),
        rx.text("BUILD YOUR DREAMS FROM CANCUN TO THE WORLD",
                font_size=Size.MEDIUM.value,
                margin_top=Size.ZERO.value,
                text_align="center"
                ),
        align_items="center",
        justify_content="center",
        margin_bottom=Size.BIG.value,
        padding_x=Size.SMALL.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
        spacing="4"
    )
