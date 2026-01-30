def compare_prices(product_name):
    data = [
        {"platform": "Amazon", "price": 2499, "link": "https://amazon.in"},
        {"platform": "Flipkart", "price": 2599, "link": "https://flipkart.com"},
        {"platform": "Myntra", "price": 2749, "link": "https://myntra.com"}
    ]

    data = sorted(data, key=lambda x: x["price"])
    return data
