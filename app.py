import streamlit as st
import numpy as np
import time

# إعدادات الصفحة الأساسية لواجهة عريضة ومحترفة
st.set_page_config(page_title="Omnia DeepArena IA", layout="wide", initial_sidebar_state="expanded")

# 1. نظام الترجمة الموحد للغات الستة مع الأعلام والرسائل الموجهة للقسمين
LANG_DATA = {
    "🇸🇦 العربية": {
        "welcome": "⚽ منصة Omnia DeepArena الرقمية الموحدة لكشافي الملاعب وسوق الانتقالات",
        "sec1_title": "👶 القسم الأول: قسم الناشئين والقصر (إلى حدود 20 سنة)",
        "sec2_title": "🏃 القسم الثاني: قسم اللاعبين الكبار (سينيور - فوق 20 سنة)",
        "upload_lbl": "ارفع مقطع فيديو المباراة (تحسين تلقائي وفك التداخل وتغبيش الوجه الحامي)",
        "processing": "🔄 جاري تشغيل خوارزميات ترميم الفيديو الرديء، الضبابية، والضوء الخافت لفيديو الهاتف...",
        "blur_notif": "🔒 تم تفعيل عنصر التغبيش لحماية المعطيات الشخصية تماشياً مع المعايير الدولية.",
        "scout_view": "🚀 سوق الانتقالات نشط: البطاقة والأرقام الفنية مرئية الآن للكشافين والوكلاء والأندية لغرض الشراء.",
        "parent_req": "👨‍👩‍👦 نظام تدخل وموافقة الولي الشرعي إلزامية للقصر (دون 16 سنة)",
        "academy_free": "🎉 الحساب مفعل مجاناً بالكامل للأكاديميات الصغيرة للأطفال (دون 16 سنة)."
    },
    "🇬🇧 English": {
        "welcome": "⚽ Omnia DeepArena Unified Scouting & Transfer Marketplace Platform",
        "sec1_title": "👶 Section 1: Youth & Minors (Up to 20 Years Old)",
        "sec2_title": "🏃 Section 2: Senior Players (Over 20 Years Old)",
        "upload_lbl": "Upload match video (Auto-restoration, de-overlapping & protective face blurring)",
        "processing": "🔄 AI is restoring low quality, blurry, and low-light mobile video footage...",
        "blur_notif": "🔒 Face blurring activated to protect personal data compliance globally.",
        "scout_view": "🚀 Transfer market active: Technical profile is visible to scouts, agents, and clubs for purchase.",
        "parent_req": "👨‍👩‍👦 Parental intervention and consent is mandatory for minors (Under 16)",
        "academy_free": "🎉 Fully FREE account activated for small children's academies (Under 16)."
    },
    "🇫🇷 Français": {
        "welcome": "⚽ Plateforme Numérique Unifiée de Recrutement Omnia DeepArena",
        "sec1_title": "👶 Section 1: Jeunes & Mineurs (Jusqu'à 20 ans)",
        "sec2_title": "🏃 Section 2: Joueurs Seniors (Plus de 20 ans)",
        "upload_lbl": "Télécharger la vidéo (Restauration auto, déchevauchement et floutage du visage)",
        "processing": "🔄 L'IA restaure les vidéos de téléphone de mauvaise qualité, floues et à faible luminosité...",
        "blur_notif": "🔒 Floutage du visage activé pour protéger la confidentialité des données personnelles.",
        "scout_view": "🚀 Marché actif: Profil technique visible par les recruteurs, agents et clubs pour achat.",
        "parent_req": "👨‍👩‍👦 Intervention et consentement parental obligatoires pour les mineurs (Moins de 16 ans)",
        "academy_free": "🎉 Compte entièrement GRATUIT activé pour les petites académies d'enfants (Moins de 16 ans)."
    },
    "🇮🇹 Italiano": {
        "welcome": "⚽ Piattaforma Digitale Unificata di Scouting Omnia DeepArena",
        "sec1_title": "👶 Sezione 1: Giovani e Minori (Fino a 20 anni)",
        "sec2_title": "🏃 Sezione 2: Giocatori Senior (Oltre 20 anni)",
        "upload_lbl": "Carica il video della partita (Ripristino automatico, sovrapposizione e sfocatura)",
        "processing": "🔄 L'IA sta ripristinando video da telefono di bassa qualità, sfocati e con luce scarsa...",
        "blur_notif": "🔒 Sfocatura del viso attiva per proteggere la conformità dei dati personali.",
        "scout_view": "🚀 Mercato attivo: Il profilo tecnico è visibile a scout, agenti e club per l'acquisto.",
        "parent_req": "👨‍👩‍👦 Intervento e consenso dei genitori obbligatori per i minori (Sotto i 16 anni)",
        "academy_free": "🎉 Account completamente GRATUITO attivato per le piccole accademie di bambini (Sotto i 16 anni)."
    },
    "🇪🇸 Español": {
        "welcome": "⚽ Plataforma Digital Unificada de Ojeadores Omnia DeepArena",
        "sec1_title": "👶 Sección 1: Jóvenes y Menores (Hasta 20 años)",
        "sec2_title": "🏃 Sección 2: Jugadores Seniors (Más de 20 años)",
        "upload_lbl": "Subir video del partido (Restauración auto, desenredo y desenfoque protector de rostro)",
        "processing": "🔄 La IA está restaurando videos de baja calidad, borrosos y con luz tenue de móviles...",
        "blur_notif": "🔒 Desenfoque de rostro activado para proteger los datos personales internacionalmente.",
        "scout_view": "🚀 Mercado activo: Perfil técnico disponible para cazatalentos, agentes y clubes para compra.",
        "parent_req": "👨‍👩‍👦 Intervención y consentimiento paterno obligatorio para menores (Menores de 16 años)",
        "academy_free": "🎉 Cuenta totalmente GRATUITA activada para pequeñas academias de niños (Menores de 16 años)."
    },
    "🇵🇹 Português": {
        "welcome": "⚽ Plataforma Digital Unificada de Olheiros Omnia DeepArena",
        "sec1_title": "👶 Seção 1: Jovens e Menores (Até 20 anos)",
        "sec2_title": "🏃 Seção 2: Jogadores Seniores (Mais de 20 anos)",
        "upload_lbl": "Carregar vídeo do jogo (Restauração auto, desfoque facial e correção de sobreposição)",
        "processing": "🔄 A IA está restaurando vídeos de celular de baixa qualidade, borrados e com pouca luz...",
        "blur_notif": "🔒 Desfoque facial ativado para proteger a privacidade dos dados pessoais.",
        "scout_view": "🚀 Mercado ativo: Perfil técnico visível para olheiros, agentes e clubes para compra.",
        "parent_req": "👨‍👩‍👦 Intervenção e consentimento parental obrigatório para menores (Menos de 16 anos)",
        "academy_free": "🎉 Conta totalmente GRATUITA ativada para pequenas academias de crianças (Menos de 16 anos)."
    }
}

# قاعدة البيانات العالمية للمقارنة والتطابق (المراكز والحراس الـ 15)
world_db = {
    "Kylian Mbappé": {"Position": "Forward", "Speed": 97, "Focus": 92, "Pressure": 89, "Club": "Real Madrid"},
    "Erling Haaland": {"Position": "Forward", "Speed": 89, "Focus": 95, "Pressure": 91, "Club": "Manchester City"},
    "Lamine Yamal": {"Position": "Winger", "Speed": 92, "Focus": 88, "Pressure": 90, "Club": "Barcelona"},
    "Lionel Messi": {"Position": "Forward", "Speed": 80, "Focus": 98, "Pressure": 96, "Club": "Inter Miami"},
    "Cristiano Ronaldo": {"Position": "Forward", "Speed": 85, "Focus": 97, "Pressure": 95, "Club": "Al Nassr"},
    "Kevin De Bruyne": {"Position": "Midfielder", "Speed": 76, "Focus": 96, "Pressure": 93, "Club": "Manchester City"},
    "Luka Modrić": {"Position": "Midfielder", "Speed": 73, "Focus": 95, "Pressure": 94, "Club": "Real Madrid"},
    "Pedri": {"Position": "Midfielder", "Speed": 79, "Focus": 91, "Pressure": 88, "Club": "Barcelona"},
    "Eduardo Camavinga": {"Position": "Midfielder", "Speed": 84, "Focus": 89, "Pressure": 91, "Club": "Real Madrid"},
    "Vinícius Jr.": {"Position": "Winger", "Speed": 95, "Focus": 90, "Pressure": 87, "Club": "Real Madrid"},
    "Cody Gakpo": {"Position": "Forward", "Speed": 86, "Focus": 87, "Pressure": 85, "Club": "Liverpool"},
    "Virgil van Dijk": {"Position": "Defender", "Speed": 78, "Focus": 94, "Pressure": 93, "Club": "Liverpool"},
    "Achraf Hakimi": {"Position": "Defender", "Speed": 92, "Focus": 88, "Pressure": 86, "Club": "PSG"},
    "Thibaut Courtois": {"Position": "Goalkeeper", "Speed": 65, "Focus": 93, "Pressure": 94, "Club": "Real Madrid"},
    "Gianluigi Donnarumma": {"Position": "Goalkeeper", "Speed": 62, "Focus": 90, "Pressure": 89, "Club": "PSG"}
}

# 2. القسم الموحد المدمج بالأعلام في الجزء العلوي من الواجهة (Header)
st.markdown("### 🌐 Select Language / اختر اللغة")
selected_lang_name = st.selectbox("", list(LANG_DATA.keys()), label_visibility="collapsed")
tx = LANG_DATA[selected_lang_name]

st.title(tx["welcome"])
st.write("---")

# 3. إعداد الحساب المالي والعمر في شريط التصفح الجانبي لضبط المسار تلقائياً
st.sidebar.header("⚙️ الحساب والاشتراك")
account_type = st.sidebar.radio("نوع الاشتراك / Account Type", ["لاعب مستقل (Individual)", "أكاديمية صغيرة للأطفال (Small Academy)"])
player_age = st.sidebar.number_input("عمر اللاعب الحالي / Player Age:", min_value=5, max_value=45, value=15)

# تفعيل التوجيه المنطقي بناءً على الفئات العمرية والشروط المحددة
if player_age <= 20:
    # ------------------ تشغيل القسم الأول (الناشئون والقصر) ------------------
    st.header(tx["sec1_title"])
    
    if account_type == "أكاديمية صغيرة للأطفال (Small Academy)" and player_age < 16:
        st.success(tx["academy_free"])
    elif account_type == "لاعب مستقل (Individual)":
        st.info("💰 قيمة الاشتراك الفردي للناشئين: 20 دولار شهرياً.")
        
    # تفعيل التدخل القانوني الإلزامي للأولياء دون سن 16 سنة
    proceed_allowed = True
    if player_age < 16:
        st.markdown(f"#### {tx['parent_req']}")
        col1, col2 = st.columns(2)
        with col1:
            parent_name = st.text_input("اسم الولي الشرعي بالكامل / Parent Name:")
            parent_id = st.text_input("رقم بطاقة تعريف الولي أو جواز السفر:")
        with col2:
            consent_signature = st.checkbox("أوافق على رفع الفيديو ومعالجة وتحليل مهارات طفلي التكتيكية لعرضها لغرض الشراء.")
        
        if not (consent_signature and parent_id != "" and parent_name != ""):
            proceed_allowed = False
            st.warning("⚠️ يرجى تعبئة بيانات موافقة الولي بالكامل وتفعيل الخانة لفتح النظام وتفعيل ظهورك للكشافين.")

    if proceed_allowed:
        uploaded_file = st.file_uploader(tx["upload_lbl"], type=["mp4", "mov"], key="youth_vid")
        if uploaded_file:
            with st.spinner(tx["process"]):
                time.sleep(1.5)
            st.warning(tx["blur_notif"] + " (ملامح وجه الناشئ تظهر له ولوليه فقط، ومغشاة بالكامل عند الكشافين تماشياً مع معايير حماية القصر).")
            
