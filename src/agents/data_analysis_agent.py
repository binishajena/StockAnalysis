import pandas as pd

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class DataAnalysisAgent:
    def normalize_and_analyze(self, data):
        """
        Normalizes the stock prices and identifies the top performer based on closing prices.
        
        Args:
        - data (pd.DataFrame): DataFrame containing stock data with columns 'Symbol', 'Close', etc.
        
        Returns:
        - pd.DataFrame: DataFrame with normalized values and the top-performing stock.
        """
        # Ensure that the data has the necessary columns
        if 'Symbol' not in data.columns or 'Close' not in data.columns:
            raise ValueError("Data must include 'Symbol' and 'Close' columns.")

        # Normalize 'Close' prices using Min-Max scaling
        data['Normalized Close'] = self.normalize_column(data['Close'])
        
        # Identify the top performer based on normalized close price
        top_performer = data.loc[data['Normalized Close'].idxmax()]

        return data, top_performer
    
    def normalize_column(self, column):
        """
        Normalize a single column using Min-Max Scaling.
        
        Args:
        - column (pd.Series): The column to normalize.
        
        Returns:
        - pd.Series: The normalized column.
        """
        scaler = MinMaxScaler()
        normalized_values = scaler.fit_transform(column.values.reshape(-1, 1))
        return pd.Series(normalized_values.flatten(), index=column.index)

# Usage Example
if __name__ == "__main__":
    data = pd.DataFrame({
        'Symbol': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA'],
        'Close': [150, 310, 2750, 3500, 800]
    })

    analysis_agent = DataAnalysisAgent()
    normalized_data, top_stock = analysis_agent.normalize_and_analyze(data)

    print("Normalized Data:")
    print(normalized_data)
    print("\nTop Performer:")
    print(top_stock)
