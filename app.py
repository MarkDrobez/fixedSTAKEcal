import streamlit as st

# Initialize bankroll
if 'bankroll' not in st.session_state:
    st.session_state.bankroll = 10000.0

st.title('🎯 Optimized Betting Calculator')

# Function to calculate stake
def calculate_stake(odds, bankroll):
    if 1.01 <= odds <= 1.60:
        return bankroll * 0.025
    elif 1.61 <= odds <= 1.90:
        return bankroll * 0.02
    elif 1.91 <= odds <= 2.20:
        return bankroll * 0.015
    elif 2.21 <= odds <= 2.80:
        return bankroll * 0.01
    elif 2.81 <= odds <= 4.00:
        return bankroll * 0.0075
    else:
        return 0

# Input odds
odds = st.number_input('Enter Odds:', min_value=1.01, max_value=4.00, step=0.01, format="%.2f")

# Display calculated stake
stake = calculate_stake(odds, st.session_state.bankroll)

if stake > 0:
    st.success(f'💸 Recommended Stake: €{stake:.2f}')
else:
    st.error('Odds out of range (1.01 - 4.00)')

# Display current bankroll
st.info(f'💰 Current Bankroll: €{st.session_state.bankroll:.2f}')

# Manual bankroll update
new_bankroll = st.number_input('Manually Update Bankroll:', min_value=0.0, step=1.0, format="%.2f")
if st.button('Update Bankroll'):
    st.session_state.bankroll = new_bankroll
    st.success(f'🔄 Bankroll updated manually to: €{st.session_state.bankroll:.2f}')

# Place Bet
if st.button('I Placed This Bet'):
    if stake <= st.session_state.bankroll:
        st.session_state.bankroll -= stake
        st.success(f'📌 Bet placed! New bankroll: €{st.session_state.bankroll:.2f}')
    else:
        st.error('❌ Insufficient funds!')
