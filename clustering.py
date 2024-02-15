import streamlit as st
import pandas as pd

st.title(':blue[Branch Clustering Model]')
df = pd.read_excel("Performance Table.xlsx")
df_agglo =  pd.read_csv("yhat_agglo.csv")
df_kmeans = pd.read_csv("yhat_kmeans.csv")
df_gmm = pd.read_csv("yhat_gmm.csv")

branch_names = df['Dlv Branch Code_'].unique()
branch_names_t = tuple(branch_names)

option_br = st.selectbox(
   "Select Branch Name/Code.",
   branch_names_t,
   index=None,
   placeholder="Select Branch Name/Code...",
)

st.write('You selected:', option_br)
st.divider()
option_model = st.selectbox(
   "Select AI/ML Model.",
   ("Agglomerative/Hierarchical Clustering", "GMM: Gaussian Mixture Model Clustering", "KNN: K-Nearest Neighbours Clustering"),
   index=None,
   placeholder="Select ML Model...",
)

st.write('You selected:', option_model)

st.divider()
if option_model == "Agglomerative/Hierarchical Clustering":
   branch_cluster_no = int(df_agglo[df_agglo['Name'] == option_br]['cluster']) +1
   st.write("Branch Belongs to Cluster No:", branch_cluster_no)
elif option_model == "GMM: Gaussian Mixture Model Clustering":
   branch_cluster_no = int(df_gmm[df_gmm['Name'] == option_br]['cluster']) +1
   st.write("Branch Belongs to Cluster No:", branch_cluster_no)
else:
   branch_cluster_no = int(df_kmeans[df_kmeans['Name'] == option_br]['cluster']) +1
   st.write("Branch Belongs to Cluster No:", branch_cluster_no)

st.write("Performance of the branch is:")
df_perf = df[df['Dlv Branch Code_'] == option_br]
st.dataframe(df_perf)
st.divider()







