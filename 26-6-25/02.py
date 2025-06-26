import pandas as pd

data = {
    'std1': {'name': 'karthi', 'branch': 'bio', 'id': '221fa14001', 'skill': ['python', 'c', 'jav']},
    'std2': {'name': 'sdfg', 'branch': 'cse', 'id': '221fa1420', 'skill': ['python', 'c', 'c++']}
}

# Create a Pandas DataFrame from your data
df = pd.DataFrame(data)

# Print the DataFrame to see the result
print(df)