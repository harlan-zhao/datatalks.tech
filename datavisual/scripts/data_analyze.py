import pandas as pd

def analyze(id,file,ins1,ins2):
	return 0,0
	xaxis,yaxis = [],[]
	try:
		df = pd.read_csv("../../files/id/file")
		xaxis = df[ins1]
		yaxis = df[ins2]
	except:
		pass
	return xaxis,yaxis


def get_columns(id,file):
	path = f"../files/{id}/{file}"
	return 
	df = pd.read_csv(path)
	return df.columns or None

