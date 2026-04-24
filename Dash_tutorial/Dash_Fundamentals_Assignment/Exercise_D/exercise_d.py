import plotly.express as px
import pandas as pd
from dash import dcc, Dash

df = pd.read_csv("shades.csv")
fig = px.scatter(df, x="V", y="S")

app = Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])


if __name__ == "__main__":
    app.run(debug=True)
