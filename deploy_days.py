from pathlib import Path

import streamlit as st

from deploy_calender.choose_random_days import get_deploy_and_avoid_dates
from deploy_calender.css_injection import add_local_css
from deploy_calender.deploy_calendar import DeployCalendar
from deploy_calender.settings import Settings, Zodiac, get_settings


def get_params() -> Settings:
    return get_settings(st.experimental_get_query_params())


st.set_page_config(
    page_title="Deploy astrological calender",
    initial_sidebar_state="expanded",
    layout="wide",
)

add_local_css(Path("css/deploy.css"))

params = get_params()

st.experimental_set_query_params(
    year=params.month.year, month=params.month.month, sign=params.sign.name
)

deploy, avoid = get_deploy_and_avoid_dates(params.month, params.sign)
month_printer = DeployCalendar(deploy, avoid)


with st.sidebar:

    def set_get_params(sign_: Zodiac) -> None:
        st.experimental_set_query_params(sign=sign_)

    st.write("Choose your zodiac sign")
    for sign in Zodiac:
        name = sign.name.capitalize()
        st.button(
            f"{sign.value} {name}",
            on_click=set_get_params,
            args=(name,),
        )

st.markdown(
    month_printer.formatmonth(params.month.year, params.month.month),
    unsafe_allow_html=True,
)
