import pandas as pd

df1 = pd.read_csv('td_file.csv')
df2 = pd.read_csv('sf_file.csv')

id_col = 'ID'
cols = []
count = 0

def compare(id, r1, r2):
	flag = False
	temp = [id]
	for col in r1.columns:
		if r1[col]==r2[col]:
			continue
		else:
			temp.append(col) 
	cols.append(temp)
	count = count + 1


for row in df1:
	id = row[id_col]
	r1 = row
	r2 = df2.loc[df2[id_col] == id]
	if count < 5:
		compare(id, r1, r2) 
	else:
		break




