import streamlit as st
from integration_utils import *
from dotenv import load_dotenv

st.write("# Dashboard")

SECRET_KEY = os.getenv("SECRET_KEY")

if SECRET_KEY is None:
    st.error("SECRET_KEY environment variable is not set.  Check Streamlit Secrets.")
    st.stop()

def main():
    st.write("### Super execlusive content that will be displayed for only authorized users...")

st.link_button("Back to smilai", "#")

load_dotenv()

received_data = extract_query(SECRET_KEY)
st.write(received_data)
validation = validate_extracted_data(received_data)
st.write(validation)


if validation['status']:
    st.success("Yout session is active.")
    main()
else:
    if validation['error_type'] == 'INVALID_TOKEN':
        st.error(validation['message'])
    elif validation['error_type'] == 'EXPIRED_TOKEN':
        st.markdown(validation['markdown'], unsafe_allow_html=True)
    else:
        st.error("Unexpected error.")