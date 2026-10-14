import time

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import style

style.apply("Plotting Demo", "📈")
style.header(
    "Demo 01",
    "Plotting",
    "A combination of plotting and animation. We generate random numbers in a loop "
    "for about five seconds and stream them into the chart.",
)
st.write("")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()


def render(values: np.ndarray):
    df = pd.DataFrame({"step": np.arange(len(values)), "value": values[:, 0]})
    return (
        alt.Chart(df)
        .mark_area(
            line={"color": style.BLUE, "strokeWidth": 2.5},
            color=alt.Gradient(
                gradient="linear",
                stops=[
                    alt.GradientStop(color="rgba(0,113,227,0.28)", offset=0),
                    alt.GradientStop(color="rgba(0,113,227,0.0)", offset=1),
                ],
                x1=1, x2=1, y1=0, y2=1,
            ),
            interpolate="monotone",
        )
        .encode(
            x=alt.X("step:Q", title=None, axis=alt.Axis(grid=False, domain=False, tickColor="#d2d2d7", labelColor="#6E6E73")),
            y=alt.Y("value:Q", title=None, axis=alt.Axis(gridColor="#ececf0", domain=False, ticks=False, labelColor="#6E6E73")),
        )
        .properties(height=380)
        .configure(background="#FFFFFF")
        .configure_view(strokeWidth=0)
    )


data = np.random.randn(1, 1)
chart = st.empty()
chart.altair_chart(render(data), width="stretch")

for i in range(1, 101):
    new_rows = data[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    data = np.concatenate([data, new_rows])
    status_text.text("%i%% Complete" % i)
    chart.altair_chart(render(data), width="stretch")
    progress_bar.progress(i)
    time.sleep(0.05)

progress_bar.empty()
status_text.empty()

st.write("")
# Plain rerun: the button has no other logic attached.
st.button("Re-run")
style.footer()
