from dash import Dash, html, dcc, Input, Output, callback
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


app = Dash()

app.layout = html.Div(
    [
        html.Div(
            children=[
                html.Label("Date Picker Single"),
                dcc.DatePickerSingle(
                    id="first-date-picker-single",
                    min_date_allowed=datetime.now() - relativedelta(years=100),
                    max_date_allowed=datetime.now() + relativedelta(years=100),
                    initial_visible_month=datetime.now(),
                    date=datetime.now(),
                ),
                html.Br(),
                html.Label("Slider"),
                html.Div(
                    dcc.Slider(
                        id="my-slider",
                        min=-0.1,
                        max=30.5,
                        step=None,
                        marks={
                            0: {
                                "label": "Sun",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                            0.39: {
                                "label": "Mercury",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                            0.72: {
                                "label": "Venus",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                            1: {
                                "label": "Earth",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                            1.52: {
                                "label": "Mars",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                            5.2: {
                                "label": "Jupiter",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                            9.54: {
                                "label": "Saturn",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                            19.2: {
                                "label": "Uranus",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                            30.06: {
                                "label": "Neptune",
                                "style": {
                                    "transform": "rotate(-90deg)",
                                    "white-space": "nowrap",
                                    "margin-top": "10px",
                                },
                            },
                        },
                        value=1,
                    ),
                    style={
                        "white-space": "nowrap",
                        "margin-top": "10px",
                    },
                ),
                html.Div(id="output", style={"marginTop": "50px"}),
            ]
        ),
    ]
)

html.Div(id="output-container-date-picker-single")


@callback(
    Output("output", "children"),
    Input("first-date-picker-single", "date"),
    Input("my-slider", "value"),
)
def update_output(date_value, slider_value):
    if date_value is None:
        return "No date selected"

    date_object = datetime.fromisoformat(date_value)
    date_string = date_object.strftime("%B %d, %Y")

    return f"You selected {date_string} and slider = {slider_value}"


if __name__ == "__main__":
    app.run(debug=True)
