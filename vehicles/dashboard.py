import pandas as pd
import plotly.express as px


def frequency_table(df):
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']
    return manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )


def manufacturer_chart(df):
    # Bar chart: how many vehicles per manufacturer
    counts = df['manufacturer'].value_counts().reset_index()
    counts.columns = ['Manufacturer', 'Count']
    fig = px.bar(counts, x='Manufacturer', y='Count',
                 color='Manufacturer', title='Vehicles per Manufacturer')
    fig.update_layout(showlegend=False)
    return fig.to_html(full_html=False, include_plotlyjs='cdn')


def price_chart(df):
    # Bar chart: average price per manufacturer (needs a 'price' column)
    if 'price' not in df.columns:
        return "<p class='text-muted'>No 'price' column found in the CSV.</p>"
    avg = df.groupby('manufacturer')['price'].mean().reset_index()
    avg.columns = ['Manufacturer', 'Average Price']
    fig = px.bar(avg, x='Manufacturer', y='Average Price',
                 color='Manufacturer', title='Average Price per Manufacturer')
    fig.update_layout(showlegend=False)
    return fig.to_html(full_html=False, include_plotlyjs=False)
