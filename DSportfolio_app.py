import streamlit as st
import os
import requests
import base64

# Setting the app to be in wide mode
st.set_page_config(layout="wide")

def get_repositories_by_topic(topic): # getting repositories
    keyword = f"#{topic.replace(' ', '')}"
    return [repo for repo in repos if repo["description"] and keyword in repo["description"]]


def get_readme_content(repo_full_name): # function to read content
    url = f"https://api.github.com/repos/{repo_full_name}/readme"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode("utf-8")
        return content
    else:
        return None


url = "https://api.github.com/users/vamado09/repos"
response = requests.get(url)
repos = response.json()
if not isinstance(repos, list):
    st.error("Failed to load repositories. Please check the API endpoint.") # this is necessary for me to know if its working or not
    repos = []


st.title("Vicente De Leon Williams")
st.subheader("**M.S. in Data Science**")
st.write("**Data Science | Machine Learning & Deep Learning | Data Engineering | Big Data Analytics**")


# Menu
# menu = ["About Me", "Data Science Projects"]
menu = ["Theme", "About Me", "Data Science Projects"]
choice = st.sidebar.selectbox("Menu", menu)

# Space between Menu and Profile
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

# Profile Picture and Details
profile_image_url = "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/profile_picture.png" 
html_profile = f'''
    <div style="display: flex; flex-direction: column; align-items: center;">
        <img src="{profile_image_url}" style="border-radius: 50%; width: 150px;">
        <div><b>Miami, Florida</b></div>
        <div>Email: <a href="mailto:vamado09@gmail.com">vamado09@gmail.com</a></div>
        <div>Languages: English and Spanish</div>
    </div>
'''
st.sidebar.markdown(html_profile, unsafe_allow_html=True)

# LinkedIn Button
linkedin_url = "https://www.linkedin.com/in/vicentedeleonw/"
html_linkedin = f'''
    <a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #2867B2; color: white; padding: 10px; text-align: center; border-radius: 5px; margin-top: 10px;">
            <span style="margin-left: 5px;">Connect with me on LinkedIn</span>
        </div>
    </a>
'''
st.sidebar.markdown(html_linkedin, unsafe_allow_html=True)

# GitHub Badge
github_url = "https://github.com/vamado09"
html_github = f'''
    <a href="{github_url}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #181717; color: white; padding: 10px; text-align: center; border-radius: 5px; margin-top: 10px;">
            <span style="margin-left: 5px;">Check out my GitHub</span>
        </div>
    </a>
'''
st.sidebar.markdown(html_github, unsafe_allow_html=True)

# Download Resume
resume_url = "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/VicenteDeLeon.pdf"
html_resume = f'''
    <a href="{resume_url}" target="_blank" download style="text-decoration: none;">
        <div style="background-color: white; border: 1px solid #888; padding: 10px; text-align: center; border-radius: 5px; margin-top: 10px;">
            <span style="color: black; margin-left: 5px;">Download My Resume</span>
        </div>
    </a>
'''
st.sidebar.markdown(html_resume, unsafe_allow_html=True)

# Choices -> Theme
if choice == "Theme":
    st.subheader("Theme Settings")
    st.markdown("""
    <style>
        .big-font {
            font-size:20px !important;
        }
        /* Custom CSS for captions */
        .caption {
            color: #333; /* Darker shade of grey */
            font-size: 16px !important;
            margin-bottom: 10px; /* Space above the image */
        }
        /* Space below images */
        .stImage {
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Hello, and welcome to my Data Science Portfolio. Please check if you have the "Light" Mode enabled for the best viewing experience. You can find the Settings Menu in the top right corner of the app. If your default setting is the "Dark" theme, please proceed to select the "Light" theme. If "Light" Mode is already your default setting, feel free to skip this section and explore the other menu options directly.</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">Instructions for Setting up the "Light" Theme:</p>', unsafe_allow_html=True)

    # Caption and image for the first step
    st.markdown('<p class="caption">Step 1: Open the settings menu</p>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/setting1.png")

    # Adding space between the images
    st.markdown('<br>', unsafe_allow_html=True)

    # Caption and image for the second step
    st.markdown('<p class="caption">Step 2: Select "Light" from the Theme dropdown</p>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/setting2.png")



# Choice -> About Me
if choice == "About Me":
    background_image_url = "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/Overview.png"

    st.subheader("Welcome to my Data Science Portfolio")
    st.write("This Streamlit Web Application offers a comprehensive overview of my data science journey throughout my time at Indiana University Bloomington. In this portfolio, you will have the opportunity to:")
    st.write("- Learn about my technical skills and expertise.")
    st.write("- Explore a collection of my completed projects.")
    st.write("- Dive into my professional experiences and achievements.")
    st.write("- Get in touch with me through provided contact information.")
    #st.write("**Important: Please remember to select 'Wide Mode' in the Settings to ensure the correct display of the application.**")

    # Custom CSS to set the background image with a linear gradient overlay
    st.markdown(f"""
    <style>
        .about-section {{
            background: linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), url({background_image_url});
            background-size: 960px 540px;
            background-repeat: no-repeat;
            background-position: center center;
            padding: 20px;
            color: black;
            min-height: 365px;
        }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="about-section">
        <h3>About Me:</h3>
        <p>
        After graduating from Florida State University with a Bachelor’s in Risk Management & Insurance, I pursued my aspiration to excel as a professional athlete, focusing on the sport of boxing. Over the course of more than 10 years, I dedicated myself to reaching the pinnacle of the Panamanian National Olympic Team and aimed to secure the esteemed world champion title. Despite my relentless efforts, this dream eventually concluded, leading to a new chapter in my life.
        </p>
        <p>
        Transitioning from the boxing ring to the real world came with personal challenges, and it was time to try new things. I embarked on a new career at Banco Aliado, S.A, a Panamanian private bank. As a Financial Risk Analyst, I delved into financial management and risk assessment, notably during the Covid-19 pandemic. This hard work led to a promotion, allowing me to become a Data Analyst in the bank's Risk Department - Portfolio Management area. In this new role, my fascination with data, statistics, and machine learning found its foundation and began to flourish.
        </p>
        <p>
        Driven by the desire for growth and a passion for continuous learning, I made the significant decision to leave behind Panama again to embrace a new adventure in the United States. I enrolled in Indiana University for a Master's in Data Science. This academic pursuit not only enriched my personal life but also empowered me professionally. My focus gravitated toward the analytical facets of Data Science, Machine Learning, and Deep Learning. These areas resonated with my curiosity and problem-solving inclination, creating a path that feels both challenging and rewarding.
        </p>
        <p>
        Reflecting on my journey from boxing to Data Science, it has been a path filled with challenges, growth, and learning. Whether in the ring or in the office, I approach problems with confidence and resilience, applying skills effectively across domains. This unique blend of experiences has shaped me into who I am today, ready to take on new challenges and opportunities. Please, feel free to check out my Data Science Projects and download a copy of my resume.
        </p>
    </div>
    """, unsafe_allow_html=True)



# Choices -> Data Science Projects
if choice == "Data Science Projects":
    st.subheader("GitHub - Data Science Projects")
    st.write("**Select one of the following Data Science topics:**")
    st.write("This section of my portfolio showcases a wide array of projects, covering a diverse range of topics within data science. These include Machine Learning and Deep Learning applications, Big Data Analytics with Hadoop and AWS, and more. After choosing a topic, please scroll down to the bottom of the page. There, you will find a detailed description along with the corresponding GitHub repository URL for more in-depth information.")
    st.write("- Data Science and AI: Nike, ML Risk Analytics, Deep Learning Principles, Applied Machine Learning, Virtual Tissue Simulation, Large Language Models, NLP, and Applied Data Science.")
    st.write("- Big Data Analytics: Apache Spark (PySpark), Apache Hadoop & AWS, and Basics of Scala Programming.")
    st.write("- Statistics and RDBS:  City of Bloomington Indiana, Data Visualization, Applied Database Technologies.")
    
    topics = [
        ["Nike", "ML Risk Analytics", "Deep Learning Principles"],
        ["Applied Machine Learning", "Virtual Tissue Simulation", "Large Language Models"],
        ["City of Bloomington Indiana", "Apache Spark (PySpark)", "Basics of Scala Programming"],
        ["Natural Language Processing", "Applied Data Science", "Applied Database Technologies"],
        ["Data Science In Practice", "Data Visualization", "Apache Hadoop & AWS"]
    ]
    
    images = [
    
        [
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/nike.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/risk2.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/DL2.png"
        ],
        [
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/ML2.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/VTS2.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/LLM.png"
        ],
        [
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/citybloomington.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/SPARK.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/SCALA2.png"
        ],
        [
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/NLP.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/ADS2.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/RDBS.png"
        ],
        [
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/DS_Practice.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/visualization.png",
            "https://raw.githubusercontent.com/vamado09/Images-Streamlit/main/HadoopAWS.png"
        ]
    ]

    selected_topic = st.session_state.get('selected_topic', None)

    # Red Button Styling
    custom_button_style = """<style>
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            border: none;
            display: block;
            margin: 0 auto;
        }
    </style>"""
    st.markdown(custom_button_style, unsafe_allow_html=True)
    
    for row_topics, row_images in zip(topics, images):
        cols = st.columns(len(row_topics))
        for i, topic in enumerate(row_topics):
            with cols[i]:
                # Centralize the title
                st.markdown(f"<div style='text-align: center;'><b>{topic}</b></div>", unsafe_allow_html=True)

                # Centralize the image
                st.markdown(f"<div style='display: flex; justify-content: center;'><img src='{row_images[i]}' width='250'/></div>", unsafe_allow_html=True)
                
                if st.button(topic):
                    selected_topic = topic
                    st.session_state.selected_topic = selected_topic

                # Add space between topics in the same row (columns)
                st.markdown("<div style='margin: 5px;'></div>", unsafe_allow_html=True)

        # Add space between the rows
        st.markdown("<div style='margin: 15px;'></div>", unsafe_allow_html=True)

    # If a topic was selected, show its repositories
    if selected_topic:
      selected_repositories = get_repositories_by_topic(selected_topic)
      for repo in selected_repositories:
        # Fetch and display README content
        readme_content = get_readme_content(repo["full_name"])  # Assuming the repo dictionary has a 'full_name' key
        if readme_content:
            st.markdown(readme_content)
        else:
            st.write("README not available or failed to fetch.")
        
        st.write(repo["description"])
        st.markdown(f"[GitHub URL]({repo['html_url']})")
