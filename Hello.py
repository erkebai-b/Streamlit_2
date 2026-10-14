import streamlit as st
import style

style.apply("Hello", "👋")

st.markdown(
    """
    <div class="eyebrow">Streamlit Multipage</div>
    <div class="hero-title">Data apps.<br><span class="grad">Beautifully simple.</span></div>
    <p class="lede">An entrypoint file plus a <code>pages/</code> folder. Streamlit builds the
    navigation for you. Each page has its own URL, title and icon.</p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">Explore the demos</div>', unsafe_allow_html=True)

demos = [
    ("pages/1_📈_Plotting_Demo.py", "📈", "Plotting", "Live, animated line charts that stream new data in real time."),
    ("pages/2_🌍_Mapping_Demo.py", "🌍", "Mapping", "3D geospatial layers over San Francisco, powered by pydeck."),
    ("pages/3_📊_DataFrame_Demo.py", "📊", "DataFrame", "Explore UN agricultural output by country with Altair."),
]
cols = st.columns(3, gap="large")
for col, (path, icon, name, blurb) in zip(cols, demos):
    with col:
        st.markdown(
            f'<div class="card"><div class="icon">{icon}</div><h4>{name}</h4><p>{blurb}</p></div>',
            unsafe_allow_html=True,
        )
        st.write("")
        st.page_link(path, label=f"Open {name}")

st.markdown('<div class="section-label">How it works</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3, gap="large")
steps = [
    ("1", "Entrypoint", "<code>Hello.py</code> is the home page you run with <code>streamlit run</code>."),
    ("2", "Pages folder", "Every script in <code>pages/</code> becomes a page in the sidebar."),
    ("3", "Ordering", "Number prefixes set the order; emoji in file names become icons."),
]
for col, (n, t, d) in zip((c1, c2, c3), steps):
    with col:
        st.markdown(
            f'<div class="card"><div class="stat">{n}</div><h4 style="margin-top:14px">{t}</h4><p>{d}</p></div>',
            unsafe_allow_html=True,
        )

style.footer()
