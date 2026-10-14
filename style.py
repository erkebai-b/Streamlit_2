"""Shared Apple-inspired styling for every page of the app."""
import streamlit as st

BLUE = "#0071E3"
INK = "#1D1D1F"
MUTED = "#6E6E73"
PALETTE = ["#0071E3", "#FF9F0A", "#30D158", "#BF5AF2", "#FF375F"]

_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --ink: #1D1D1F; --muted: #6E6E73; --blue: #0071E3;
  --card: #FFFFFF; --bg: #F5F5F7; --hair: rgba(0,0,0,0.08);
}
html, body, [class*="css"], .stApp, .stMarkdown, button, input, textarea, select {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text",
               "Inter", "Helvetica Neue", Arial, sans-serif !important;
  -webkit-font-smoothing: antialiased;
  letter-spacing: -0.011em;
}
.stApp { background: var(--bg); }
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] {
  background: rgba(245,245,247,0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid var(--hair);
}
.block-container { max-width: 1080px; padding-top: 4rem; padding-bottom: 5rem; }

/* Frosted sidebar */
section[data-testid="stSidebar"] {
  background: rgba(255,255,255,0.72) !important;
  backdrop-filter: saturate(180%) blur(24px);
  -webkit-backdrop-filter: saturate(180%) blur(24px);
  border-right: 1px solid var(--hair);
}
section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] {
  border-radius: 10px; padding: 0.45rem 0.75rem; margin: 2px 0;
  font-weight: 500; transition: background .2s ease;
}
section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"]:hover { background: rgba(0,0,0,0.05); }
section[data-testid="stSidebar"] a[aria-current="page"] { background: rgba(0,113,227,0.10) !important; }
section[data-testid="stSidebar"] a[aria-current="page"] span { color: var(--blue) !important; font-weight: 600; }

/* Typography */
h1, h2, h3 { color: var(--ink); letter-spacing: -0.025em; }
.eyebrow { color: var(--blue); font-weight: 600; font-size: 0.95rem; margin-bottom: 0.4rem; }
.hero-title {
  font-size: clamp(2.6rem, 6vw, 4.6rem); line-height: 1.04; font-weight: 700;
  letter-spacing: -0.035em; color: var(--ink); margin: 0 0 1rem;
}
.hero-title .grad {
  background: linear-gradient(90deg, #0071E3 0%, #BF5AF2 55%, #FF375F 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.lede { font-size: clamp(1.1rem, 2vw, 1.4rem); line-height: 1.45; color: var(--muted); max-width: 680px; }
.page-title { font-size: clamp(2.2rem, 4.5vw, 3.2rem); font-weight: 700; letter-spacing: -0.03em; color: var(--ink); line-height: 1.08; margin: 0 0 .6rem; }
.section-label { font-size: 1.5rem; font-weight: 600; letter-spacing: -0.02em; margin: 3rem 0 1rem; color: var(--ink); }

/* Cards */
.card {
  background: var(--card); border-radius: 22px; padding: 28px 26px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04), 0 8px 28px rgba(0,0,0,0.06);
  height: 100%; transition: transform .35s cubic-bezier(.2,.8,.2,1), box-shadow .35s ease;
}
.card:hover { transform: translateY(-4px); box-shadow: 0 2px 4px rgba(0,0,0,0.05), 0 18px 40px rgba(0,0,0,0.10); }
.card .icon { font-size: 2.2rem; margin-bottom: 14px; }
.card h4 { margin: 0 0 6px; font-size: 1.25rem; font-weight: 600; color: var(--ink); letter-spacing: -0.02em; }
.card p { margin: 0; color: var(--muted); font-size: 0.98rem; line-height: 1.45; }
.stat { font-size: 2.4rem; font-weight: 700; letter-spacing: -0.03em; color: var(--ink); line-height: 1; }
.stat-label { color: var(--muted); font-size: 0.9rem; margin-top: 6px; }

/* Wrap native blocks (charts, tables, maps) in card styling */
div[data-testid="stVegaLiteChart"], div[data-testid="stArrowVegaLiteChart"],
div[data-testid="stDeckGlJsonChart"], div[data-testid="stDataFrame"] {
  background: var(--card); border-radius: 22px; padding: 16px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04), 0 8px 28px rgba(0,0,0,0.06);
  overflow: hidden; box-sizing: border-box;
}

/* Page links as pill buttons */
a[data-testid="stPageLink-NavLink"] {
  background: var(--blue); border-radius: 980px; padding: 0.55rem 1.2rem;
  justify-content: center; transition: background .2s ease;
}
a[data-testid="stPageLink-NavLink"]:hover { background: #0077ED; }
a[data-testid="stPageLink-NavLink"] p, a[data-testid="stPageLink-NavLink"] span { color: #fff !important; font-weight: 500; }

/* Buttons */
.stButton > button {
  border-radius: 980px; border: none; background: var(--blue); color: #fff;
  padding: 0.55rem 1.4rem; font-weight: 500; transition: background .2s ease, transform .1s ease;
}
.stButton > button:hover { background: #0077ED; color: #fff; }
.stButton > button:active { transform: scale(0.98); }

/* Inputs */
div[data-baseweb="select"] > div { border-radius: 12px; border-color: var(--hair); background: #fff; }
span[data-baseweb="tag"] { background: rgba(0,113,227,0.10) !important; border-radius: 8px; }
span[data-baseweb="tag"] span { color: var(--blue) !important; }
.stProgress > div > div > div > div { background: var(--blue); }

.foot { color: var(--muted); font-size: 0.82rem; text-align: center; margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--hair); }
</style>
"""


def apply(page_title: str, page_icon: str) -> None:
    """Configure the page and inject the shared stylesheet. Call first on every page."""
    st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")
    st.markdown(_CSS, unsafe_allow_html=True)


def header(eyebrow: str, title: str, lede: str) -> None:
    st.markdown(
        f'<div class="eyebrow">{eyebrow}</div>'
        f'<div class="page-title">{title}</div>'
        f'<p class="lede">{lede}</p>',
        unsafe_allow_html=True,
    )


def footer() -> None:
    st.markdown(
        '<div class="foot">Built with Streamlit · Multipage app tutorial</div>',
        unsafe_allow_html=True,
    )
