def affordable(products, budget):
    for product in products:
        if product["price"] <= budget:
            yield product


def best_rated(products):
    return max(products, key=lambda p: p["rating"])


def total_price(products):
    return sum(p["price"] for p in products)
