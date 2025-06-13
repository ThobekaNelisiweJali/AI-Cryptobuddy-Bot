crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    },
    "Polkadot": {
        "price_trend": "falling",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7 / 10
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 5 / 10
    },
    "Ripple": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "low",
        "sustainability_score": 7 / 10
    },
    "Litecoin": {
        "price_trend": "falling",
        "market_cap": "low",
        "energy_use": "medium",
        "sustainability_score": 4 / 10
    }
}

def get_trending_cryptos():
    rising = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
    falling = [c for c in crypto_db if crypto_db[c]["price_trend"] == "falling"]

    response = ""
    if rising:
        response += "🔼 Top-performing cryptos: " + ", ".join(rising) + ". "
    if falling:
        response += "🔽 Least-performing cryptos: " + ", ".join(falling) + "."
    return response or "No clear trends available right now."

def get_most_sustainable():
    max_score = max([data["sustainability_score"] for data in crypto_db.values()])
    sustainable = [name for name, data in crypto_db.items() if data["sustainability_score"] == max_score]
    return f"🌱 Most sustainable crypto(s): {', '.join(sustainable)} with a score of {max_score*10}/10."

def recommend_long_term():
    candidates = [name for name, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
    if candidates:
        best = max(candidates, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"📈 Long-term pick: {best}. It's rising, has a high market cap, and decent sustainability."
    else:
        return "No strong long-term growth candidates found right now."

def get_sustainability_info(coin):
    coin = coin.title()
    if coin in crypto_db:
        score = crypto_db[coin]["sustainability_score"] * 10
        energy = crypto_db[coin]["energy_use"]
        return f"{coin} ⚡ Energy: {energy}, 🌱 Sustainability: {score}/10."
    return f"Sorry, I don't have sustainability info for {coin}."

def get_market_cap_info(coin):
    coin = coin.title()
    if coin in crypto_db:
        return f"{coin} has a market cap that is considered {crypto_db[coin]['market_cap']}."
    return f"Sorry, no market cap info for {coin}."

def get_market_facts():
    total = len(crypto_db)
    efficient = [c for c in crypto_db if crypto_db[c]["energy_use"] == "low"]
    volatile = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising" or crypto_db[c]["price_trend"] == "falling"]

    return (
        f"📊 Crypto Market Stats:\n"
        f"• Total coins tracked: {total}\n"
        f"• Energy-efficient: {', '.join(efficient)}\n"
        f"• Volatile assets: {', '.join(volatile)}\n"
        f"• Fear & Greed Index: {simulate_fear_greed()}"
    )

def simulate_fear_greed():
    import random
    index = random.randint(20, 80)
    mood = "Fear 😟" if index < 40 else "Greed 😄" if index > 60 else "Neutral 😐"
    return f"{index}/100 — {mood}"

def crypto_buddy_response(user_query):
    user_query = user_query.lower().strip()

    greetings = ["hello", "hi", "hey", "howdy"]
    if any(g in user_query for g in greetings):
        return "👋 Hey there! I'm CryptoBuddy. Ask me about trends, market caps, sustainability, or market stats!"

    if "trend" in user_query or "trending" in user_query or "up" in user_query or "falling" in user_query:
        return get_trending_cryptos()

    if "sustainable" in user_query or "sustainability" in user_query or "eco" in user_query:
        coin = next((c for c in crypto_db if c.lower() in user_query), None)
        return get_sustainability_info(coin) if coin else get_most_sustainable()

    if "long-term" in user_query or "long term" in user_query or "recommend" in user_query:
        return recommend_long_term()

    if "market cap" in user_query or "market capitalization" in user_query:
        coin = next((c for c in crypto_db if c.lower() in user_query), None)
        return get_market_cap_info(coin) if coin else "Which coin's market cap would you like to know?"

    if "fact" in user_query or "stats" in user_query or "info" in user_query:
        return get_market_facts()

    return (
        "❓ I'm not sure how to help with that. Try asking about:\n"
        "- Which coins are trending?\n"
        "- Most sustainable coin?\n"
        "- Long-term investment suggestion?\n"
        "- Market cap of Ethereum?\n"
        "- General crypto facts."
    )
