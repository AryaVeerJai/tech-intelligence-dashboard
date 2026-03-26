import plotly.express as px
import pandas as pd

data = {
"Country": ["USA","China","Russia","India","Germany","UK"],
"Attacks":[120,95,80,70,50,40]
}

df = pd.DataFrame(data)

fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Attacks",
    title="Global Cyber Threat Activity",
    color_continuous_scale="Reds"
)

fig.write_image("assets/cyber-map.png")

print("Cyber threat map updated.")
