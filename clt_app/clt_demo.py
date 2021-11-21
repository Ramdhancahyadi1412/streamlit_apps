import streamlit as st
import numpy as np
import  matplotlib.pyplot as plt


st.title('Illustrating the Central Limit Theorem with Streamlit')
st.subheader('An App by Tyler Richards')
st.write(('This app simulates a thousand coin flips using the chance of heads input below,'
          'and then sample with replacement from that population and plots the histogram of the'
          'means of the samples, in order to illustrate the central limit theorem!'))

perc_heads = st.number_input(label='Chance of Coins Landing on Heads', min_value=0.0, max_value=1.0, value=.5)
# graph_title = st.text_input(label='Graph Title')
binom_dist = np.random.binomial(1,perc_heads,1000)

list_means = []
for i in range (0,1000):
    list_means.append(np.random.choice(binom_dist,100,replace=True).mean())

    
fig, ax = plt.subplots()
plt.hist(list_means, range=[0,1])
plt.title('Distribution of Graph Coin Simulated by streamlit')
st.pyplot(fig)
# st.write(np.mean(binom_dist))
