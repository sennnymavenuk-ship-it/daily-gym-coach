# ══════════════════════════════════════════════════════════════
# Daily Gym Coach App
# Built with Streamlit + Groq API (Free)
# ══════════════════════════════════════════════════════════════

import streamlit as st
from groq import Groq

# ── Page Configuration ────────────────────────────────────────
st.set_page_config(
    page_title="Daily Gym Coach 💪",
    page_icon="🏋️",
    layout="centered"
)

# ── Custom CSS Styling ────────────────────────────────────────
st.markdown("""
    <style>
    .main {
        background-color: #0f0f0f;
    }
    .stButton > button {
        background-color: #02C39A;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #028090;
        color: white;
    }
    h1 {
        color: #02C39A;
    }
    h2, h3 {
        color: #0A7EA4;
    }
    </style>
""", unsafe_allow_html=True)

# ── App Header ────────────────────────────────────────────────
st.title("🏋️ Daily Gym Coach")
st.subheader("Your FREE Personal AI Fitness Coach")
st.markdown(
    "Fill in your details below and get a fully "
    "personalised workout plan, nutrition advice "
    "and daily motivation — completely free! 💪"
)
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
        placeholder="e.g. Bad knee, lower back pain "
                    "or type None"
    )

st.markdown("---")

# ── Nutrition Section ─────────────────────────────────────────
st.markdown("### 🍽️ Nutrition Check")

food_today = st.text_area(
    "What have you eaten today?",
    placeholder="e.g. Porridge for breakfast, "
                "chicken salad for lunch, "
                "apple as a snack...",
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

# ── Generate Plan Button ──────────────────────────────────────
generate = st.button(
    "🚀 Generate My Daily Plan!",
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
            "Your coach is preparing your "
            "personalised plan... 💪"
        ):
            try:
                client = Groq(
                    api_key=st.secrets["GROQ_API_KEY"]
                )

                prompt = f"""You are an expert personal 
fitness coach. Create a complete and detailed daily 
fitness plan for this person:

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

Please provide ALL of the following clearly 
and in a friendly motivating way:

🏋️ TODAYS WORKOUT PLAN
List 5 to 7 exercises suitable for their 
level and available equipment.
For each exercise include:
- Exercise name
- Sets and reps
- Rest time between sets
- Body parts worked
- One simple form tip to avoid injury
End with a 5 minute warm up and 
5 minute cool down routine.

🥗 NUTRITION ADVICE
- Review what they have eaten today honestly
- Suggest what to eat for remaining meals
- Include protein, carbs and healthy fats advice
- Suggest hydration improvements if needed
- Keep advice simple and realistic

💪 DAILY MOTIVATION MESSAGE
- Make it personal based on their energy level
- Keep it short, punchy and energising
- End with a powerful one line affirmation

🔄 RECOVERY AND INJURY TIPS
- 3 specific stretches to do after the workout
- Sleep recommendation for their goal
- Any specific advice based on their injuries
- Warning signs to watch out for

Keep everything practical, safe, achievable 
and encouraging throughout."""

                # ── Call Groq API ─────────────────────────────
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    max_tokens=2000,
                    temperature=0.7,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a friendly, "
                            "expert personal fitness coach "
                            "who creates safe, practical and "
                            "motivating workout plans."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                result = response.choices[0].message.content

                # ── Display Results ───────────────────────────
                st.markdown("---")
                st.success("✅ Your Daily Plan is Ready!")
                st.balloons()

                st.markdown(
                    "## 📋 Your Personalised Daily Plan"
                )
                st.markdown(result)

                # ── Download Button ───────────────────────────
                st.markdown("---")
                st.download_button(
                    label="📥 Download My Plan as Text File",
                    data=result,
                    file_name="my_gym_plan_today.txt",
                    mime="text/plain",
                    use_container_width=True
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
                st.info(
                    "Please check your GROQ_API_KEY "
                    "is set correctly in Streamlit secrets"
                )

st.markdown("---")

# ── Chat Section ──────────────────────────────────────────────
st.markdown("### 💬 Ask Your Coach Anything")
st.markdown(
    "Have a question about your workout, "
    "nutrition or fitness? Ask below! 👇"
)

# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box
if user_input := st.chat_input(
        "Ask your coach a question..."):

    # Add user message to history
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

                chat_response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    max_tokens=1000,
                    temperature=0.7,
                    messages=[
                        {
                            "role": "system",
                            "content": """You are a friendly, 
knowledgeable and experienced personal fitness coach. 
Answer all questions about fitness, nutrition, 
recovery and health in a warm, encouraging and 
practical way. Always give specific actionable advice. 
If asked about pain or injuries always recommend 
seeing a qualified medical professional. 
Never give medical diagnoses."""
                        }
                    ] + [
                        {
                            "role": m["role"],
                            "content": m["content"]
                        }
                        for m in st.session_state.messages
                    ]
                )

                reply = (
                    chat_response.choices[0]
                    .message.content
                )

                st.markdown(reply)

                # Add reply to chat history
                st.session_state.messages.append(
                    {"role": "assistant",
                     "content": reply}
                )

            except Exception as e:
                st.error(f"Chat error: {e}")

# ── Clear Chat Button ─────────────────────────────────────────
if st.session_state.messages:
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<center>🏋️ Daily Gym Coach | "
    "Built with ❤️ by Senthil | "
    "Powered by Groq AI | "
    "Completely Free 💪</center>",
    unsafe_allow_html=True
)
