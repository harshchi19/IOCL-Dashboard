# IOCL-Dashboard
# NetZero Nexus

NetZero Nexus is a prototype dashboard designed to help organizations and stakeholders visualize and analyze their efforts towards achieving net-zero emissions. This tool provides an interactive interface to filter, explore, and visualize key metrics related to greenhouse gas (GHG) mitigation and cost-saving initiatives.

## Features

- **Dynamic Filtering**: Filter data by location, scenario, initiative, cost-saving range, alignment with government targets, customization required, and sellability to other companies.
- **Key Metrics**: Visual representation of total GHG mitigated and total cost savings.
- **Scenario Analysis**: Analyze the frequency and impact of different scenarios on GHG mitigation and cost savings.
- **Alignment with Government Targets**: Visualize the alignment of initiatives with government emission targets.
- **Initiative Distribution**: Breakdown of initiatives by frequency and impact.
- **GHG Mitigated vs. Cost Saving**: Scatter plot visualization to understand the relationship between GHG mitigation and cost savings across different scenarios.
- **Monthly GHG Trend by Location**: Visual representation of total GHG mitigated by location.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/harshchi19/net-zero-nexus.git
    cd net-zero-nexus
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Add Dataset**:
    Place your dataset file `net_zero_dashboard_data.xlsx` in the project root directory.

4. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

Once the application is running, open your web browser and navigate to the provided local URL (typically `http://localhost:8501`). Use the sidebar to configure filters and explore the various visualizations and metrics provided.

## File Structure

- `app.py`: The main Streamlit application file.
- `requirements.txt`: A list of required Python packages.
- `net_zero_dashboard_data.xlsx`: The dataset file (to be added by the user).

## Dataset

The dataset should include the following columns:

- `Location`
- `Scenario_Analysis`
- `Initiative_Name`
- `Cost_Saving`
- `GHG_Mitigated`
- `Alignment_with_Government_Target`
- `Customization_Required`
- `Sellable_to_Other_Companies`
- `MIRR` (Modified Internal Rate of Return)

## Visualizations

### Key Metrics
Displays total GHG mitigated and total cost saving with delta values indicating changes compared to the mean.

### Scenario Analysis
Bar chart showing the frequency of different scenarios in the dataset.

### Alignment with Government Target
Pie chart visualizing the alignment of initiatives with government emission targets.

### Initiative Distribution
Horizontal bar chart showing the top 10 initiatives by frequency.

### GHG Mitigated vs. Cost Saving
Scatter plot to visualize the relationship between GHG mitigated and cost savings, with the size of the points representing the MIRR.

### Monthly GHG Trend by Location
Bar chart showing the total GHG mitigated by different locations.

## Contribution

Contributions to improve the dashboard and extend its functionality are welcome. Please fork the repository, create a new branch, and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
