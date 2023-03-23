import csv

def example():
    """
    Create a histogram for the TG column using Streamlit and Python. The
    "weather.csv" has a column TG that contains temperature in Celsius. The file
    is in a folder called "files". 
   
    Remarks
    -------
    To create a histogram for the TG column in the "weather.csv" file using
    Streamlit and Python, we can follow these steps:

    1. Install the necessary packages: streamlit and pandas
    2. Load the "weather.csv" file using pandas
    3. Create a histogram using the streamlit histogram function
    
    Run the script using streamlit run command in the terminal as follows:
    `streamlit run code/bread_board/gpt/plot_histogram_csv_file.py`, You can now
    view your Streamlit app in your browser.
    
    """

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load data
    df = pd.read_csv('code/bread_board/files/weather.csv')

    # Plot histogram
    plt.hist(df['TG'], bins=50)
    plt.title('Temperature Histogram')
    plt.xlabel('Temperature (Celsius)')
    plt.ylabel('Count')
    st.pyplot()

if __name__ == "__main__":
    example()