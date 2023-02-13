# backend/inference.py
import torch
torch.cuda.current_device()
from decord import VideoReader, cpu
import numpy as np
from math import ceil
from pytube import YouTube
from transformers import XCLIPProcessor, XCLIPModel

# load model and move to GPU if available
model_name = "microsoft/xclip-base-patch16-zero-shot"
processor = XCLIPProcessor.from_pretrained(model_name)
model = XCLIPModel.from_pretrained(model_name)
model = model.to("cuda") if torch.cuda.is_available() else model


# extract video frames that will be analyzed dividing the video in "window" seconds chunks
def frames_sampling(video, window):
    youtube_url = video
    yt = YouTube(youtube_url)
    streams = yt.streams.filter(file_extension='mp4')
    file_path = streams[0].download()

    # Load the video using Decord
    video = VideoReader(file_path, num_threads=1, ctx=cpu(0))

    # Get the number of frames and fps
    frames = len(video)
    fps = ceil(video.get_avg_fps())

    # Calculate the duration of the video
    duration = ceil(frames / fps)

    # Time window duration in seconds
    clip_duration = window

    # Calculate the number of clips
    num_clips = int(duration / clip_duration)

    # Calculate frame indices and extract them
    frames_idx = np.linspace(start=0, stop=frames, num=32 * num_clips)
    frames_idx = np.clip(frames_idx, 0, frames - 1).astype(np.float64)
    clips = video.get_batch(frames_idx).asnumpy()
    clips = np.array_split(clips, int(clips.shape[0] / 32))

    return clips


# analyze preprocessed frames in search for described scene
def search_scene(clips, text, window):
    results = []
    for i in range(len(clips)):
        inputs = processor(text=text, videos=list(clips[i]), return_tensors="pt", padding=True)
        inputs = inputs.to("cuda") if torch.cuda.is_available() else inputs
        # forward pass
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits_per_video
            results.append(logits)

    # Sort results from most to least similar scene
    time_results = {}
    for i in range(len(results)):
        time = i * window
        time_results[time] = float(results[i])

    sorted_dict = dict(sorted(time_results.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
