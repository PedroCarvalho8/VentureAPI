import time

import streamlit as st
from streamlit_javascript import st_javascript


def theme():
    dark = {"primaryColor": "#ff4b4b", "backgroundColor": "#0e1117", "secondaryBackgroundColor": "#262730",
            "textColor": "#fafafa", "base": "dark", "font": "\"Source Sans Pro\", sans-serif",
            "linkText": "hsla(209, 100%, 59%, 1)", "fadedText05": "rgba(250, 250, 250, 0.1)",
            "fadedText10": "rgba(250, 250, 250, 0.2)", "fadedText20": "rgba(250, 250, 250, 0.3)",
            "fadedText40": "rgba(250, 250, 250, 0.4)", "fadedText60": "rgba(250, 250, 250, 0.6)",
            "bgMix": "rgba(26, 28, 36, 1)", "darkenedBgMix100": "hsla(228, 16%, 72%, 1)",
            "darkenedBgMix25": "rgba(172, 177, 195, 0.25)", "darkenedBgMix15": "rgba(172, 177, 195, 0.15)",
            "lightenedBg05": "hsla(220, 24%, 10%, 1)", "borderColor": "rgba(250, 250, 250, 0.2)",
            "borderColorLight": "rgba(250, 250, 250, 0.1)"}

    light = {"primaryColor": "#ff4b4b", "backgroundColor": "#ffffff", "secondaryBackgroundColor": "#f0f2f6",
             "textColor": "#31333F", "base": "light", "font": "\"Source Sans Pro\", sans-serif", "linkText": "#0068c9",
             "fadedText05": "rgba(49, 51, 63, 0.1)", "fadedText10": "rgba(49, 51, 63, 0.2)",
             "fadedText20": "rgba(49, 51, 63, 0.3)", "fadedText40": "rgba(49, 51, 63, 0.4)",
             "fadedText60": "rgba(49, 51, 63, 0.6)", "bgMix": "rgba(248, 249, 251, 1)",
             "darkenedBgMix100": "hsla(220, 27%, 68%, 1)", "darkenedBgMix25": "rgba(151, 166, 195, 0.25)",
             "darkenedBgMix15": "rgba(151, 166, 195, 0.15)", "lightenedBg05": "hsla(0, 0%, 100%, 1)",
             "borderColor": "rgba(49, 51, 63, 0.2)", "borderColorLight": "rgba(49, 51, 63, 0.1)"}

    st_theme = st_javascript(
        """window.getComputedStyle(window.parent.document.getElementsByClassName("stApp")[0]).getPropertyValue("color-scheme")""")

    time.sleep(0.3)

    return dark if st_theme == "dark" else light
