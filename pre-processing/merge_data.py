import numpy as np
import pandas as pd

train = pd.read_csv(r"D:\9. ky2nam3\ML\Project_ML\data\train.csv")
test = pd.read_csv(r"D:\9. ky2nam3\ML\Project_ML\data\test.csv")

max_train_id = train['Index'].max()
test['Index'] = test['Index'] + max_train_id + 1

combined = pd.concat([train, test], ignore_index=True)

combined.to_csv(r"D:\9. ky2nam3\ML\Project_ML\data\Airline_Passenger_Satisfaction_data.csv", index=False)
print("Data merged successfully!")