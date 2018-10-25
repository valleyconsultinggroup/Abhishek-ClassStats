import json
import requests
from scipy.stats import norm

#Currrently gets cs70 course grades
#Looking to generalize
def get_grade_distribution():
	response = requests.get("https://www.berkeleytime.com/grades/sections/355888&361043&361044&365180&368533&380435&349014&354277&371872&350604&362159&362160&366943&352898&370016&373756&375708&351801&377253&357444&359466&363587/")
	response = json.loads(response.text)
	return response

grades = ["A+", "A", "A-", "B+", "B"] 
dist = get_grade_distribution()
for grade in grades:
	low_percentile = dist[grade]['percentile_low']
	high_percentile = dist[grade]['percentile_high']

	low_SD = norm.ppf(low_percentile)
	high_SD = norm.ppf(high_percentile)

	print(f"To get a grade of {grade}, you must be between {low_SD} and {high_SD} SD.")
	

