import streamlit as st

# --- Food Menu with more options ---
menu = {
    "Burger 🍔": 5.99,
    "Pizza 🍕": 8.99,
    "Sushi 🍣": 12.99,
    "Pasta 🍝": 7.49,
    "Cendol 🍧": 3.50,
    "Fried Rice 🍚": 6.00,
    "Satay 🍢": 8.00,
    "Ice Cream 🍨": 4.00
}

# --- Session state to track if order is submitted ---
if 'order_submitted' not in st.session_state:
    st.session_state.order_submitted = False

# --- Main App ---
st.set_page_config(page_title="Delivery App", page_icon="🛵")
st.title("🛵 Simple Food Delivery App")

# If order is submitted, show thank you page
if st.session_state.order_submitted:
    st.success("🎉 Order received!")
    st.subheader("Thank you for your order!")
    st.write("Your food is on the way! 🚚")
    st.button("Start a New Order", on_click=lambda: st.session_state.update(order_submitted=False))
else:
    # --- Step 1: User Info ---
    st.header("Step 1: Your Info")
    name = st.text_input("Your name")
    address = st.text_area("Delivery address")

    # Google Maps-like input: user enters lat/lon
    st.markdown("Optional: 📍 Enter your location (coordinates for Google Maps)")
    latitude = st.number_input("Latitude", format="%.6f", step=0.000001)
    longitude = st.number_input("Longitude", format="%.6f", step=0.000001)

    if latitude and longitude:
        st.map(data={'lat': [latitude], 'lon': [longitude]})

    # --- Step 2: Food Selection ---
    st.header("Step 2: Choose Your Food")
    selected_items = []
    quantities = {}

    for item, price in menu.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.checkbox(f"{item} — ${price:.2f}"):
                selected_items.append(item)
        with col2:
            if item in selected_items:
                quantities[item] = st.number_input(f"Qty", min_value=1, max_value=10, key=item)

    # --- Step 3: Submit Order ---
    if name and address and selected_items:
        st.header("Step 3: Order Summary")
        total = sum(menu[item] * quantities[item] for item in selected_items)
        
        for item in selected_items:
            st.write(f"{quantities[item]} × {item} = ${menu[item] * quantities[item]:.2f}")
        st.write(f"**Total: ${total:.2f}**")

        if st.button("Place Order"):
            st.success("Order placed successfully!")
            st.session_state.order_submitted = True
    elif name and address:
        st.warning("Please select at least one item.")
