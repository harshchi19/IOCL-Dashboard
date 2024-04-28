import pandas as pd
import random
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Load the provided dataset
df = pd.read_excel('net_zero_dashboard_data.xlsx')

#######################################
# PAGE SETUP
#######################################

st.set_page_config(page_title="NetZero Nexus", page_icon="♻️", layout="wide")

st.title("NetZero Nexus")
st.markdown("_Prototype v1.0_")

with st.sidebar:
    st.header("Configuration")
    
    # Filter by location
    selected_location = st.multiselect(
        "Select Location",
        df['Location'].unique().tolist()
    )
    
    # Filter by scenario
    selected_scenario = st.multiselect(
        "Select Scenario",
        df['Scenario_Analysis'].unique().tolist()
    )
    
    # Filter by initiative
    selected_initiative = st.multiselect(
        "Select Initiative",
        df['Initiative_Name'].unique().tolist()
    )
    
    # Filter by cost saving range
    min_cost_saving = st.number_input("Minimum Cost Saving", value=0)
    max_cost_saving = st.number_input("Maximum Cost Saving", value=df['Cost_Saving'].max())
    
    # Filter by alignment with government target
    alignment_options = df['Alignment_with_Government_Target'].unique().tolist()
    selected_alignment = st.multiselect(
        "Alignment with Government Target",
        alignment_options
    )
    
    # Filter by customization required
    customization_options = df['Customization_Required'].unique().tolist()
    selected_customization = st.multiselect(
        "Customization Required",
        customization_options
    )
    
    # Filter by sellable to other companies
    sellable_options = df['Sellable_to_Other_Companies'].unique().tolist()
    selected_sellable = st.multiselect(
        "Sellable to Other Companies",
        sellable_options
    )

#######################################
# DATA PREPROCESSING
#######################################

# Filter data based on selected options
filtered_df = df[
    (df['Location'].isin(selected_location)) &
    (df['Scenario_Analysis'].isin(selected_scenario)) &
    (df['Initiative_Name'].isin(selected_initiative)) &
    (df['Cost_Saving'].between(min_cost_saving, max_cost_saving)) &
    (df['Alignment_with_Government_Target'].isin(selected_alignment)) &
    (df['Customization_Required'].isin(selected_customization)) &
    (df['Sellable_to_Other_Companies'].isin(selected_sellable))
]

# Calculate total GHG mitigated and total cost saving
total_ghg_mitigated = filtered_df['GHG_Mitigated'].sum()
total_cost_saving = filtered_df['Cost_Saving'].sum()

#######################################
# VISUALIZATION METHODS
#######################################

def plot_total_ghg_and_cost():
    fig = go.Figure()

    # Add total GHG mitigated
    fig.add_trace(
        go.Indicator(
            mode="number+delta",
            value=total_ghg_mitigated,
            delta={"reference": total_ghg_mitigated - filtered_df['GHG_Mitigated'].mean()},
            title={"text": "Total GHG Mitigated", "font": {"size": 20}},
            domain={"row": 0, "column": 0}
        )
    )

    # Add total cost saving
    fig.add_trace(
        go.Indicator(
            mode="number+delta",
            value=total_cost_saving,
            delta={"reference": total_cost_saving - filtered_df['Cost_Saving'].mean()},
            title={"text": "Total Cost Saving", "font": {"size": 20}},
            domain={"row": 0, "column": 1}
        )
    )

    fig.update_layout(
        grid={"rows": 1, "columns": 2},
        margin=dict(t=20, b=20, l=10, r=10)
    )

    st.plotly_chart(fig)


def plot_scenario_analysis():
    scenario_counts = filtered_df['Scenario_Analysis'].value_counts().reset_index()
    scenario_counts.columns = ['Scenario', 'Frequency']

    fig = px.bar(
        scenario_counts,
        x='Scenario',
        y='Frequency',
        labels={'Scenario': 'Scenario', 'Frequency': 'Frequency'},
        title='Scenario Analysis',
    )

    st.plotly_chart(fig)



def plot_impact_alignment():
    alignment_counts = filtered_df['Alignment_with_Government_Target'].value_counts()

    fig = px.pie(
        alignment_counts,
        values=alignment_counts.values,
        names=alignment_counts.index,
        title='Alignment with Government Target'
    )

    st.plotly_chart(fig)

def plot_initiative_distribution():
    initiative_counts = filtered_df['Initiative_Name'].value_counts().reset_index()
    initiative_counts.columns = ['Initiative', 'Frequency']

    fig = px.bar(
        initiative_counts,
        x='Frequency',
        y='Initiative',
        orientation='h',
        labels={'Frequency': 'Frequency', 'Initiative': 'Initiative'},
        title='Top 10 Initiatives by Frequency'
    )

    st.plotly_chart(fig)



def plot_ghg_vs_cost():
    fig = px.scatter(
        filtered_df,
        x='GHG_Mitigated',
        y='Cost_Saving',
        color='Scenario_Analysis',
        size='MIRR',
        hover_name='Initiative_Name',
        labels={'GHG_Mitigated': 'GHG Mitigated', 'Cost_Saving': 'Cost Saving'},
        title='GHG Mitigated vs. Cost Saving (Size: MIRR)'
    )

    st.plotly_chart(fig)

def plot_monthly_ghg_trend():
    # Ensure that the required columns exist in the DataFrame
    if 'Location' not in filtered_df.columns or 'GHG_Mitigated' not in filtered_df.columns:
        st.error("The DataFrame does not contain necessary columns.")
        return
    
    # Aggregate GHG data by location
    location_ghg = filtered_df.groupby('Location')['GHG_Mitigated'].sum().reset_index()

    # Plot bar chart
    fig = px.bar(
        location_ghg,
        x='Location',
        y='GHG_Mitigated',
        labels={'GHG_Mitigated': 'Total GHG Mitigated', 'Location': 'Location'},
        title='Total GHG Mitigated by Location'
    )

    st.plotly_chart(fig)







#######################################
# STREAMLIT LAYOUT
#######################################

st.header("Key Metrics")
plot_total_ghg_and_cost()

st.header("Scenario Analysis")
plot_scenario_analysis()

st.header("Alignment with Government Target")
plot_impact_alignment()

st.header("Initiative-wise Analysis")
plot_initiative_distribution()

st.header("GHG Mitigated vs. Cost Saving")
plot_ghg_vs_cost()

st.header("Monthly GHG Trend by Location")
plot_monthly_ghg_trend()

# Display a sample of the filtered dataset
with st.expander("View Filtered Dataset Sample"):
    st.dataframe(filtered_df.head(10))
