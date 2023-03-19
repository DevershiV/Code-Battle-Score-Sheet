import streamlit as st
import pandas as pd
from datetime import datetime
import time

st.set_page_config(page_title="Code Battle", page_icon="⚔️", layout="wide",initial_sidebar_state = 'auto')

with open("designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)
st.header("")
st.header("")
st.header("Code Battle")

# Get time of each contestant from the string
# name_time is to calculate average and name_total is to calculate ranks.

shruti_time = []
shruti_total = []
shrey_time = []
shrey_total = []
vishnu_time = []
vishnu_total = []
devershi_time = []
devershi_total = []
for i in st.session_state.timing:
    shruti = i.find("Shruti")
    if shruti != -1:
        shruti_time.append(i[shruti+9:i.find("\n",shruti+9)if i.find("\n",shruti+9)!=-1 else len(i)])
        shruti_total.append(i[shruti+9:i.find("\n",shruti+9)if i.find("\n",shruti+9)!=-1 else len(i)])
    else:
        shruti_total.append(10**10)
    shrey = i.find("Shrey")
    if shrey != -1:
        shrey_time.append(i[shrey+8:i.find("\n",shrey+8)if i.find("\n",shrey+9)!=-1 else len(i)])
        shrey_total.append(i[shrey+8:i.find("\n",shrey+8)if i.find("\n",shrey+9)!=-1 else len(i)])
    else:
        shrey_total.append(10**10)
    vishnu = i.find("Vishnu")
    if vishnu != -1:
        vishnu_time.append(i[vishnu+9:i.find("\n",vishnu+9)if i.find("\n",vishnu+9)!=-1 else len(i)])
        vishnu_total.append(i[vishnu+9:i.find("\n",vishnu+9)if i.find("\n",vishnu+9)!=-1 else len(i)])
    else:
        vishnu_total.append(10**10)
    devershi = i.find("Devershi")
    if devershi != -1:
        devershi_time.append(i[devershi+11:i.find("\n",devershi+11)if i.find("\n",devershi+9)!=-1 else len(i)])
        devershi_total.append(i[devershi+11:i.find("\n",devershi+11)if i.find("\n",devershi+9)!=-1 else len(i)])
    else:
        devershi_total.append(10**10)

# Converting time string to seconds

for i in range(len(shruti_time)):
    pt = datetime.strptime(shruti_time[i],'%M:%S')
    shruti_time[i] = pt.second + pt.minute*60
for i in range(len(shrey_time)):
    pt = datetime.strptime(shrey_time[i],'%M:%S')
    shrey_time[i] = pt.second + pt.minute*60
for i in range(len(vishnu_time)):
    pt = datetime.strptime(vishnu_time[i],'%M:%S')
    vishnu_time[i] = pt.second + pt.minute*60
for i in range(len(devershi_time)):
    pt = datetime.strptime(devershi_time[i],'%M:%S')
    devershi_time[i] = pt.second + pt.minute*60
for i in range(st.session_state.num_questions):
    if shruti_total[i] != 10**10:
        pt = datetime.strptime(shruti_total[i],'%M:%S')
        shruti_total[i] = pt.second + pt.minute*60
    if shrey_total[i] != 10**10:
        pt = datetime.strptime(shrey_total[i],'%M:%S')
        shrey_total[i] = pt.second + pt.minute*60
    if vishnu_total[i] != 10**10:
        pt = datetime.strptime(vishnu_total[i],'%M:%S')
        vishnu_total[i] = pt.second + pt.minute*60
    if devershi_total[i] != 10**10:
        pt = datetime.strptime(devershi_total[i],'%M:%S')
        devershi_total[i] = pt.second + pt.minute*60
    
# Calculating Average

avg = [sum(shruti_time) / len(shruti_time),sum(shrey_time) / len(shrey_time),sum(vishnu_time) / len(vishnu_time),sum(devershi_time) / len(devershi_time)]

# Calculating Ranks

st.subheader("Ranks")

shruti_rank = {"1":0,"2":0,"3":0,"4":0}
shrey_rank = {"1":0,"2":0,"3":0,"4":0}
vishnu_rank = {"1":0,"2":0,"3":0,"4":0}
devershi_rank = {"1":0,"2":0,"3":0,"4":0}

for i in range(st.session_state.num_questions):
    rank = [shruti_total[i],shrey_total[i],vishnu_total[i],devershi_total[i]]
    rank.sort()
    if shruti_total[i] != 10**10:
        shruti_rank[str(rank.index(shruti_total[i])+1)]+=1
    if shrey_total[i] != 10**10:
        shrey_rank[str(rank.index(shrey_total[i])+1)]+=1
    if vishnu_total[i] != 10**10:
        vishnu_rank[str(rank.index(vishnu_total[i])+1)]+=1
    if devershi_total[i] != 10**10:
        devershi_rank[str(rank.index(devershi_total[i])+1)]+=1
    
con = st.container()
col1, col2, col3, col4= con.columns([3,3,3,3])
with col1:
    st.write("Devershi")
    st.write("🥇 "+str(devershi_rank["1"]))
    st.write("🥈 "+str(devershi_rank["2"]))
    st.write("🥉 "+str(devershi_rank["3"]))
    st.write("💩 "+str(devershi_rank["4"]))
with col2:
    st.write("Shrey")
    st.write("🥇 "+str(shrey_rank["1"]))
    st.write("🥈 "+str(shrey_rank["2"]))
    st.write("🥉 "+str(shrey_rank["3"]))
    st.write("💩 "+str(shrey_rank["4"]))
with col3:
    st.write("Shruti")
    st.write("🥇 "+str(shruti_rank["1"]))
    st.write("🥈 "+str(shruti_rank["2"]))
    st.write("🥉 "+str(shruti_rank["3"]))
    st.write("💩 "+str(shruti_rank["4"]))
with col4:
    st.write("Vishnu")
    st.write("🥇 "+str(vishnu_rank["1"]))
    st.write("🥈 "+str(vishnu_rank["2"]))
    st.write("🥉 "+str(vishnu_rank["3"]))
    st.write("💩 "+str(vishnu_rank["4"]))

# Bar Graph for Average

st.subheader("Average time for each Question")

bar = {'Average':avg,
        'Gladiator':['Shruti','Shrey','Vishnu','Devershi']}
bar_data = pd.DataFrame(bar)
st.bar_chart(data=bar_data,x="Gladiator")

# Line Graph

st.subheader("Stats")

for i in range(st.session_state.num_questions):
    if shruti_total[i] == 10**10:
        shruti_total[i] = 0
    else:
        shruti_total[i] = (shruti_total[i]/60)
    if shrey_total[i] == 10**10:
        shrey_total[i] = 0
    else:
        shrey_total[i] = (shrey_total[i]/60)
    if vishnu_total[i] == 10**10:
        vishnu_total[i] = 0
    else:
        vishnu_total[i] = (vishnu_total[i]/60)
    if devershi_total[i] == 10**10:
        devershi_total[i] = 0
    else:
        devershi_total[i] = (devershi_total[i]/60)
line = {'devershi':devershi_total,
        'shruti':shruti_total,
        'shrey':shrey_total,
        'vishnu':vishnu_total,
        'date':st.session_state.date}
chart_data = pd.DataFrame(line)
st.line_chart(data=chart_data,x="date")
