import pandas as pd
import numpy as np
import plotly.offline as plt
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def linear_regression(data, x_var, y_var, visualize=False):
    x_mean = data[x_var].mean()
    y_mean = data[y_var].mean()

    numerator = np.sum((data[x_var] - x_mean) * (data[y_var] - y_mean))
    denominator = np.sum(np.square(data[x_var] - x_mean))

    theta_one = numerator / denominator
    theta_zero = y_mean - theta_one * x_mean

    print("theta zero", theta_zero)
    print("theta_one", theta_one)

    # regressor = LinearRegression()
    # regressor.fit(data[x_var].values.reshape(-1, 1), data[y_var].values.reshape(-1, 1))
    # y_pred = regressor.predict(data[x_var].values.reshape(-1, 1))
    # print("Mean Absolute Error:", np.sqrt(metrics.mean_squared_error(data[y_var].values.reshape(-1, 1), y_pred)))
    #
    # error = np.sqrt(np.sum(np.square(data[y_var] - (theta_zero + theta_one * data[x_var]))) / data[x_var].size)
    # print("Error: ", error)
    #
    # return

    if visualize:
        data_graph = [go.Scatter(
            x=data[x_var],
            y=data[y_var],
            mode='markers',
            name='Original Values'
        ), go.Scatter(
            x=data[x_var],
            y=theta_zero + theta_one * data[x_var],
            name='Predicted Values'
        )]

        data_figure = go.Figure(data_graph)
        data_figure.update_xaxes(title_text='Sq. Ft.')
        data_figure.update_yaxes(title_text='Price')

        plt.plot(data_figure, filename='../output_files/house_price.html')


if __name__ == '__main__':
    data = pd.read_csv('../datasets/kc_house_data.csv')
    linear_regression(data, x_var='sqft_living', y_var='price')
