import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
percentiles = df['value'].quantile([0.025, 0.975])
df = df[(df['value'] >= percentiles[0]) & (df['value'] <= percentiles[1])]
def draw_line_plot():
  df_line = df.copy()
  plt.figure(figsize=(12, 6))
    plt.plot(df_line.index, df_line['value'], marker='o')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    plt.show()
    return plt
def draw_bar_plot():
   df_bar = df.copy()
  df_bar = df_bar.resample('M').mean()
plt.figure(figsize=(12, 6))
    plt.bar(df_bar.index, df_bar['value'])
    plt.title('Monthly Average Page Views per Year')
    plt.xlabel('Year')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=45)
    plt.legend(title='Months')
    plt.tight_layout()
    plt.show()
    return plt
def draw_box_plot():
  df_box = df.copy()
  plt.figure(figsize=(12, 6))
  plt.subplot(1, 2, 1)
    sns.boxplot(data=df_box['value'].resample('Y'))
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df_box['value'].resample('M'))
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    plt.tight_layout()
    plt.show()
    return plt
draw_line_plot()
draw_bar_plot()
draw_box_plot()
