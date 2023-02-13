import streamlit as st

st.subheader("PRECOMPUTED EXAMPLES")
st.markdown("""
Given the costs to deploy the model with GPU and the enormous difference
 in computing time between running on CPU vs GPU, some precomputed examples can be found on the left sidebar.
 Each of them just took about 2-3 minutes running on a single Tesla T4 GPU.
 
 In [Example 1 Security Camera](+_Example_1_Security_Camera) the model is able to find several scenes where people enter or exit a car
 from the description "Person getting in or out of a car". We used a time window of 20 seconds instead of the default 10
 due to RAM limitations, this made it harder for the model since it had less frames to infer from. Amazingly, 
 it managed to find several relevant scenes in a 1 hour video both at day and night.
 
 In [Example 2 Trailcam Footage](+_Example_2_Trailcam_Footage) the model is able to distinguish not only between different types of animals 
 but also their actions and correctly find scenes of "birds drinking water",  again both with full colour footage
 and night vision footage.
"""
            )
st.sidebar.caption('Created by [Dave Dominguez](https://github.com/Davegdd)')