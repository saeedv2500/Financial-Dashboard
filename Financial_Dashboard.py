from dash import Dash, dcc, html  # Dash components for building the app
import pandas as pd  # For handling data manipulation
import plotly.express as px  # For creating visualizations
import dash_bootstrap_components as dbc  # For using Bootstrap themes

# Reading data from an Excel file
df = pd.read_excel('Financial Sample.xlsx')

# Replacing missing values in the "Discount Band" column with "No Discount"
df['Discount Band'] = df['Discount Band'].fillna('No Discount')

# Adding a new column to calculate Discount Percentage
df['Discount Percentage'] = (df['Discounts'] / df['Gross Sales']) * 100

# Removing extra spaces from column names
df.columns = df.columns.str.strip()

# Initialize the Dash app and apply the Bootstrap "Cyborg" theme
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Custom colors for the visualizations
custom_colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845']  # Gold, orange, and red shades

# Define the layout of the Dash app
app.layout = html.Div(
    style={'backgroundColor': 'black', 'color': 'gold', 'padding': '20px'},  # Black background and gold text
    children=[
        # Main title of the dashboard
        html.H1("Financial Data Analysis Dashboard", style={'textAlign': 'center', 'color': 'gold'}),

        # Subtitle or description
        html.Div("Interactive Dashboard for Sales and Profit Analysis",
                 style={'textAlign': 'center', 'color': 'gold', 'font-size': '18px'}),

        # Bar chart: Trend of Sales Over Time
        html.Div(
            style={'background-color': '#333', 'padding': '20px', 'border-radius': '10px', 'margin-bottom': '20px'},
            children=[
                html.H2("Trend of Sales Over Time", style={'color': 'gold'}),
                dcc.Graph(
                    figure=px.bar(
                        df, x='Date', y='Sales', title='Trend of Sales Over Time',
                        color_discrete_sequence=custom_colors
                    )
                )
            ]
        ),

        # Bar chart: Comparison of Sales and Profit
        html.Div(
            style={'background-color': '#333', 'padding': '20px', 'border-radius': '10px', 'margin-bottom': '20px'},
            children=[
                html.H2("Comparison of Sales and Profit Over Time", style={'color': 'gold'}),
                dcc.Graph(
                    figure=px.bar(
                        df, x='Date', y=['Sales', 'Profit'],
                        title='Comparison of Sales and Profit Over Time',
                        barmode='group', color_discrete_sequence=custom_colors
                    )
                )
            ]
        ),

        # Scatter plot: Relationship between Units Sold and Profit
        html.Div(
            style={'background-color': '#333', 'padding': '20px', 'border-radius': '10px', 'margin-bottom': '20px'},
            children=[
                html.H2("Relationship between Units Sold and Profit", style={'color': 'gold'}),
                dcc.Graph(
                    figure=px.scatter(
                        df, x='Units Sold', y='Profit', color='Segment', size='Gross Sales',
                        title='Relationship between Units Sold and Profit',
                        color_discrete_sequence=custom_colors
                    )
                )
            ]
        ),

        # Pie chart: Percentage Share of Sales by Country
        html.Div(
            style={'background-color': '#333', 'padding': '20px', 'border-radius': '10px', 'margin-bottom': '20px'},
            children=[
                html.H2("Percentage Share of Sales by Country", style={'color': 'gold'}),
                dcc.Graph(
                    figure=px.pie(
                        df, values='Sales', names='Country',
                        title='Percentage Share of Sales by Country',
                        hole=0.4, color_discrete_sequence=custom_colors
                    )
                )
            ]
        ),

        # Treemap: Visualization of Gross Sales by Country and Product
        html.Div(
            style={'background-color': '#333', 'padding': '20px', 'border-radius': '10px', 'margin-bottom': '20px'},
            children=[
                html.H2("Treemap of Gross Sales by Country and Product", style={'color': 'gold'}),
                dcc.Graph(
                    figure=px.treemap(
                        df, path=['Country', 'Product'], values='Gross Sales',
                        title='Treemap of Gross Sales by Country and Product',
                        color='Gross Sales', color_continuous_scale='Reds'
                    )
                )
            ]
        ),

        # Box plot: Profit Distribution by Discount Band
        html.Div(
            style={'background-color': '#333', 'padding': '20px', 'border-radius': '10px'},
            children=[
                html.H2("Profit Distribution by Discount Band", style={'color': 'gold'}),
                dcc.Graph(
                    figure=px.box(
                        df, x='Discount Band', y='Profit',
                        title='Profit Distribution by Discount Band',
                        color='Discount Band', color_discrete_sequence=custom_colors
                    )
                )
            ]
        )
    ]
)

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)

