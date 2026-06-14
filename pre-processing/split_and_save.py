import os
import pandas as pd
from sklearn.model_selection import train_test_split

input_path = r"D:\9. ky2nam3\ML\Project_ML\data\preprocessed_data.csv"

output_dir = r"D:\9. ky2nam3\ML\Project_ML\data\original_data"
os.makedirs(output_dir, exist_ok=True)


df = pd.read_csv(input_path)


ratios = {
    "4_1": 0.2,
    "7_3": 0.3,
    "6_4": 0.4
}

file_names = {
    "4_1": ("train41.csv", "test41.csv"),
    "7_3": ("train73.csv", "test73.csv"),
    "6_4": ("train64.csv", "test64.csv")
}

for ratio, test_size in ratios.items():
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=42, shuffle=True)

    train_name, test_name = file_names[ratio]
    train_df.to_csv(os.path.join(output_dir, train_name), index=False)
    test_df.to_csv(os.path.join(output_dir, test_name), index=False)

print("Đã lưu 6 file train/test tương ứng vào thư mục:", output_dir)
