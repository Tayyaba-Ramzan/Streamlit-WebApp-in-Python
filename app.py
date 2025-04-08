import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import io
import contextlib
import random

# Load Lottie Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page Config
st.set_page_config(
    page_title="Python Mega Info Hub",
    page_icon="🐍",
    layout="wide"
)

# Sidebar Navigation
with st.sidebar:
    st.title("🐍 Python Hub")
    st.image("https://cdn.dribbble.com/users/1162077/screenshots/3848914/programmer.gif", use_container_width=True)
    st.markdown("### 🧭 Navigation")
    selected_option = st.radio("Go to section", [
        "🏠 Home", "📜 History of Python", "🎯 Why Learn Python?", "📚 Popular Libraries",
        "📘 Python Resources", "🧠 Python Quiz", "💻 Try Python Code", "🎤 Interview Prep", "📬 Contact"
    ])
    trending_libs = ["pandas", "numpy", "fastapi", "typer", "poetry"]

with st.sidebar:
    st.markdown("### 📈 Trending Python Libraries")
    for lib in trending_libs:
        st.write(f"🔹 {lib}")


    python_tips = [
    "Use list comprehensions to write concise loops.",
    "Avoid using mutable default arguments in functions.",
    "Use enumerate() when looping over indexes and items.",
    "Use virtual environments to manage dependencies.",
    "Leverage f-strings for clean and fast string formatting.",
    "Use 'with' statement to handle file operations safely.",
    "Use 'type hints' to improve code readability and tooling.",
    "Use sets to remove duplicates from a list.",
    "Use 'zip()' to iterate over multiple lists in parallel.",
    "Explore the power of generators for memory-efficient looping."
]
with st.sidebar:
    st.markdown("### 🧠 Today's Python Tip")
    st.info(random.choice(python_tips))


# Header Image
st.image("https://docs.temporal.io/assets/images/banner-python-temporal-0d345d125b6892840c54f7e1460c8a5a.png", use_container_width=True)

# Title
st.title("🐍 Welcome to the Python Mega Info Hub!")
st.markdown("Your one-stop portal for everything related to Python! 🚀")

# Page Content
if selected_option == "🏠 Home":
    st.header("💡 What You’ll Learn")
    st.markdown("""
    - ✅ Python History & Evolution  
    - ✅ Benefits of Python  
    - ✅ Libraries & Frameworks  
    - ✅ Beginner to Advanced Resources  
    - ✅ Quiz, Interview Prep & Live Coding  
    """)

elif selected_option == "📜 History of Python":
    st.header("📜 A Brief History of Python")
    st.markdown("""
    - **Created by:** Guido van Rossum  
    - **First Released:** 1991  
    - Python was inspired by the **ABC language**.  
    - The name “Python” comes from **Monty Python’s Flying Circus**.  
    """)
    st.success("Fun Fact: Python is used by Google, NASA, Netflix, and even Pixar!")

elif selected_option == "🎯 Why Learn Python?":
    st.header("🎯 Why Python is the Best Language for You?")
    st.markdown("""
    - 🔥 High Demand in Jobs  
    - 📦 Huge Collection of Libraries  
    - 🤖 Great for AI, ML, Web, and Automation  
    - 🐍 Beginner-Friendly Syntax  
    - 🌐 Strong Community Support  
    """)
    st.info("Tip: Start with basics, then build real-world projects!")

elif selected_option == "📚 Popular Libraries":
    st.header("📚 Popular Python Libraries")
    st.markdown("""
    - **NumPy** – Numerical computations  
    - **Pandas** – Data analysis  
    - **Matplotlib / Seaborn** – Data visualization  
    - **Scikit-learn** – Machine learning  
    - **Streamlit** – Build web apps  
    - **Flask / Django** – Web frameworks  
    - **TensorFlow / PyTorch** – Deep learning  
    """)
    st.warning("Don’t just learn – create something amazing!")

elif selected_option == "📘 Python Resources":
    st.header("📘 Learn Python - Free Resources")
    
    st.subheader("Official Docs")
    st.markdown("[📖 Python Documentation](https://docs.python.org/3/)")
    
    st.subheader("YouTube Tutorials")
    st.markdown("""
    - [Code With Harry](https://youtu.be/7wnove7K-ZQ)  
    - [Harshit Vashisth](https://youtu.be/RAwntanK4wQ)  
    - [FreeCodeCamp](https://youtu.be/eWRfhZUzrAc)  
    """)
    
    st.subheader("Free Courses")
    st.markdown("""
    - [Python for Everybody (Coursera)](https://www.youtube.com/watch?v=8DvywoWv6fI)  
    - [Complete Python Code Mastery](https://youtu.be/mMzwOZQJIcE)  
    """)

elif selected_option == "🧠 Python Quiz":
    st.header("🧠 Test Your Python Knowledge!")

    questions = [
        {"question": "What does `len()` do in Python?", "options": ["Returns length", "Prints string", "Adds numbers", "None"], "answer": "Returns length"},
        {"question": "Which one is a valid Python data type?", "options": ["integer", "loop", "define", "null"], "answer": "integer"},
        {"question": "What is the output of `2 ** 3`?", "options": ["6", "8", "9", "Error"], "answer": "8"},
        {"question": "Which library is used for data analysis?", "options": ["Seaborn", "Tkinter", "Pandas", "Django"], "answer": "Pandas"},
        {"question": "Which of the following is immutable?", "options": ["List", "Tuple", "Dictionary", "Set"], "answer": "Tuple"},
    ]

    score = 0
    if 'submitted' not in st.session_state:
        st.session_state['submitted'] = False

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}: {q['question']}")
        user_ans = st.radio("Choose one:", q["options"], key=f"q{i}")

    if st.button("Submit Quiz"):
        st.session_state['submitted'] = True
        # Check answers and calculate score
        for i, q in enumerate(questions):
            user_ans = st.session_state.get(f"q{i}")
            if user_ans == q["answer"]:
                score += 1

        st.success(f"🎉 You scored {score}/{len(questions)}!")

        # Show balloons animation if score is 5 out of 5
        if score == 5:
            st.balloons()


elif selected_option == "💻 Try Python Code":
    st.header("💻 Run Your Python Code Here")
    user_code = st.text_area("Write your Python code below:", height=200)

    if st.button("Run Code"):
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):
                exec(user_code, {})
            st.success("✅ Code executed successfully!")
            st.code(output.getvalue(), language="python")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

elif selected_option == "🎤 Interview Prep":
    st.header("🎤 Python Interview Questions")

    questions = {
        "👉 What is the difference between list and tuple?": "Lists are mutable, tuples are immutable.",
        "👉 What is Python's GIL?": "GIL (Global Interpreter Lock) prevents multiple threads from executing at once.",
        "👉 What is the difference between `is` and `==`?": "`is` checks identity, `==` checks value equality.",
        "👉 What is a lambda function?": "Anonymous function defined using the lambda keyword.",
        "👉 What is the use of `*args` and `**kwargs`?": "`*args` is for variable arguments, `**kwargs` for keyword args.",
        "👉 Explain list comprehension.": "Compact syntax to create new lists using expressions.",
    }

    for q, a in questions.items():
        with st.expander(q):
            st.write(a)

elif selected_option == "📬 Contact":
    st.header("📬 Contact Us")
    st.markdown("Feel free to reach out for queries, suggestions or collaboration!")
    st.text("📧 Email: tayyabaramzan.it@gmail.com")
    st.text("🔗 GitHub: https://github.com/Tayyaba-Ramzan")
    st.text("🔗 LinkedIn: https://www.linkedin.com/in/tayyabaRamzan/")

# Footer
st.markdown("---")
st.markdown("© 2025 | Made with ❤️ using Streamlit | Designed by **Tayyaba Ramzan**")
