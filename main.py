import streamlit as st
import pandas

st.title("Company Website")
st.write("Here is the description of the company. Blah blah blah")

col1,col2, col3 = st.columns(3)

data = pandas.read_csv("data.csv")

num_employees = len(data)

# Calculate num_col1
num_col1 = num_employees // 3 + (1 if num_employees % 3 > 0 else 0)
# Calculate num_col2
num_col2 = num_employees // 3 + (1 if num_employees % 3 > 1 else 0)
# Calculate num_col3 (remaining employees)
num_col3 = num_employees // 3

with col1:
    for index, row in data[:num_col1].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row['image'])

with col2:
    for index, row in data[num_col1:num_col1+num_col2].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row['image'])

with col3:
    for index, row in data[num_col1+num_col2:].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row['image'])