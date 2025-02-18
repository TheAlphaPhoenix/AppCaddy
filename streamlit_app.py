import streamlit as st
import time

# --- App Configuration ---
st.set_page_config(
    page_title="App Caddy - Smart App Management",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Sidebar Navigation ---
st.sidebar.title("📌 App Caddy")
page = st.sidebar.radio(
    "Navigation", ["🏠 Dashboard", "🔍 Discover Apps", "📂 Manage Hubs", "⚙️ Settings"]
)

# --- Sample App Hubs Data (Mock Data) ---
app_hubs = {
    "📌 Productivity": ["Notion", "Evernote", "Trello"],
    "💬 Social Media": ["Instagram", "Twitter", "Snapchat"],
    "💪 Fitness": ["MyFitnessPal", "Strava", "Nike Training Club"],
    "🎬 Entertainment": ["Netflix", "Spotify", "Twitch"],
}

# --- Dashboard Page ---
if page == "🏠 Dashboard":
    st.title("📱 Your App Hubs")
    st.markdown("Easily manage and organize your favorite apps into **smart hubs**!")

    for category, apps in app_hubs.items():
        with st.expander(f"🔹 {category}"):
            st.write(", ".join(apps))
            if st.button(f"➕ Manage {category}"):
                st.success(f"🔧 Managing {category}...")

# --- Discover Apps Page ---
elif page == "🔍 Discover Apps":
    st.title("🔍 Discover New Apps")
    search_query = st.text_input("🔎 Search for apps...")
    recommended_apps = ["Asana", "Duolingo", "Clubhouse", "Calm", "Google Keep"]

    if search_query:
        st.write(f"🎯 Showing results for: **{search_query}**")
        search_results = [app for app in recommended_apps if search_query.lower() in app.lower()]
        if search_results:
            st.write(", ".join(search_results))
        else:
            st.warning("🚫 No results found. Try another keyword.")
    else:
        st.write("🔥 **Trending Apps:**")
        st.write(", ".join(recommended_apps))

# --- Manage Hubs Page ---
elif page == "📂 Manage Hubs":
    st.title("📂 Manage Your App Hubs")
    hub_name = st.text_input("🆕 Create a new App Hub")

    if st.button("➕ Create Hub"):
        if hub_name:
            app_hubs[hub_name] = []
            st.success(f"✅ Created new App Hub: **{hub_name}**")
            time.sleep(1)  # Simulate app refresh
        else:
            st.warning("⚠️ Please enter a valid hub name.")

    st.subheader("📌 Your App Hubs")
    for hub, apps in app_hubs.items():
        with st.expander(f"🔹 {hub} ({len(apps)} apps)"):
            st.write(", ".join(apps) if apps else "No apps added yet.")
            add_app = st.text_input(f"📲 Add an app to {hub}", key=hub)
            if st.button(f"➕ Add to {hub}", key=f"btn_{hub}") and add_app:
                app_hubs[hub].append(add_app)
                st.success(f"✅ Added **{add_app}** to **{hub}**")
                time.sleep(1)  # Simulate refresh

# --- Settings Page ---
elif page == "⚙️ Settings":
    st.title("⚙️ App Caddy Settings")
    theme = st.radio("🎨 Choose Theme", ["Light Mode", "Dark Mode"])
    notifications = st.checkbox("🔔 Enable Notifications")
    st.success(f"✅ Theme set to **{theme}**")
    if notifications:
        st.info("🔔 Notifications enabled!")

# --- Footer ---
st.markdown("---")
st.write("💡 **App Caddy - Your Smart App Management Tool** | 🚀 Future updates will include AI-powered app recommendations & cloud sync.")
