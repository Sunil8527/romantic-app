import streamlit as st
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import io

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




# 🎥 Video Section
st.header("🎥 Special Videos For You")

videos = ["video1.mp4"]

for vid in videos:
    if os.path.exists(vid):
        video_file = open(vid, 'rb')
        st.video(video_file.read())
    else:
        st.warning(f"{vid} not found")



# Romantic Questions
questions = [
    "What was your first impression of me? 💭",
    "When did you realize you love me? ❤️",
    "What is your favorite memory with me? 🌸",
    "How much you love me darling? 💑",
    "Where do you want to travel together? ✈️",
    "Tell me about our 1st night how was your experience? 😊",
    "One thing you wish we do more together? 💫",
    "How romanctic you are with me ? 🌙"
]

st.header("💌 Answer these for me")

responses = {}

for q in questions:
    responses[q] = st.text_input(q)

if st.button("Submit 💖"):
    st.success("Aww, thank you for answering! I love you ❤️")

    st.subheader("Your Answers 💕")

    text_data = "💖 Your Lovely Answers 💖\n\n"
    text_data += f"Date: {datetime.now()}\n\n"

    for q, ans in responses.items():
        if ans:
            st.write(f"**{q}**")
            st.write(ans)
            text_data += f"{q}\n{ans}\n\n"

# 🖼️ Create PNG image
    img = Image.new('RGB', (800, 1000), color=(255, 240, 245))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    y_text = 20
    for line in text_data.split("\n"):
        draw.text((20, y_text), line, fill=(0, 0, 0), font=font)
        y_text += 30

    # Save to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # 📥 Download button for PNG
    st.download_button(
        label="📥 Download as Image 💖",
        data=img_bytes,
        file_name="love_answers.png",
        mime="image/png"
    )

st.markdown("---")
st.write("Made with ❤️ just for you")

