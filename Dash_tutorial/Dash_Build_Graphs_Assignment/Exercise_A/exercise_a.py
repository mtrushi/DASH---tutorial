from dash import Dash, dcc, html, Input, Output, no_update
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv"
)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
        dcc.Dropdown(
            id="state-dropdown",
            options=df.state.unique(),
            value=["Alabama", "Arkansas"],
            multi=True,
        ),
        dcc.Graph(id="graph1"),
        html.Div(id="table-here"),
    ]
)


@app.callback(
    Output(component_id="graph1", component_property="figure"),
    Input(component_id="state-dropdown", component_property="value"),
)
def update_graph(states_selected):
    df_country = df[df.state.isin(states_selected)]
    fig1 = px.bar(data_frame=df_country, x="state", y=["beef", "pork", "fruits fresh"])
    return fig1


@app.callback(
    Output(component_id="table-here", component_property="children"),
    Input(component_id="graph1", component_property="hoverData"),
    prevent_initial_call=True,
)
def update(data_hovered):
    # print(data_hovered)
    x_axis_data = data_hovered["points"][0]["x"]
    dff = df[df.state == x_axis_data]
    grid = dag.AgGrid(
        id="tabular-data",
        rowData=dff.to_dict("records"),
        columnDefs=[{"field": x} for x in dff.columns],
    )
    # print(dff)
    return grid


if __name__ == "__main__":
    app.run(debug=True)
