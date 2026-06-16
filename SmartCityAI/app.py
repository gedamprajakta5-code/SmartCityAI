import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🏙️ Smart City Planner")

st.markdown("""
### AI-Powered Urban Infrastructure Analysis & Development Recommendation System

Analyze city zones, identify infrastructure gaps,
calculate development priorities, and generate smart recommendations.
""")

st.header("Zone A")

pop_a = st.number_input("Population A", min_value=1000)
traffic_a = st.selectbox("Traffic A", ["Low", "Medium", "High"])
hospital_a = st.number_input("Hospitals A", min_value=0)
park_a = st.number_input("Parks A", min_value=0)

st.header("Zone B")

pop_b = st.number_input("Population B", min_value=1000)
traffic_b = st.selectbox("Traffic B", ["Low", "Medium", "High"])
hospital_b = st.number_input("Hospitals B", min_value=0)
park_b = st.number_input("Parks B", min_value=0)

st.header("Zone C")

pop_c = st.number_input("Population C", min_value=1000)
traffic_c = st.selectbox("Traffic C", ["Low", "Medium", "High"])
hospital_c = st.number_input("Hospitals C", min_value=0)
park_c = st.number_input("Parks C", min_value=0)

if st.button("Analyze City"):
    zone_names =[]
    priority_scores = []
    hospital_scores = []
    park_scores = []
    hospital_counts = []
    park_counts = []

    st.header("Analysis Results")

    zones = [
        ("Zone A", pop_a, traffic_a, hospital_a, park_a),
        ("Zone B", pop_b, traffic_b, hospital_b, park_b),
        ("Zone C", pop_c, traffic_c, hospital_c, park_c)
    ]

    for zone, pop, traffic, hospitals, parks in zones:

        st.subheader(zone)

        suggestions = []
        priority_score = 0
        sustainability_score = 100

        if traffic == "High":
            suggestions.append("🚦 Increase public transport and improve roads")
            priority_score += 30
            sustainability_score -= 30

        if hospitals < pop / 20000:
            suggestions.append("🏥 More hospitals required")
            priority_score += 40
            sustainability_score -= 40

        if parks < pop / 15000:
            suggestions.append("🌳 Build additional parks")
            priority_score += 30
            sustainability_score -= 30

        if len(suggestions) == 0:
            suggestions.append("✅ Infrastructure looks balanced")
        if priority_score >= 80:
                priority = "🔴 Critical"
        elif priority_score >= 50:
                priority = "🟠 High"
        elif priority_score >= 20:
                priority = "🟡 Medium"
        else:
                priority = "🟢 Low"
        st.write(f"Priority Score: {priority_score}/100")
        st.write(f"Priority Level: {priority}")

        st.write(f"🌱 Sustainability Score: {sustainability_score}/100")

        zone_names.append(zone)
        priority_scores.append(priority_score)
        hospital_scores.append(hospitals)
        park_scores.append(parks)
        hospital_counts.append(hospitals)
        park_counts.append(parks)

        for s in suggestions:
            st.write(s)

        ranking_df = pd.DataFrame({"Zone": zone_names,"Priority Score": priority_scores})
        ranking_df = ranking_df.sort_values(by="Priority Score",ascending=False)
        st.header("🏆 Development Priority Ranking")
        for i, row in enumerate(ranking_df.itertuples(), start=1):
            st.write(f"{i}. {row.Zone} ({row._2}/100)")
            
        st.header("📈 Development Priority Comparison")
        df = pd.DataFrame({
                "Zone": zone_names,
                "Priority Score": priority_scores})
        fig, ax = plt.subplots()
        ax.bar(df["Zone"], df["Priority Score"])
        ax.set_ylabel("Priority Score")
        ax.set_title("Zone Development Priority")

        st.pyplot(fig)

        st.header("🏥 Hospital Comparison")
        fig2, ax2 = plt.subplots()
        
        ax2.bar(zone_names, hospital_counts)
        ax2.set_ylabel("Number of Hospitals")
        ax2.set_title("Hospitals by Zone")
        st.pyplot(fig2)

        st.header("🌳 Parks Comparison")

        fig3, ax3 = plt.subplots()
        ax3.bar(zone_names, park_counts)
        
        ax3.set_ylabel("Number of Parks")
        ax3.set_title("Parks by Zone")
        
        st.pyplot(fig3)
            