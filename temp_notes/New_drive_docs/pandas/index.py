# region RESOURCES
# ----------------

# github 
'''
https://github.com/TirendazAcademy/PANDAS-TUTORIAL
https://github.com/pb111/Data-Analysis-with-Pandas/blob/master/Data%20Analysis%20with%20Pandas.ipynb
https://github.com/mrdbourke/zero-to-mastery-ml/blob/master/section-2-data-science-and-ml-tools/introduction-to-pandas.ipynb
https://github.com/Asabeneh/Pandas/blob/main/pandas.ipynb
https://github.com/donnemartin/data-science-ipython-notebooks/blob/master/pandas/pandas.ipynb
'''




# endregion 



# region TOPICS
# -------------





# endregion






# DATAFRAME
'''
.head() 
Displays the first N rows of the DataFrame (default N=5).
df.head(number_of_rows)

.tail()
Displays the last N rows of the DataFrame (default N=5).
df.tail(number_of_rows)

.shape()
Returns a tuple (number of rows, number of columns).
df.shape

.info()
Provides a summary of the DataFrame (column types, non-null counts).
df.info()

.describe()
Returns statistical summary (mean, std, min, etc.) of numerical columns.
df.describe()

.dtypes
Displays the data types of each column.
df.dtypes()

.columns
Returns the column labels.
df.columns()

.isnull()
Returns a DataFrame where each value is True if it is NaN, otherwise False.
df.isnull()

.notnull()
Returns a DataFrame where each value is True if it is not NaN, otherwise False.
df.notnull()

.dropna()
Removes rows or columns with missing values (NaN).
df.dropna(axis=0)  # Removes rows with NaN
df.dropna(axis=1)  # Removes columns with NaN

.fillna()
Fills missing (NaN) values with a specified value.
df.fillna(value_to_be_filled)

.replace() 
Replaces values in the DataFrame with specified values.
df.replace(5, 10)

.rename() 
Renames columns or index labels.
df.rename(columns={'col1': 'new_col1'}, inplace=True)

.sort_values() 
Sorts the DataFrame by one or more columns.
df.sort_values(by='col2', ascending=False)

.sort_index()
Sorts the DataFrame by row index.
df.sort_index(ascending=False)

.set_index()
Sets a column as the index of the DataFrame.
df.set_index('col1', inplace=True)

.reset_index()
Resets the index, turning it into a regular column.
df.reset_index(inplace=True)

.iloc[] 
Accesses rows and columns by integer-location indexing.
df.iloc[1:4, 2:4]

.loc[] 
Accesses rows and columns by label-based indexing.
df.loc[1:3, ['col1', 'col2']]

.at[] 
Fast access to a single element by row label and column label.
df.at[0, 'col1']

.iat[] 
Fast access to a single element by row index and column index.
df.iat[0, 1]

.apply()
Applies a function along a DataFrame axis (rows/columns).
df['col1'].apply(lambda x: x * 2)

.applymap()
Applies a function elementwise to the entire DataFrame.
df.applymap(lambda x: x * 2)

.map()
Maps values in a Series based on a function or dictionary.
df['col1'].map({1: 'A', 2: 'B', 3: 'C'})

.transform()
Applies a function and returns a DataFrame with the same shape.
df['col1'].transform(lambda x: x - 1)

.groupby()
Groups the DataFrame by one or more columns.
df.groupby('col1').sum()

.agg()
Applies aggregation functions to the grouped data.
df.groupby('col1').agg({'col2': 'sum', 'col3': 'mean'})

.merge()
Merges DataFrames based on a common column.

.concat()
Concatenates multiple DataFrames along a particular axis.

.pivot()
Reshapes the DataFrame by turning unique values from a column into new columns.
df.pivot(index='col1', columns='col2', values='col3')

.melt()
Unpivots a DataFrame from wide to long format.
df.melt(id_vars=['col1'], value_vars=['col2', 'col3'])

.drop()
Removes rows or columns by label.
df.drop('col1', axis=1)  # Drops the column 'col1'
df.drop(0, axis=0)  # Drops the row with index 0

.duplicated()
Marks duplicate rows as True.
df.duplicated()

.unique()
Returns unique values in a column.
df['col1'].unique()

.value_counts()
Returns the count of unique values in a column.
df['col1'].value_counts()


.corr()
Computes pairwise correlation between columns.
df.corr()

.corrwith()
Computes correlation with another DataFrame or Series.

.pivot_table()
Creates a pivot table with aggregated data.
df.pivot_table(values='col3', index='col1', columns='col2', aggfunc='sum')

.stack()
Stacks the DataFrame (converts columns to rows).
df.stack()

.unstack()
Unstacks the DataFrame (converts rows to columns).
df.unstack()

.to_csv()
Writes the DataFrame to a CSV file.
df.to_csv('file.csv')

.to_excel()
Writes the DataFrame to an Excel file.
df.to_excel('file.xlsx')

.to_sql()
Writes the DataFrame to a SQL database.
df.to_sql('table_name', con=connection)

.astype()
Converts column data types.
df['col1'] = df['col1'].astype('float')

.query() / .query('col1 > 5 and col2 < 3')
Filters the DataFrame using a query string.

.isin() / df[df['col1'].isin([1, 2, 3])]
Checks if each element in the DataFrame is contained in a list or Series.

.pivot_table()
Creates a pivot table from a DataFrame.
'''

# SERIES 
'''
head()
Returns the first N elements of the Series (default N=5).
series.head(3)

.tail()
Returns the last N elements of the Series (default N=5).
series.tail(2)

.shape
Returns a tuple (number of elements in the Series).
series.shape

.size
Returns the number of elements in the Series.
series.size

.dtype
Returns the data type of the Series.
series.dtype

.index
Returns the index (labels) of the Series.
series.index

.values
Returns the values of the Series as a NumPy array.
series.values

.isnull()
Returns a Series where each element is True if it's NaN, else False.
series.isnull()

.notnull()
Returns a Series where each element is True if it's not NaN, else False.
series.notnull()

.dropna()
Removes NaN values from the Series.
series.dropna()

.fillna()
Replaces NaN values with a specified value.
series.fillna(0)

.replace()
Replaces specified values with other values.
series.replace(1, 10)

.map()
Applies a function, dictionary, or Series to map values in the Series.
series.map({1: 'A', 2: 'B', 3: 'C'})

.apply()
Applies a function along the Series.
series.apply(lambda x: x * 2)

# .applymap()
# Applies a function elementwise (only for DataFrames, but works for Series if you use apply()).
# df.applymap(lambda x: x * 2)

.astype()
Converts the data type of the Series.
series.astype('float')

.unique()
Returns the unique values in the Series.
series.unique()

.nunique()
Returns the number of unique elements in the Series.
series.nunique()

.value_counts()
Returns a Series with counts of unique values.
series.value_counts()

.sort_values()
Sorts the Series in ascending or descending order.
series.sort_values(ascending=False)

.sort_index()
Sorts the Series by its index.
series.sort_index()

.cumsum()
Returns the cumulative sum of the Series.
series.cumsum()

.cumprod()
Returns the cumulative product of the Series.
series.cumprod()

.sum()
Returns the sum of the Series.
series.sum()

.prod()
Returns the product of the Series.
series.prod()

.mean()
Returns the mean (average) of the Series.
series.mean()

.median()
Returns the median of the Series.
series.median()

.min()
Returns the minimum value in the Series.
series.min()

.max()
Returns the maximum value in the Series.
series.max()

.abs()
Returns the absolute values of the Series.
series.abs()

.idxmin()
Returns the index of the minimum value in the Series.
series.idxmin()

.idxmax()
Returns the index of the maximum value in the Series.
series.idxmax()

.shift()
Shifts the values of the Series by a specified number of periods.
series.shift(1)

.diff()
Computes the difference between consecutive elements of the Series.
series.diff()

.corr()
Computes the correlation between the Series and another Series.
series.corr(other_series)

.cov()
Computes the covariance between the Series and another Series.
series.cov(other_series)

.clip()
Limits the values of the Series to within a given range.
series.clip(lower=0, upper=10)

.str (string methods)
Accesses string methods for Series of string values.
series.str.upper()  # Converts all strings to uppercase

.cat (category methods)
Accesses methods for Series of categorical data.
series.cat.codes  # Returns codes for categorical data

.plot()
Plots the Series using Matplotlib (if installed).
series.plot(kind='line')

'''




# region DOUBTS
# -------------
.transform() vs .apply()



# endregion



