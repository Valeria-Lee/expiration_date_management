import flet as ft
from flet_camera import Camera

def main(page: ft.Page):
    # nomas ponle el e referente al eventos
    def do_something(e):
        print("hola miguelon")

    page.fonts = {
        "Inter": "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap",
    }

    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # Resolutions based on iPad mini 8.3 dimensions on figma.
    page.title = "Expiration check manager"
    page.window.width = 1024
    page.window.height = 768
    page.window.resizable = False 
    
    page.add(ft.Container(
        content=ft.Text("smart intelligence",size=36,weight=900,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
        height=64,
        padding=6,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.bottom_right,
            colors=["#28377A","#BDD1E3"])
    ))
    
    def home_view(page):
        return ft.View(
            "/",
            [
            ft.Container(
            content=ft.Text(
            "Select an option",
            size=64,
            color="#28377A"),
            alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.Column(
                controls=[ft.ElevatedButton(text="Add new lot",
                style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=48,weight=ft.FontWeight.NORMAL),padding=20),
                on_click=do_something
                ),
                ft.ElevatedButton(text="Check trolley",
                style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=48,weight=ft.FontWeight.NORMAL),padding=20),
                on_click=do_something
                )],
                spacing=24,),
                alignment=ft.alignment.center,
                height=720
            )]
        )

    def scan_view(page):
        return ft.View(
            "/scan",
            [
                
            ]
        )

ft.app(main)
