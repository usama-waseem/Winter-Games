import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 16)
data = pd.read_csv('WinterGames.csv')
print(data)
print(len(data.columns))
print(len(data))
print(data.isna().sum())
print(data.dtypes)
print(data.describe())


# Create subset for snowboard and alpine skiing, describe two different subsets and have their mean values of age
# Overall
snowboard = data[data['discipline'] == 'Snowboard']
ski = data[data['discipline'] == 'Ski']
print(snowboard.describe())
print(ski.describe())

# 2014 Snowboarding and SKi data
print('2014 Snowboarding and Ski')
snowboard_2014 = snowboard[snowboard['olympics'] == 2014]
ski_2014 = ski[ski['olympics'] == 2014]
print('--Snowboard--\n', snowboard_2014.describe())
print('--Ski--\n', ski_2014.describe())
# --------------------------------------------------------
# 2018 Snowboarding and Ski data
print('2018 Snowboarding and Ski')
snowboard_2018 = snowboard[snowboard['olympics'] == 2018]
ski_2018 = ski[ski['olympics'] == 2018]
print('--Snowboard--\n', snowboard_2018.describe())
print('--Ski--\n', ski_2018.describe())
# --------------------------------------------------------
# 2022 Snowboarding and Ski data
print('2022 Snowboarding and Ski')
snowboard_2022 = snowboard[snowboard['olympics'] == 2022]
ski_2022 = ski[ski['olympics'] == 2022]
print('--Snowboard--\n', snowboard_2022.describe())
print('--Ski--\n', ski_2022.describe())

# Plotting snowboard vs ski based on olympics year
fig, ax = plt.subplots(figsize=(4, 4))
n = 3
r = np.arange(n)
w = 0.25
snowboard_sport = [snowboard_2014['age'].mean(), snowboard_2018['age'].mean(), snowboard_2022['age'].mean()]
ski_sport = [ski_2014['age'].mean(), ski_2018['age'].mean(), ski_2022['age'].mean()]
plt_snowboard = plt.bar(r, snowboard_sport, 0.25, label='Snowboard', color='darkcyan', edgecolor='black',
                        linewidth=1.5)
plt_ski = plt.bar(r+w, ski_sport, 0.25, label='Ski', color='limegreen', edgecolor='black', linewidth=1.5)
plt.xticks(r+w/2, ['2014', '2018', '2022'])
plt.title('Average Age of Snowboard and Ski Athletes')
plt.xlabel('Olympics Year')
plt.ylabel('Average Age of Athletes')
fig.tight_layout()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)
plt.legend(bbox_to_anchor=(1, 1))
for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{round(bar_value, 2):,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
            size=9)


# Creating subsets for gender (female athletes snowboarding & female athletes alpine skiing)
snowbaord_f =snowboard[snowboard['sex'] == 'f']
ski_f = ski[ski['sex'] == 'f']
# print(snowbaord_f.describe())
# print(ski_f.describe())

# 2014 female athletes
print('2014 Female Athletes')
snowboard_2014_f = snowboard_2014[snowboard_2014['sex'] == 'f']
ski_2014_f = ski_2014[ski_2014['sex'] == 'f']
print('--Snowboard--\n', snowboard_2014_f.describe())
print('--Ski--\n', ski_2014_f.describe())
# --------------------------------------------------------
# 2018 female athletes
print('2018 Female Athletes')
snowboard_2018_f = snowboard_2018[snowboard_2018['sex'] == 'f']
ski_2018_f = ski_2018[ski_2018['sex'] == 'f']
print('--Snowboard--\n', snowboard_2018_f.describe())
print('--Ski--\n', ski_2018_f.describe())
# --------------------------------------------------------
# 2022 female athletes
print('2022 Female Athletes')
snowboard_2022_f = snowboard_2022[snowboard_2022['sex'] == 'f']
ski_2022_f = ski_2022[ski_2022['sex'] == 'f']
print('--Snowboard--\n', snowboard_2022_f.describe())
print('--Ski--\n', ski_2022_f.describe())

# Plotting snowboard vs ski based on female athletes
fig, ax = plt.subplots(figsize=(4, 4))
n = 3
r = np.arange(n)
w = 0.25
snowboard_sport_f = [snowboard_2014_f['age'].mean(), snowboard_2018_f['age'].mean(), snowboard_2022_f['age'].mean()]
ski_sport_f = [ski_2014_f['age'].mean(), ski_2018_f['age'].mean(), ski_2022_f['age'].mean()]
plt_snowboard_f = plt.bar(r, snowboard_sport_f, 0.25, label='Female \n Snowboard \n Athletes', color='darkcyan',
                        edgecolor='black', linewidth=1.5)
plt_ski_f = plt.bar(r+w, ski_sport_f, 0.25, label='Female \n Ski Athletes', color='limegreen',
                    edgecolor='black', linewidth=1.5)
plt.xticks(r+w/2, ['2014', '2018', '2022'])
plt.title('Average Age of Female Snowboard and Ski Athletes')
plt.xlabel('Olympics Year')
plt.ylabel('Average Age of Female Athletes')
fig.tight_layout()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)
plt.legend(bbox_to_anchor=(1, 1))
for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{round(bar_value, 2):,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
            size=9)



# Creating subsets for gender (male athletes snowboarding & male athletes alpine skiing)
snowboard_m = snowboard[snowboard['sex'] == 'm']
ski_m = ski[ski['sex'] == 'm']
# print(snowboard_m.describe())
# print(ski_m.describe())

# 2014 male athletes
print('2014 Male Athletes')
snowboard_2014_m = snowboard_2014[snowboard_2014['sex'] == 'm']
ski_2014_m = ski_2014[ski_2014['sex'] == 'm']
print('--Snowboard--\n', snowboard_2014_m.describe())
print('--Ski--\n', ski_2014_m.describe())
# --------------------------------------------------------
# 2018 male athletes
print('2018 Male Athletes')
snowboard_2018_m = snowboard_2018[snowboard_2018['sex'] == 'm']
ski_2018_m = ski_2018[ski_2018['sex'] == 'm']
print('--Snowboard--\n', snowboard_2018_m.describe())
print('--Ski--\n', ski_2018_m.describe())
# --------------------------------------------------------
# 2022 male athletes
print('2022 Male Athletes')
snowboard_2022_m = snowboard_2022[snowboard_2022['sex'] == 'm']
ski_2022_m = ski_2022[ski_2022['sex'] == 'm']
print('--Snowboard--\n', snowboard_2022_m.describe())
print('--Ski--\n', ski_2022_m.describe())

# Plotting snowboard vs ski based on male athletes
fig, ax = plt.subplots(figsize=(4, 4))
n = 3
r = np.arange(n)
w = 0.25
snowboard_sport_m = [snowboard_2014_m['age'].mean(), snowboard_2018_m['age'].mean(), snowboard_2022_m['age'].mean()]
ski_sport_m = [ski_2014_m['age'].mean(), ski_2018_m['age'].mean(), ski_2022_m['age'].mean()]
plt_snowboard_m = plt.bar(r, snowboard_sport_m, 0.25, label='Male Snowboard \n Athletes', color='darkcyan',
                        edgecolor='black', linewidth=1.5)
plt_ski_m = plt.bar(r+w, ski_sport_m, 0.25, label='Male Ski \n Athletes', color='limegreen',
                    edgecolor='black', linewidth=1.5)
plt.xticks(r+w/2, ['2014', '2018', '2022'])
plt.title('Average Age of Male Snowboard and Ski Athletes')
plt.xlabel('Olympics Year')
plt.ylabel('Average Age of Male Athletes')
fig.tight_layout()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)
plt.legend(bbox_to_anchor=(1, 1))
for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{round(bar_value, 2):,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
            size=9)


# Plotting Count Male and Female athletes of Snowboard
fig, ax = plt.subplots(figsize=(4, 4))
n = 3
r = np.arange(n)
w = 0.25
snowboard_male = [snowboard_2014_m['sex'].count(), snowboard_2018_m['sex'].count(), snowboard_2022_m['sex'].count()]
snowboard_female = [snowboard_2014_f['sex'].count(), snowboard_2018_f['sex'].count(), snowboard_2022_f['sex'].count()]
plt_snowboard_math = plt.bar(r, snowboard_male, 0.25, label='Male Snowboard\nAthletes', color='lightskyblue',
                        edgecolor='black', linewidth=1.5)
plt_snowboard_fath = plt.bar(r+w, snowboard_female, 0.25, label='Female\nSnowboard Athletes', color='violet',
                    edgecolor='black', linewidth=1.5)
plt.xticks(r+w/2, ['2014', '2018', '2022'])
plt.title('Number of Male and Female Snowboard Athletes')
plt.xlabel('Olympics Year')
plt.ylabel('Athletes Count')
fig.tight_layout()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)
plt.legend(bbox_to_anchor=(1, 1))
for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{bar_value:,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
            size=9)


# Plotting Male and Female athletes of Ski
fig, ax = plt.subplots(figsize=(4, 4))
n = 3
r = np.arange(n)
w = 0.25
ski_male = [ski_2014_m['sex'].count(), ski_2018_m['sex'].count(), ski_2022_m['sex'].count()]
ski_female = [ski_2014_f['sex'].count(), ski_2018_f['sex'].count(), ski_2022_f['sex'].count()]
plt_ski_math = plt.bar(r, ski_male, 0.25, label='Male Ski \n Athletes', color='lightskyblue',
                        edgecolor='black', linewidth=1.5)
plt_ski_fath = plt.bar(r+w, ski_female, 0.25, label='Female Ski \n Athletes', color='violet',
                    edgecolor='black', linewidth=1.5)
plt.xticks(r+w/2, ['2014', '2018', '2022'])
plt.title('Number of Male and Female Ski Athletes')
plt.xlabel('Olympics Year')
plt.ylabel('Athletes Count')
fig.tight_layout()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)
plt.legend(bbox_to_anchor=(1, 1))
for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{bar_value:,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
            size=9)
plt.show()

