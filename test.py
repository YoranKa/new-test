import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample Data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [10, 20, 30, 40]
})

# Create a sample figure
fig = px.bar(df, x="Category", y="Value", title="Sample Bar Chart")

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sample Dashboard"),
    dcc.Graph(
        id='sample-bar-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)