import pandas as pd

csv_t = pd.read_csv('data.csv')

csv_t = pd.DataFrame(csv_t.day.str.split(':', 12).tolist(), columns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])

print(csv_t)
csv_t.to_csv('data_s.csv', encoding="utf-8-sig")
print(csv_t.shape)