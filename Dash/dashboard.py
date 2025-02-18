import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import requests
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the dashboard
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Fraud Detection Dashboard", className="text-center my-4"))),
    
    # Summary Boxes
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Total Transactions", className="card-title"),
            html.P(id="total-transactions", className="card-text")
        ]), className="mb-4"), width=4),
        
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Fraud Cases", className="card-title"),
            html.P(id="fraud-cases", className="card-text")
        ]), className="mb-4"), width=4),
        
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Fraud Percentage", className="card-title"),
            html.P(id="fraud-percentage", className="card-text")
        ]), className="mb-4"), width=4),
    ], className="mb-4"),
    
    # Fraud trend over time
    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Fraud Cases Over Time", className="card-title"),
                    dcc.Graph(id="fraud-trend")
                ])
            ), className="mb-4"
        )
    ),
    
    # Fraud geography
    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Fraud Cases by Country", className="card-title"),
                    dcc.Graph(id="fraud-geo")
                ])
            ), className="mb-4"
        )
    ),

    # Interval component for auto-updating
    dcc.Interval(id='interval-component', interval=20000, n_intervals=0)
], fluid=True)

# Callback to update summary stats
@app.callback(
    [Output('total-transactions', 'children'),
     Output('fraud-cases', 'children'),
     Output('fraud-percentage', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_summary_boxes(n):
    response = requests.get("http://127.0.0.1:5000/summary").json()
    total_transactions = f"{response['total_transactions']}"
    fraud_cases = f"{response['fraud_cases']}"
    fraud_percentage = f"{response['fraud_percentage']:.2f}%"
    
    return total_transactions, fraud_cases, fraud_percentage

# Callback to update fraud trend graph
@app.callback(
    Output('fraud-trend', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_fraud_trend(n):
    response = requests.get("http://127.0.0.1:5000/fraud_trends").json()
    fraud_trend_df = pd.DataFrame(response)
    
    fig = px.line(fraud_trend_df, x='purchase_time', y='class', title="Fraud Cases Over Time",
                  labels={'purchase_time': 'Purchase Time', 'class': 'Fraud Cases'})
    fig.update_layout(template="plotly_white")
    return fig

# Callback to update fraud geography graph
@app.callback(
    Output('fraud-geo', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_fraud_geo(n):
    response = requests.get("http://127.0.0.1:5000/fraud_geography").json()
    fraud_geo_df = pd.DataFrame(response)
    
    fig = px.choropleth(fraud_geo_df, locations="country", color="class",
                        locationmode='country names', title="Fraud Cases by Country",
                        labels={'class': 'Fraud Cases'})
    fig.update_layout(template="plotly_white")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)