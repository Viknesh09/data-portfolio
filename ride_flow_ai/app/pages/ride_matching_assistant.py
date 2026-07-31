# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import streamlit as st
import pandas as pd
import numpy as np

st.title("🚖 AI Ride Matching Assistant")

np.random.seed(42)

drivers = pd.DataFrame({

    'driver_name':[

        'Rahul',

        'Arjun',

        'Vikram',

        'Suresh'
    ],

    'rating':[

        4.8,

        4.5,

        4.9,

        4.3
    ],

    'eta':[

        5,

        10,

        7,

        3
    ],

    'cancellation_risk':[

        0.10,

        0.30,

        0.05,

        0.40
    ]
})

demand_score = st.slider(

    "Demand Level",

    1,

    10,

    5
)

drivers['match_score'] = (

    drivers['rating'] * 0.5

    -

    drivers['eta'] * 0.1

    -

    drivers['cancellation_risk'] * 5

    +

    demand_score * 0.1
)

best_driver = drivers.sort_values(

    by='match_score',

    ascending=False
)

st.write(best_driver)

top_driver = best_driver.iloc[0]

st.success(

    f"Recommended Driver: {top_driver['driver_name']}"
)
