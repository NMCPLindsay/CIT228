def sandwich_order(name, **sandwich):
    sandwich['name']=name
    return sandwich

sandwich_ingredients=sandwich_order('Reuben', ingredients=['Corned Beef', 'Saurkraut', 'Swiss Cheese', 'Thousand-Island'])
print(sandwich_ingredients)
sandwich_ingredients=sandwich_order('Reuben', ingredients=['Corned Beef', 'Saurkraut', 'Swiss Cheese', 'Thousand-Island'], cut='half')
print(sandwich_ingredients)
sandwich_ingredients=sandwich_order('Reuben', ingredients=['Corned Beef', 'Saurkraut', 'Swiss Cheese', 'Thousand-Island'], cut='X', Toasted='Yes')
print(sandwich_ingredients)
