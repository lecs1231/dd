import streamlit as st
from PIL import Image
import random
import time

# Fun sound effect (You can replace the file with your own sound)
def play_sound(sound_file):
    st.audio(sound_file)

# App title
st.title("🔥 ROAST ME 🔥")

# Roast Levels
roast_level = st.radio("Choose your roast level:", ('Mild', 'Medium', 'Savage'))

# List of images and roast texts for different roast levels
images = [
    ("1.jpg", {
        "Mild": "You look like you’d offer someone directions... and then get them lost by accident. But at least you're smiling! 😊",
        "Medium": "That turtleneck is tighter than my schedule, but hey, you're ready for winter or to read Sartre in the park! 😏",
        "Savage": "That smile's cute, but those glasses scream, 'I overanalyze everything'—including this roast. And that turtleneck? It’s holding on tighter than my last bit of patience. 😎"
    }),
    ("2.jpg", {
        "Mild": "Your effort is admirable, but your stance says 'I try too hard, but make it look easy.' 😂",
        "Medium": "That pose is saying, 'I don't care,' but those shoes are trying way too hard to keep up with the vibe. 😆",
        "Savage": "Oh, flexing again? Those sneakers are just as confused as I am about why you're on this hill, pretending it's not a photoshoot. 😝"
    }),
    ("3.jpg", {
        "Mild": "Your bag looks like it’s full of compliments because you clearly know how to rock an outfit! 😄",
        "Medium": "Casual, but just enough to say 'I’m kind of a big deal.' 😎",
        "Savage": "Ah, trying to distract us with that oversized bag? Sorry, the roast still burns through! 😂"
    }),
    ("4.jpg", {
        "Mild": "That red shirt really pops! Just like your confidence. 😊",
        "Medium": "You’re giving off 'I didn’t try, but still look great' vibes! 😏",
        "Savage": "That chill pose? It’s like you're ready to crush dreams with just a glance. 😂"
    }),
    ("5.jpg", {
        "Mild": "Oh, that relaxed vibe with the sun hitting you just right! 🌞",
        "Medium": "Those shoes look like they're ready to sprint... away from all responsibilities. 😆",
        "Savage": "Posing like you're auditioning for 'Most Chill Human Alive,' and you're winning! 😂"
    })
]

# State to track the current image index
if 'index' not in st.session_state:
    st.session_state.index = 0

def next_image():
    if st.session_state.index < len(images) - 1:
        st.session_state.index += 1

def prev_image():
    if st.session_state.index > 0:
        st.session_state.index -= 1

# Buttons for next and previous
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("Previous"):
        prev_image()

with col3:
    if st.button("Next"):
        next_image()

# Get the current image and its corresponding roast
image_path, roast_dict = images[st.session_state.index]
roast_text = roast_dict[roast_level]

# Display the image and roast
image = Image.open(image_path)
st.image(image, use_column_width=True)
st.write(roast_text)

# Play a sound effect when the roast is delivered (can use a random sound for fun)
if st.button("Roast me!"):
    play_sound('roast_sound.mp3')  # Replace 'roast_sound.mp3' with your own sound file
    st.write("🔥 That roast hit hard, didn't it?")

# Add reaction emojis
st.write("React to this roast! 😂 😱 🔥 😭")
reaction = st.selectbox("Choose your reaction:", ["", "😂", "😱", "🔥", "😭"])

if reaction:
    st.write(f"You reacted with {reaction}!")

# Option to upload own image for a custom roast
st.write("Want to be roasted? Upload your own image!")
user_image = st.file_uploader("Upload your image here")

if user_image:
    st.image(user_image, use_column_width=True)
    # Play a special sound effect when a custom roast is prepared
    st.write("“Oh, you're brave! Let me prepare a special roast for you...” 🔥")
    play_sound('1.mp3')  # Replace with a different sound for custom roasts
    time.sleep(1)
    st.write("“Ah, I see you’ve mastered the art of uploading... now prepare for the roast of a lifetime!” 😂")

# Credits and Footer
st.markdown("""
    ---
    Created with ❤️ by lexx.
    """)
