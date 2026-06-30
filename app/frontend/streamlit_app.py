import pandas as pd
import streamlit as st
from app.services.analyst_service import analyst_service
from app.utils.data_loaders import load_data


def show_dataset_info(df):
    c1, c2, c3 = st.columns(3)

    c1.metric("Rows", f"{len(df):,}")
    c2.metric("Columns", len(df.columns))
    c3.metric("Missing Values", int(df.isna().sum().sum()))

    with st.expander("Dataset Preview"):
        st.dataframe(df.head(), width="stretch", hide_index=True)

    with st.expander("Columns and Data types"):
        # st.write(df.dtypes.astype(str))
        st.dataframe(
                pd.DataFrame({"Column": df.columns,"Data Type": df.dtypes.astype(str).values}),
                use_container_width=True,
                hide_index=True
            )



def show_response(response):

    data = response.get("data")
    chart = response.get("chart")
    insight = response.get("insight")

    # SINGLE VALUE RESULT
    if (isinstance(data, pd.DataFrame)and data.shape == (1, 1)):
        value = data.iloc[0, 0]
        label = data.columns[0]

        if isinstance(value, (int, float)):
            value = f"{value:,.2f}"

        st.metric(label, value)

    # NORMAL TABLE RESULT
    elif isinstance(data, pd.DataFrame) and not data.empty:
        if chart is not None:

            table_tab, chart_tab = st.tabs(["📋 Result Table", "📈 Visualization"])

            with table_tab:
                st.dataframe(data,hide_index=True, width='content')

            with chart_tab:
                st.plotly_chart(chart, width='content')
        else:
            st.dataframe(data,hide_index=True, width='content')

    # INSIGHTS
    if insight:
        st.markdown("---")
        st.markdown(insight)


st.set_page_config(
    page_title="AI DA Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Analyst Assistant")
st.caption("Upload a dataset and ask questions...")


if "df" not in st.session_state:
    st.session_state.df = None

if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    uploaded_file = st.file_uploader(
        "Upload CSV or Excel",
        type=["csv", "xlsx", "xls"]
    )

    st.divider()
    new_analysis = st.button('New Analysis', width='stretch')
    if new_analysis:
        keys = ["df", "uploaded_file_name", "messages"]

        for key in keys:
            if key in st.session_state:
                del st.session_state[key]

        st.rerun() 

    st.divider()
    if 'df' in st.session_state:
        st.subheader('Ask Your Question:')
        question = st.chat_input("")
        submit = st.button('Submit', width='stretch')




if uploaded_file:

    if st.session_state.uploaded_file_name != uploaded_file.name:
        st.session_state.df = load_data(uploaded_file)
        st.session_state.uploaded_file_name = uploaded_file.name

    df = st.session_state.df

    show_dataset_info(df)

    st.divider()

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):

            if msg["role"] == "user":
                st.write(msg["content"])

            else:
                show_response(msg["content"])

    # question = st.chat_input("Ask something about your data...")

    if submit or question:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.write(question)

        with st.spinner("Analyzing..."):
            response = analyst_service.analyze(df, question)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):
            show_response(response)

else:
    st.info("Upload a CSV or Excel file to get started.")