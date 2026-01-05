import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('medical_examination.csv')
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = df['overweight'].apply(lambda x: 1 if x > 25 else 0)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
def draw_cat_plot():
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='feature', value_name='count')
  df_cat = df_cat.pivot_table(index='feature', columns='cardio', values='count')
  df_cat_long = df_cat.reset_index().melt(id_vars='feature', value_vars=[0, 1], var_name='cardio', value_name='count')
  plt.figure(figsize=(10, 8))
    fig = sns.catplot(x='feature', y='count', hue='cardio', data=df_cat_long, kind='bar', palette='Set1')
    plt.xticks(rotation=90)
    plt.show()
    return fig
def draw_heat_map():
  df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                   (df['height'] >= df['height'].quantile(0.025)) & 
                   (df['height'] <= df['height'].quantile(0.975)) & 
                   (df['weight'] >= df['weight'].quantile(0.025)) & 
                   (df['weight'] <= df['weight'].quantile(0.975))]
corr = df_heat.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
plt.figure(figsize=(12, 10))
fig = sns.heatmap(corr, mask=mask, cmap='coolwarm', vmax=.3, center=0,
                      square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()
  return fig
draw_cat_plot()
draw_heat_map()

mask = np.triu(np.ones_like(corr, dtype=bool))
