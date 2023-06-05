import socket

import streamlit as st

def get_ip_address(url):

    try:

        ip_address = socket.gethostbyname(url)

        return ip_address

    except socket.gaierror:

        return "Invalid URL or hostname"

def main():

    st.title("Website IP Address Lookup")

    website_name = st.text_input("Enter the website name:")

    

    if st.button("Get IP Address"):

        ip_address = get_ip_address(website_name)

        st.write(f"The IP address of {website_name} is: {ip_address}")

if __name__ == "__main__":

    main()

