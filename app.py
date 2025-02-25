import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "Hotel Reservations.csv"
df = pd.read_csv(file_path)


st.image("/Users/mataoyu/Desktop/hotel/1.jpg", use_container_width=True)
st.title("Hotel Reservation Analysis of Ritz hotel Paris 🏨")
st.markdown("""
### About the Dataset
This dataset contains **36,275 hotel reservations** with details about guests, booking trends, cancellations, and pricing.
""")


st.subheader("🔍 Explore the Data")
st.markdown("You can sort, search, and filter the data using the options below.")


num_rows = st.slider("Select number of rows to display", min_value=5, max_value=50, value=10)
st.dataframe(df.head(num_rows))  


status_filter = st.selectbox("Filter by Booking Status", ["All", "Not Canceled", "Canceled"])
if status_filter == "Not Canceled":
    df_filtered = df[df["booking_status"] == "Not_Canceled"]
elif status_filter == "Canceled":
    df_filtered = df[df["booking_status"] == "Canceled"]
else:
    df_filtered = df


st.write(f"Showing {len(df_filtered)} records:")
st.dataframe(df_filtered)


st.subheader("📊 Key Data Insights")
st.write(f"📌 Total Reservations: {len(df)}")
st.write(f"📌 Total Unique Guests: {df['Booking_ID'].nunique()}")

st.image("/Users/mataoyu/Desktop/hotel/2.jpg", caption="Hotel Booking Statistics", use_container_width=True)


st.subheader("📉 Booking Cancellations")
fig, ax = plt.subplots()
sns.countplot(x=df['booking_status'], palette='coolwarm', ax=ax)
ax.set_title("Canceled vs Not Canceled Bookings")
st.pyplot(fig)


st.subheader("💰 Average Room Price per Room Type")

room_types = st.multiselect("Select Room Types to Display", options=df["room_type_reserved"].unique(), default=df["room_type_reserved"].unique())
df_filtered_room = df[df["room_type_reserved"].isin(room_types)]

fig, ax = plt.subplots()
sns.barplot(x='room_type_reserved', y='avg_price_per_room', data=df_filtered_room, ax=ax, palette='viridis')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_title("Room Price by Room Type")
st.pyplot(fig)

st.image("/Users/mataoyu/Desktop/hotel/3.jpg", caption="Hotel Booking Statistics", use_container_width=True)


st.subheader("📌 Recommendations for Hotel Management")
st.markdown("""
- ✅ **Reduce cancellations** by implementing a flexible booking policy.
- ✅ **Adjust pricing strategy** based on room type demand.
- ✅ **Enhance guest experience** with personalized offers for repeated guests.
""")


st.subheader("🚀 Future Enhancements")
st.markdown("""
- 🤖 Add **predictive models** to estimate cancellations.
- 📊 Create a **dynamic dashboard** with real-time updates.
- 🗣️ Implement **guest sentiment analysis** using review data.
""")


st.image("/Users/mataoyu/Desktop/hotel/4.jpg", use_container_width=True)

echo "streamlit
pandas
matplotlib
seaborn" > requirements.txt
