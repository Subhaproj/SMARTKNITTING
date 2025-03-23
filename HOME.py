# import flet as ft
# from PAGE1 import get_page1_view
# from PAGE2 import get_page2_view
# from PAGE3 import get_page3_view
# from PAGE4 import get_page4_view
# from flet import *

# def main(page: ft.Page):
#     page.title = "SMART KNITTING"
#     page.theme_mode = ft.ThemeMode.LIGHT  # Light theme
#     page.bgcolor = ft.Colors.BLUE_100  # Background color for home

#     # Hover effect for containers
#     def on_hover(e):
#         if e.data == "true":  # Mouse enters the container
#             e.control.scale = 1.1  # Slight zoom in
#         else:  # Mouse leaves the container
#             e.control.scale = 1.0  # Return to original size
#         e.control.update()

#     # Define containers with unique click actions
#     container1 = ft.Container(
#         content=ft.Column(
#             [
#                 ft.Image(src="icons8-knitting-machine-100.png", width=150, height=150, fit=ft.ImageFit.COVER),
#                 ft.Container(
#                     content=ft.Text("Machine 1", size=15, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
#                     padding=ft.Padding(left=20, top=0, right=15, bottom=0),
#                 ),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         ),
#         width=300,
#         height=200,
#         padding=ft.Padding(left=80, top=10, right=20, bottom=10),
#         bgcolor=ft.Colors.BLUE_400,
#         border_radius=10,
#         shadow=ft.BoxShadow(spread_radius=5, blur_radius=10, color=ft.Colors.BLACK38),
#         animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
#         on_hover=on_hover,  # Add zoom effect on hover
#         on_click=lambda e: (page.views.append(get_page1_view(page)), page.go("/PAGE1"))# Navigate to PAGE1
        
#     )

#     container2 = ft.Container(
#         content=ft.Column(
#             [
#                 ft.Image(src="icons8-knitting-machine-100.png", width=150, height=150, fit=ft.ImageFit.COVER),
#                 ft.Container(
#                     content=ft.Text("Machine 2", size=15, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
#                     padding=ft.Padding(left=20, top=0, right=15, bottom=0),
#                 ),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         ),
#         width=300,
#         height=200,
#         padding=ft.Padding(left=80, top=10, right=20, bottom=10),
#         bgcolor=ft.Colors.BLUE_400,
#         border_radius=10,
#         shadow=ft.BoxShadow(spread_radius=5, blur_radius=10, color=ft.Colors.BLACK38),
#         animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
#         on_hover=on_hover,  # Add zoom effect on hover
#         on_click=lambda e: (page.views.append(get_page2_view(page)), page.go("/PAGE2")) # Navigate to PAGE2
#     )

#     container3 = ft.Container(
#         content=ft.Column(
#             [
#                 ft.Image(src="icons8-knitting-machine-100.png", width=150, height=150, fit=ft.ImageFit.COVER),
#                 ft.Container(
#                     content=ft.Text("Machine 3", size=15, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
#                     padding=ft.Padding(left=20, top=0, right=15, bottom=0),
#                 ),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         ),
#         width=300,
#         height=200,
#         padding=ft.Padding(left=80, top=10, right=20, bottom=10),
#         bgcolor=ft.Colors.BLUE_400,
#         border_radius=10,
#         shadow=ft.BoxShadow(spread_radius=5, blur_radius=10, color=ft.Colors.BLACK38),
#         animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
#         on_hover=on_hover,  # Add zoom effect on hover
#         on_click=lambda e: (page.views.append(get_page3_view(page)), page.go("/PAGE3")) # Navigate to PAGE3
#     )

#     container4 = ft.Container(
#         content=ft.Column(
#             [
#                 ft.Image(src="icons8-knitting-machine-100.png", width=150, height=150, fit=ft.ImageFit.COVER),
#                 ft.Container(
#                     content=ft.Text("Machine 4", size=15, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
#                     padding=ft.Padding(left=20, top=0, right=15, bottom=0),
#                 ),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         ),
#         width=300,
#         height=200,
#         padding=ft.Padding(left=80, top=10, right=20, bottom=10),
#         bgcolor=ft.Colors.BLUE_400,
#         border_radius=10,
#         shadow=ft.BoxShadow(spread_radius=5, blur_radius=10, color=ft.Colors.BLACK38),
#         animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
#         on_hover=on_hover,  # Add zoom effect on hover
#         on_click=lambda e: (page.views.append(get_page4_view(page)),page.go("/PAGE4"))  # Navigate to PAGE4
#     )

#     # Define the home view
#     home_view = ft.View(
#         route="/HOME",
#         controls=[
#             ft.Column(
#                 [
#                     ft.Row(
#                         [container1, container2],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=30,
#                     ),
#                     ft.Row(
#                         [container3, container4],
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         spacing=30,
#                     ),
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 spacing=30,
#             )
#         ],
#         bgcolor=ft.Colors.BLUE_100,
#         padding=ft.Padding(left=10, top=180, right=10, bottom=20),
#     )

#     # Set the initial view to HOME
#     page.views.append(home_view)
#     page.go("/HOME")

# if __name__ == "__main__":
#     ft.app(target=main,view=WEB_BROWSER)
import flet as ft
from PAGE1 import get_page1_view
from PAGE2 import get_page2_view
from PAGE3 import get_page3_view
from PAGE4 import get_page4_view
from flet import *
def main(page: ft.Page):
    page.title = "SMART KNITTING"
    page.theme_mode = ft.ThemeMode.LIGHT  # Light theme
    page.bgcolor = ft.Colors.BLUE_100  # Background color for home
      
    # Hover effect for containers
    def on_hover(e):
        if e.data == "true":  # Mouse enters the container
            e.control.scale = 1.1  # Slight zoom in
        else:  # Mouse leaves the container
            e.control.scale = 1.0  # Return to original size
        e.control.update()

    # Function to create a reusable container
    def create_machine_container(title, page_function):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="icons8-knitting-machine-100.png", width=100, height=100, fit=ft.ImageFit.COVER),
                    ft.Text(title, size=15, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=300,
            height=200,
            padding=ft.Padding(left=20, right=20,top=40,bottom=40),
            bgcolor=ft.Colors.BLUE_400,
            border_radius=10,
            shadow=ft.BoxShadow(spread_radius=5, blur_radius=10, color=ft.Colors.BLACK38),
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            on_hover=on_hover,  # Add zoom effect on hover
            on_click=lambda e: (page.views.append(page_function(page)), page.go(page_function(page).route)),
        )

    # Responsive layout with Flexible rows
    home_view = ft.View(
    route="/HOME",
    scroll=ft.ScrollMode.AUTO,
    controls=[
        ft.ResponsiveRow(
            [
                ft.Column(
                    [
                        ft.Container(
                            content=create_machine_container("Machine 1", get_page1_view),
                            padding=ft.Padding(left=20, right=10, top=10, bottom=10)
                        ),
                        ft.Container(
                            content=create_machine_container("Machine 2", get_page2_view),
                            padding=ft.Padding(left=20, right=10, top=10, bottom=10)
                        ),
                    ],
                    col={"sm": 12, "md": 6},
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                
                ft.Column(
                    [
                        ft.Container(
                            content=create_machine_container("Machine 3", get_page3_view),
                            padding=ft.Padding(left=20, right=10, top=10, bottom=10)
                        ),
                        ft.Container(
                            content=create_machine_container("Machine 4", get_page4_view),
                            padding=ft.Padding(left=20, right=10, top=10, bottom=10)
                        ),
                    ],
                    col={"sm": 12, "md": 6},
                    alignment=ft.MainAxisAlignment.CENTER,
                    
                ),
            ]
            
        )
        
    ],
    bgcolor=ft.Colors.BLUE_100,
    padding=ft.Padding(left=100, right=0, top=80, bottom=5),
    
)
    scroll=ft.ScrollMode.AUTO,
    # Set the initial view to HOME
    page.views.append(home_view)
    page.go("/HOME")

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
