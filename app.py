import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="FiberX - Textile Fiber Explorer",
    page_icon="🧶",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Styling (Navy, Teal, White, Gradient palette + Tabs & Comparison)
st.markdown("""
<style>
/* Font and global typography */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.stApp {
    background-color: #0B1120;
    color: #F8FAFC;
}

.block-container {
    max-width: 860px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Header Navbar */
.fx-navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 24px;
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
    border: 1px solid #334155;
    border-radius: 16px;
    margin-bottom: 20px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}

.fx-brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.fx-brand-logo {
    font-size: 26px;
    line-height: 1;
}

.fx-brand-text {
    font-size: 22px;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #FFFFFF;
}

.fx-badge {
    background: rgba(20, 184, 166, 0.15);
    color: #2DD4BF;
    border: 1px solid rgba(45, 212, 191, 0.4);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.4px;
}

/* Hero Section */
.fx-hero {
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 65%, #0D3B3A 100%);
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 24px 26px;
    margin-bottom: 22px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.2);
}

.fx-hero-tag {
    color: #2DD4BF;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.fx-hero-title {
    color: #FFFFFF;
    font-size: 26px;
    font-weight: 700;
    margin: 0 0 8px 0;
    letter-spacing: -0.4px;
}

.fx-hero-desc {
    color: #94A3B8;
    font-size: 14px;
    line-height: 1.6;
    margin: 0;
}

/* Streamlit Tabs Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: transparent;
    border-bottom: 1px solid #334155;
    padding-bottom: 2px;
    margin-bottom: 20px;
}

.stTabs [data-baseweb="tab"] {
    background-color: #1E293B;
    border: 1px solid #334155;
    border-radius: 10px 10px 0 0;
    color: #94A3B8;
    padding: 10px 22px;
    font-weight: 600;
    font-size: 14px;
    transition: all 0.2s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #F8FAFC;
    border-color: #0D9488;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #0F172A 0%, #134E4A 100%) !important;
    border-color: #14B8A6 !important;
    color: #2DD4BF !important;
}

/* Highlighted Classification Card */
.fx-highlight-card {
    background: linear-gradient(135deg, #0F172A 0%, #134E4A 60%, #042F2E 100%);
    border-radius: 16px;
    padding: 24px 28px;
    color: #FFFFFF;
    margin: 18px 0 22px 0;
    box-shadow: 0 10px 25px rgba(13, 148, 136, 0.2);
    border: 1px solid rgba(45, 212, 191, 0.35);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.fx-highlight-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 30px rgba(13, 148, 136, 0.28);
    border-color: #2DD4BF;
}

.fx-fiber-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 14px;
}

.fx-fiber-title {
    font-size: 28px;
    font-weight: 700;
    color: #FFFFFF;
    margin: 0;
    letter-spacing: -0.5px;
}

.fx-pill {
    background: rgba(45, 212, 191, 0.15);
    color: #5EEAD4;
    border: 1px solid rgba(45, 212, 191, 0.4);
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
}

.fx-class-meta {
    font-size: 12px;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-weight: 600;
    margin-bottom: 6px;
}

.fx-class-text {
    font-size: 18px;
    font-weight: 600;
    color: #2DD4BF;
    margin: 0;
    line-height: 1.4;
}

/* Modern Content Cards */
.fx-card {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 18px;
    min-height: 140px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.fx-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 24px -4px rgba(0, 0, 0, 0.3);
    border-color: #0D9488;
}

.fx-card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
}

.fx-card-icon {
    font-size: 18px;
    line-height: 1;
}

.fx-card-title {
    font-size: 15px;
    font-weight: 700;
    color: #FFFFFF;
    margin: 0;
    letter-spacing: -0.2px;
}

.fx-card-body {
    font-size: 14px;
    line-height: 1.6;
    color: #CBD5E1;
    margin: 0;
}

/* Full Width Cards */
.fx-card-wide {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.fx-card-wide:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px -4px rgba(0, 0, 0, 0.3);
    border-color: #0D9488;
}

/* Fact Card */
.fx-fact-card {
    background: linear-gradient(135deg, #042F2E 0%, #115E59 100%);
    border: 1px solid #14B8A6;
    border-radius: 14px;
    padding: 20px 22px;
    margin: 20px 0;
    display: flex;
    align-items: flex-start;
    gap: 16px;
    box-shadow: 0 6px 18px rgba(20, 184, 166, 0.18);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.fx-fact-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(20, 184, 166, 0.28);
}

.fx-fact-icon {
    font-size: 24px;
    line-height: 1;
}

.fx-fact-title {
    font-size: 12px;
    font-weight: 700;
    color: #5EEAD4;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 0 0 6px 0;
}

.fx-fact-text {
    font-size: 14px;
    line-height: 1.6;
    color: #F0FDFA;
    margin: 0;
    font-weight: 500;
}

/* Comparison Styles */
.fx-compare-header-card {
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 70%, #0F766E 100%);
    border: 1px solid rgba(45, 212, 191, 0.35);
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 18px;
    min-height: 110px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
}

.fx-warning-card {
    background: linear-gradient(135deg, #451A03 0%, #78350F 100%);
    border: 1px solid #F59E0B;
    border-radius: 14px;
    padding: 16px 20px;
    margin: 16px 0 20px 0;
    box-shadow: 0 4px 14px rgba(245, 158, 11, 0.15);
}

.fx-warning-title {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #FBBF24;
    font-size: 15px;
    font-weight: 700;
}

.fx-warning-desc {
    margin: 6px 0 0 0;
    font-size: 14px;
    line-height: 1.5;
    color: #FEF3C7;
}

.fx-compare-row {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.fx-compare-row:hover {
    transform: translateY(-2px);
    border-color: #0D9488;
}

.fx-compare-row-title {
    font-size: 15px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid #334155;
    display: flex;
    align-items: center;
    gap: 8px;
}

.fx-compare-cols {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
}

@media (max-width: 768px) {
    .fx-compare-cols {
        grid-template-columns: 1fr;
        gap: 12px;
    }
}

.fx-compare-cell {
    background: #0F172A;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 14px 16px;
}

.fx-compare-cell-label {
    font-size: 12px;
    font-weight: 700;
    color: #2DD4BF;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
}

.fx-compare-cell-val {
    font-size: 14px;
    line-height: 1.55;
    color: #CBD5E1;
}

/* Footer */
.fx-footer {
    text-align: center;
    padding: 26px 12px 14px 12px;
    border-top: 1px solid #334155;
    margin-top: 34px;
    color: #94A3B8;
    font-size: 13px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# 1. Branding Header Navbar
st.markdown("""
<div class="fx-navbar">
    <div class="fx-brand">
        <span class="fx-brand-logo">🧶</span>
        <span class="fx-brand-text">FiberX</span>
    </div>
    <div class="fx-badge">Textile Engineering Explorer</div>
</div>
""", unsafe_allow_html=True)

# 2. Hero Section
st.markdown("""
<div class="fx-hero">
    <div class="fx-hero-tag">Textile Science & Engineering</div>
    <div class="fx-hero-title">Interactive Fiber Intelligence</div>
    <p class="fx-hero-desc">
        Explore natural and synthetic textile fibers across scientific classification, 
        mechanical properties, manufacturing advantages, trade limitations, and global production.
    </p>
</div>
""", unsafe_allow_html=True)

# Complete Seven-Fiber Dataset (Single Source of Truth)
FIBERS = {
    "Cotton": {
        "classification": "Natural cellulosic fiber (Seed hair)",
        "properties": "Soft, breathable, absorbent, biodegradable, good heat resistance",
        "advantages": "Comfortable against skin, hypoallergenic, easy to dye, versatile",
        "limitations": "Prone to wrinkling and shrinkage, slow to dry, susceptible to mildew",
        "end_uses": "T-shirts, denim, bedsheets, towels, medical gauze",
        "producing_countries": "India, China, United States, Brazil, Pakistan",
        "fact": "Cotton fibers grow inside a protective boll and originate as single-celled seed hairs."
    },
    "Polyester": {
        "classification": "Synthetic polymer fiber (Polyethylene terephthalate - PET)",
        "properties": "High strength, lightweight, hydrophobic (quick drying), wrinkle-resistant",
        "advantages": "Durable, shape-retaining, low cost, resistant to stretching and chemicals",
        "limitations": "Low breathability, prone to static build-up, pilling, non-biodegradable",
        "end_uses": "Activewear, sportswear, fleece jackets, sewing threads, upholstery",
        "producing_countries": "China, India, Taiwan, Indonesia, United States",
        "fact": "Polyester is the world's most widely produced fiber, often recycled from plastic drink bottles."
    },
    "Wool": {
        "classification": "Natural protein fiber (Animal fleece - Sheep)",
        "properties": "Crimped texture, natural elasticity, flame retardant, moisture-wicking, thermal insulator",
        "advantages": "Warm in cold weather, cool in heat, wrinkle-resistant, renewable and biodegradable",
        "limitations": "Can shrink or felt with heat and agitation, vulnerable to moth damage",
        "end_uses": "Sweaters, suits, winter coats, thermal blankets, carpets",
        "producing_countries": "Australia, China, New Zealand, United Kingdom, South Africa",
        "fact": "Wool fibers have microscopic surface scales and natural crimp that trap insulating pockets of still air."
    },
    "Silk": {
        "classification": "Natural protein fiber (Continuous filament - Silkworm cocoon)",
        "properties": "Natural triangular prism luster, high tensile strength, smooth and lightweight",
        "advantages": "Luxurious drape, soft hand feel, temperature regulating, hypoallergenic",
        "limitations": "Delicate, weakened by perspiration and direct sunlight, requires gentle hand-wash or dry cleaning",
        "end_uses": "Luxury evening wear, sarees, scarves, neckties, high-end bedding",
        "producing_countries": "China, India, Uzbekistan, Vietnam, Thailand",
        "fact": "A single silkworm cocoon can unwind into an unbroken silk filament stretching up to 900 meters long."
    },
    "Jute": {
        "classification": "Natural cellulosic fiber (Bast / Stem fiber)",
        "properties": "High tensile strength, low extensibility, coarse texture, 100% biodegradable",
        "advantages": "Very low cost, environmentally friendly, good acoustic and thermal insulation",
        "limitations": "Coarse surface restricts apparel use, weakens when damp, brittle when dry",
        "end_uses": "Burlap sacks, packaging, ropes, twine, carpet backing, eco shopping bags",
        "producing_countries": "India, Bangladesh, China, Myanmar",
        "fact": "Jute is nicknamed the 'Golden Fiber' for its natural golden sheen and tremendous economic importance."
    },
    "Hemp": {
        "classification": "Natural cellulosic fiber (Bast / Stem fiber)",
        "properties": "Exceptionally strong, UV-protective, antimicrobial, softens over repeated washes",
        "advantages": "Highly sustainable crop, requires little water or pesticides, durable and long-lasting",
        "limitations": "Higher processing cost, coarse initial feel compared to cotton, limited supply chains",
        "end_uses": "Canvas sails, durable workwear, jeans, ropes, sustainable composite materials",
        "producing_countries": "China, France, Canada, United States",
        "fact": "Hemp is one of the oldest textile fibers in recorded human history, cultivated for over 10,000 years."
    },
    "Acrylic": {
        "classification": "Synthetic polymer fiber (Polyacrylonitrile)",
        "properties": "Lightweight, soft, wool-like feel, warm, accepts vibrant dye colors",
        "advantages": "Affordable wool substitute, moth-resistant, quick drying, machine washable",
        "limitations": "Prone to static electricity and pilling, heat sensitive, sheds microplastics",
        "end_uses": "Knitted sweaters, winter beanies, blankets, fake fur, outdoor awnings",
        "producing_countries": "China, Turkey, India, South Korea",
        "fact": "Acrylic fiber was originally invented to mimic the warmth and bulk of natural wool at a fraction of the cost."
    }
}

# 3. Main Interface Tabs
tab_explore, tab_compare = st.tabs(["🔍 Fiber Explorer", "⚖️ Compare Fibers"])

# ==========================================
# TAB 1: INDIVIDUAL FIBER EXPLORER
# ==========================================
with tab_explore:
    fiber = st.selectbox(
        "Select a textile fiber to explore:",
        options=list(FIBERS.keys()),
        index=0,
        key="explorer_fiber_select"
    )

    if fiber:
        data = FIBERS[fiber]
        
        # Highlighted Classification Card (Educational Reference badge)
        st.markdown(f"""
        <div class="fx-highlight-card">
            <div class="fx-fiber-header">
                <h2 class="fx-fiber-title">🧵 {fiber}</h2>
                <span class="fx-pill">Educational Reference</span>
            </div>
            <div class="fx-class-meta">Classification & Origin</div>
            <div class="fx-class-text">{data['classification']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Modern Content Cards
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="fx-card">
                <div class="fx-card-header">
                    <span class="fx-card-icon">🔍</span>
                    <span class="fx-card-title">Key Properties</span>
                </div>
                <p class="fx-card-body">{data['properties']}</p>
            </div>
            <div class="fx-card">
                <div class="fx-card-header">
                    <span class="fx-card-icon">🌟</span>
                    <span class="fx-card-title">Advantages</span>
                </div>
                <p class="fx-card-body">{data['advantages']}</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="fx-card">
                <div class="fx-card-header">
                    <span class="fx-card-icon">⚠️</span>
                    <span class="fx-card-title">Limitations</span>
                </div>
                <p class="fx-card-body">{data['limitations']}</p>
            </div>
            <div class="fx-card">
                <div class="fx-card-header">
                    <span class="fx-card-icon">👗</span>
                    <span class="fx-card-title">Common End Uses</span>
                </div>
                <p class="fx-card-body">{data['end_uses']}</p>
            </div>
            """, unsafe_allow_html=True)

        # Producing Countries Card (Full Width)
        st.markdown(f"""
        <div class="fx-card-wide">
            <div class="fx-card-header">
                <span class="fx-card-icon">🌍</span>
                <span class="fx-card-title">Major Producing Countries</span>
            </div>
            <p class="fx-card-body">{data['producing_countries']}</p>
            <div style="font-size: 11px; color: #64748B; margin-top: 8px; border-top: 1px solid #334155; padding-top: 6px;">
                <em>Primary fiber harvest & industrial synthesis benchmarks (FAOSTAT / USDA FAS / Textile Exchange / IWTO / ISC 2022–2024 reports; distinct from garment manufacturing or apparel exports).</em>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Interesting Fact Card
        st.markdown(f"""
        <div class="fx-fact-card">
            <div class="fx-fact-icon">💡</div>
            <div>
                <div class="fx-fact-title">Memorable Fiber Fact</div>
                <p class="fx-fact-text">{data['fact']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 2: SIDE-BY-SIDE FIBER COMPARISON
# ==========================================
with tab_compare:
    st.markdown("""
    <div style="margin-bottom: 18px;">
        <div class="fx-hero-tag">Comparative Textile Analysis</div>
        <div style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin: 4px 0 8px 0;">
            Side-by-Side Fiber Comparison
        </div>
        <p style="color: #94A3B8; font-size: 14px; margin: 0; line-height: 1.5;">
            Select two fibers to evaluate their classifications, physical properties, advantages, 
            limitations, and industrial manufacturing suitability.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_sel_a, col_sel_b = st.columns(2)
    with col_sel_a:
        fiber_a = st.selectbox(
            "Select Fiber A:",
            options=list(FIBERS.keys()),
            index=0,  # Cotton
            key="compare_fiber_a"
        )
    with col_sel_b:
        fiber_b = st.selectbox(
            "Select Fiber B:",
            options=list(FIBERS.keys()),
            index=1,  # Polyester
            key="compare_fiber_b"
        )

    # Identical selection safeguard
    if fiber_a == fiber_b:
        st.markdown(f"""
        <div class="fx-warning-card">
            <div class="fx-warning-title">
                <span>⚠️</span>
                <span>Identical Fiber Selected ({fiber_a})</span>
            </div>
            <p class="fx-warning-desc">
                You have selected <strong>{fiber_a}</strong> for both sides. To analyze practical differences, 
                trade-offs, and alternative applications, select a different second fiber.
            </p>
        </div>
        """, unsafe_allow_html=True)

    data_a = FIBERS[fiber_a]
    data_b = FIBERS[fiber_b]

    # Side-by-side Top Summaries
    col_sum_a, col_sum_b = st.columns(2)
    with col_sum_a:
        st.markdown(f"""
        <div class="fx-compare-header-card">
            <div style="font-size: 11px; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.6px;">Fiber A</div>
            <div style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin: 4px 0;">🧵 {fiber_a}</div>
            <div style="font-size: 13px; color: #2DD4BF; font-weight: 600;">{data_a['classification']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col_sum_b:
        st.markdown(f"""
        <div class="fx-compare-header-card">
            <div style="font-size: 11px; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.6px;">Fiber B</div>
            <div style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin: 4px 0;">🧵 {fiber_b}</div>
            <div style="font-size: 13px; color: #2DD4BF; font-weight: 600;">{data_b['classification']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Side-by-Side Attribute Comparison Rows
    comparison_attributes = [
        ("🔍 Key Properties", "properties"),
        ("🌟 Advantages", "advantages"),
        ("⚠️ Limitations", "limitations"),
        ("👗 Common End Uses", "end_uses"),
        ("🌍 Major Producing Countries", "producing_countries"),
        ("💡 Memorable Fiber Fact", "fact")
    ]

    for title, key in comparison_attributes:
        note_html = ""
        if key == "producing_countries":
            note_html = """
            <div style="font-size: 11px; color: #64748B; margin-top: 10px; border-top: 1px solid #334155; padding-top: 6px;">
                <em>Primary fiber harvest & industrial synthesis benchmarks (FAOSTAT / USDA FAS / Textile Exchange / IWTO / ISC 2022–2024 reports; distinct from garment manufacturing or apparel exports).</em>
            </div>
            """
        st.markdown(f"""
        <div class="fx-compare-row">
            <div class="fx-compare-row-title">{title}</div>
            <div class="fx-compare-cols">
                <div class="fx-compare-cell">
                    <div class="fx-compare-cell-label">{fiber_a}</div>
                    <div class="fx-compare-cell-val">{data_a[key]}</div>
                </div>
                <div class="fx-compare-cell">
                    <div class="fx-compare-cell-label">{fiber_b}</div>
                    <div class="fx-compare-cell-val">{data_b[key]}</div>
                </div>
            </div>
            {note_html}
        </div>
        """, unsafe_allow_html=True)

# 4. Footer
st.markdown("""
<div class="fx-footer">
    <strong>FiberX</strong> • Built for Textile Web App Development with Streamlit & GitHub<br/>
    <span style="font-size: 12px; color: #64748B;">Educational reference for learners, educators, and textile engineering students</span>
</div>
""", unsafe_allow_html=True)
