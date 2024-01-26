import streamlit as st

from app_pages.multi_page import MultiPage

from app_pages.page1 import page1_body
from app_pages.page2 import page2_body


app = MultiPage(app_name="Multi-page Streamlit App")

app.app_page("Page 1", page1_body)
app.app_page("Page 2", page2_body)

app.run()
