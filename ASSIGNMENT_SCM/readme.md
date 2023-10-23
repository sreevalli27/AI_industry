
# Units Sold Prediction

## Data Preprocessing

The original dataset Traindata.csv was loaded into a Pandas dataframe. The following preprocessing steps were taken:

- Checked for null values and dropped rows with NaNs
- Removed duplicated rows
- Looked at summary statistics and correlations between features
- Removed store_id column due to high multicollinearity (high VIF)

## Exploratory Data Analysis 

The data was explored visually using seaborn heatmap to view correlations. 

Key insights:

- units_sold is positively correlated with total_price and is_featured_sku
- Negative correlation between units_sold and is_display_sku

## Model Building

The data was split into training and test sets with a 80-20 split. The features were scaled using StandardScaler.

The following regression models were evaluated using RMSE and R^2 scores on the test set:

- Linear Regression
- Ridge 
- Lasso
- ElasticNet
- SGD Regressor
- SVR
- KNeighbors Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Random Forest Regressor

KNeighborsRegressor performed the best with lowest RMSE.

Hyperparameter tuning was done for KNeighborsRegressor:

- Tried different n_neighbors values from 1 to 100. 13 neighbors gave minimum RMSE 
- Tried p values from 1 to 5. p=1 gave best performance.

The final model used KNeighborsRegressor with n_neighbors=13 and p=1.

The final RMSE on test set was 39.86.
The final R^2 on test set was  0.57.

## Conclusion

A KNeighborsRegressor model was built to predict the units sold for products based on features like price and whether the product was featured. The model performance was 39.86 as measured by RMSE. The model coefficients were saved and used to make predictions on new unseen data.