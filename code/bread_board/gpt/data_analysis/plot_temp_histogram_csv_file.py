import csv

def plot_annual_temp_histogram():
    """
    The `weather.csv` has a column TG that contains temperature in Celsius. 
    The file is in a folder called `files`.
    This program creates a histogram for the TG column using [Streamlit](https://streamlit.io/).  
   
    Remarks
    -------
    To create a histogram for the TG column in the `weather.csv` file using
    Streamlit, follow these steps:

    1. Install the necessary packages: streamlit and pandas
    2. Load the "weather.csv" file using pandas
    3. Create a histogram using the streamlit histogram function
    
    Run the script using streamlit run command in the terminal as follows:
    `streamlit run code/bread_board/gpt/plot_histogram_csv_file.py`. You can
    view your Streamlit app in your browser.
    
    """

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load data
    df = pd.read_csv('code/bread_board/files/weather.csv')

    # Calculate the mean temperature
    mean_temp = df['TG'].mean()
    print(f'The mean temperature is: {mean_temp:.2f} C')

    # Plot histogram
    plt.hist(df['TG'], bins=50)
    plt.title('Temperature Histogram')
    plt.xlabel('Temperature (Celsius)')
    plt.ylabel('Count')
    st.pyplot()

if __name__ == "__main__":
    print("Warning: to view this Streamlit app in a browser, run it with the following command: streamlit run plot_annual_temp_csv_file.py")