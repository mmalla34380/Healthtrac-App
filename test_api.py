import dash
from dash import html, dcc
import requests
import plotly.express as px
import pandas as pd
print("RUNNING THIS FILE:", __file__)
app = dash.Dash(__name__)


def fetch_data():
    res = requests.get("http://127.0.0.1:8000/data")
    return pd.DataFrame(res.json())


app.layout = html.Div([
    html.H2(
    "HealthTrack Dashboard",
    style={
        "textAlign": "center",
        "color": "darkgreen",  # nice blue shade
        "fontWeight": "bold"
    }
    ),
    dcc.Interval(id='interval', interval=5000, n_intervals=0),
    dcc.Graph(id='graph')
])


@app.callback(
    dash.Output('graph', 'figure'),
    [dash.Input('interval', 'n_intervals')]
)
def update_graph(n):
    df = fetch_data()
    if df.empty:
        return px.line()
    fig = px.line(df, x='timestamp', y='heart_rate', title="Heart Rate Trend")
    return fig


if __name__ == '__main__':
    app.run(debug=True, port=8050)

