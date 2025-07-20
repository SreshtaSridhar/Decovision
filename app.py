
import streamlit as st
import openai
import os



# Function to generate AI decoration image
def generate_decoration(description):
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=description,
            n=1,
            size="1024x1024"
        )
        return response.data[0].url
    except Exception as e:
        return f"Error: {e}"

# Function to estimate quantity and cost
def estimate_decor_cost(description):
    keywords = {
        "balloons": (50, 0.5),
        "ribbons": (30, 0.2),
        "flowers": (20, 1.5),
        "lights": (10, 3.0),
        "candles": (15, 2.0),
        "tablecloths": (5, 8.0)
    }

    estimated_items = {}
    total_cost = 0

    for item, (quantity, price) in keywords.items():
        if item in description.lower():
            estimated_items[item] = {"quantity": quantity, "price": price}
            total_cost += quantity * price

    return estimated_items, total_cost

# Streamlit UI
st.title("🎉 AI Event Decorator")

# Description input
description = st.text_area("Describe your event decoration theme:", "Elegant wedding setup with white flowers and soft lighting.")

# Room image upload
uploaded_image = st.file_uploader("Upload a photo of your room (optional)", type=["jpg", "png", "jpeg"])

# Generate button
if st.button("Generate Decoration"):
    with st.spinner("Creating your AI-powered decoration..."):
        # Generate AI image
        ai_image_url = generate_decoration(description)
        
        # Estimate cost & quantity
        items, total_cost = estimate_decor_cost(description)

        # Display AI-generated image
        if ai_image_url.startswith("http"):
            st.image(ai_image_url, caption="AI-Generated Decoration", use_column_width=True)
        else:
            st.error("Failed to generate image. Please try again.")

        # Display cost & quantity details
        st.subheader("📋 Estimated Decoration Items & Cost")
        if items:
            for item, details in items.items():
                st.write(f"**{item.capitalize()}**: {details['quantity']} pieces @ ${details['price']} each")
            st.write(f"💰 **Total Estimated Cost**: ${total_cost:.2f}")
        else:
            st.write("No decorations were detected from your description.")

# Display uploaded image if available
if uploaded_image:
    st.image(uploaded_image, caption="Your Uploaded Room", use_column_width=True)
