import calendar
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import pandas as pd
#from sqlalchemy import create_engine

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Lohith12##',
    'database': 'apexsdg',
}

conn = mysql.connector.connect(**db_config)
mycursor = conn.cursor(dictionary=True)

page_title = "Data entry for ECO SDG ACTIVITIES"
page_icon = ":money_with_wings:"
layout = "centered"

st.set_page_config(page_title = page_title, page_icon = page_icon, layout = layout)
st.title(page_title + " ")

sh_club_name = []
st_names = []
nat_day = {}
aclist = []
ac_det = {
    'activity_id': ' ',
    'from_date': ' ',
    'to_date': ' ',
    'outcomes' : ' ',
    'planning' : ' ',
    'mat_avail' : ' ',
    'mat_collec' : ' ',
    'role' : ' ',
    'aware' : ' ',
    'np_cov' : ' ',
    'collab' : ' ',
    'checklist' : ' ',
    'location' : ' ',
    'steps' : ' ',
    'precautions' : ' ',
    'tools_support' : ' ',
    'learnings' : ' ',
    'village_support' : ' ',
    'final_learnings' : ' ',
    'feedback' : ' ',
    'self_eval' : ' ',
    'notes' : ' '
}

def general_info():
 
  global college_name, district, state, website, head_name, fb_link, yt_link, dignitaries, total_participants, total_strength, date
  college_name = st.text_input("College Name")
  district = st.text_input("District")
  state = st.text_input("State")
  website = st.text_input("Website")
  head_name = st.text_input("Name of the head of the institution")
  fb_link = st.text_input("facebook link")
  yt_link = st.text_input("youtube link")
  dignitaries = st.text_input("dignitaries")
  total_participants = st.number_input("Total participants")
  #global total_activities = st.number_input("Total activities")
  total_strength = st.number_input("Total strength")
  date = st.date_input("Date:", key = "date1")


def national_international_day():
  #nat_intl_day, intl_date
  num_natldays = st.number_input("Number of National/Intl days" , min_value=1, max_value=100, value=1, key="natday")
  for i in range(1, num_natldays + 1):
      nat_intl_day = st.text_input("National or International Day celebrated", key=f"{i}")
      intl_date = st.date_input("Date:", key=f"date{i+1}")
      nat_day[nat_intl_day] = intl_date
      #st_names.append(student_name)


def faculty_names():
  global faculty_names
  faculty_names = st.text_input("Faculty names, comma separated")
 

def student_names(shcnum):
   
    num_students = st.number_input("Number of students" , min_value=1, max_value=100, value=1, key=f"shclub{shcnum}")
    for i in range(1, num_students + 1):
      student_name = st.text_input(f"Student Name {i}", key = f"stname {shcnum}+{i}")
      st_names.append(student_name)
   
def shclubnames():
   num_shclubs = st.number_input("Number of self help clubs" , min_value=1, max_value=100, value=1)
   for j in range(1, num_shclubs+1):
     shclubname = st.text_input(f"Self help club name {j}" , key = f"shclub {j}")
     sh_club_name.append(shclubname)
     student_names(j)

def activity_table():
     acsql = "select activity_name from activity_table"
     dataframe = pd.read_sql_query(acsql, conn)
     for column, values in dataframe.items():
       if (column == "activity_name"):
         for value in values:
          #st.write(f"Activity list: {value}")
           aclist.append(value)
   #aclist = mycursor.fetchall()
   
   #st.write(f"Activity list : {values}")
   

def activity_details(iter):
 
  ac_det["from_date"] = st.date_input("From Date:", key=f"from_date {iter}")
  ac_det["to_date"] = st.date_input("To Date:", key=f"to_date {iter}")
  ac_det["outcomes"] = st.text_input("Outcomes", key=f"Outcomes {iter}")
  ac_det["planning"] = st.text_input("Planning", key=f"Planning {iter}")
  ac_det["mat_avail"] = st.text_input("Material availability", key=f"mat_avail {iter}")
  ac_det["mat_collec"] = st.text_input("Material Collection", key=f"mat_collec {iter}")
  ac_det["role"] = st.text_input("List of the material and role of the material", key=f"role {iter}")
  ac_det["aware"] = st.radio("Were you aware of this activity earlier?", ('Yes','No'), key=f"aware {iter}")
  ac_det["collab"] = st.text_input("Did you collaborate with other organizations to create a bigger one? ", key=f"collab {iter}")
  ac_det["checklist"] = st.text_input("Has the organizing team prepared and follow a checklist for conducting the activity?", key=f"checklist {iter}")
  ac_det["location"] = st.text_input("Where did you conduct this program?", key=f"location {iter}")
  ac_det["steps"] = st.text_input("What are the steps involved in conducting the activity work? / Mention step by step procedure followed? Write in bullet points.", key=f"steps {iter}")
  ac_det["precautions"] = st.text_input("What are the precautions taken for conducting the activity? ", key=f"precaution {iter}")
  ac_det["tools_support"] = st.text_input("What were the tools/support systems used for conducting the activity ", key=f"tools_support {iter}")
  ac_det["learnings"] = st.text_input("What was your learning at various steps of implementation of the activity?", key=f"learnings {iter}")
  ac_det["village_support"] = st.text_input("How was the support from the students/neighborhood/ village/school", key=f"village_support {iter}")
  ac_det["final_learnings"] = st.text_input("What have you learned from this process while working for the District Eco-SDGs Championship 2024? ", key=f"final_learnings {iter}")
  ac_det["feedback"] = st.text_input("Did you collect the feedback from the participants of the activity ?", key=f"feedback {iter}")
  ac_det["self_evaluation"] = st.text_input("What is your self evaluation for this effort ?", key=f"self_eval {iter}")
  ac_det["notes"] = st.text_input("Any notes/comments ?", key=f"notes {iter}")

def main():
  #with st.form("data_entry", clear_on_submit=True):
    with st.expander("General Information"):
      general_info()

    with st.expander("National or International days celebrated"):
      national_international_day()

    with st.expander("Faculty Coordinators names"):
      faculty_names()

    with st.expander("Students in self help club names"):
      shclubnames()

    with st.expander("Activities"):
        activity_table()
        #st.write(f"List of activities : {aclist}")
        num_activities = st.number_input("Number of activities" , min_value=1, max_value=100, value=1)
        for k in range(1, num_activities+1):
           option = st.selectbox(f"Which activity do you like to report " , aclist, key=f"activity {k}")
           if option:
              st.write(f"You selected : {option}" )
              #with st.expander("Activity Details"):
              activity_details(k)

    #with st.expander("Activity Details"):
     # activity_details()

     
    submitted = st.button("Submit")
   
    if submitted:
     college_sql = "insert into college_info (college_name, district, state, website, head_name, fb_link, yt_link, total_participants, total_strength, dignitaries, date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
     values = (college_name, district, state, website, head_name, fb_link, yt_link, int(total_participants), int(total_strength), dignitaries, date)
     st.write(f"Sql {college_sql}")
     st.write(f"Sql {values}")

     mycursor.execute(college_sql, values)
     
     conn.commit()

     mycursor.execute("select last_insert_id()")
     id = mycursor.fetchone()
     
     if id is not None:
       college_id = id['last_insert_id()']
       st.write(f"My id is {college_id}")
       #Tuple is of this form -  {'last_insert_id()': 28}
     
     #Insert into national_international_day
     for key in nat_day:
        natdayname = key
        natdaydate = nat_day[key]
        nat_sql = "insert into national_international_days (college_id, national_international_day, date) values (%s, %s, %s);"
        nvalues = (college_id, natdayname, natdaydate)
        mycursor.execute(nat_sql, nvalues)
        st.write(f"My nat sql - {nat_sql} ")
        st.write(f"My nat values - {college_id} , {natdayname} , {natdaydate} ")
        conn.commit()

     mycursor.close()
     conn.close()

if __name__ == "__main__":
    main()
