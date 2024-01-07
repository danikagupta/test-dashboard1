import streamlit as st
import random

import pandas as pd
import altair as alt

languages=["English","हिंदी","മലയാളം","සිංහල"]

def setup_sidebar():
    st.sidebar.markdown("# LiteraLearn")
    st.sidebar.image("assets/icon128px-red.png")
    images=["assets/img1.jpg","assets/img2.jpg","assets/img3.jpg",
            "assets/img4.jpg","assets/img5.jpg","assets/img6.jpg",
            "assets/img7.jpg","assets/img8.jpg","assets/img9.jpg",
            "assets/img10.jpg","assets/img11.jpg","assets/img12.jpg",
            "assets/img13.jpg"]
    random_image=random.choice(images)
    st.sidebar.image(random_image)
    #bu=st.sidebar.button("Reset", type="primary")
    #if bu:
    #    st.rerun()

def setup_chart(df,lang,goal,reading,reached,last_year,width,height):
  st.write(f"# {lang}")
  total_hours = df['Hours Worked'].sum()

  chart = alt.Chart(df).mark_bar(size=10).encode(
    x=alt.X('Day', sort=df['Day'].tolist()),
    y=alt.Y('Hours Worked', axis=alt.Axis(ticks=False, labels=False, title=None, grid=False)),
    color=alt.value('steelblue') 
  ).configure_axis(
    domain=False  # Remove axis line 
  ).properties(
    width=width,
    height=height
  )
  chart.configure_title(fontSize=14).configure(background='#D9E9F0')

  st.write(f"Time spent: {total_hours} hours")
  st.altair_chart(chart)
  table1={"Goal":goal,"Reading":reading}
  table2={"Level reached":reached,"Reached last year":last_year}
  st.data_editor(table1,key=lang+"1")
  st.data_editor(table2,key=lang+"2")
  #df1_html = pd.DataFrame(table1).to_html(index=False, header=False)
  #st.markdown(df1_html, unsafe_allow_html=True)


def run():
  setup_sidebar()
    # Sample DataFrame with hours worked for each day of the week
  data1 = {
      'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      'Hours Worked': [8, 8.5, 7, 9, 6, 4, 5]
  }
  df1 = pd.DataFrame(data1)
    # Sample DataFrame with hours worked for each day of the week
  data2 = {
      'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      'Hours Worked': [8, 8.5, 7, 9, 3, 4, 0]
  }
  df2 = pd.DataFrame(data2)
  c1,c2=st.columns([1,1])
  col1=c1.container(border=True)
  col2=c2.container(border=True)
  with col1:
    setup_chart(df1,languages[2],"2/3 Days","103 days",5,1,300,200)
  with col2:
    setup_chart(df2,languages[0],"2/3 Days","103 days",5,1,300,200)
 


if __name__ == "__main__":
    run()
