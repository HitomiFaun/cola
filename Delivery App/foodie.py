import streamlit as st

# --- Menu items ---
menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Sushi": 12.99,
    "Pasta": 7.49,
    "Cendol": 3.50
}

st.title("🍔 Simple Delivery App")

# --- Step 1: User info ---
st.header("Step 1: Enter Your Info")
name = st.text_input("What's your name?")
address = st.text_area("Delivery address")

# --- Step 2: Select food items ---
st.header("Step 2: Select Your Food")
selected_items = []
for item, price in menu.items():
    if st.checkbox(f"{item} - ${price:.2f}"):
        selected_items.append(item)

# --- Step 3: Confirm Order ---
if selected_items and name and address:
    st.header("🧾 Order Summary")
    total = sum(menu[item] for item in selected_items)
    
    for item in selected_items:
        st.write(f"- {item} (${menu[item]:.2f})")
    
    st.write(f"**Total: ${total:.2f}**")
    
    if st.button("Place Order"):
        st.success(f"Thank you {name}! Your order will be delivered to {address}. Enjoy your meal! 🛵")

elif name and address and not selected_items:
    st.warning("Please select at least one item to order.")

