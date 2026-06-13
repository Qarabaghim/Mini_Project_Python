import os
import json
import streamlit as st

def is_valid_phone(number):
    return (
        len(number) == 11
        and number.startswith("09")
        and number.isdigit()
    )

def load_phonebook():

    if os.path.exists("phonebook.json"):
        with open("phonebook.json", "r") as f:
            return json.load(f)

    return {}


def save_phonebook():

    with open("phonebook.json", "w") as f:
        json.dump(st.session_state.phonebook, f)


def init_session():

    if "phonebook" not in st.session_state:
        st.session_state.phonebook = load_phonebook()


def add_contact():

    st.subheader("Add Contact")

    name = st.text_input("Name")
    number = st.text_input("Phone Number")

    if st.button("Save"):

        if not is_valid_phone(number):
            st.error(
                "Phone number must start with 09 and contain 11 digits"
            )
            return

        st.session_state.phonebook[name] = number

        save_phonebook()

        st.success("Saved!")


def show_contacts():

    st.subheader("All Contacts")

    if not st.session_state.phonebook:
        st.warning("Phonebook is Empty")
        return

    for name, number in st.session_state.phonebook.items():
        st.write(f"📞 {name} : {number}")


def search_contact():

    st.subheader("Search Contact")

    name = st.text_input("Name")

    if st.button("Search"):

        if name in st.session_state.phonebook:
            st.success(
                st.session_state.phonebook[name]
            )
        else:
            st.error("Not Found")


def edit_contact():

    st.subheader("Edit Contact")

    name = st.text_input("Name")

    if name:

        if name in st.session_state.phonebook:

            new_number = st.text_input("New Number")

            if st.button("Update"):

                if not is_valid_phone(new_number):
                    st.error(
                        "Phone number must start with 09 and contain 11 digits"
                    )
                    return

                st.session_state.phonebook[name] = new_number

                save_phonebook()

                st.success("Updated")

        else:
            st.error("Not Found")


def delete_contact():

    st.subheader("Delete Contact")

    name = st.text_input("Name")

    if st.button("Delete"):

        if name in st.session_state.phonebook:

            del st.session_state.phonebook[name]

            save_phonebook()

            st.success("Deleted")

        else:
            st.error("Not Found")


def main():

    st.set_page_config(
        page_title="Phonebook",
        page_icon="📞"
    )

    st.title("📞 Phone Book")
    st.write("---")

    init_session()

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Add",
            "Show",
            "Search",
            "Edit",
            "Delete"
        ]
    )

    if menu == "Add":
        add_contact()

    elif menu == "Show":
        show_contacts()

    elif menu == "Search":
        search_contact()

    elif menu == "Edit":
        edit_contact()

    elif menu == "Delete":
        delete_contact()



if __name__ == "__main__":
    main()
