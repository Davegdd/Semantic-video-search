import streamlit as st

# defines an h1 header
st.title("Example 1 Security Camera")

# display the select widget for the video source
source = st.selectbox("Choose video source", ["YouTube"])

if source == "YouTube":
    # display text input box
    st.caption("Enter YouTube URL")
    st.code("https://www.youtube.com/watch?v=cbXOhnudzxk&t=1415s", language="markdown")

st.caption("Describe scene to find")
st.code("Person getting in or out of a car", language="markdown")

window = st.number_input("Select time window (seconds)", min_value=20, max_value=20)

st.markdown("***")

st.number_input("Number of results to display", min_value=4, max_value=4, value=4)

time_frames = ['56:40', '50:40', '14:40', '52:40']

# display scene time selection buttons
time = st.radio("Times of most similar scenes", time_frames)

# convert back to seconds and render video
minutes, seconds = map(int, time.split(":"))
time = minutes * 60 + seconds

st.video("https://www.youtube.com/watch?v=cbXOhnudzxk&t=1415s", format="video/mp4", start_time=int(time))
st.sidebar.caption('Created by [Dave Dominguez](https://github.com/Davegdd)')