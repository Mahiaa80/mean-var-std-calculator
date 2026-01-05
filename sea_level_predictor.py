import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df = pd.read_csv('epa-sea-level.csv')
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
line = slope * df['Year'] + intercept
plt.plot(df['Year'], line, 'r', label=f'Trend line (slope={slope:.2f})')
line_2050 = slope * 2050 + intercept
plt.axvline(x=2050, color='r', linestyle='--', label=f'Prediction for 2050 (level={line_2050:.2f})')
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
line_recent = slope_recent * df_recent['Year'] + intercept_recent
plt.plot(df_recent['Year'], line_recent, 'g--', label=f'Recent trend line (slope={slope_recent:.2f})')
line_recent_2050 = slope_recent * 2050 + intercept_recent
plt.axvline(x=2050, color='g', linestyle='--', label=f'Recent prediction for 2050 (level={line_recent_2050:.2f})')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)
plt.savefig('sea_level_rise.png')
plt.show()
