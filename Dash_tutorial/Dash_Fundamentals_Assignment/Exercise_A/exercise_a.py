from dash import Dash, dcc, html
import pandas as pd
import numpy as np

# Read the file into a df
df = pd.read_csv("shades.csv")

# Get unique brand names and groups
brand_ndarray = pd.unique(pd.Series(df["brand"]))
group_ndarray = pd.unique(pd.Series(df["group"]))

# Sort group values
group_ndarray.sort()

# Create labels array
group_labels = np.array(
    [
        "Fenty Beauty's PRO FILT'R Foundation Only",
        "Make Up For Ever's Ultra HD Foundation Only",
        "US Best Sellers",
        "BIPOC-recommended Brands with BIPOC Founders",
        "BIPOC-recommended Brands with White Founders",
        "Nigerian Best Sellers",
        "Japanese Best Sellers",
        "Indian Best Sellers",
    ]
)

# Organize in a dict
group_dictionary = dict(zip(group_labels, group_ndarray))

app = Dash()
app.layout = html.Div(
    [
        # Create dropdown that uses brands as options
        dcc.Dropdown([i for i in brand_ndarray], "Revlon", id="brand-dropdown"),
        # Create radioitem that uses sorted group values (0-7)
        # dcc.RadioItems([i for i in group_ndarray], group_ndarray[0]),
        # Create radioitem with values from group assigned to given labels
        dcc.RadioItems(
            options=[{"label": i, "value": j} for i, j in group_dictionary.items()],
            value=0,
        ),
        html.Div(id="dd-output-container"),
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
