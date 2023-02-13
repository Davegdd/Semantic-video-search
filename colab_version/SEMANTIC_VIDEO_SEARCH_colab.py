# frontend/streamlit_app.py

import streamlit as st
import inference_colab

current_frames = []

try:
  current_times = st.session_state.time
except:
  current_times = {}

st.sidebar.caption('Created by [Dave Dominguez](https://github.com/Davegdd)')

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("SEMANTIC VIDEO SEARCH")

# display the select widget for the video source
source = st.selectbox("Choose video source", ["YouTube"])

if source == "YouTube":
    # display text input box
    video = st.text_input("Enter YouTube URL")

text = st.text_input("Describe scene to find")

window = st.number_input("Select time window (seconds)", min_value=1, value=10)


# extract video frames that will be analyzed
@st.cache
def preprocess(video_path, time_window):
    frames = inference_colab.frames_sampling(video_path, time_window)
    current_frames.clear()
    current_frames.extend(frames)
    return frames


# analyze preprocessed frames in search for described scene
def search(description, time_window):
    times = inference_colab.search_scene(current_frames, description, time_window)
    current_times.clear()
    current_times.update(times)
    return current_times


# display clickable Search button
if st.button("Search"):
    if video is not None and text is not None:
        frames = preprocess(video, window)
        times = search(text, window)
        st.session_state.time = current_times

st.markdown("***")

keys = current_times.keys()
keys = [key for key in keys]

time_frames = keys

# number of results to display
top_k = st.number_input("Number of results to display", min_value=1, max_value=len(time_frames), value=3)
time_frames = time_frames[:top_k]

# convert seconds to minutes and seconds
mins_secs = [(str(int(secs) // 60) + ":" + f"{int(secs) % 60:02d}") for secs in time_frames]

# display scene time selection buttons
time = st.radio("Times of most similar scenes", mins_secs) if time_frames else "0:00"

# convert back to seconds and render video
minutes, seconds = map(int, time.split(":"))
time = minutes * 60 + seconds

if video:
    st.video(video, format="video/mp4", start_time=int(time))
