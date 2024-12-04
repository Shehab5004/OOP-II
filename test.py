
import pandas as pd
from scipy.stats import skew, kurtosis
import statistics
data = {"year": [2010 , 2011 , 2012 , 2010 , 2011 , 2012 , 2010 , 2011 , 2012 ],
        "team": ["FCBarcelona", "FCBarcelona", "FCBarcelona", "RMadrid", "RMadrid", "RMadrid", "ValenciaCF", "ValenciaCF","ValenciaCF"],
        "wins": [30, 28, 32, 29, 32, 26, 21, 17, 19], 
        "draws": [6, 7, 4, 5, 4, 7, 8, 10, 8], 
        "losses": [2, 3, 2, 4, 2, 5, 9, 11, 11]}

df = pd.DataFrame(data, columns = ["year","team","wins","draws","losses"])

print(df)

a = statistics.mean(df["wins"])
print(a)

c = statistics.mean(df["draws"])
d = statistics.stdev(df["wins"])
e = skew(df["losses"])
f = kurtosis(df["draws"])

print(c)
print(d)
print(e)
print(f)


"""
x=[14.6,24.3,24.9,27,27.2,27.4,28.2,28.8,29.9,30.7,31.5,31.6,32.3,32.8,33.3,33.6,34.3,36.9,38.3,44]
import statistics
import pandas
import numpy
# Using statistics module
statistics.quantiles(x,n=4) # Returns 3 quartiles
statistics.mean(x)
statistics.stdev(x)
(x[1]-statistics.mean(x))/statistics.stdev(x) #zscore for the 2nd obs, x[1]=24.3
statistics.median(x)
statistics.mode(x)
statistics.harmonic_mean(x)
statistics.geometric_mean(x)
"""