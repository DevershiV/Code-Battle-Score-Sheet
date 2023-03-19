import streamlit as st
import csv

st.set_page_config(page_title="Code Battle", page_icon="⚔️", layout="wide",initial_sidebar_state = 'auto')

with open("designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)

st.header("")
st.header("Code Store")
st.text("-------------------------------------------------------------------------------------------------------------------------")

indata = []
with open("Code Battle Spreadsheet - Sheet1.csv", mode ='r',encoding='cp1252') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        indata.append(lines)
indata.pop(0)
st.session_state.question = []
st.session_state.shruti = []
st.session_state.devershi = []
st.session_state.shrey = []
st.session_state.vishnu = []
st.session_state.timing = []
st.session_state.date = []
# st.write(indata)
st.session_state.num_questions = len(indata)
for i in reversed(indata):
    st.session_state.question.append(i[0])
    st.session_state.shruti.append(i[1])
    st.session_state.devershi.append(i[2])
    st.session_state.shrey.append(i[3])
    st.session_state.vishnu.append(i[4])
    st.session_state.timing.append(i[5])
    st.session_state.date.append(i[6])
for i in range(st.session_state.num_questions):
    con = st.container()
    col1, col2, col3, col4= con.columns([0.3,2, 3, 1])
    with col1:
        st.write(st.session_state.num_questions-i)
    with col2:
        st.markdown(st.session_state.question[i])
    with col3:
        st.write("Shruti")
        st.code(st.session_state.shruti[i], language='python')
        st.write("Devershi")
        st.code(st.session_state.devershi[i], language='python')
        st.write("Shrey")
        st.code(st.session_state.shrey[i], language='python')
        st.write("Vishnu")
        st.code(st.session_state.vishnu[i], language='java')
    with col4:
        st.text(st.session_state.timing[i])
    con.text("-------------------------------------------------------------------------------------------------------------------------")

# Update dates

dates = {}
# st.write(st.session_state.date)
for i in range(len(st.session_state.date)):
    if st.session_state.date[i] not in dates:
        dates[st.session_state.date[i]] = 1
    else:
        dates[st.session_state.date[i]] += 1
    st.session_state.date[i] = st.session_state.date[i] + " - " + str(dates[st.session_state.date[i]])