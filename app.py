import sys
import os

# Ensure the project root directory is in sys.path for deployment environments like Render
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="Student Smart Campus AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

from modules.database import ensure_db_dir
from modules.auth import render_login_register_page
from modules.dashboard import render_dashboard_page
from modules.students import (
    render_add_student_page,
    render_update_student_page,
    render_delete_student_page,
    render_student_list_page
)
from modules.announcements import render_announcements_page
from modules.notices import render_notices_page
from modules.history import render_history_page
from modules.utils import record_audit_log

# Ensure database directory and default JSON structures exist
ensure_db_dir()

# Inject Custom CSS Stylesheet
def inject_custom_css():
    css_path = os.path.join("assets", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

inject_custom_css()

# Session State Initialization
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user" not in st.session_state:
    st.session_state["user"] = None

def main():
    if not st.session_state["authenticated"]:
        render_login_register_page()
    else:
        user = st.session_state.get("user", {})
        
        # Sidebar Setup
        logo_path = os.path.join("assets", "logo.png")
        if os.path.exists(logo_path):
            st.sidebar.image(logo_path, width=130)
        
        st.sidebar.markdown(
            f"""
            <div style="padding: 10px 0px 15px 0px; border-bottom: 1px solid #334155; margin-bottom: 15px;">
                <h3 style="margin: 0; color: #FFFFFF; font-size: 1.1rem;">Smart Campus AI</h3>
                <p style="margin: 3px 0 0 0; color: #94A3B8; font-size: 0.8rem;">Logged in as: <b>{user.get('username', 'User')}</b></p>
                <span style="display: inline-block; background: #1E40AF; color: #93C5FD; padding: 2px 8px; border-radius: 6px; font-size: 0.75rem; margin-top: 5px;">{user.get('role', 'Student')}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Try streamlit_option_menu with fallback
        try:
            from streamlit_option_menu import option_menu
            selected_page = option_menu(
                menu_title="Campus Navigation",
                options=[
                    "Dashboard",
                    "Add Student",
                    "Update Student",
                    "Delete Student",
                    "Student List",
                    "History",
                    "Announcements",
                    "Notice Board",
                    "Logout"
                ],
                icons=[
                    "speedometer2",
                    "person-plus-fill",
                    "pencil-square",
                    "trash3-fill",
                    "table",
                    "clock-history",
                    "megaphone-fill",
                    "pin-angle-fill",
                    "box-arrow-right"
                ],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "transparent"},
                    "icon": {"color": "#60A5FA", "font-size": "16px"},
                    "nav-link": {
                        "font-size": "14px",
                        "text-align": "left",
                        "margin": "4px 0px",
                        "color": "#E2E8F0",
                        "border-radius": "8px"
                    },
                    "nav-link-selected": {
                        "background-color": "#2563EB",
                        "color": "#FFFFFF",
                        "font-weight": "600"
                    }
                }
            )
        except Exception:
            selected_page = st.sidebar.radio(
                "Navigation",
                [
                    "Dashboard",
                    "Add Student",
                    "Update Student",
                    "Delete Student",
                    "Student List",
                    "History",
                    "Announcements",
                    "Notice Board",
                    "Logout"
                ]
            )

        # Route Pages
        if selected_page == "Dashboard":
            render_dashboard_page()
        elif selected_page == "Add Student":
            render_add_student_page()
        elif selected_page == "Update Student":
            render_update_student_page()
        elif selected_page == "Delete Student":
            render_delete_student_page()
        elif selected_page == "Student List":
            render_student_list_page()
        elif selected_page == "History":
            render_history_page()
        elif selected_page == "Announcements":
            render_announcements_page()
        elif selected_page == "Notice Board":
            render_notices_page()
        elif selected_page == "Logout":
            record_audit_log(user.get("username", "User"), "Logout Success")
            st.session_state["authenticated"] = False
            st.session_state["user"] = None
            st.success("You have been logged out.")
            st.rerun()

if __name__ == "__main__":
    main()
