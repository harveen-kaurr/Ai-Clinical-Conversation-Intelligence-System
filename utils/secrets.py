import os

import streamlit as st


def get_secret(key: str) -> str | None:
    """Read a config value from Streamlit secrets, falling back to the environment.

    Streamlit Cloud provides secrets via st.secrets; local development uses a
    .env file loaded into the environment. st.secrets raises instead of
    returning a default when no secrets.toml exists at all (e.g. local dev),
    so that case has to be caught explicitly.
    """

    try:
        value = st.secrets.get(key)
    except Exception:
        value = None

    return value or os.getenv(key)
