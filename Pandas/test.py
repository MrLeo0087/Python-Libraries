# errors='coerce' forces any unconvertible text (like '2100 - 2850') into NaN
house_df['total_sqft'] = pd.to_numeric(house_df['total_sqft'], errors='coerce')