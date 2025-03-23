
# # # import flet as ft
# # # import matplotlib.pyplot as plt
# # # from io import BytesIO
# # # import base64

# # # # Function to create a bar graph as a base64 image
# # # def create_bar_graph(title, categories, data):
# # #     plt.figure(figsize=(6, 4))
# # #     plt.bar(categories, data, color='#87CEEB')
# # #     plt.xlabel('Categories')
# # #     plt.ylabel('Scores')
# # #     plt.title(title)

# # #     buffer = BytesIO()
# # #     plt.savefig(buffer, format='png')
# # #     buffer.seek(0)
# # #     img_base64 = base64.b64encode(buffer.read()).decode()
# # #     buffer.close()
# # #     return img_base64

# # # # Function to create a pie chart as a base64 image
# # # def create_pie_chart(title, categories, data):
# # #     plt.figure(figsize=(6, 6))
# # #     plt.pie(data, labels=categories, autopct='%1.1f%%', startangle=140, colors=['#FF6666', '#3399FF', '#66FF66', '#FFCC33'], textprops={'fontsize': 10})  # Adjust font size for labels
# # #     plt.title(title, fontsize=14)  # Adjust title font size

# # #     buffer = BytesIO()
# # #     plt.savefig(buffer, format='png')
# # #     buffer.seek(0)
# # #     img_base64 = base64.b64encode(buffer.read()).decode()
# # #     buffer.close()
# # #     return img_base64

# # # # Function to create the PAGE1 view with a top-left button
# # # def get_page1_view(page):
# # #     print("PAGE1 view is being created!")

# # #     # Example data for each month
# # #     monthly_data = {
# # #         "January": [80, 90, 85],
# # #         "February": [75, 85, 80],
# # #         "March": [85, 95, 90],
# # #         "April": [60, 70, 65],
# # #         "May": [90, 85, 80],
# # #         "June": [70, 75, 65],
# # #         "July": [95, 90, 85],
# # #         "August": [85, 80, 75],
# # #         "September": [75, 85, 80],
# # #         "October": [80, 90, 85],
# # #         "November": [60, 75, 70],
# # #         "December": [90, 95, 85],
# # #     }

# # #     # Example yearly data (average scores per subject for all months)
# # #     yearly_data = {
# # #         "2022": [85, 88, 81],
# # #         "2023": [90, 87, 85],
# # #         "2024": [88, 85, 84],
# # #         "2025": [30, 85, 50],
# # #     }

# # #     # Initial graph setup for "January" (default)
# # #     bar_graph_image = ft.Image(
# # #         src_base64=create_bar_graph("Student Scores for January", ['Math', 'Science', 'History'], monthly_data["January"]),
# # #         width=500,
# # #         height=400,
# # #     )
# # #     pie_chart_image = ft.Image(
# # #         src_base64=create_pie_chart("Student Scores for January", ['Math', 'Science', 'History'], monthly_data["January"]),
# # #         width=500,
# # #         height=400,
# # #     )

# # #     # Function to update both graphs based on selected checkbox
# # #     def update_month_graph(selected_month):
# # #         for checkbox in checkboxes:
# # #             checkbox.value = (checkbox.label == selected_month)  # Uncheck others and keep the selected one checked
# # #             checkbox.update()

# # #         # Update the graphs for the selected month
# # #         bar_graph_image.src_base64 = create_bar_graph(f"Student Scores for {selected_month}", ['Math', 'Science', 'History'], monthly_data[selected_month])
# # #         pie_chart_image.src_base64 = create_pie_chart(f"Student Scores for {selected_month}", ['Math', 'Science', 'History'], monthly_data[selected_month])

# # #         bar_graph_image.update()
# # #         pie_chart_image.update()

# # #     # Function to update both graphs based on the selected year from the dropdown
# # #     def update_year_graph(e):
# # #         selected_year = e.control.value
# # #         bar_graph_image.src_base64 = create_bar_graph(
# # #             f"Yearly Student Scores for {selected_year}",
# # #             ['Math', 'Science', 'History'],
# # #             yearly_data[selected_year],
# # #         )
# # #         pie_chart_image.src_base64 = create_pie_chart(
# # #             f"Yearly Student Scores for {selected_year}",
# # #             ['Math', 'Science', 'History'],
# # #             yearly_data[selected_year],
# # #         )
# # #         bar_graph_image.update()
# # #         pie_chart_image.update()

# # #     # Function to handle search input
# # #     def handle_search(e):
# # #         search_query = search_bar.value.lower()
# # #         for checkbox in checkboxes:
# # #             checkbox.visible = search_query in checkbox.label.lower()
# # #             checkbox.update()

# # #     # Function to clear the search bar
# # #     def clear_search(e):
# # #         search_bar.value = ""
# # #         handle_search(e)  # Reset visibility of all checkboxes
# # #         search_bar.update()

# # #     # Create checkboxes for each month
# # #     checkboxes = [
# # #         ft.Checkbox(
# # #             label=month,
# # #             value=(month == "January"),  # Default selection
# # #             on_change=lambda e, month=month: update_month_graph(month),
# # #         )
# # #         for month in monthly_data.keys()
# # #     ]

# # #     # Create dropdown for yearly data selection
# # #     year_dropdown = ft.Dropdown(
# # #         label="Select Year",
# # #         options=[ft.dropdown.Option(year) for year in yearly_data.keys()],
# # #         value="2022",
# # #         on_change=update_year_graph,
# # #     )

# # #     # Add a search bar for filtering months and a clear button
# # #     search_bar = ft.TextField(
# # #         label="Search Month",
# # #         on_change=handle_search,
# # #         width=800
# # #     )

# # #     clear_button = ft.ElevatedButton(
# # #         text="Clear",
# # #         on_click=clear_search,
# # #         width=200,
# # #         height=50
# # #     )

# # #     # Return the PAGE1 view with the top-left button
# # #     return ft.View(
# # #         route="/PAGE1",
# # #         controls=[
# # #             ft.Row(
# # #                 controls=[
# # #                     ft.ElevatedButton(  # Add button on the top-left
# # #                         text="Go Back",
# # #                         on_click=lambda e: (page.views.pop(), page.go("/HOME")),
# # #                     )
                    
# # #                 ],
# # #                 alignment=ft.MainAxisAlignment.START,  # Align button to the left
# # #             ),
# # #             ft.Row(
# # #                 controls=[
# # #                     ft.Text(
# # #                 "Graph Search by Month and Year",
# # #                 size=30,
# # #                 weight=ft.FontWeight.BOLD,
# # #                 color=ft.Colors.BLACK,
                
# # #             ),
# # #                 ],
# # #                 alignment=ft.MainAxisAlignment.CENTER,
# # #             ),
            
# # #             ft.Row(
# # #                 controls=[
# # #                     search_bar,  # Search bar for filtering months
# # #                     clear_button,  # Clear button next to search bar
# # #                 ],
# # #                 alignment=ft.MainAxisAlignment.CENTER,
# # #                 spacing=10,
# # #             ),
# # #             ft.Container(
# # #                 ft.Row(controls=checkboxes + [year_dropdown]),  # Display checkboxes and dropdown in a row
# # #                 padding=ft.padding.only(bottom=10, top=20, left=50),  # Add padding below monthly/yearly controls
# # #             ),
# # #             ft.Container(
# # #                 ft.Row(  # Display both graphs side by side
# # #                     controls=[
# # #                         bar_graph_image,
# # #                         pie_chart_image,
# # #                     ]
# # #                 ),
# # #                 padding=ft.padding.only(left=100, top=80, right=100),  # Add padding above the graphs
# # #             ),
# # #         ],
# # #         bgcolor=ft.Colors.BLUE_100,
# # #     )



# import flet as ft
# import matplotlib.pyplot as plt
# from io import BytesIO
# import base64
# from flet import *
# # Function to create a bar graph as a base64 image
# def create_bar_graph(title, categories, data):
#     plt.figure(figsize=(6, 4))
#     plt.bar(categories, data, color='#87CEEB')
#     plt.xlabel('Defect Types')
#     plt.ylabel('Frequency')
#     plt.title(title)
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     img_base64 = base64.b64encode(buffer.read()).decode()
#     buffer.close()
#     return img_base64

# # Function to create a pie chart as a base64 image
# def create_pie_chart(title, categories, data):
#     plt.figure(figsize=(6, 6))
#     plt.pie(data, labels=categories, autopct='%1.1f%%', startangle=140,
#             colors=['#FF6666', '#3399FF', '#66FF66', '#FFCC33'], textprops={'fontsize': 10})
#     plt.title(title, fontsize=14)
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     img_base64 = base64.b64encode(buffer.read()).decode()
#     buffer.close()
#     return img_base64

# # Function to create the PAGE1 view
# def get_page1_view(page):
#     # Example data
#     monthly_data = {
#         "January": [80, 90, 85],
#         "February": [75, 85, 80],
#         "March": [85, 95, 90],
#          "April": [60, 70, 65],
#         "May": [90, 85, 80],
#         "June": [70, 75, 65],
#         "July": [95, 90, 85],
#         "August": [85, 80, 75],
#         "September": [75, 85, 80],
#         "October": [80, 90, 85],
#         "November": [60, 75, 70],
#         "December": [90, 95, 85],
#     }
#     yearly_data = {
#         "2022": [85, 88, 81],
#         "2023": [90, 87, 85],
#         "2024": [88, 85, 84],
#         "2025": [30, 85, 50],
#     }

#     # Initial graph setup
#     bar_graph_image = ft.Image(
#         src_base64=create_bar_graph("Knitting Fabric Defects for January", ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'], monthly_data["January"]),
#         expand=True,
#     )
#     pie_chart_image = ft.Image(
#         src_base64=create_pie_chart("Defect Distribution for January", ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'], monthly_data["January"]),
#         expand=True,
#     )

#     # Function to update graphs
#     def update_month_graph(selected_month):
#         for checkbox in checkboxes:
#             checkbox.value = (checkbox.label == selected_month)  # Uncheck others and keep the selected one checked
#             checkbox.update() 
            
#         bar_graph_image.src_base64 = create_bar_graph(
#             f"Knitting Fabric Defects for {selected_month}",
#             ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
#             monthly_data[selected_month]
#         )
#         pie_chart_image.src_base64 = create_pie_chart(
#             f"Defect Distribution for {selected_month}",
#             ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
#             monthly_data[selected_month]
#         )
#         bar_graph_image.update()
#         pie_chart_image.update()

#     def update_year_graph(e):
#         selected_year = e.control.value
#         bar_graph_image.src_base64 = create_bar_graph(
#             f"Yearly Defects in Knitting Fabric ({selected_year})",
#             ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
#             yearly_data[selected_year]
#         )
#         pie_chart_image.src_base64 = create_pie_chart(
#             f"Yearly Defect Distribution ({selected_year})",
#             ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
#             yearly_data[selected_year]
#         )
#         bar_graph_image.update()
#         pie_chart_image.update()

#      # Function to handle search input
#     def handle_search(e):
#         search_query = search_bar.value.lower()
#         for checkbox in checkboxes:
#             checkbox.visible = search_query in checkbox.label.lower()
#             checkbox.update()

#     # Function to clear the search bar
#     def clear_search(e):
#         search_bar.value = ""
#         handle_search(e)  # Reset visibility of all checkboxes
#         search_bar.update()    

#     # Create checkboxes
#     checkboxes = [
#         ft.Checkbox(
#             label=month,
#             value=(month == "January"),
#             on_change=lambda e, month=month: update_month_graph(month),
#             expand=True,
#             label_style=ft.TextStyle(size=12),  # Set font size to 12 (adjust as needed)
            
#         )
#         for month in monthly_data.keys()
#     ]

#     # Dropdown for yearly data
#     year_dropdown = ft.Dropdown(
#         label="Select Year",
#         options=[ft.dropdown.Option(year) for year in yearly_data.keys()],
#         value="2022",
#         on_change=update_year_graph,
#     )
#      # Add a search bar for filtering months and a clear button
#     search_bar = ft.TextField(
#         label="Search Month",
#         on_change=handle_search,
#         width=900,
#         expand=True,
#     )

#     clear_button = ft.ElevatedButton(
#         text="Clear",
#         on_click=clear_search,
#         width=200,
#         height=50,
        

#     )
#     # Return the PAGE1 view
#     return ft.View(
#         route="/PAGE1",
#         scroll=ft.ScrollMode.AUTO,
#         controls=[
#             ft.Row(
#                 controls=[
#                     ft.ElevatedButton(
#                         text="Go Back",
#                         on_click=lambda e: (page.views.pop(), page.go("/HOME"))
#                     ),
#                 ],
#                 alignment=ft.MainAxisAlignment.START,
#             ),
#             ft.Row(
#                 controls=[
#                     ft.Text(
#                 "Defects Overview by Month and Year",
#                 size=25,
#                 weight=ft.FontWeight.BOLD,
#                 color=ft.Colors.BLACK,
                
#             ),
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#             ),
            
#             ft.Row(
#                 controls=[
#                     search_bar,  # Search bar for filtering months
#                     clear_button,  # Clear button next to search bar
                    
#                 ],
            
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 spacing=10,
#             ),
#             ft.Row(controls=checkboxes, alignment=ft.CrossAxisAlignment.CENTER, spacing=5,),
#             ft.ResponsiveRow(
#                 controls=[
#                     year_dropdown,
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 spacing=20,
#             ),
#             ft.ResponsiveRow(
#                 controls=[
#                     ft.Column(controls=[bar_graph_image], expand=True),
#                     ft.Column(controls=[pie_chart_image], expand=True),
#                 ],
#                 spacing=20,
#             ),
            
#         ],
#     )
    

# # Main function to test navigation
# def main(page: ft.Page):
#     page.go("/PAGE1")
#     page.views.append(get_page1_view(page))
    

# if __name__ == "__main__":
#     ft.app(target=main,view=WEB_BROWSER)


# # import flet as ft
# # import matplotlib.pyplot as plt
# # from io import BytesIO
# # import base64
# # from flet import *

# # # Function to create a bar graph as a base64 image
# # def create_bar_graph(title, categories, data):
# #     plt.figure(figsize=(6, 4))
# #     plt.bar(categories, data, color='#87CEEB')
# #     plt.xlabel('Defect Types')
# #     plt.ylabel('Frequency')
# #     plt.title(title)
# #     buffer = BytesIO()
# #     plt.savefig(buffer, format='png')
# #     buffer.seek(0)
# #     img_base64 = base64.b64encode(buffer.read()).decode()
# #     buffer.close()
# #     return img_base64

# # # Function to create a pie chart as a base64 image
# # def create_pie_chart(title, categories, data):
# #     plt.figure(figsize=(6, 6))
# #     plt.pie(data, labels=categories, autopct='%1.1f%%', startangle=140,
# #             colors=['#FF6666', '#3399FF', '#66FF66', '#FFCC33'], textprops={'fontsize': 10})
# #     plt.title(title, fontsize=14)
# #     buffer = BytesIO()
# #     plt.savefig(buffer, format='png')
# #     buffer.seek(0)
# #     img_base64 = base64.b64encode(buffer.read()).decode()
# #     buffer.close()
# #     return img_base64

# # # Function to create the PAGE1 view
# # def get_page1_view(page):
# #     # Example data
# #     monthly_data = {
# #         "January": [80, 90, 85],
# #         "February": [75, 85, 80],
# #         "March": [85, 95, 90],
# #         "April": [60, 70, 65],
# #         "May": [90, 85, 80],
# #         "June": [70, 75, 65],
# #         "July": [95, 90, 85],
# #         "August": [85, 80, 75],
# #         "September": [75, 85, 80],
# #         "October": [80, 90, 85],
# #         "November": [60, 75, 70],
# #         "December": [90, 95, 85],
# #     }
# #     yearly_data = {
# #         "2022": [85, 88, 81],
# #         "2023": [90, 87, 85],
# #         "2024": [88, 85, 84],
# #         "2025": [30, 85, 50],
# #     }

# #     # Initial graph setup
# #     bar_graph_image = ft.Image(
# #         src_base64=create_bar_graph("Knitting Fabric Defects for January", ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'], monthly_data["January"]),
# #         expand=True,
# #     )
# #     pie_chart_image = ft.Image(
# #         src_base64=create_pie_chart("Defect Distribution for January", ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'], monthly_data["January"]),
# #         expand=True,
# #     )

# #     # Function to update graphs
# #     def update_month_graph(selected_month):
# #         bar_graph_image.src_base64 = create_bar_graph(
# #             f"Knitting Fabric Defects for {selected_month}",
# #             ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
# #             monthly_data[selected_month]
# #         )
# #         pie_chart_image.src_base64 = create_pie_chart(
# #             f"Defect Distribution for {selected_month}",
# #             ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
# #             monthly_data[selected_month]
# #         )
# #         bar_graph_image.update()
# #         pie_chart_image.update()

# #     def update_year_graph(e):
# #         selected_year = e.control.value
# #         bar_graph_image.src_base64 = create_bar_graph(
# #             f"Yearly Defects in Knitting Fabric ({selected_year})",
# #             ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
# #             yearly_data[selected_year]
# #         )
# #         pie_chart_image.src_base64 = create_pie_chart(
# #             f"Yearly Defect Distribution ({selected_year})",
# #             ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
# #             yearly_data[selected_year]
# #         )
# #         bar_graph_image.update()
# #         pie_chart_image.update()

# #     # Create checkboxes for months
# #     checkboxes = [
# #         ft.Checkbox(
# #             label=month,
# #             value=(month == "January"),
# #             on_change=lambda e, month=month: update_month_graph(month),
# #             label_style=ft.TextStyle(size=12),  # Adjust label size
# #         )
# #         for month in monthly_data.keys()
# #     ]

# #     # Dropdown for months
# #     month_dropdown = ft.Dropdown(
# #         label="Select Month",
# #         options=[ft.dropdown.Option(month) for month in monthly_data.keys()],
# #         value="January",
# #         on_change=lambda e: update_month_graph(e.control.value),
# #     )

# #     # Dropdown for years
# #     year_dropdown = ft.Dropdown(
# #         label="Select Year",
# #         options=[ft.dropdown.Option(year) for year in yearly_data.keys()],
# #         value="2022",
# #         on_change=update_year_graph,
# #     )

# #     # Detect and adapt layout based on screen size
# #     def get_month_controls():
# #         if page.width > 800:  # For larger screens, use checkboxes
# #             return ft.Row(controls=checkboxes, spacing=5)
# #         else:  # For smaller screens, use a dropdown
# #             return ft.Row(controls=[month_dropdown], alignment=ft.MainAxisAlignment.CENTER)

# #     # Adapt layout when the screen is resized
# #     def on_resize(e):
# #         page.controls[-1] = get_month_controls()  # Update the month controls dynamically
# #         page.update()

# #     page.on_resize = on_resize  # Attach resize event

# #     # Return the PAGE1 view
# #     return ft.View(
# #         route="/PAGE1",
# #         scroll=ft.ScrollMode.AUTO,
# #         controls=[
# #             ft.Row(
# #                 controls=[
# #                     ft.ElevatedButton(
# #                         text="Go Back",
# #                         on_click=lambda e: (page.views.pop(), page.go("/HOME"))
# #                     ),
# #                 ],
# #                 alignment=ft.MainAxisAlignment.START,
# #             ),
# #             ft.Row(
# #                 controls=[
# #                     ft.Text(
# #                         "Defects Overview by Month and Year",
# #                         size=25,
# #                         weight=ft.FontWeight.BOLD,
# #                         color=ft.Colors.BLACK,
# #                     ),
# #                 ],
# #                 alignment=ft.MainAxisAlignment.CENTER,
# #             ),
# #             year_dropdown,  # Year dropdown is always displayed
# #             get_month_controls(),  # Dynamically show month controls (checkboxes or dropdown)
# #             ft.ResponsiveRow(
# #                 controls=[
# #                     ft.Column(controls=[bar_graph_image], expand=True),
# #                     ft.Column(controls=[pie_chart_image], expand=True),
# #                 ],
# #                 spacing=20,
# #             ),
# #         ],
# #     )

# # # Main function to test navigation
# # def main(page: ft.Page):
# #     page.go("/PAGE1")
# #     page.views.append(get_page1_view(page))

# # if __name__ == "__main__":
# #     ft.app(target=main, view=ft.AppView.WEB_BROWSER)

import flet as ft
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Function to create a bar graph as a base64 image
def create_bar_graph(title, categories, data):
    plt.figure(figsize=(6, 4))
    plt.bar(categories, data, color='#87CEEB')
    plt.xlabel('Defect Types')
    plt.ylabel('Frequency')
    plt.title(title)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode()
    buffer.close()
    return img_base64

# Function to create a pie chart as a base64 image
def create_pie_chart(title, categories, data):
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=categories, autopct='%1.1f%%', startangle=140, colors=['#FF6666', '#3399FF', '#66FF66', '#FFCC33'], textprops={'fontsize': 10})  # Adjust font size for labels
    plt.title(title, fontsize=14)  # Adjust title font size

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode()
    buffer.close()
    return img_base64

# Function to create the PAGE1 view with a top-left button
def get_page1_view(page):
    print("PAGE1 view is being created!")

    # Example data for defects in each month
    monthly_data = {
        "January": [30, 50, 20],
        "February": [40, 45, 15],
        "March": [25, 55, 20],
        "April": [35, 40, 25],
        "May": [20, 50, 30],
        "June": [30, 45, 25],
        "July": [40, 30, 30],
        "August": [25, 35, 40],
        "September": [35, 40, 25],
        "October": [30, 45, 25],
        "November": [20, 50, 30],
        "December": [40, 35, 25],
    }

    # Example yearly data (average defects per type for all months)
    yearly_data = {
        "2022": [35, 40, 25],
        "2023": [30, 45, 25],
        "2024": [25, 50, 25],
        "2025": [40, 35, 30],
    }

    # Initial graph setup for "January" (default)
    bar_graph_image = ft.Image(
        src_base64=create_bar_graph("Knitting Fabric Defects for January", ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'], monthly_data["January"]),
        width=500,
        height=400,
    )
    pie_chart_image = ft.Image(
        src_base64=create_pie_chart("Defect Distribution for January", ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'], monthly_data["January"]),
        width=500,
        height=310,
    )

    # Function to update both graphs based on selected checkbox
    def update_month_graph(selected_month):
        for checkbox in checkboxes:
            checkbox.value = (checkbox.label == selected_month)
            checkbox.update()

        # Update the graphs for the selected month
        bar_graph_image.src_base64 = create_bar_graph(
            f"Knitting Fabric Defects for {selected_month}",
            ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
            monthly_data[selected_month]
        )
        pie_chart_image.src_base64 = create_pie_chart(
            f"Defect Distribution for {selected_month}",
            ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
            monthly_data[selected_month]
        )

        bar_graph_image.update()
        pie_chart_image.update()

    # Function to update both graphs based on the selected year from the dropdown
    def update_year_graph(e):
        selected_year = e.control.value
        bar_graph_image.src_base64 = create_bar_graph(
            f"Yearly Defects in Knitting Fabric ({selected_year})",
            ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
            yearly_data[selected_year],
        )
        pie_chart_image.src_base64 = create_pie_chart(
            f"Yearly Defect Distribution ({selected_year})",
            ['Missed Stitches', 'Yarn Breaks', 'Fabric Tears'],
            yearly_data[selected_year],
        )
        bar_graph_image.update()
        pie_chart_image.update()

    # Function to handle search input
    def handle_search(e):
        search_query = search_bar.value.lower()
        for checkbox in checkboxes:
            checkbox.visible = search_query in checkbox.label.lower()
            checkbox.update()

    # Function to clear the search bar
    def clear_search(e):
        search_bar.value = ""
        handle_search(e)
        search_bar.update()

    # Create checkboxes for each month
    checkboxes = [
        ft.Checkbox(
            label=month,
            value=(month == "January"),
            on_change=lambda e, month=month: update_month_graph(month),
        )
        for month in monthly_data.keys()
    ]

    # Create dropdown for yearly data selection
    year_dropdown = ft.Dropdown(
        label="Select Year",
        options=[ft.dropdown.Option(year) for year in yearly_data.keys()],
        value="2022",
        on_change=update_year_graph,
    )

    # Add a search bar for filtering months and a clear button
    search_bar = ft.TextField(
        label="Search Month",
        on_change=handle_search,
        width=800
    )

    clear_button = ft.ElevatedButton(
        text="Clear",
        on_click=clear_search,
        width=200,
        height=50
    )

    # Return the PAGE1 view
    return ft.View(
        route="/PAGE1",
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text="Go Back",
                        on_click=lambda e: (page.views.pop(), page.go("/HOME")),
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Row(
                controls=[
                    ft.Text(
                        "Defects Overview by Month and Year",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    search_bar,
                    clear_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            ft.Container(
                ft.Row(controls=checkboxes + [year_dropdown]),
                padding=ft.padding.only(bottom=10, top=20, left=90),
            ),
            ft.Container(
                ft.Row(
                    controls=[
                        bar_graph_image,
                        pie_chart_image,
                    ]
                ),
                padding=ft.padding.only(left=200, top=50, right=100),
            ),
        ],
        bgcolor=ft.Colors.BLUE_100,
    )
