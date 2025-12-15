from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np


def evaluate_model(model, X_test, y_test, model_type='baseline'):
if model_type == 'deep_learning':
preds = model.predict(X_test).flatten()
else:
preds = model.predict(X_test)


mse = mean_squared_error(y_test, preds)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)


print(f"===== {model_type.upper()} MODEL EVALUATION =====")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R² Score: {r2:.4f}\n")


return {'MSE': mse, 'RMSE': rmse, 'MAE': mae, 'R2': r2}