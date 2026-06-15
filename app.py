import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
 
st.title("ADR Reaction Explorer")
 
drug = st.text_input("Drug name", "ibuprofen")
 
if drug:
    url = f'https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:"{drug}"&count=patient.reaction.reactionmeddrapt.exact'
    r = requests.get(url).json()
    if "results" not in r:
        st.warning(f"No results for {drug}")
    else:
        df = pd.DataFrame(r["results"]).head(15).iloc[::-1]
        fig, ax = plt.subplots()
        df.plot.barh(x="term", y="count", ax=ax, legend=False)
        ax.set_title(f"Top reactions: {drug}")
        st.pyplot(fig)
 
st.caption(
    "Data: FDA FAERS via openFDA. Spontaneous adverse-event reports - "
    "subject to reporting bias, no exposure denominator. "
    "Counts do not imply causation."
)
