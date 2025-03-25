import streamlit as st
import math

# Function to calculate bet sizes based on bankroll
def calculate_bet(bankroll):
    odds_ranges = {
        (1.01, 1.60): 0.025,
        (1.61, 1.90): 0.02,
        (1.91, 2.20): 0.015,
        (2.21, 2.80): 0.01,
        (2.81, 4.00): 0.0075,
    }
    
    bet_sizes = {}
    for (low, high), percentage in odds_ranges.items():
        bet_amount = math.ceil(bankroll * percentage)  # Round up to the nearest whole number
        bet_sizes[f"{low:.2f} - {high:.2f}"] = bet_amount
    
    return bet_sizes

# Streamlit App UI
st.set_page_config(page_title="Bet Size Calculator", page_icon="🎲", layout="centered")
st.title("🎯 Bet Size Calculator")
st.markdown("Use this tool to calculate your optimal bet sizes based on your bankroll.")

# User Input
st.sidebar.header("Input Settings")
bankroll = st.sidebar.number_input("💰 Enter your bankroll (€):", min_value=0.0, format="%.2f")

# Display Bet Sizes Automatically
if bankroll > 0:
    st.subheader("📊 Recommended Bet Sizes for Each Odds Range:")
    bet_sizes = calculate_bet(bankroll)
    
    st.table({"Odds Range": list(bet_sizes.keys()), "Bet Amount (€)": [f"{amount}" for amount in bet_sizes.values()]})
else:
    st.info("Enter your bankroll to calculate bet sizes.")
