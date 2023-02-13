import streamlit as st

st.subheader("About")
st.markdown("""
:red[Please use GPU for anything that is not playing around with a video shorter than 5 minutes since using CPU takes really long (for a 15 minute video it takes just 2-3 minutes in a GPU vs 30 minutes in a CPU!)]

This app allows you to find a scene in a video by just describing it in natural language. It uses [X-CLIP](https://arxiv.org/pdf/2208.02816.pdf), an extension of the model [CLIP](https://arxiv.org/pdf/2103.00020.pdf) (Contrastive Language-Image Pre-Training) which forms parts of the current trend of multimodal models and more specifically the trend in using natural language as a training signal for learning about a domain other than language. Using text as the supervision allows for impressive zero-shot performance and generalization.

Just input a YouTube video URL and a description and click search. The time window is the duration of the chunks the video will be split into for analysis (the 10 seconds default usually works fine), the higher this value the shorter the runtime and the less RAM is used but also maybe the lower the performance. The results will be ordered from most to least relevant and will cover the whole video, so what you are looking for is probably on the top 5 or so results, being less related the lower they are.

The model has several limitations that are really well explained in the corresponding papers and it won’t get everything right. Nevertheless it does show an amazing level of specificity and usually offers relevant results and it is an example of the fascinating near future in multimodal AI research.

"""
            )
st.sidebar.caption('Created by [Dave Dominguez](https://github.com/Davegdd)')