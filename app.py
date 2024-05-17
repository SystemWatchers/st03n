import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='PTE ST03N DIA ANALYZER')
st.title('Performance Analyzer')
st.subheader('Give me DIA workload from ST03N in excel form')

uploaded_file = st.file_uploader('Choose an XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)

    # Sort the DataFrame by 'Number of Dialog Steps' in descending order and select the top 10
    df_top10 = df.sort_values('Number of Dialog Steps', ascending=False).head(10)

    # Create the bar plot
    # fig = px.bar(
    #     df_top10,
    #     x='Report or Transaction name',
    #     y='Number of Dialog Steps',
    #     color='Number of Dialog Steps',
    #     color_continuous_scale=["green", "red"]
    # )

    # # Display the plot
    # st.subheader('Top 10 - Number of Dialogue Steps')
    # st.plotly_chart(fig)

    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Total Response Time (s)', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Total Response Time (s)',
        color='Total Response Time (s)',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Total Response times')
    st.plotly_chart(fig)

    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Average response Time/Dialog Step (ms)', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Average response Time/Dialog Step (ms)',
        color='Average response Time/Dialog Step (ms)',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Average Response times')
    st.plotly_chart(fig)

    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Total Database Time (s)', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Total Database Time (s)',
        color='Total Database Time (s)',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Total Database Time (s)')
    st.plotly_chart(fig)

    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Ø DB Time (ms)', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Ø DB Time (ms)',
        color='Ø DB Time (ms)',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Average DB Time (ms)')
    st.plotly_chart(fig)

    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Total Sequential Read Time (s)', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Total Sequential Read Time (s)',
        color='Total Sequential Read Time (s)',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Total Sequential Read Time (s)')
    st.plotly_chart(fig)

    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Average Sequential Read Time (ms)', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Average Sequential Read Time (ms)',
        color='Average Sequential Read Time (ms)',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Average Sequential Read Time (ms)')
    st.plotly_chart(fig)


    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Number of Logical Database Changes', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Number of Logical Database Changes',
        color='Number of Logical Database Changes',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Number of Logical Database Changes')
    st.plotly_chart(fig)

    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Average Time for Logical DB Changes (ms)', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Average Time for Logical DB Changes (ms)',
        color='Average Time for Logical DB Changes (ms)',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Average Time for Logical DB Changes (ms)')
    st.plotly_chart(fig)

    # Sort the DataFrame by 'Total Response Time (s)' in descending order and select the top 10
    df_top10 = df.sort_values('Requested Data (KB)', ascending=False).head(10)

    # Create the bar plot
    fig = px.bar(
        df_top10,
        x='Report or Transaction name',
        y='Requested Data (KB)',
        color='Requested Data (KB)',
        color_continuous_scale=["green", "red"]
    )

    # Display the plot
    st.subheader('Top 10 - Highest Requested Data (KB)')
    st.plotly_chart(fig)