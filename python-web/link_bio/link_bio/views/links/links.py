import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio import constants as const


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Github", 
            "Repositorio personal",
            "icons/github-brands-solid.svg",
            const.GITHUB_URL
            ),
        link_button(
            "LinkedIn", 
            "Perfil profesional",
            "icons/linkedin.svg",
            const.LINKEDIN_URL
            ),
        link_button(
            "X",
            "Cuenta de Twitter",
            "icons/x-twitter.svg",
            const.TWITTER_X_URL
            ),
        link_button(
            "Instagram",
            "Perfil de Instagram",
            "icons/instagram.svg",
            const.INSTAGRAM_URL
            ),
        
        title("Contacto"),
        link_button(
            "Email",
            "¿Quieres que siga creando más contenido?",
            "icons/envelope.svg",
            f"mailto:{const.EMAIL}"
            ),
        width= "100%",
        spacing="2"     
    )