from dash import Dash, dcc, html, Input, Output, no_update
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv"
)

# Continue building your figure below
fig = px.bar(df, x="state", y="pork", range_y=[0, 200], text_auto=True)
fig.update_xaxes(title=None)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
        dcc.Graph(id="graph1", figure=fig),
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
