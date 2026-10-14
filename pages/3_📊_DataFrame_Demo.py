from urllib.error import URLError

import altair as alt
import pandas as pd
import streamlit as st
import style

style.apply("DataFrame Demo", "📊")
style.header(
    "Demo 03",
    "DataFrame",
    "Visualise pandas DataFrames with <code>st.write</code> and Altair. "
    "Data courtesy of the UN Data Explorer.",
)
st.write("")


@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    df = get_UN_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries] / 1_000_000.0

        latest = data.columns[-1]
        stat_cols = st.columns(min(len(countries), 4), gap="large")
        for col, country in zip(stat_cols, countries[:4]):
            with col:
                st.markdown(
                    f'<div class="card"><div class="stat">${data.loc[country, latest]:,.0f}B</div>'
                    f'<div class="stat-label">{country} · {latest}</div></div>',
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="section-label">Gross agricultural production ($B)</div>', unsafe_allow_html=True)
        st.dataframe(data.sort_index().round(1), width="stretch")

        long = data.T.reset_index()
        long = pd.melt(long, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(long)
            .mark_area(opacity=0.28, line={"strokeWidth": 2.5}, interpolate="monotone")
            .encode(
                x=alt.X("year:T", title=None, axis=alt.Axis(grid=False, domain=False, labelColor="#6E6E73")),
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None, title=None,
                        axis=alt.Axis(gridColor="#ececf0", domain=False, ticks=False, labelColor="#6E6E73")),
                color=alt.Color("Region:N", scale=alt.Scale(range=style.PALETTE),
                                legend=alt.Legend(orient="top", title=None, labelColor="#1D1D1F")),
            )
            .properties(height=400)
            .configure(background="#FFFFFF")
        .configure_view(strokeWidth=0)
        )
        st.markdown('<div class="section-label">Trend</div>', unsafe_allow_html=True)
        st.altair_chart(chart, width="stretch")
except URLError as e:
    st.error("**This demo requires internet access.**\n\nConnection error: %s" % e.reason)

style.footer()
