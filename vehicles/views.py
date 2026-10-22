import pandas as pd
from django.shortcuts import render
from .dashboard import frequency_table, manufacturer_chart, price_chart


def dashboard_view(request):
    df = pd.read_csv("dummy_data/vehicles_data_1000.csv")
    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
        "manufacturer_chart": manufacturer_chart(df),
        "price_chart": price_chart(df),
    })
