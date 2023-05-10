import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import pandas as pd

# Load data
df = pd.read_csv('your_data_file.csv')

# Create Dash app
app = dash.Dash()

# Define app layout
app.layout = html.Div([
    dcc.Graph(id='my-graph'),
    html.Button('Update Graph', id='update-graph-button')
])

# Define app callbacks
@app.callback(Output('my-graph', 'figure'),
              [Input('update-graph-button', 'n_clicks')])
def update_graph(n_clicks):
    # Create plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='lines'))
    fig.update_layout(title='My Plot', xaxis_title='X', yaxis_title='Y')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
