# ══════════════════════════════════════════════════════════════
# Daily Gym Coach App
# Built with Streamlit + Claude API
# ══════════════════════════════════════════════════════════════

import streamlit as st
import anthropic

# ── Page Configuration ────────────────────────────────────────
st.set_page_config(
    page_title="Daily Gym Coach 💪",
    page_icon="🏋️",
    layout="centered"
)

# ── App Title and Description ─────────────────────────────────
st.title("🏋️ Daily Gym Coach")
st.subheader("Your FREE Personal AI Fitness Coach")
st.markdown("---")

# ── User Input Form ───────────────────────────────────────────
st.markdown("### 📋 Tell Me About You")

col1, col2 = st.columns(2)

with col1:
    goal = st.selectbox(
        "🎯 Your Fitness Goal",
        ["Lose Weight", "Build Muscle", 
         "Improve Fitness", "Increase Strength",
         "Improve Flexibility", "General Health"]
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

with col2:
    equipment = st.multiselect(
        "🏋️ Equipment Available",
        ["No equipment (bodyweight only)",
         "Dumbbells", "Barbell", 
         "Resistance bands", "Pull up bar",
         "Treadmill", "Full gym access",
         "Kettlebells", "Exercise bike"],
        default=["No equipment (bodyweight only)"]
    )
    
    energy = st.selectbox(
        "⚡ Energy Level Today",
        ["High — feeling great!",
         "Medium — feeling okay",
         "Low — feeling tired",
         "Very low — exhausted"]
    )
    
    injuries = st.text_input(
        "🩹 Any Injuries? (or type None)",
        placeholder="e.g. Bad knee, lower back pain"
    )

st.markdown("---")
st.markdown("### 🍽️ Nutrition Check")

food_today = st.text_area(
    "What have you eaten today?",
    placeholder="e.g. Porridge for breakfast, "
                "chicken salad for lunch...",
    height=80
)

st.markdown("---")

# ── Generate Button ───────────────────────────────────────────
if st.button("🚀 Generate My Daily Plan!", 
             use_container_width=True,
             type="primary"):
    
    if not equipment:
        st.warning("Please select at least one equipment option!")
    else:
        equipment_str = ", ".join(equipment)
        
        # ── Show loading spinner ──────────────────────────────
        with st.spinner("Your coach is preparing your plan... 💪"):
            
            try:
                client = anthropic.Anthropic(
                    api_key=st.secrets["ANTHROPIC_API_KEY"]
                )
                
                # ── Build the prompt ──────────────────────────
                prompt = f"""You are an expert personal fitness 
coach. Create a complete daily fitness plan for this person:

PROFILE:
- Fitness Goal: {goal}
- Fitness Level: {level}
- Training Days Per Week: {days}
- Equipment Available: {equipment_str}
- Energy Level Today: {energy}
- Injuries or Conditions: {injuries or 'None'}
- Food eaten today: {food_today or 'Not provided'}

Please provide ALL of the following in a clear, 
friendly and motivating way:

1. TODAYS WORKOUT PLAN
   - List 5 to 7 exercises
   - For each exercise include:
     * Sets and reps
     * Rest time
     * Body parts worked
     * Simple form tip
   - Make it suitable for their level and equipment

2. NUTRITION ADVICE
   - Review what they ate today
   - Suggest what to eat for remaining meals
   - Keep it practical and realistic

3. DAILY MOTIVATION MESSAGE
   - Personal and energising
   - Acknowledge their energy level today
   - Short and punchy

4. RECOVERY TIPS
   - 3 stretches to do after workout
   - Sleep and hydration advice
   - Any warnings based on their injuries

Keep everything practical, safe and achievable. 
Use encouraging language throughout."""

                # ── Call Claude API ───────────────────────────
                message = client.messages.create(
                    model="claude-sonnet-4-6",
                    max_tokens=2000,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                
                response = message.content[0].text
                
                # ── Display Results ───────────────────────────
                st.markdown("---")
                st.success("✅ Your Daily Plan is Ready!")
                
                st.markdown("## 📋 Your Personalised Daily Plan")
                st.markdown(response)
                
                # ── Download Button ───────────────────────────
                st.download_button(
                    label="📥 Download My Plan as Text File",
                    data=response,
                    file_name="my_gym_plan_today.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Something went wrong: {e}")
                st.info("Please check your API key is set up correctly")

st.markdown("---")

# ── Chat Section ──────────────────────────────────────────────
st.markdown("### 💬 Ask Your Coach Anything")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt_input := st.chat_input(
        "Ask your coach a question..."):
    
    st.session_state.messages.append(
        {"role": "user", "content": prompt_input})
    
    with st.chat_message("user"):
        st.markdown(prompt_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Coach is thinking..."):
            try:
                client = anthropic.Anthropic(
                    api_key=st.secrets["ANTHROPIC_API_KEY"]
                )
                
                chat_response = client.messages.create(
                    model="claude-sonnet-4-6",
                    max_tokens=1000,
                    system="""You are a friendly, 
knowledgeable personal fitness coach. Answer 
questions about fitness, nutrition, recovery 
and health in a warm, encouraging and practical 
way. If asked about injuries always recommend 
seeing a professional.""",
                    messages=[
                        {"role": m["role"], 
                         "content": m["content"]}
                        for m in st.session_state.messages
                    ]
                )
                
                reply = chat_response.content[0].text
                st.markdown(reply)
                st.session_state.messages.append(
                    {"role": "assistant", 
                     "content": reply})
                     
            except Exception as e:
                st.error(f"Error: {e}")

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ by Senthil | "
    "Powered by Claude AI</center>",
    unsafe_allow_html=True
)
