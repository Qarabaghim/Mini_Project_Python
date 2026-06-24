import os
import json
import streamlit as st


def is_valid_phone(number):
    return(
        len(number) == 11
        and number.startswith("09")
        and number.isdigit()
    )


if "phonoebook" not in st.session_state:
    if os.path.exists("phonebook.json"):
        with open("phonebook.json", "r") as f:
            st.session_state.phonebook = json.load(f)
    else:
        st.session_state.phonebook = {}


st.set_page_config(page_title="phonebook", page_icon="📞")
st.title("phone book")
st.write("___")


menu = st.sidebar.selectbox(
    "Menu",
    ["Add", "Show", "Search", "Edit", "Delete"]
)


# Add
if menu == "Add":
    name = st.text_input("Name")
    number = st.text_input("Phone Number")
    if st.button("Save"):
        if is_valid_phone(number):
            st.session_state.phonebook[name] = number
            st.success("Saved!")
        with open("phonebook.json", "w") as f:
            json.dump(st.session_state.phonebook, f)
    else:
        st.error("Phone number is invalid")


# Show
elif menu == "Show":
    if st.session_state.phonebook:
        for name, number in st.session_state.phonebook.items():
            st.write(f"{name} : {number}")
    else:
        st.write("Phonebook is Empty")


# Search
elif menu == "Search":
    name = st.text_input("Name")
    if st.button("Search"):
        if name in st.session_state.phonebook:
            st.success(
                st.session_state.phonebook[name]
            )
        else:
            st.error("Not Found")


# Edit
elif menu == "Edit":
    name = st.text_input("Name")
    if name in st.session_state.phonebook:
        new_number = st.text_input("New Number")
        if st.button("Update"):
            if is_valid_phone(new_number):
                st.session_state.phonebook[name] = new_number
                st.success("Updated")
                with open("phonebook.json", "w") as f:
                    json.dump(st.session_state.phonebook, f)
            else:
                st.write("Phone number is invalid")
        elif name:
            st.error("Not Found")


# Delete
elif menu == "Delete":
    name = st.text_input("Name")
    if st.button("Delete"):
        if name in st.session_state.phonebook:
            del st.session_state.phonebook[name]
            with open("phonebook.json", "w") as f:
                json.dump(st.session_state.phonebook, f)
            st.success("Deleted")
        else:
            st.error("Not Found")
