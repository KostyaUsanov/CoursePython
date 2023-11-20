def find_common_items(last_week_purchases, current_week_purchases):
    a = list(set(last_week_purchases).intersection(current_week_purchases))
    a.sort()
    return a


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']


c = find_common_items(last_week_items, current_week_items)

print(f"Общие товары: {c}")  # TODO Распечатайте общие товары
