import numpy as np
import pandas as pd
import math

from .column import Column

# # Example usage:
# # Prepare input data:
# column_X = [1, 2, 3, 4, 5]
# column_Y = [5, 4, 3, 2, 1]
# chart_type = 'scatter'

# # How to use it:
# feature_extractor = Features(column_X, column_Y, chart_type)
# feature_vector = feature_extractor.calculate_features()
# print(feature_vector)

class Features:
    """
    This part is used for generating the feature vector.

        Attributes:
            x(list): Column X.
            y(list): Column Y.
            chart_type: 'bar', 'pie', 'line', or 'scatter'.
        
        Returns:
            List containing 14 features:
            [
                the number of distinct values in column x,
                the number of tuples in column x,
                the ratio of unique values in column x,
                the max value in column x,
                the min value in column x,
                the data type of column x,
                the number of distinct values in column y,
                the number of tuples in column y,
                the ratio of unique values in column y,
                the max value in column y,
                the min value in column y,
                the data type of column y,
                the correlation of two columns,
                the visualization type
            ]
    """
    # Modifed Features to take 2 Column objects which contain name: str, values: list of values, and type: str
    def __init__(self, x: Column, y: Column, chart_type):
        self.x = x
        self.y = y
        # Jason added
        self.x_col_type = x.type
        self.y_col_type = y.type
        self.chart_type = chart_type

    def calculate_features(self):
        
        x = self.x.values
        y = self.y.values

        # Features for column X
        d_x = len(set(x))
        len_x = len(x)
        r_x = d_x / len_x if len_x > 0 else 0
        max_x = max(x) if len_x > 0 else None
        min_x = min(x) if len_x > 0 else None
        T_x = self.x_col_type #self.get_column_type(self.x)

        # Features for column Y
        d_y = len(set(y))
        len_y = len(y)
        r_y = d_y / len_y if len_y > 0 else 0
        max_y = max(y) if len_y > 0 else None
        min_y = min(y) if len_y > 0 else None
        T_y = self.y_col_type #self.get_column_type(self.y)

        # Correlation between X and Y
        correlation_x_y = self.calculate_correlation(x, y)

        # Create the feature vector
        feature_vector = [
            d_x, len_x, r_x, max_x, min_x, T_x,
            d_y, len_y, r_y, max_y, min_y, T_y,
            correlation_x_y, self.chart_type
        ]

        return feature_vector

    def get_column_type(self, column):
        """
        Determine the data type of a column using pandas.
        """
        dtype = pd.Series(column).dtype.name
        if 'int' in dtype or 'float' in dtype:
            return 'Numerical'
        elif 'datetime' in dtype:
            return 'Temporal'
        else:
            return 'Categorical'

    def calculate_correlation(self, column_x, column_y):
        """
        Calculate the correlation between two columns.
        """
        if not column_x or not column_y:
            return 0  # If any of the columns is empty, return 0

        data1 = column_x
        data2 = column_y
        log_data1 = log_data2 = []

        # Check if the columns are categorical. If true, return 0.
        if self.get_column_type(column_x) == 'Categorical' or self.get_column_type(column_y) == 'Categorical':
            return 0

        # Check if the columns have positive values for logarithmic transformations
        if self.get_column_type(column_x) != 'Temporal' and min(column_x) > 0:
            log_data1 = list(map(math.log, data1))
        if self.get_column_type(column_y) != 'Temporal' and min(column_y) > 0:
            log_data2 = list(map(math.log, data2))


        result = 0
        # Calculate and compare correlation
        try:
            result = abs(np.corrcoef(data1, data2)[0, 1])  # Linear correlation
        except Exception as e:
            result = 0

        # Exponential correlation
        if log_data2:
            try:
                r = abs(np.corrcoef(data1, log_data2)[0, 1])
                if r > result:
                    result = r
            except Exception as e:
                result = 0

        # Logarithmic correlation
        if log_data1:
            try:
                r = abs(np.corrcoef(log_data1, data2)[0, 1])
                if r > result:
                    result = r
            except Exception as e:
                result = 0

        # Power correlation
        if log_data1 and log_data2:
            try:
                r = abs(np.corrcoef(log_data1, log_data2)[0, 1])
                if r > result:
                    result = r
            except Exception as e:
                result = 0

        if not -1 <= result <= 1:
            result = 0

        return result