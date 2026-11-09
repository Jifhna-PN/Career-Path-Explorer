import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Career Path Explorer",
    layout="wide"
)


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

data = pd.read_csv("data/career_skills.csv")


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("Career Path Explorer")

st.caption(
    "Skill-based career exploration and learning roadmap"
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Your Skills")

skills = sorted(data["Skill"].unique())

selected_skills = st.sidebar.multiselect(
    "Select the skills you already know",
    skills
)

st.sidebar.caption(
    "Your selections are compared with the skills "
    "defined in the career dataset."
)


# --------------------------------------------------
# Start Application
# --------------------------------------------------

if not selected_skills:

    st.info(
        "Select your current skills from the sidebar "
        "to explore career paths."
    )

    st.subheader("How it works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**1. Select Skills**")
        st.write(
            "Choose the technical skills you currently know."
        )

    with col2:
        st.markdown("**2. Explore Careers**")
        st.write(
            "Compare your skills with different career paths."
        )

    with col3:
        st.markdown("**3. Build a Roadmap**")
        st.write(
            "Identify skills you can learn for your selected career."
        )

    st.stop()


# --------------------------------------------------
# Career Analysis
# --------------------------------------------------

career_results = []

for career in data["Career"].unique():

    career_data = data[
        data["Career"] == career
    ]

    required_skills = career_data[
        "Skill"
    ].tolist()

    matched_skills = [
        skill
        for skill in selected_skills
        if skill in required_skills
    ]

    missing_skills = [
        skill
        for skill in required_skills
        if skill not in selected_skills
    ]

    match_percentage = (
        len(matched_skills)
        / len(required_skills)
    ) * 100

    career_results.append(
        {
            "Career": career,
            "Match": round(match_percentage, 1),
            "Matched Skills": len(matched_skills),
            "Skills to Learn": len(missing_skills)
        }
    )


career_df = pd.DataFrame(career_results)


# --------------------------------------------------
# Summary Metrics
# --------------------------------------------------

st.subheader("Your Skill Summary")

total_skills = len(selected_skills)

career_count = len(career_df)

average_match = career_df["Match"].mean()

highest_match = career_df["Match"].max()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Your Skills",
        total_skills
    )

with col2:
    st.metric(
        "Career Paths",
        career_count
    )

with col3:
    st.metric(
        "Average Match",
        f"{average_match:.1f}%"
    )

with col4:
    st.metric(
        "Highest Match",
        f"{highest_match:.1f}%"
    )


st.divider()


# --------------------------------------------------
# Career Comparison
# --------------------------------------------------

st.subheader("Career Match Comparison")

display_df = career_df[
    [
        "Career",
        "Match",
        "Matched Skills",
        "Skills to Learn"
    ]
].copy()

display_df.columns = [
    "Career",
    "Match (%)",
    "Matched Skills",
    "Skills to Learn"
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# Career Chart
# --------------------------------------------------

fig, ax = plt.subplots(
    figsize=(10, 4)
)

ax.bar(
    career_df["Career"],
    career_df["Match"]
)

ax.set_ylabel("Skill Match (%)")

ax.set_ylim(0, 100)

ax.set_title(
    "Skill Match Across Career Paths"
)

plt.xticks(
    rotation=25,
    ha="right"
)

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


st.divider()


# --------------------------------------------------
# Career Explorer
# --------------------------------------------------

st.subheader("Explore a Career")

selected_career = st.selectbox(
    "Choose a career",
    career_df["Career"].tolist()
)


# --------------------------------------------------
# Selected Career Data
# --------------------------------------------------

career_data = data[
    data["Career"] == selected_career
]

required_skills = career_data[
    "Skill"
].tolist()


matched_skills = [
    skill
    for skill in selected_skills
    if skill in required_skills
]


missing_skills = [
    skill
    for skill in required_skills
    if skill not in selected_skills
]


match_percentage = (
    len(matched_skills)
    / len(required_skills)
) * 100


# --------------------------------------------------
# Selected Career Header
# --------------------------------------------------

st.markdown(
    f"### {selected_career}"
)

st.progress(
    int(match_percentage)
)

st.caption(
    f"{match_percentage:.1f}% of the skills in the "
    f"current dataset are already covered by your profile."
)


# --------------------------------------------------
# Skill Details
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.markdown("#### Skills You Have")

    if matched_skills:

        for skill in matched_skills:
            st.write(skill)

    else:

        st.write(
            "No matching skills yet."
        )


with col2:

    st.markdown("#### Skills to Learn")

    if missing_skills:

        for skill in missing_skills:

            skill_row = career_data[
                career_data["Skill"] == skill
            ].iloc[0]

            st.write(
                f"{skill} — {skill_row['Level']}"
            )

    else:

        st.write(
            "All listed skills are already covered."
        )


st.divider()


# --------------------------------------------------
# Learning Roadmap
# --------------------------------------------------

st.subheader("Learning Roadmap")

level_order = {
    "Beginner": 1,
    "Intermediate": 2,
    "Advanced": 3
}


roadmap = []

for skill in missing_skills:

    skill_row = career_data[
        career_data["Skill"] == skill
    ].iloc[0]

    roadmap.append(
        {
            "Skill": skill,
            "Category": skill_row["Category"],
            "Level": skill_row["Level"],
            "Order": level_order[
                skill_row["Level"]
            ]
        }
    )


roadmap.sort(
    key=lambda x: x["Order"]
)


if roadmap:

    roadmap_df = pd.DataFrame(roadmap)

    roadmap_df.insert(
        0,
        "Step",
        range(1, len(roadmap_df) + 1)
    )

    st.dataframe(
        roadmap_df[
            [
                "Step",
                "Skill",
                "Category",
                "Level"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

else:

    st.success(
        "No additional skills are required based "
        "on the current dataset."
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Career Path Explorer | Built with Python, Pandas, "
    "Matplotlib and Streamlit"
)