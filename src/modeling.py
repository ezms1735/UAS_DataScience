from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


# Baseline Model
def baseline_model(X_train, y_train):
model = LinearRegression()
model.fit(X_train, y_train)
return model


# Advanced Model
def advanced_model(X_train, y_train):
model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)
return model


# Deep Learning Model
def deep_learning_model(input_dim):
model = Sequential([
Dense(128, activation='relu', input_shape=(input_dim,)),
Dropout(0.3),
Dense(64, activation='relu'),
Dropout(0.3),
Dense(1, activation='linear')
])
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
return model