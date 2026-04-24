import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

df = pd.read_csv(
    "https://github.com/plotly/datasets/raw/refs/heads/master/Dash-Course/US-Exports/2011_us_ag_exports.csv"
)

app = Dash()

app.layout = html.Div(
    [
        html.Div(id="my-title", children="Sweet home"),
        dcc.Dropdown(df["state"].to_list(), value="Alabama", id="state-dropdown"),
        dcc.Graph(id="graph1"),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
