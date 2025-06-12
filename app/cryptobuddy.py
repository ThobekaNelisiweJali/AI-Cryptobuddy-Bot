crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    },
    "Polkadot": {
        "price_trend": "falling",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 5/10
    },
    "Ripple": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "low",
        "sustainability_score": 7/10
    },
    "Litecoin": {
        "price_trend": "falling",
        "market_cap": "low",
        "energy_use": "medium",
        "sustainability_score": 4/10
    }
}

def get_trending_cryptos():
    trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
    if trending:
        return "Trending up cryptos: " + ", ".join(trending)
    else:
        return "No cryptos are currently trending up."

def get_most_sustainable():
    max_score = max([data["sustainability_score"] for data in crypto_db.values()])
    sustainable = [name for name, data in crypto_db.items() if data["sustainability_score"] == max_score]
    return f"The most sustainable crypto(s): {', '.join(sustainable)} with a sustainability score of {max_score*10}/10."

def recommend_long_term():
    candidates = [name for name, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
    if candidates:
        best = max(candidates, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"For long-term growth, consider {best}! It’s trending up with good market cap and sustainability."
    else:
        return "No top picks found for long-term growth based on current data."

def get_sustainability_info(coin):
    coin = coin.title()
    if coin in crypto_db:
        sustainability = crypto_db[coin]["sustainability_score"] * 10
        energy_use = crypto_db[coin]["energy_use"]
        return f"{coin} has a sustainability score of {sustainability}/10 and its energy use is {energy_use}."
    else:
        return f"Sorry, I don't have data on {coin}."

def get_market_cap_info(coin):
    coin = coin.title()
    if coin in crypto_db:
        market_cap = crypto_db[coin]["market_cap"]
        return f"{coin} has a market capitalization that is considered {market_cap}."
    else:
        return f"Sorry, I don't have data on {coin}."

def crypto_buddy_response(user_query):
    user_query = user_query.lower()

    if "trending" in user_query or "trend" in user_query or "up" in user_query:
        response = get_trending_cryptos()

    elif "sustainable" in user_query or "sustainability" in user_query or "eco" in user_query:
        words = user_query.split()
        coins_in_query = [coin for coin in crypto_db.keys() if coin.lower() in words]
        if coins_in_query:
            response = get_sustainability_info(coins_in_query[0])
        else:
            response = get_most_sustainable()

    elif "long-term" in user_query or "long term" in user_query or "recommend" in user_query:
        response = recommend_long_term()

    elif "market cap" in user_query or "market capitalization" in user_query:
        words = user_query.split()
        coins_in_query = [coin for coin in crypto_db.keys() if coin.lower() in words]
        if coins_in_query:
            response = get_market_cap_info(coins_in_query[0])
        else:
            response = "Please specify which crypto you want to know about market cap."

    else:
        response = "Sorry, I didn't understand that. Please ask about trends, sustainability, long-term recommendations, or market cap."

    return response

# Optional: keep this for local console testing
if __name__ == "__main__":
    print("Hi! I'm CryptoBuddy, your friendly crypto advisor. Ask me anything about crypto trends and sustainability!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_query = input("You: ").lower()
        if user_query == "exit":
            print("CryptoBuddy: Goodbye! Stay savvy with your investments! 🚀")
            break
        print(f"CryptoBuddy: {crypto_buddy_response(user_query)}\n")