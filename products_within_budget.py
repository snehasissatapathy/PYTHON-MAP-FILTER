"""
## 3. Products Within Budget Report  *(Medium)*

=================================================
PRODUCTS WITHIN BUDGET REPORT
=================================================

Problem Statement:
You are given a LIST of TUPLES, where each
tuple represents a product:
        (product_name, price)

Write a Python program that builds a REPORT
DICTIONARY in the following form:

   {
     "within_budget":  [list of (name, price) tuples],
     "over_budget":    [list of (name, price) tuples],
     "categories":     {
                         "cheap":    set of names with price <  50,
                         "moderate": set of names with 50 <= price <= 200,
                         "costly":   set of names with price >  200
                       },
     "cheapest":       (name, price),
     "costliest":      (name, price)
   }

-------------------------------------------------
Input Example:
products = [
   ("Pen",    10),
   ("Book",   150),
   ("Bag",    500),
   ("Pencil", 5),
   ("Lamp",   300),
   ("Mug",    80),
]
budget = 200

Output Example:
{
  'within_budget': [('Pen',10), ('Book',150),
                    ('Pencil',5), ('Mug',80)],
  'over_budget':   [('Bag',500), ('Lamp',300)],
  'categories': {
      'cheap':    {'Pen', 'Pencil'},
      'moderate': {'Book', 'Mug'},
      'costly':   {'Bag', 'Lamp'}
  },
  'cheapest':  ('Pencil', 5),
  'costliest': ('Bag', 500)
}

-------------------------------------------------
Explanation:
Iterate once through the product list and
classify every item:
   price <  50  -> cheap
   50..200      -> moderate
   price > 200  -> costly
Compare each price to the budget to split it
into within/over budget. While iterating, also
remember the smallest and largest prices seen
so far to find the cheapest and costliest
products.
=================================================

"""
def build_report(products, budget):
    report = {
        "within_budget": [],
        "over_budget": [],
        "categories": {
            "cheap": set(),
            "moderate": set(),
            "costly": set()
        }
    }

    for name, price in products:
        # Budget classification
        if price <= budget:
            report["within_budget"].append((name, price))
        else:
            report["over_budget"].append((name, price))
        if price < 50:
            report["categories"]["cheap"].add(name)
        elif 50 <= price <= 200:
            report["categories"]["moderate"].add(name)
        else:
            report["categories"]["costly"].add(name)
    report["cheapest"] = min(products, key=lambda x: x[1])
    report["costliest"] = max(products, key=lambda x: x[1])

    return report
products = [
    ("Pen", 20),
    ("Notebook", 80),
    ("Bag", 350),
    ("Bottle", 120),
    ("Pencil", 10)
]

budget = 100
result = build_report(products, budget)

print(result)