from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

# Read the file
df = pd.read_csv("shades.csv")

app = Dash()

# Create column definitions from DataFrame columns
columnDefs = [{"field": x} for x in df.columns]

# Build AG Grid component
grid = dag.AgGrid(
    id="get-started-grid",
    rowData=df.to_dict("records"),  # Convert DataFrame to list of dicts
    columnDefs=columnDefs,
    dashGridOptions={"pagination": True},
    columnSize="sizeToFit",
)

app.layout = html.Div([grid])

if __name__ == "__main__":
    app.run(debug=True)
