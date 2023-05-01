import streamlit as st
#
# st.title("title")
# st.header("header")
# st.subheader("subheader")
# st.text("strealit text")
# st.markdown("## markdown")
#
# st.success("success")
# st.warning("warning")
# st.info("info")
# st.error("error")
# st.exception("exception")
#
# st.write("normal text")
# st.write("## a markdown text")
# st.write(1+2)
# st.write(dir(st))
#
# st.help(range)

import pandas as pd

df=pd.read_csv('iris.csv')
st.subheader("method1")
st.dataframe(df)

st.subheader("method2")
st.dataframe(df.style.highlight_max(axis=0))

st.subheader("method3")
st.table(df)
