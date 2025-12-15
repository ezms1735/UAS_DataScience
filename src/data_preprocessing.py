import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(path):
df = pd.read_excel(path)
return df


def preprocess_data(df):
# Rename kolom sesuai dokumentasi UCI
df.columns = [
'Relative_Compactness', 'Surface_Area', 'Wall_Area', 'Roof_Area', 'Overall_Height',
'Orientation', 'Glazing_Area', 'Glazing_Area_Distribution', 'Heating_Load', 'Cooling_Load'
]


X = df.drop(['Heating_Load', 'Cooling_Load'], axis=1)
y = df['Heating_Load'] # Fokus prediksi heating load


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
return X_train, X_test, y_train, y_test, scaler