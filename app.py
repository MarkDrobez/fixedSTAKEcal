import streamlit as st

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
        bet_sizes[f"{low} - {high}"] = bankroll * percentage
    
    return bet_sizes

# Streamlit App
st.title("Bet Size Calculator")

# User Input
bankroll = st.number_input("Enter your bankroll (€):", min_value=0.0, format="%.2f")

# Display Bet Sizes Automatically
if bankroll > 0:
    bet_sizes = calculate_bet(bankroll)
    st.subheader("Recommended Bet Sizes for Each Odds Range:")
    for odds_range, amount in bet_sizes.items():
        st.write(f"{odds_range}: €{amount:.2f}")
