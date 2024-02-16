import streamlit as st
import pandas as pd

st.title(':blue[Branch Clustering Model]')
############################################################
st.divider()

option_model = st.selectbox(
   "Select AI/ML Model...",
   ("Agglomerative/Hierarchical Clustering", "GMM: Gaussian Mixture Model Clustering", "KNN: K-Nearest Neighbours Clustering"),
   index=None,
   placeholder="Select ML Model...",
)
st.write('You selected:', option_model)
############################################################

st.header("Branch Details:")
st.divider()

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

if option_model == "Agglomerative/Hierarchical Clustering":
   branch_cluster_no = 5 -  int(df_agglo[df_agglo['Name'] == option_br]['cluster'])
   st.write("Branch Belongs to Cluster No:", branch_cluster_no)
elif option_model == "GMM: Gaussian Mixture Model Clustering":
   branch_cluster_no = 5 - int(df_gmm[df_gmm['Name'] == option_br]['cluster']) 
   st.write("Branch Belongs to Cluster No:", branch_cluster_no)
else:
   branch_cluster_no = 5 -  int(df_kmeans[df_kmeans['Name'] == option_br]['cluster']) 
   st.write("Branch Belongs to Cluster No:", branch_cluster_no)

st.write("Performance of the branch is:")
df_perf = df[df['Dlv Branch Code_'] == option_br]
st.dataframe(df_perf)
st.divider()

st.header("Performance Based Clusters:")

#option_model_1 = st.selectbox(
#   "Select AI/ML Model.",
#   ("Agglomerative/Hierarchical Clustering", "GMM: Gaussian Mixture Model Clustering", "KNN: K-Nearest Neighbours Clustering"),
#   index=None,
#   placeholder="Select ML Model...",
#)

df_agglo_fin = df.copy()
df_agglo_fin['cluster']  = df_agglo['cluster']
df_gmm_fin = df.copy()
df_gmm_fin['cluster']  = df_gmm['cluster']
df_kmeans_fin = df.copy()
df_kmeans_fin['cluster']  = df_kmeans['cluster']

Cluster_no = st.slider('Choose Cluster Number', 1, 5, 1)
st.write("Chosen ", Cluster_no, 'Cluster Number...')
st.write("Showing Branches with belong to the cluster")

if option_model  == "Agglomerative/Hierarchical Clustering":
   st.write("mmmmm")
   st.dataframe(df_agglo_fin[df_agglo_fin['cluster'] == (5 - Cluster_no)])
if option_model  == "GMM: Gaussian Mixture Model Clustering":
   st.dataframe(df_gmm_fin[df_gmm_fin['cluster'] == (5 - Cluster_no)])
if option_model  == "KNN: K-Nearest Neighbours Clustering":
   st.dataframe(df_kmeans_fin[df_kmeans_fin['cluster'] == (5 - Cluster_no)])
#else:
# pass
   
st.divider()
                





