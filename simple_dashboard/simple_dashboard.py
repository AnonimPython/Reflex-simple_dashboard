import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def link(
    icon: str = "between-horizontal-start",
    text: str = "Hi",
    href: str = "#",
    ) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon,color="white"),
            rx.text(text,color="white"),
        ),
    href=href,
    _hover={"text_decoration": "none","background_color":"#f600cf"},
    transition="background-color 0.3s ease-in-out",
    background_color="#27292b",
    padding="5px 10px",
    width="100%",
    border_radius="5px",
    )

def card_box(
    main_text: str = "MAIN CONTENT",
    addition_text: str = "ADDITION CONTENT",
    ) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(main_text,font_size="15px",padding="5px"),
            margin_top="5px",
            height="70%",
            background="#333536",
            border_radius="10px",
            text_align="center",
        ),
        rx.box(
            rx.text(addition_text,font_size="15px",padding="5px"),
            margin_top="5px",
            border_radius="10px",
            height="30%", 
            background="#333536",
            text_align="center",
        ),
        width="50%",
        height="200px",
        background="#27292b",
        padding="20px",
        border_radius="20px",
    )

def index() -> rx.Component:
    return rx.container(
        #* left | top | main
        rx.hstack(
            # left
            rx.box(
                rx.hstack(
                    # text + image
                    rx.image("logo.png",width="30px",height="30px"),
                    rx.heading("TechLive",color="white"), 
                    align="center",
                    align_self="center",
                    margin_bottom="50px",
                    
                ),
                # links
                rx.box(
                    
                    rx.vstack(
                        link(
                            icon="grid-2x2",
                            text= "Dashboard",
                            href="#",
                        ),
                        link(
                            icon="notepad-text",
                            text= "Reports",
                            href="#",
                        ),
                        link(
                            icon="database",
                            text= "Data Sources",
                            href="#",
                        ),
                        link(
                            icon="filter",
                            text= "Filter",
                            href="#",
                        ),
                        link(
                            icon="bolt",
                            text= "Settings",
                            href="#",
                        ),
                        link(
                            icon="log-out",
                            text= "Log Out",
                            href="#",
                        ),
                        gap="10px",
                    ),
                ),
                background="#1b1a1d",
                width="300px",
                min_width="200px",
                height="80vh",
                min_height="500px",
                border_radius="20px",
                padding="20px",
            ),
            rx.vstack(
            # top
            rx.box(
                rx.flex(
                    # left
                    rx.text("Dashboard",padding="18px 20px"),
                    # right
                    rx.box(
                        rx.hstack(
                            rx.box(
                            rx.icon(
                                tag="bell",
                                size=24,
                                color="white",
                            ),
                            background_color="#282a2c",
                            padding="8px",
                            border_radius="50%",
                            align_self="center",
                            justify_content="center",
                        ),
                        # person
                        rx.box(
                            rx.image(
                                "/person.jpg",
                                width="40px",
                                height="40px",
                                border_radius="50%",
                                object_fit="cover",
                            ),
                            margin_right="10px",
                            
                        ),
                        ),
                        # icon with background
                        
                        padding="10px",
                        
                    ),
                    
                    width="100%",
                    justify="between",
                    
                ),
                align="center",
                aling_self="center",
                border_radius="20px",
                width="600px",
                height="60px",
                background="#1b1a1d",
                margin_left="20px",
            ),
            # main
            rx.box(
                # name
                rx.text("Welcome Jason!",font_size="30px",weight="bold"),   
                rx.box(
                    rx.flex(
                        rx.text("Overview",font_size="15px",background="#27292b",padding="5px",border_radius="10px"),
                    ),    
                    margin_top="20px",
                ),
                # main content
                #! for test a simple cards with text
                rx.box(
                    rx.flex(
                        card_box(),
                        card_box(),
                        gap="20px",
                    ),    
                    margin_top="20px",
                ),
                align="center",
                aling_self="center",
                padding="30px 20px",
                border_radius="20px",
                width="600px",
                height="100%",
                background="#1b1a1d",
                margin_left="20px", 
            ),
            ),
            width="100%",
            height="100vh",
        ),
        background="#232428",
        color="white",
        margin="auto",
        width="100%",
        height="100vh",
    )


app = rx.App()
app.add_page(index)
