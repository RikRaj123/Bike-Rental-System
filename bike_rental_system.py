
import pandas as pd
import numpy as np
bike_name=["Kawasaki Ninja 3000","Honda SB Shine","Royal Enfield","Activa 6G"]
bike_milage=[10,100,20,60]
bike_stock=[1,4,2,5]
bikedata={"bike_name":bike_name,"bike_milage":bike_milage,"bike_stock":bike_stock}
df = pd.DataFrame(bikedata)
print(df)
