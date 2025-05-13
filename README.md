Demand Forecasting for a Retail Store
Live streamlit app :
https://codeclaudeinternshipretail-demand-forecasting.streamlit.app/

Overview
This Streamlit app uses Facebook Prophet to forecast the future demand for products in a retail store. It analyzes historical sales data and predicts future demand, providing helpful insights into seasonal trends, forecasts, and model performance.

The app allows you to upload your own sales data or use a default dataset (retail_store_inventory.csv) to make predictions.

Features
Upload Dataset: The app automatically loads retail_store_inventory.csv if available, or asks the user to upload a custom CSV file.
Forecast Horizon: Users can select a forecast horizon (from 7 to 90 days) using a slider.
Forecast Visualization: Displays a plot of the forecasted demand.
Model Evaluation: Shows the Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to evaluate the model's accuracy.
Forecast Data Table: Presents the forecasted demand with uncertainty intervals.

Technologies Used
Python: The main programming language.
Streamlit: For creating the web app interface.
Facebook Prophet: For time series forecasting.
Pandas: For data manipulation and preprocessing.
Matplotlib: For generating forecast plots.
Scikit-learn: For calculating model evaluation metrics (MAE, RMSE).
NumPy: For numerical operations.


Dataset
The dataset used should have the following columns:
Date: The date of each sale (in YYYY-MM-DD format).
Units Sold: The number of units sold on each date.

If you don’t upload a file, the app will use the default file retail_store_inventory.csv.

How to Run
1. Clone the repository
git clone https://github.com/ritikashinde/CodeClaudeInternship_retail-demand-forecasti

3. Install Dependencies
Make sure you have all the required packages by installing them from the requirements.txt:
pip install -r requirements.txt

3. Run the Streamlit app
https://codeclaudeinternshipretail-demand-forecasting.streamlit.app/
This will start a local server, and the app will be available in your browser.

5. Upload or Use Default Dataset
Once the app is running, it will automatically check if retail_store_inventory.csv is present in the directory. If the file is found, it will be used as the default dataset. If the file is not found, the app will prompt you with an error message. You can also upload your own CSV file if you prefer.

6. Set Forecast Horizon
Adjust the forecast horizon by selecting a number of days (from 7 to 90 days) using the slider.

7. View Results
Forecast Plot: The app will display the predicted demand.
Evaluation Metrics: MAE and RMSE values will be shown for evaluating the model.
Forecast Data: A table will display forecasted demand along with the uncertainty intervals.
Example Output
Forecast Plot: A visual representation of the predicted demand for the selected horizon.
Model Evaluation: Displays MAE and RMSE, allowing you to gauge the model's accuracy.
Forecast Table: A table showing the forecasted demand values with lower and upper uncertainty intervals.

Acknowledgments
Facebook Prophet Documentation
Streamlit Documentation
Pandas Documentation
Matplotlib Documentation
