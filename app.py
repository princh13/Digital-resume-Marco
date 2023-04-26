from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Marco Principe"
PAGE_ICON = ":wave:"
NAME = "Marco Principe "
DESCRIPTION = """
As a sales professional in both software and real estate industries, I developed strong interpersonal and analytical skills. Building on this experience, I transitioned into an analyst role at Accenture where I gained expertise in data analysis and problem solving. With a passion for working with data, I am now seeking an analyst position where I can leverage my skills and experience.
"""
EMAIL = "marcoprincipe1013@gmail.com"
SOCIAL_MEDIA = {
    "Substack" : "https://ascendcapital.substack.com/",
    "LinkedIn": "https://www.linkedin.com/in/marco-principe-55a48218b",
    "GitHub": "https://github.com/princh13?tab=repositories",
    "Twitter": "https://twitter.com/MarcoPrincipe_",
}


PROJECTS = {
    "🏆 T20 Cricket World Cup - Comparing and measuring statistics to create a Top 11 Lineup" : "https://app.powerbi.com/groups/me/reports/e44ca005-99b7-439d-95b8-adbc03683a59/ReportSection",
    "🏆 NFL Rushing Stats - Rushing statistics for NFL skill positions" : "",
    "🏆 Real Estate Analysis - Analyzing real estate market trends in major US cities" : "",
    "🏆 Marketing Analysis - Analyzing customer behavior and campaign performance for a digital marketing agency" : ""
    
}

CERTIFICATIONS = { 
    " "



}





st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Hands on experience with Python & Excel 
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Proficient in consultative sales techniques, with a strong ability of building and maintaining relationships
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- ► 👩‍💻 Programming: Python, SQL 
- ► 📊 Data Visulization: PowerBi, MS Excel, Plotly
- ► 🗄️ Databases: MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Analyst | Accenture **")
st.write("12/2022 - Present")
st.write(
    """
- ►	Developed and executed targeted digital marketing strategies to align solutions with client business goals, resulting in a 50 percent decrease in onboarding time and a quarterly SSG increase of 20%.
- ►	Analyzed market trends and customer insights to identify new partnership opportunities and direct business development strategies to create and present comprehensive partnership proposals to clients, including budget and ROI projections
- ►	Piloted advertising consulting project for 70+ direct clients, achieving an average customer satisfaction score of 4.8/5, driving a quarterly revenue growth increase of 50% 

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Account Executive | Otter **")
st.write("04/2022 - 09/2022")
st.write(
    """
-  ► Performed 9000+ cold calls,  
-  ► 8400/month of recurring revenue and roughly 16,000 of total revenue 
-  ► Working closely with existing clients to uncover potential area of service expansion

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "** Sales Representative | Royal Lepage **")
st.write("12/2020 - 12/2022")
st.write(
    """
- ► Reduced clients purchase price by ~15% when representing the buyer
- ►	500+ Doors knocked representing brokerage team, generating high quality leads for lead broker
- ►	Pre-construction sales center experience, over 50 million in sales volume
- ►	Wrote python scripts to score leads based on their likelihood to convert 

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


