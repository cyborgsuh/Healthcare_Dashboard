
from streamlit_extras.echo_expander import echo_expander

def example1():
    with echo_expander():
        import streamlit as st

        st.markdown(
            """
            This component is a combination of `st.echo` and `st.expander`.
            The code inside the `with echo_expander()` block will be executed,
            and the code can be shown/hidden behind an expander
            """
        )
        
        
example1