app.layout = html.Div(
    [
        # Dropdown to filter developing/developed country.
        html.Div(
            [
                dcc.Dropdown(
                    id="status-dropdown",
                    # Create available options from the dataset
                    options=[{"label": s, "value": s}
                             for s in df.Status.unique()],
                ),
            ]
        ),
        # Dropdown to filter countries with average schooling years.
        html.Div(
            [
                dcc.Dropdown(
                    id="schooling-dropdown",
                    options=[
                        {"label": y, "value": y}
                        for y in range(
                            int(df.Schooling.min()), int(
                                df.Schooling.max()) + 1
                        )
                    ],  # add options from the dataset.
                ),
            ]
        ),
        # Placeholder to render teh chart.
        html.Div(dcc.Graph(id="life-exp-vs-gdp"), className="chart"),

        # Slider to select year.
        dcc.Slider(
            "year-slider",
            # dynamically select minimum and maximum years from the dataset.
            min=df.Year.min(),
            max=df.Year.max(),
            step=None,
            # set markers at one year interval.
            marks={year: str(year) for year in range(
                df.Year.min(), df.Year.max() + 1)},
            value=df.Year.min(),
        ),
    ],
)
