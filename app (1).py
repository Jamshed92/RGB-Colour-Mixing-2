import streamlit as st

st.set_page_config(
    page_title="RGB Colour Mixer",
    page_icon="🎨",
    layout="centered",
)

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #777;
        margin-bottom: 25px;
    }
    .colour-box {
        height: 220px;
        border-radius: 18px;
        border: 2px solid rgba(128, 128, 128, 0.25);
        margin: 12px 0 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-title">🎨 RGB Colour Mixer</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">Mix Red, Green and Blue to create your own colours.</div>',
    unsafe_allow_html=True,
)

presets = {
    "Custom Colour": (128, 128, 128),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Orange": (255, 165, 0),
    "Purple": (128, 0, 128),
    "Pink": (255, 105, 180),
}

if "red" not in st.session_state:
    st.session_state.red = 128
    st.session_state.green = 128
    st.session_state.blue = 128


def apply_preset():
    red_value, green_value, blue_value = presets[st.session_state.preset]
    st.session_state.red = red_value
    st.session_state.green = green_value
    st.session_state.blue = blue_value


st.subheader("Choose a colour")
st.selectbox(
    "Colour presets",
    options=list(presets.keys()),
    key="preset",
    on_change=apply_preset,
)

st.subheader("Adjust RGB values")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔴 Red")
    red = st.slider("Red intensity", 0, 255, key="red")

with col2:
    st.markdown("### 🟢 Green")
    green = st.slider("Green intensity", 0, 255, key="green")

with col3:
    st.markdown("### 🔵 Blue")
    blue = st.slider("Blue intensity", 0, 255, key="blue")

hex_colour = f"#{red:02X}{green:02X}{blue:02X}"
rgb_colour = f"rgb({red}, {green}, {blue})"

st.subheader("Your Mixed Colour")
st.markdown(
    f'<div class="colour-box" style="background-color: {hex_colour};"></div>',
    unsafe_allow_html=True,
)

value1, value2 = st.columns(2)
with value1:
    st.markdown("**RGB Code**")
    st.code(rgb_colour, language=None)
with value2:
    st.markdown("**HEX Code**")
    st.code(hex_colour, language=None)

st.color_picker("Colour preview", value=hex_colour, disabled=True)

if st.button("Reset to Default", use_container_width=True):
    st.session_state.red = 128
    st.session_state.green = 128
    st.session_state.blue = 128
    st.session_state.preset = "Custom Colour"
    st.rerun()

st.divider()
st.subheader("How RGB Colour Mixing Works")
st.write(
    "RGB stands for Red, Green and Blue. Each channel has an intensity "
    "between 0 and 255. Mixing these three light colours creates different "
    "colours on digital screens."
)
st.markdown(
    """
    - **Red + Green = Yellow**
    - **Red + Blue = Magenta**
    - **Green + Blue = Cyan**
    - **Red + Green + Blue at maximum = White**
    - **All three colours at zero = Black**
    """
)
st.caption("RGB Colour Mixer | Built with Python and Streamlit")
