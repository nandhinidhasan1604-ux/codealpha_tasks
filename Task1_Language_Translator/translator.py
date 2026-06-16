import streamlit as st
import requests
from gtts import gTTS
import base64
import streamlit.components.v1 as components

st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="centered")

# ===== INJECT BACKGROUND ANIMATION =====
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        background: linear-gradient(125deg, #0d0221, #0a1628, #130428);
        overflow: hidden;
        width: 100vw;
        height: 100vh;
    }
    canvas {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
    }
</style>
</head>
<body>
<canvas id="canvas"></canvas>
<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });

    const particles = [];
    const colors = ['#00c6ff', '#a855f7', '#0072ff', '#ff6b6b', '#ffffff'];

    for (let i = 0; i < 150; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 3 + 0.5,
            color: colors[Math.floor(Math.random() * colors.length)],
            speedX: (Math.random() - 0.5) * 0.6,
            speedY: (Math.random() - 0.5) * 0.6,
            alpha: Math.random()
        });
    }

    const shoots = [];
    function addShoot() {
        shoots.push({
            x: -200,
            y: Math.random() * canvas.height * 0.7,
            len: Math.random() * 200 + 100,
            speed: Math.random() * 10 + 6,
            alpha: 1
        });
    }
    setInterval(addShoot, 1500);

    function animate() {
        ctx.fillStyle = 'rgba(13, 2, 33, 0.2)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        particles.forEach(p => {
            p.x += p.speedX;
            p.y += p.speedY;
            p.alpha += (Math.random() - 0.5) * 0.03;
            p.alpha = Math.max(0.05, Math.min(1, p.alpha));

            if (p.x < 0) p.x = canvas.width;
            if (p.x > canvas.width) p.x = 0;
            if (p.y < 0) p.y = canvas.height;
            if (p.y > canvas.height) p.y = 0;

            ctx.save();
            ctx.globalAlpha = p.alpha;
            ctx.fillStyle = p.color;
            ctx.shadowColor = p.color;
            ctx.shadowBlur = 8;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        });

        for (let i = shoots.length - 1; i >= 0; i--) {
            const s = shoots[i];
            ctx.save();
            ctx.globalAlpha = s.alpha;
            const grad = ctx.createLinearGradient(s.x - s.len, s.y, s.x, s.y);
            grad.addColorStop(0, 'transparent');
            grad.addColorStop(1, '#00c6ff');
            ctx.strokeStyle = grad;
            ctx.lineWidth = 2.5;
            ctx.shadowColor = '#00c6ff';
            ctx.shadowBlur = 10;
            ctx.beginPath();
            ctx.moveTo(s.x - s.len, s.y + 15);
            ctx.lineTo(s.x, s.y);
            ctx.stroke();
            ctx.restore();

            s.x += s.speed;
            s.alpha -= 0.006;

            if (s.x > canvas.width + 200 || s.alpha <= 0) {
                shoots.splice(i, 1);
            }
        }

        requestAnimationFrame(animate);
    }
    animate();
</script>
</body>
</html>
""", height=0, scrolling=False)

# ===== CSS FOR STREAMLIT UI =====
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

    * { font-family: 'Poppins', sans-serif; }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(125deg, #0d0221, #0a1628, #130428) !important;
    }

    [data-testid="stHeader"] { background: transparent !important; }

    .main-title {
        text-align: center;
        font-size: 50px;
        font-weight: 800;
        background: linear-gradient(90deg, #00c6ff, #a855f7, #ff6b6b, #00c6ff);
        background-size: 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: titleShift 4s ease infinite;
        margin-bottom: 5px;
    }

    @keyframes titleShift {
        0%   { background-position: 0%; }
        50%  { background-position: 100%; }
        100% { background-position: 0%; }
    }

    .subtitle {
        text-align: center;
        color: #a0aec0;
        font-size: 15px;
        margin-bottom: 20px;
    }

    .glass-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 24px;
        padding: 30px;
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 40px rgba(0,0,0,0.4);
    }

    .stTextArea textarea {
        background: rgba(5,5,30,0.95) !important;
        color: #00e5ff !important;
        border-radius: 12px !important;
        border: 1.5px solid rgba(0,198,255,0.5) !important;
        font-size: 16px !important;
        caret-color: #00c6ff !important;
    }

    .stTextArea textarea::placeholder {
        color: rgba(0,229,255,0.4) !important;
    }

    .stTextArea textarea:focus {
        border: 1.5px solid #00c6ff !important;
        box-shadow: 0 0 15px rgba(0,198,255,0.3) inset !important;
    }

    .stSelectbox > div > div {
        background: rgba(5,5,30,0.95) !important;
        color: #00e5ff !important;
        border-radius: 12px !important;
        border: 1.5px solid rgba(0,198,255,0.5) !important;
    }

    label, p { color: #a0aec0 !important; }

    .stButton > button {
        background: linear-gradient(90deg, #00c6ff, #0072ff, #a855f7) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        width: 100% !important;
        border: none !important;
        padding: 14px !important;
        transition: all 0.3s ease !important;
        animation: btnPulse 3s ease infinite !important;
    }

    @keyframes btnPulse {
        0%, 100% { box-shadow: 0 4px 20px rgba(0,114,255,0.5); }
        50%       { box-shadow: 0 4px 35px rgba(168,85,247,0.8); }
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
    }

    .result-box {
        background: rgba(0,198,255,0.08);
        border-left: 4px solid #00c6ff;
        border-radius: 16px;
        padding: 20px;
        color: #e0f7ff !important;
        font-size: 18px;
        margin-top: 15px;
        animation: fadeIn 0.5s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    hr { border-color: rgba(255,255,255,0.1) !important; }
    footer { visibility: hidden; }

    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: #0d0221; }
    ::-webkit-scrollbar-thumb { background: #00c6ff; border-radius: 3px; }
    </style>
""", unsafe_allow_html=True)

# ===== TRANSLATION FUNCTION =====
def translate_text(text, source, target):
    url = "https://api.mymemory.translated.net/get"
    params = {"q": text, "langpair": f"{source}|{target}"}
    response = requests.get(url, params=params)
    data = response.json()
    return data["responseData"]["translatedText"]

# ===== LANGUAGES =====
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Arabic": "ar",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn"
}

gtts_lang = {
    "en": "en", "ta": "ta", "hi": "hi", "fr": "fr",
    "es": "es", "de": "de", "ja": "ja", "ar": "ar",
    "te": "te", "ml": "ml", "kn": "kn"
}

# ===== UI =====
st.markdown('<div class="main-title">🌐 Language Translator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">✨ Powered by MyMemory API • 12 Languages • Voice Support</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("🔤 Translate FROM:", list(languages.keys()))
with col2:
    target = st.selectbox("🌍 Translate TO:", list(languages.keys()))

text = st.text_area("✏️ Enter text here:", height=150,
                    placeholder="Type something to translate...")

if st.button("🚀 Translate Now"):
    if text.strip():
        if source == target:
            st.warning("⚠️ Source and Target language are the same!")
        else:
            with st.spinner("✨ Translating via MyMemory API..."):
                try:
                    result = translate_text(
                        text,
                        languages[source],
                        languages[target]
                    )

                    st.markdown(
                        f'<div class="result-box">📝 <b>Translated Text:</b><br><br>{result}</div>',
                        unsafe_allow_html=True)

                    st.markdown("---")
                    col3, col4 = st.columns(2)

                    with col3:
                        st.markdown("📋 **Copy Text:**")
                        st.code(result, language="")

                    with col4:
                        target_code = languages[target]
                        if target_code in gtts_lang:
                            tts = gTTS(text=result, lang=gtts_lang[target_code])
                            tts.save("output.mp3")
                            with open("output.mp3", "rb") as f:
                                audio_data = f.read()
                            b64 = base64.b64encode(audio_data).decode()
                            audio_html = f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
                            st.markdown("🔊 **Listen:**")
                            st.markdown(audio_html, unsafe_allow_html=True)
                        else:
                            st.info("🔊 Audio not available for this language")

                except Exception as e:
                    st.error(f"❌ Translation failed! Check internet. Error: {e}")
    else:
        st.warning("⚠️ Please enter some text!")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#555;margin-top:20px;font-size:13px;">Built with ❤️ using MyMemory Translation API & Streamlit</p>', unsafe_allow_html=True)
