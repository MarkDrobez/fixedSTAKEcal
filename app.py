import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize bankroll
if 'bankroll' not in st.session_state:
    st.session_state.bankroll = 10000.0

# Initialize bet log
if 'bet_log' not in st.session_state:
    st.session_state.bet_log = pd.DataFrame(columns=['Timestamp', 'Odds', 'Stake', 'Remaining Bankroll'])

st.title('🎯 Optimized Betting Calculator')

col1, col2 = st.columns([2, 1])

# Left column (Bet Log)
with col1:
    st.subheader('📋 Bet Log')
    st.dataframe(st.session_state.bet_log, height=350)

# Right column (Calculator and buttons)
with col2:
    st.info(f'💰 Bankroll: €{st.session_state.bankroll:.2f}')

    # Function to calculate stake
    def calculate_stake(odds, bankroll):
        if 1.40 <= odds <= 1.60:
            return round(bankroll * 0.025, 1)
        elif 1.61 <= odds <= 1.90:
            return round(bankroll * 0.02, 1)
        elif 1.91 <= odds <= 2.20:
            return round(bankroll * 0.015, 1)
        elif 2.21 <= odds <= 2.80:
            return round(bankroll * 0.01, 1)
        elif 2.81 <= odds <= 4.00:
            return round(bankroll * 0.0075, 1)
        else:
            return 0

    # Input odds
    odds = st.number_input('Enter Odds:', min_value=1.40, max_value=4.00, step=0.01, format="%.2f")

    # Display calculated stake
    stake = calculate_stake(odds, st.session_state.bankroll)

    if stake > 0:
        st.success(f'💸 Stake: €{stake:.1f}')
        if st.button('I Placed This Bet'):
            if stake <= st.session_state.bankroll:
                st.session_state.bankroll -= stake
                new_bet = {'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                           'Odds': odds,
                           'Stake': stake,
                           'Remaining Bankroll': st.session_state.bankroll}
                st.session_state.bet_log = pd.concat([pd.DataFrame([new_bet]), st.session_state.bet_log], ignore_index=True)
                st.success('📌 Bet placed!')
            else:
                st.error('❌ Insufficient funds!')
    else:
        st.error('Odds out of range (1.40 - 4.00)')

    st.markdown('---')
    st.subheader('Adjust Bankroll')
    adjust_amount = st.number_input('New bankroll:', min_value=0.0, format="%.2f")
    if st.button('Update Bankroll'):
        st.session_state.bankroll = adjust_amount
        st.success('✅ Bankroll updated!')
