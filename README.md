# Semantic video search
Search a scene in a video using natural language with the multimodal model X-CLIP which combines NLP and CV.

![readme GIF](https://user-images.githubusercontent.com/108660081/218450520-5cedc40a-a4d4-40a6-b1fc-36852fc001ba.gif)


This app allows you to find a scene in a video by just describing it in natural language. It uses [X-CLIP](https://arxiv.org/pdf/2208.02816.pdf), an extension of the model [CLIP](https://arxiv.org/pdf/2103.00020.pdf) (Contrastive Language-Image Pre-Training) which forms parts of the current trend of multimodal models and more specifically the trend in using natural language as a training signal for learning about a domain other than language. Using text as the supervision allows for impressive zero-shot performance and generalization.

Just input a YouTube video URL and a description and click search. The time window is the duration of the chunks the video will be split into for analysis (the 10 seconds default usually works fine), the higher this value the shorter the runtime and the less RAM is used but also maybe the lower the performance. The results will be ordered from most to least relevant and will cover the whole video, so what you are looking for is probably on the top 5 or so results, being less related the lower you go.
The model has several limitations that are really well explained in the corresponding papers and it won’t get everything right. Nevertheless it does show an amazing level of specificity and usually offers relevant results and it is an example of the fascinating near future in multimodal AI research.


# Install
## Option 1 Docker
Download the [docker-compose](https://github.com/Davegdd/Semantic-video-search/blob/main/docker-compose.yml) file in a local folder and run (make sure you have Docker installed):

```
docker-compose up
```

Wait a couple minutes so that all dependencies and the model are downloaded and you stop seeing the "http connection error..." and go to localhost http://localhost:8501/

## Option 2 Colab (with GPU acceleration)
There is a huge difference in runtime from running with CPU vs GPU (for a 20 minute video it takes just 2-3 minutes in a GPU vs 30 minutes in a CPU!) so using GPU is
strongly recommended and depending on the use case even the only practical option. Open the Colab notebook below to run with free GPU in 3 clicks:

<a target="_blank" href="https://colab.research.google.com/github/Davegdd/Semantic-video-search/blob/main/colab_version/semantic_video_search_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


