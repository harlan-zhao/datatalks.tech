import pandas as pd
import os
from django.conf import settings

def analyze(id,file,ins1,ins2):
	path = os.path.join(settings.BASE_DIR, f"files\\{id}\\{file}")
	xaxis,yaxis = [],[]
	df = pd.read_csv(path)
	Xaxis = ['Python', 'JavaScript', 'C#', 'PHP', 'C++', 'Java']
	Yaxis = [25, 30, 8, 22, 12, 17]
	return Xaxis,Yaxis
	


def get_columns(id,file):
	path = os.path.join(settings.BASE_DIR, f"files\\{id}\\{file}")
	df = pd.read_csv(path)
	columns = list(df.columns.values)
	return columns or None

