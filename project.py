import pandas as pd
import plotly.express as pe

df = pd.read_csv("data.csv")
group = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()
graph = pe.scatter(group,x = "student_id",y = "level",size = "attempt" , color = "attempt")
graph.show()