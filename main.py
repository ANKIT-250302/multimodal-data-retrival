import streamlit as st

# Title of the app
# st.title('Simple Streamlit Application')

# # About section
# st.header('About')
# st.write('''
# This is a simple Streamlit application.
# Streamlit is an open-source app framework for Machine Learning and Data Science projects.
# It allows you to build and deploy powerful data apps in just a few lines of code.
# ''')

# # Main content
# st.header('Main Content')
# st.write('Welcome to the main content of the app!')


def about_me():

    st.title('Simple Streamlit Application')

    # About section
    st.header('About')
    st.write('''
    This is a simple Streamlit application.
    Streamlit is an open-source app framework for Machine Learning and Data Science projects.
    It allows you to build and deploy powerful data apps in just a few lines of code.
    ''')

    # Main content
    st.header('Main Content')
    st.write('Welcome to the main content of the app!')


def demo():
    st.header('Work in progress')




def pg1():

    about_me()

def pg2():

    demo()


    

page_names_to_funcs = {
    "About Me":pg1,
    "Demo":pg2
}

selected_page = st.sidebar.radio(" ",page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


if __name__ == '__main__':
    st.write('Streamlit app is running')
