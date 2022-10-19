import streamlit as st
import streamlit.components.v1 as components

@st.cache(suppress_st_warning=True)
def footer():
    components.html(
    """<iframe src="https://www.amazon.in/review/create-review/?ie=UTF8&channel=glance-detail&asin=B09SPH652Z" title="Amazon Review"></iframe>
    """)

def main():
    st.markdown("# RawRX - 100% Food Based Supplement")
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email address:")
    phone = st.text_input("Enter your phone number:")
    address = st.text_input("Enter your address:")
    footer()
    st.markdown("## Promise no SPAM!")


if __name__ == "__main__":
    st.set_page_config(
        "Feedback Tool",
        "💰",
        initial_sidebar_state="auto",
        layout="centered",
    )
    main()