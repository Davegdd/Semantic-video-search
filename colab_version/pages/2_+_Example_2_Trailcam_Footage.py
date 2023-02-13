import streamlit as st

# defines an h1 header
st.title("Example 2 Trailcam Footage")

# display the select widget for the video source
source = st.selectbox("Choose video source", ["YouTube"])

if source == "YouTube":
    # display text input box
    st.caption("Enter YouTube URL")
    st.code("https://www.youtube.com/watch?v=exPhtg0_l7k", language="markdown")

st.caption("Describe scene to find")
st.code("Birds drinking water", language="markdown")

window = st.number_input("Select time window (seconds)", min_value=10, max_value=10)

st.markdown("***")

st.number_input("Number of results to display", min_value=6, max_value=6, value=6)

time_frames = ['7:50', '15:50', '13:40', '7:40', '2:20', '12:40']

# display scene time selection buttons
time = st.radio("Times of most similar scenes", time_frames)

# convert back to seconds and render video
minutes, seconds = map(int, time.split(":"))
time = minutes * 60 + seconds

st.video("https://www.youtube.com/watch?v=exPhtg0_l7k", format="video/mp4", start_time=int(time))
st.sidebar.caption('Created by [Dave Dominguez](https://github.com/Davegdd)')