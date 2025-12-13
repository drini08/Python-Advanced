import streamlit as st

def main():
    st.title("Hello, World!")


    if st.button("Click Me!"):
        st.write("Button Clicked!")

    st.checkbox("Check Me")

    if st.checkbox("Check me to show some text"):
        st.write("You're seeing this text bcuz u checked the checkbox!")

    user_input = st.text_input("Enter text", "Sample text")
    st.write("You entered:", user_input)

    age = st.number_input("Enter your age", min_value=0, max_value=110)
    st.write(f"Your age is: {age}")

    message = st.text_area("Enter your message")
    st.write(f"Your message: {message}")

    choice = st.radio("Pick one", ["Choice 1", "CHoice 2", "CHoic 3"])
    st.write(f"You chose: {choice}")

    if st.button("Submit"):
        st.success("You have submitted successfully")

    try:
        1/0
    except Exception as e:
        st.exception(e)



if __name__ == '__main__':
    main()

