import os, json
from pathlib import Path
from datetime import datetime
from urllib.parse import quote
import streamlit as st
from PIL import Image, ImageOps

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
DATA_FILE = ROOT / "site_data.json"

DEFAULT = {
    "brand_name": "THE ARTISTIC STUDIO",
    "tagline": "Create • Inspire • Express",
    "founder_name": "Mansi Pokhriyal",
    "founder_bio": "Artist & Founder of THE ARTISTIC STUDIO.",
    "about": "THE ARTISTIC STUDIO is a creative space built around art, culture and handmade expression. Our journey began with creations inspired by Aipan, the traditional folk art of Uttarakhand. Our vision is broader than one art form: we want to bring different forms of creativity together through thoughtful products and artistic services.",
    "phone": "9286205557",
    "email": "pokhriyal mansi19@gmail.com",
    "instagram": "https://www.instagram.com/the_artistic.studio/",
    "whatsapp": "https://wa.me/919286205557",
    "products": [
        {"name":"Aipan Art Pooja Thali","price":"₹150","folder":"pooja_thali","description":"A steel pooja thali decorated with Aipan-inspired artwork, bringing a traditional touch to pooja spaces and festive rituals.","details":["Steel thali","20 cm radius (as provided)","Decorative painted artwork","Inspired by Uttarakhand’s Aipan folk art"]},
        {"name":"Aipan Art Keychains","price":"₹100","folder":"keychains","description":"Hand-decorated keychains inspired by Aipan motifs. Designed for everyone — not limited to any gender.","details":["MDF base","Acrylic colours","Varnish and protective coating","Made for everyday carry; avoid prolonged soaking"]}
    ],
    "upcoming":[
        {"name":"Moulded Clay Art","description":"A new collection of moulded-clay creations is in the works."},
        {"name":"Pipe Cleaner Art","description":"Playful handmade creations made with pipe cleaners are coming soon."}
    ],
    "services":[
        {"name":"Face Art","folder":"face_art","description":"Colourful face-art designs for celebrations, parties, school events, stalls and special occasions.","details":["Skin-friendly colours","Washable designs","Designs for children and adults","Event and stall enquiries welcome"]},
        {"name":"Mehendi","folder":"mehendi","description":"Mehendi services for celebrations and special occasions. Share your event details to enquire about designs and availability.","details":["Custom design enquiries","Festive and event bookings","Share date and location for availability"]}
    ]
}

def load_data():
    if DATA_FILE.exists():
        try:
            d = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            out = DEFAULT.copy()
            out.update(d)
            return out
        except Exception:
            pass
    return DEFAULT.copy()

def save_data(d):
    DATA_FILE.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")

def pics(folder):
    p = ASSETS / folder
    if not p.exists(): return []
    return sorted([x for x in p.iterdir() if x.is_file() and x.suffix.lower() in {".png",".jpg",".jpeg",".webp"}])

def wa(phone, message):
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) == 10: digits = "91" + digits
    return f"https://wa.me/{digits}?text={quote(message)}"

st.set_page_config(page_title="THE ARTISTIC STUDIO", page_icon="🎨", layout="wide")
d = load_data()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
:root{--wine:#651323;--wine2:#7b2636;--cream:#f7f0e5;--ink:#2b2020}
.stApp{background:#fbf8f2;color:var(--ink);font-family:'DM Sans',sans-serif}
.block-container{max-width:1200px;padding-top:1rem}
h1,h2,h3{
    font-family:'Playfair Display',serif!important;
    color:var(--wine)!important;
    line-height:1.5!important;
    padding-top:0.15em!important;
    padding-bottom:0.15em!important;
    overflow:visible!important;
}
.hero{background:linear-gradient(115deg,#5d1020,#7b2636 65%,#93545a);color:#fff8ed;padding:2.8rem 2.2rem;border-radius:22px}
.hero h1{color:#fff8ed!important;font-size:clamp(2.2rem,5vw,4rem);margin:.25rem 0}
.hero p{color:#f7e9dc;font-size:1.05rem}
.eyebrow{letter-spacing:.17em;text-transform:uppercase;font-size:.75rem;font-weight:700;color:#e9cdb7}
.panel{background:#fffdf9;border:1px solid #eadfd2;border-radius:18px;padding:1.15rem;height:100%}
.price{font-size:1.3rem;font-weight:800;color:#7b1e31}
.pill{display:inline-block;border:1px solid #d9b8aa;color:#651323;padding:.25rem .65rem;border-radius:99px;font-size:.75rem}
.small{color:#786c68;font-size:.92rem}
a{color:#7b1e31!important}
div.stButton>button,div.stLinkButton>a{border-radius:999px!important;background:#651323!important;color:white!important;border:1px solid #651323!important}
div.stButton>button:hover,div.stLinkButton>a:hover{background:#7b2636!important}
section[data-testid="stFileUploader"]{background:#fffdf9}
</style>
""", unsafe_allow_html=True)

# Header: original logo is used as a file, never recreated.
logo = ASSETS / "logo.png"
h1,h2,h3 = st.columns([1,4,1], vertical_alignment="center")
with h1:
    if logo.exists(): st.image(str(logo), width=100)
    else: st.caption("Add exact logo at assets/logo.png")
with h2:
            st.markdown(
            f"<div style='font-family:Playfair Display,serif;"
            f"font-size:1.85rem;"
            f"line-height:2;"
            f"padding:20px 0 15px 0;"
            f"margin:0;"
            f"overflow:visible;'>"
            f"{d['brand_name']}</div>",
            unsafe_allow_html=True
        )
            st.caption(d["tagline"])
with h3:
    st.markdown("<div style='text-align:right;font-weight:600'><a href='#about-us'>About Us ↗</a></div>", unsafe_allow_html=True)

# Search bar under brand header
query = st.text_input("Search the studio", placeholder="Search products, services or art…", label_visibility="collapsed")
q = query.strip().lower()

st.markdown(f"""
<div class="hero">
 <div class="eyebrow">Welcome to</div>
 <h1>{d['brand_name']}</h1>
 <p>Art that carries a story. Handmade creations and creative services inspired by tradition and imagination.</p>
 <b>{d['tagline']}</b>
</div>
""", unsafe_allow_html=True)

st.markdown("")
st.markdown("## Upcoming Products")
st.caption("A preview of the collections currently in development.")
upcoming = [x for x in d["upcoming"] if not q or q in x["name"].lower() or q in x["description"].lower()]
if upcoming:
   cols = st.columns(2, gap="large")

for col, item in zip(cols, upcoming):
        with col:

            image_file = (
                "clay_art_1.jpg"
                if "clay" in item["name"].lower()
                else "pipe_cleaner_1.jpg"
            )

            image_path = ASSETS / "products" / image_file

            img = ImageOps.fit(
                Image.open(image_path).convert("RGB"),
                (900, 400)
            )

            st.image(
                img,
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class='panel'>
                    <span class='pill'>COMING SOON</span>
                    <h3>{item['name']}</h3>
                    <p>{item['description']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

else:
    st.info("No upcoming category matches your search.")
   
st.markdown("---")
st.markdown("## Our Products")
st.caption("Browse the available collection. Select Buy Now to place an order request through WhatsApp; payment is arranged directly with the studio.")
products = [x for x in d["products"] if not q or q in x["name"].lower() or q in x["description"].lower() or q in " ".join(x.get("details",[])).lower()]
if products:
    for product in products:
     a,b = st.columns([1,1.35], vertical_alignment="top")

     with a:
        images = pics(product["folder"])
        if images:
           if product["folder"] == "keychains":
                        caption = ["Aipan Keychains" for x in images]
           elif product["folder"] == "pooja_thali":
                        caption = ["Pooja Thali" for x in images]
           else:
            caption = [x.stem.replace("_", " ").title() for x in images]

           st.image(
              [str(x) for x in images],
              caption=caption,
              width=350
            )
        else:
             st.info(f"Add original product photos to assets/{product['folder']}/")
        with b:
            st.markdown(f"### {product['name']}")
            st.markdown(f"<div class='price'>{product['price']}</div>", unsafe_allow_html=True)
            st.write(product["description"])
            for item in product.get("details",[]): st.markdown(f"- {item}")
            st.link_button("Buy Now · Order on WhatsApp", wa(d["phone"], f"Hello! I would like to order: {product['name']} ({product['price']}). Please share the next steps."))
        st.markdown("---")
else: st.info("No products match your search.")


st.markdown("## Our Services")
st.caption("For services, send an enquiry with your event details.")

services = [
    x for x in d["services"]
    if not q
    or q in x["name"].lower()
    or q in x["description"].lower()
]

for service in services:

    left, right = st.columns(
        [1, 1.35],
        vertical_alignment="top"
    )

    with left:
        folder = service["folder"]
        images = pics(folder)

        # Face Art image fallback
        if not images and folder == "face_art":
            face_image = ASSETS / "face_art_0.jpeg"
            if face_image.exists():
                images = [face_image]

        # Mehndi / Mehendi folder fallback
        if not images and folder in ("mehndi", "mehendi"):
            alternate_folder = (
                "mehendi" if folder == "mehndi" else "mehndi"
            )
            images = pics(alternate_folder)

        if images:
            if folder == "face_art":
                captions = ["Face Art"] * len(images)

            elif folder in ("mehndi", "mehendi"):
                captions = ["Mehndi"] * len(images)

            else:
                captions = [
                    x.stem.replace("_", " ").title()
                    for x in images
                ]

            st.image(
                [str(x) for x in images],
                caption=captions,
                width=400
            )

        else:
            st.info(
                f"Add portfolio photos to assets/{folder}/"
            )

    with right:
        st.markdown(f"### {service['name']}")
        st.write(service["description"])

        for item in service.get("details", []):
            st.markdown(f"- {item}")

        with st.form(f"enquiry_{folder}"):
            name = st.text_input(
                "Your Name",
                key=f"name_{folder}"
            )

            event = st.text_input(
                "Event / Occasion",
                key=f"event_{folder}"
            )

            date = st.text_input(
                "Preferred date",
                key=f"date_{folder}"
            )

            location = st.text_input(
                "Location",
                key=f"location_{folder}"
            )

            notes = st.text_area(
                "Additional details (optional)",
                key=f"notes_{folder}"
            )

            submit = st.form_submit_button(
                f"Enquire about {service['name']}"
            )

        if submit:
            message = (
                f"{service['name']} enquiry\n"
                f"Name: {name}\n"
                f"Event: {event}\n"
                f"Date: {date}\n"
                f"Location: {location}\n"
                f"Details: {notes}"
            )

            st.link_button(
                "Continue enquiry on WhatsApp",
                wa(d["phone"], message)
            )

        st.markdown("---")

st.markdown(
    "<div id='about-us'></div>",
    unsafe_allow_html=True
)

st.markdown("## About Us")
st.write(d["about"])

founder_pic = ASSETS / "founder.jpg"

fa, fb = st.columns([1, 2], vertical_alignment="center")

with fa:
    if founder_pic.exists():
        founder_image = ImageOps.fit(
            Image.open(founder_pic).convert("RGB"),
            (600, 600),
            centering=(0.5, 0.35)
        )
        st.image(founder_image, use_container_width=True)
    else:
        st.info("Founder photo can be added later at assets/founder.jpg.")

with fb:
    st.markdown(f"### {d['founder_name']}")
    st.caption("Artist & Founder")
    st.write(d["founder_bio"])
    st.write("The studio is growing step by step, with a focus on original artwork, thoughtful materials and creative expression.")

st.markdown("---")
st.markdown("## Connect With Us")
c1,c2,c3 = st.columns(3)
with c1: st.markdown(f"**Call:** [{d['phone']}](tel:{d['phone']})")
with c2: st.markdown(f"**Instagram:** [@the_artistic.studio]({d['instagram']})")
with c3: st.markdown(f"**Email:** {d['email']}")
st.link_button("WhatsApp the Studio", d["whatsapp"])
st.caption(f"© {datetime.now().year} {d['brand_name']} · Create • Inspire • Express")

# Optional admin panel for future updates.
with st.expander("Studio Admin — update photos and website details"):
    password = os.getenv("ADMIN_PASSWORD", "")
    if not password:
        st.warning("Admin panel is locked until you set ADMIN_PASSWORD. See README.txt.")
    else:
        entered = st.text_input("Admin password", type="password")
        if entered == password:
            st.success("Admin access enabled.")
            st.markdown("#### Upload / replace images")
            ul = st.file_uploader("Exact original logo", type=["png","jpg","jpeg"], key="admin_logo")
            uf = st.file_uploader("Founder photo", type=["png","jpg","jpeg","webp"], key="admin_founder")
            if ul: (ASSETS/"logo.png").write_bytes(ul.getvalue()); st.success("Logo saved.")
            if uf: (ASSETS/"founder.jpg").write_bytes(uf.getvalue()); st.success("Founder photo saved.")
            for folder,label in [("pooja_thali","Pooja thali"),("keychains","Keychains"),("face_art","Face art"),("mehendi","Mehendi")]:
                files = st.file_uploader(f"Add {label} photos", type=["png","jpg","jpeg","webp"], accept_multiple_files=True, key=f"upload_{folder}")
                if files:
                    dest=ASSETS/folder
                    dest.mkdir(parents=True,exist_ok=True)
                    for f in files: (dest/Path(f.name).name).write_bytes(f.getvalue())
            st.markdown("#### Contact and About Us")
            d["phone"] = st.text_input("Primary contact", d["phone"])
            d["email"] = st.text_input("Email", d["email"])
            d["instagram"] = st.text_input("Instagram URL", d["instagram"])
            d["whatsapp"] = st.text_input("WhatsApp URL", d["whatsapp"])
            d["about"] = st.text_area("About the studio", d["about"])
            d["founder_bio"] = st.text_area("Founder bio", d["founder_bio"])
            st.markdown("#### Product prices and descriptions")
            for i,p in enumerate(d["products"]):
                p["price"] = st.text_input(f"{p['name']} price", p["price"], key=f"pprice{i}")
                p["description"] = st.text_area(f"{p['name']} description", p["description"], key=f"pdesc{i}")
            if st.button("Save changes"):
                save_data(d)
                st.success("Saved. Refresh the page to see the updates.")
        elif entered:
            st.error("Incorrect password.")
