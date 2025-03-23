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

# Function to create the PAGE3 view with a top-left button
def get_page3_view(page):
    print("PAGE3 view is being created!")

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

    # Return the PAGE3 view
    return ft.View(
        route="/PAGE3",
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
