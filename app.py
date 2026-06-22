# ══════════════════════════════════════════════════════════════
# Daily Gym Coach App
# Dark Theme + Interactive Colors
# Built with Streamlit + Groq API (Free)
# ══════════════════════════════════════════════════════════════

import streamlit as st
from groq import Groq

# ── Page Configuration ────────────────────────────────────────
st.set_page_config(
    page_title="Daily Gym Coach 💪",
    page_icon="🏋️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── Full Dark Theme CSS ───────────────────────────────────────
st.markdown("""
<style>
/* ── Main Background ── */
.stApp {
    background-color: #0A0A0A;
    color: #FFFFFF;
}

/* ── Main content area ── */
.main .block-container {
    background-color: #0A0A0A;
    padding-top: 2rem;
}

/* ── Title styling ── */
h1 {
    color: #02C39A !important;
    text-align: center;
    font-size: 3rem !important;
    font-weight: 900 !important;
    text-shadow: 0 0 20px #02C39A;
    letter-spacing: 2px;
}

h2 {
    color: #0A7EA4 !important;
    border-left: 4px solid #02C39A;
    padding-left: 10px;
}

h3 {
    color: #02C39A !important;
    font-size: 1.2rem !important;
}

/* ── Subheader ── */
.stApp p {
    color: #CCCCCC;
}

/* ── Select boxes ── */
.stSelectbox > div > div {
    background-color: #1A1A2E !important;
    color: #FFFFFF !important;
    border: 1px solid #02C39A !important;
    border-radius: 8px !important;
}

.stSelectbox > div > div:hover {
    border-color: #0A7EA4 !important;
    box-shadow: 0 0 10px #02C39A55 !important;
}

/* ── Multiselect ── */
.stMultiSelect > div > div {
    background-color: #1A1A2E !important;
    border: 1px solid #028090 !important;
    border-radius: 8px !important;
    color: #FFFFFF !important;
}

.stMultiSelect > div > div:hover {
    border-color: #02C39A !important;
    box-shadow: 0 0 10px #02C39A55 !important;
}

/* ── Multiselect tags ── */
.stMultiSelect span {
    background-color: #028090 !important;
    color: #FFFFFF !important;
    border-radius: 5px !important;
}

/* ── Text input ── */
.stTextInput > div > div > input {
    background-color: #1A1A2E !important;
    color: #FFFFFF !important;
    border: 1px solid #0A7EA4 !important;
    border-radius: 8px !important;
}

.stTextInput > div > div > input:focus {
    border-color: #02C39A !important;
    box-shadow: 0 0 10px #02C39A55 !important;
}

/* ── Text area ── */
.stTextArea > div > div > textarea {
    background-color: #1A1A2E !important;
    color: #FFFFFF !important;
    border: 1px solid #0A7EA4 !important;
    border-radius: 8px !important;
}

.stTextArea > div > div > textarea:focus {
    border-color: #02C39A !important;
    box-shadow: 0 0 10px #02C39A55 !important;
}

/* ── Number input ── */
.stNumberInput > div > div > input {
    background-color: #1A1A2E !important;
    color: #FFFFFF !important;
    border: 1px solid #0A7EA4 !important;
    border-radius: 8px !important;
}

/* ── Generate button ── */
.stButton > button {
    background: linear-gradient(
        135deg, #02C39A, #0A7EA4
    ) !important;
    color: #FFFFFF !important;
    font-size: 20px !important;
    font-weight: 900 !important;
    border-radius: 12px !important;
    padding: 15px !important;
    border: none !important;
    letter-spacing: 1px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px #02C39A55 !important;
}

.stButton > button:hover {
    background: linear-gradient(
        135deg, #0A7EA4, #02C39A
    ) !important;
    box-shadow: 0 6px 25px #02C39A99 !important;
    transform: translateY(-2px) !important;
}

/* ── Download button ── */
.stDownloadButton > button {
    background-color: #1A1A2E !important;
    color: #02C39A !important;
    border: 2px solid #02C39A !important;
    border-radius: 10px !important;
    font-weight: bold !important;
    transition: all 0.3s ease !important;
}

.stDownloadButton > button:hover {
    background-color: #02C39A !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 15px #02C39A55 !important;
}

/* ── Success message ── */
.stSuccess {
    background-color: #0D2B1F !important;
    border: 1px solid #02C39A !important;
    border-radius: 10px !important;
    color: #02C39A !important;
}

/* ── Warning message ── */
.stWarning {
    background-color: #2B1F0D !important;
    border: 1px solid #F0C040 !important;
    border-radius: 10px !important;
}

/* ── Error message ── */
.stError {
    background-color: #2B0D0D !important;
    border: 1px solid #E74C3C !important;
    border-radius: 10px !important;
}

/* ── Info message ── */
.stInfo {
    background-color: #0D1F2B !important;
    border: 1px solid #0A7EA4 !important;
    border-radius: 10px !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: #02C39A !important;
}

/* ── Chat input ── */
.stChatInput > div {
    background-color: #1A1A2E !important;
    border: 1px solid #0A7EA4 !important;
    border-radius: 12px !important;
}

.stChatInput input {
    color: #FFFFFF !important;
    background-color: #1A1A2E !important;
}

.stChatInput input:focus {
    border-color: #02C39A !important;
}

/* ── Chat messages ── */
.stChatMessage {
    background-color: #1A1A2E !important;
    border-radius: 12px !important;
    border: 1px solid #222244 !important;
    margin-bottom: 10px !important;
}

/* ── User chat bubble ── */
[data-testid="stChatMessageContent"] {
    color: #FFFFFF !important;
}

/* ── Divider ── */
hr {
    border-color: #02C39A33 !important;
}

/* ── Labels ── */
.stSelectbox label,
.stMultiSelect label,
.stTextInput label,
.stTextArea label,
.stNumberInput label {
    color: #02C39A !important;
    font-weight: bold !important;
    font-size: 0.95rem !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-track {
    background: #0A0A0A;
}
::-webkit-scrollbar-thumb {
    background: #02C39A;
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: #0A7EA4;
}

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background-color: #1A1A2E !important;
    border: 1px solid #02C39A !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

/* ── Sidebar ── */
.css-1d391kg {
    background-color: #0D0D1A !important;
}
</style>
""", unsafe_allow_html=True)

# ── Glowing Header ────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding: 20px 0;'>
    <h1 style='color:#02C39A; 
               font-size:3rem; 
               font-weight:900;
               text-shadow: 0 0 30px #02C39A;
               letter-spacing:3px;'>
        🏋️ DAILY GYM COACH
    </h1>
    <p style='color:#888888; 
              font-size:1.1rem;
              letter-spacing:2px;'>
        YOUR FREE PERSONAL AI FITNESS COACH
    </p>
    <p style='color:#02C39A; font-size:0.9rem;'>
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    </p>
</div>
""", unsafe_allow_html=True)

# ── Stats Row ─────────────────────────────────────────────────
col_s1, col_s2, col_s3, col_s4 = st.columns(4)
with col_s1:
    st.metric("💪 Workouts", "Free")
with col_s2:
    st.metric("🥗 Nutrition", "Included")
with col_s3:
    st.metric("🔥 Motivation", "Daily")
with col_s4:
    st.metric("💬 Coach Chat", "24/7")

st.markdown("---")

# ── User Input Form ───────────────────────────────────────────
st.markdown("### 📋 Tell Me About You")

col1, col2 = st.columns(2)

with col1:
    goal = st.selectbox(
        "🎯 Your Fitness Goal",
        [
            "Lose Weight",
            "Build Muscle",
            "Improve Fitness",
            "Increase Strength",
            "Improve Flexibility",
            "General Health"
        ]
    )

    level = st.selectbox(
        "📊 Your Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    days = st.selectbox(
        "📅 Training Days Per Week",
        ["2 days", "3 days", "4 days",
         "5 days", "6 days"]
    )

    age = st.number_input(
        "🎂 Your Age",
        min_value=16,
        max_value=80,
        value=30
    )

with col2:
    equipment = st.multiselect(
        "🏋️ Equipment Available",
        [
            "No equipment (bodyweight only)",
            "Dumbbells",
            "Barbell",
            "Resistance bands",
            "Pull up bar",
            "Treadmill",
            "Full gym access",
            "Kettlebells",
            "Exercise bike"
        ],
        default=["No equipment (bodyweight only)"]
    )

    energy = st.selectbox(
        "⚡ Energy Level Today",
        [
            "High — feeling great!",
            "Medium — feeling okay",
            "Low — feeling tired",
            "Very low — exhausted"
        ]
    )

    gender = st.selectbox(
        "👤 Gender",
        ["Male", "Female", "Prefer not to say"]
    )

    injuries = st.text_input(
        "🩹 Any Injuries or Health Conditions?",
        placeholder="e.g. Bad knee or type None"
    )

st.markdown("---")
st.markdown("### 🍽️ Nutrition Check")

food_today = st.text_area(
    "What have you eaten today?",
    placeholder="e.g. Porridge for breakfast, "
                "chicken salad for lunch...",
    height=80
)

water = st.selectbox(
    "💧 How much water have you drunk today?",
    [
        "Less than 1 litre",
        "About 1 litre",
        "About 1.5 litres",
        "2 litres or more"
    ]
)

st.markdown("---")

# ── Generate Button ───────────────────────────────────────────
generate = st.button(
    "🚀 GENERATE MY DAILY PLAN!",
    use_container_width=True,
    type="primary"
)

if generate:
    if not equipment:
        st.warning(
            "⚠️ Please select at least "
            "one equipment option!"
        )
    else:
        equipment_str = ", ".join(equipment)

        with st.spinner(
            "🔥 Your coach is building your "
            "personalised plan..."
        ):
            try:
                client = Groq(
                    api_key=st.secrets["GROQ_API_KEY"]
                )

                prompt = f"""You are an expert personal 
fitness coach. Create a complete daily fitness plan:

PROFILE:
- Age: {age}
- Gender: {gender}
- Fitness Goal: {goal}
- Fitness Level: {level}
- Training Days Per Week: {days}
- Equipment Available: {equipment_str}
- Energy Level Today: {energy}
- Injuries or Conditions: {injuries or 'None'}
- Food eaten today: {food_today or 'Not provided'}
- Water intake today: {water}

Please provide ALL of the following:

🏋️ TODAYS WORKOUT PLAN
List 5 to 7 exercises. For each include:
- Exercise name
- Sets and reps
- Rest time
- Body parts worked
- One form tip
End with warm up and cool down.

🥗 NUTRITION ADVICE
- Review todays food honestly
- Suggest remaining meals
- Protein, carbs and fats advice
- Hydration tips

💪 DAILY MOTIVATION
- Personal to their energy level
- Short and punchy
- Powerful one line affirmation

🔄 RECOVERY TIPS
- 3 stretches after workout
- Sleep recommendation
- Injury specific advice

Keep everything practical, safe and motivating."""

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    max_tokens=2000,
                    temperature=0.7,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a friendly "
                            "expert personal fitness coach."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                result = (
                    response.choices[0].message.content
                )

                st.markdown("---")
                st.success(
                    "✅ Your Daily Plan is Ready!"
                )
                st.balloons()

                st.markdown("""
<div style='background: linear-gradient(
    135deg, #0D2B1F, #0D1F2B);
    border: 1px solid #02C39A;
    border-radius: 15px;
    padding: 20px;
    margin: 10px 0;'>
""", unsafe_allow_html=True)

                st.markdown(
                    "## 📋 Your Personalised Daily Plan"
                )
                st.markdown(result)
                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

                st.markdown("---")
                st.download_button(
                    label="📥 Download My Plan",
                    data=result,
                    file_name="my_gym_plan_today.txt",
                    mime="text/plain",
                    use_container_width=True
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
                st.info(
                    "Check your GROQ_API_KEY "
                    "in Streamlit secrets"
                )

st.markdown("---")

# ── Chat Section ──────────────────────────────────────────────
st.markdown("### 💬 Ask Your Coach Anything")
st.markdown(
    "<p style='color:#888;'>Have a question? "
    "Your AI coach is here 24/7 👇</p>",
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input(
        "Ask your coach anything..."):

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Coach is thinking... 🤔"):
            try:
                client = Groq(
                    api_key=st.secrets["GROQ_API_KEY"]
                )

                chat_response = (
                    client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        max_tokens=1000,
                        temperature=0.7,
                        messages=[
                            {
                                "role": "system",
                                "content": """You are a 
friendly expert personal fitness coach. Give warm, 
practical and motivating advice. For injuries always 
recommend seeing a medical professional."""
                            }
                        ] + [
                            {
                                "role": m["role"],
                                "content": m["content"]
                            }
                            for m in
                            st.session_state.messages
                        ]
                    )
                )

                reply = (
                    chat_response.choices[0]
                    .message.content
                )
                st.markdown(reply)
                st.session_state.messages.append(
                    {"role": "assistant",
                     "content": reply}
                )

            except Exception as e:
                st.error(f"Chat error: {e}")

if st.session_state.messages:
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; 
            padding: 20px;
            color: #444444;'>
    <p style='color:#02C39A; 
              font-weight:bold;
              letter-spacing:2px;'>
        🏋️ DAILY GYM COACH
    </p>
    <p style='font-size:0.8rem;'>
        Built with ❤️ by Senthil | 
        Powered by Groq AI | 
        Completely Free 💪
    </p>
    <p style='font-size:0.75rem; color:#333;'>
        Always consult a doctor before 
        starting any new fitness programme
    </p>
</div>
""", unsafe_allow_html=True)
