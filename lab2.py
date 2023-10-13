import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
data = pd.read_csv('googleplaystore.csv', sep=';', encoding='utf8')

# 1. ТОП-10 додатків за завантаженнями
top_10_downloads = data.nlargest(10, 'Installs')
plt.figure(figsize=(10, 5))
plt.barh(top_10_downloads['App'], top_10_downloads['Installs'])
plt.xlabel('Завантаження')
plt.ylabel('Додаток')
plt.title('ТОП-10 додатків за завантаженнями')
plt.gca().invert_yaxis()
plt.show()

# 2. Порівняння середнього рейтингу безкоштовних та платних додатків в категорії "Ігри"
games = data[data['Category'] == 'GAME']
free_games = games[games['Type'] == 'Free']
paid_games = games[games['Type'] == 'Paid']

avg_rating_free = free_games['Rating'].mean()
avg_rating_paid = paid_games['Rating'].mean()

if avg_rating_free > avg_rating_paid:
    print('Безкоштовні ігри мають більший середній рейтинг.')
else:
    print('Платні ігри мають більший середній рейтинг.')

# 3. Кругова діаграма розподілу частки додатків за віковими групами
content_rating_counts = data['Content Rating'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(content_rating_counts, labels=content_rating_counts.index, autopct='%1.1f%%')
plt.title('Розподіл додатків за віковими групами')
plt.show()

# 4. Список додатків, які не оновлювалися більше 7 років
current_year = 2023
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
outdated_apps = data[data['Last Updated'].dt.year < current_year - 7]
print('Список додатків, які не оновлювалися більше 7 років:')
print(outdated_apps['App'])

# 5. Порівняння середньої ваги безкоштовних додатків із довільних 5 категорій
categories = data['Category'].value_counts().head(5).index
avg_sizes = []

for category in categories:
    category_data = data[data['Category'] == category]
    free_apps = category_data[category_data['Type'] == 'Free']
    avg_size = free_apps['Size'].mean()
    avg_sizes.append(avg_size)

plt.figure(figsize=(10, 5))
plt.bar(categories, avg_sizes)
plt.xlabel('Категорія')
plt.ylabel('Середня вага (МБ)')
plt.title('Середня вага безкоштовних додатків у довільних 5 категоріях')
plt.show()