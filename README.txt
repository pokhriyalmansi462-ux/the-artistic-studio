THE ARTISTIC STUDIO — Website v2

Run locally:
  pip install -r requirements.txt
  streamlit run app.py

Admin panel:
Set a strong ADMIN_PASSWORD before starting the app.
Windows PowerShell: $env:ADMIN_PASSWORD="your-strong-password"
macOS/Linux: export ADMIN_PASSWORD="your-strong-password"

Original image folders:
  assets/logo.png             exact original logo file
  assets/founder.jpg          founder photograph
  assets/pooja_thali/         original pooja thali photos
  assets/keychains/           original keychain photos
  assets/face_art/            face art portfolio
  assets/mehendi/             mehendi portfolio
  assets/frames/              optional frame samples

Page order:
Header (logo + studio name + About Us link), search bar, welcome banner,
Upcoming Products, Our Products, Our Services (Face Art + Mehendi), About Us,
Founder and Contact.

Products:
Aipan Art Pooja Thali ₹150
Aipan Art Keychains ₹100
Buy Now buttons initiate a WhatsApp order request. This starter does not take
online payments or complete a checkout transaction.

Services:
Face Art and Mehendi use enquiry forms that prepare a WhatsApp enquiry.

Important:
- The logo is not recreated. Put the exact original image at assets/logo.png.
- Founder image can be added later at assets/founder.jpg.
- Email copied from the business card should be verified before publishing.
- Verify all product specifications and claims before publishing.
- Set a strong admin password and use persistent storage when deploying publicly.
