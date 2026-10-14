from urllib.error import URLError

import pandas as pd
import pydeck as pdk
import streamlit as st
import style

style.apply("Mapping Demo", "🌍")
style.header(
    "Demo 02",
    "Mapping",
    "Geospatial data with <code>st.pydeck_chart</code>. Toggle layers in the sidebar "
    "to explore bike rentals and BART traffic across San Francisco.",
)
st.write("")


@st.cache_data
def from_data_file(filename):
    url = "https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/%s" % filename
    return pd.read_json(url)


try:
    ALL_LAYERS = {
        "Bike Rentals": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
            color_range=[[219, 234, 254], [147, 197, 253], [96, 165, 250], [59, 130, 246], [0, 113, 227], [30, 64, 175]],
        ),
        "Bart Stop Exits": pdk.Layer(
            "ScatterplotLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_color=[255, 55, 95, 170],
            get_radius="[exits]",
            radius_scale=0.05,
        ),
        "Bart Stop Names": pdk.Layer(
            "TextLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_text="name",
            get_color=[29, 29, 31, 220],
            get_size=14,
            get_alignment_baseline="'bottom'",
        ),
        "Outbound Flow": pdk.Layer(
            "ArcLayer",
            data=from_data_file("bart_path_stats.json"),
            get_source_position=["lon", "lat"],
            get_target_position=["lon2", "lat2"],
            get_source_color=[191, 90, 242, 170],
            get_target_color=[0, 113, 227, 170],
            auto_highlight=True,
            width_scale=0.0001,
            get_width="outbound",
            width_min_pixels=3,
            width_max_pixels=30,
        ),
    }
    st.sidebar.markdown("### Map Layers")
    selected_layers = [
        layer for layer_name, layer in ALL_LAYERS.items() if st.sidebar.checkbox(layer_name, True)
    ]
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_provider="carto",
                map_style="light",
                initial_view_state={"latitude": 37.76, "longitude": -122.4, "zoom": 11, "pitch": 50},
                layers=selected_layers,
            ),
            height=560,
        )
    else:
        st.error("Please choose at least one layer in the sidebar.")
except URLError as e:
    st.error("**This demo requires internet access.**\n\nConnection error: %s" % e.reason)

style.footer()
