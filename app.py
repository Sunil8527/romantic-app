import streamlit as st
import os

st.set_page_config(page_title="For My Love ❤️", page_icon="❤️")

# 🎵 Background Music (add your audio file in same folder)
audio_file = open('romantic.mp3', 'rb')
st.audio(audio_file.read(), format='audio/mp3')

st.title("💖 A Special Page Just For You 💖")
st.write("Hey love, I made this just for you 😊")

# 📸 Photo Gallery
st.header("📸 Our Beautiful Memories")

photos = [
    ("photo1.jpg", "Our First Memory ❤️"),
    ("photo2.jpg", "My Favorite Moment 💕"),
    ("photo3.jpg", "Forever Together 💑"),
    ("photo4.jpg", "Another Cute Moment 😍"),
    ("photo5.jpg", "Smiles Together 😊"),
    ("photo6.jpg", "My 1st child ❤️")
]

for img, caption in photos:
    if os.path.exists(img):
        st.image(img, caption=caption)
    else:
        st.warning(f"{img} not found")

# # 🎥 Video Section
# st.header("🎥 Special Videos For You")

# videos = ["video1.mp4", "video2.mp4"]

# for vid in videos:
#     if os.path.exists(vid):
#         video_file = open(vid, 'rb')
#         st.video(video_file.read())
#     else:
#         st.warning(f"{vid} not found")



# Romantic Questions
questions = [
    "What was your first impression of me? 💭",
    "When did you realize you love me? ❤️",
    "What is your favorite memory with me? 🌸",
    "What do you love most about us? 💑",
    "Where do you want to travel together? ✈️",
    "What makes you happiest in our relationship? 😊",
    "One thing you wish we do more together? 💫",
    "Your dream date with me? 🌙"
]

st.header("💌 Answer these for me")

responses = {}

for q in questions:
    responses[q] = st.text_input(q)

if st.button("Submit 💖"):
    st.success("Aww, thank you for answering! I love you ❤️")

    st.subheader("Your Answers 💕")
    for q, ans in responses.items():
        if ans:
            st.write(f"**{q}**")
            st.write(ans)

st.markdown("---")
st.write("Made with ❤️ just for you")
st.write("Pls my love share your answer ss to me on whatsapp")
