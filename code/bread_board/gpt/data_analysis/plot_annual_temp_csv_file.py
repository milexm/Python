import csv

def plot_annual_temp():
    """
    The `weather.csv` has a column TG that contains temperature in Celsius.  The
    file is in a folder called `files`.  The "weather.csv" file also has a
    "DATE" column which contains the temperature observation date in the format
    "YYYYMMDD".  This program, using [Streamlit](https://streamlit.io/),
    aggregates the annual temperatures and plots them.  This code will plot the
    annual mean temperature over time, with the year on the x-axis and the
    temperature on the y-axis.
   
    Remarks
    -------
    To create a histogram for the TG column in the "weather.csv" file using
    Streamlit and Python, we can follow these steps:

    1. Install the necessary packages: streamlit and pandas
    2. Load the "weather.csv" file using pandas
    3. Create a histogram using the streamlit histogram function
    
    Run the script using streamlit run command in the terminal as follows:
    `streamlit run code/bread_board/gpt/plot_annual_temp_csv_file.py`. You can
    view your Streamlit app in your browser.
    
    """

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt

    # Set CSV file path 
    csv_file_path = "code/bread_board/files/stockholm_weather.csv" 
    
    # Read the data from the CSV file
    data = pd.read_csv(csv_file_path)

    # Convert DATE column to datetime format
    data["DATE"] = pd.to_datetime(data["DATE"], format="%Y%m%d")

    # Group the data by year and compute the mean temperature
    annual_temps = data.groupby(data["DATE"].dt.year)["TG"].mean()

    # Plot the data
    plt.plot(annual_temps.index, annual_temps.values)

    # Set the plot title and axis labels
    plt.title("Annual Mean Temperature")
    plt.xlabel("Year")
    plt.ylabel("Temperature (Celsius)")

    # Display the plot using Streamlit
    st.pyplot()


if __name__ == "__main__":

    print("Warning: to view this Streamlit app in a browser, run it with the following command: streamlit run plot_annual_temp_csv_file.py")