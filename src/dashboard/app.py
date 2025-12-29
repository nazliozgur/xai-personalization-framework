"""
v3.6 IMPROVEMENT 3: Main Dashboard Entry Point
Dual-Entry System: Admin vs User view selection

Author: Nazlı Özgür
Date: December 2025
"""
import streamlit as st
from admin_view import render_admin_view
from user_view import render_user_view

# Page config
st.set_page_config(
    page_title="XAE-Frame v3.6 - Dashboard",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar: Stakeholder selection
st.sidebar.title("XAE-Frame v3.6")
st.sidebar.markdown("---")

view = st.sidebar.selectbox(
    "**Select Your View:**",
    [
        "👤 End-User (Actionable Insights)",
        "🔧 Admin/Manager (Full Model Truth)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**👤 End-User View:**  
- Actionable recommendations
- Counterfactual explanations
- Simple language

**🔧 Admin View:**  
- Full SHAP analysis
- Proxy risk analysis
- Compliance metrics
- Technical details
""")

# Render appropriate view
if "Admin/Manager" in view:
    render_admin_view()
else:
    render_user_view()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("XAE-Frame v3.6 | Nazlı Özgür | 2025")
