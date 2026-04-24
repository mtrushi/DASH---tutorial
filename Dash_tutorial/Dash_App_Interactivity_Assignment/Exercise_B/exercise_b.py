import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
from dash.exceptions import PreventUpdate

df = pd.read_csv(
    "https://github.com/plotly/datasets/raw/refs/heads/master/Dash-Course/US-Exports/2011_us_ag_exports.csv"
)


app = Dash()

app.layout = html.Div(
    [
        html.Div(id="my-title", children="Sweet home"),
        dcc.Dropdown(
            df["state"].to_list(),
            value=["Alabama"],
            id="state-dropdown",
            debounce=True,
            multi=True,
        ),
        dcc.Graph(id="graph1"),
    ]
)


@callback(
    Output(component_id="graph1", component_property="figure"),
    Input(component_id="state-dropdown", component_property="value"),
)
def update_graph(state_selected):
    if state_selected is None:
        raise PreventUpdate

    df_country = df[df["state"].isin(state_selected)]
    fig = px.bar(df_country, x="state", y=["beef", "pork", "fruits fresh"])
    return fig


if __name__ == "__main__":
    app.run(debug=True)
