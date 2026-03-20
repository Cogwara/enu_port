# 🚀 QUICK START GUIDE - MRCHRYS ENT NIG LTD Website

Get the website up and running in 5 minutes!

## Step 1: Install Python Dependencies

```bash
# Navigate to project directory
cd enu

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install all required packages
pip install -r requirements.txt
```

## Step 2: Setup Database

```bash
# Run migrations to create database
python manage.py migrate

# Create admin user (for accessing admin panel)
python manage.py createsuperuser
# Follow prompts to create your admin account
```

## Step 3: Run the Development Server

```bash
# Start Django development server
python manage.py runserver
```

The website will be available at: **http://localhost:8000**

## Step 4: Access Admin Panel

1. Go to: http://localhost:8000/admin
2. Log in with your superuser credentials
3. Manage:
   - Contact messages
   - Services
   - Projects

## ✨ What You Get

### Pages
- ✅ **Home** - Hero section with services preview
- ✅ **About** - Company information, vision & mission
- ✅ **Services** - All 10+ service categories
- ✅ **Projects** - Portfolio showcase
- ✅ **Contact** - Contact form + contact info

### Features
- ✅ Responsive design (mobile-friendly)
- ✅ Professional dark blue & orange theme
- ✅ WhatsApp integration
- ✅ Contact form with database storage
- ✅ Admin panel for content management
- ✅ SEO-friendly structure

## 📝 Customize Content

### Update Company Info
Edit `website/views.py` - locate `COMPANY_INFO` dictionary:

```python
COMPANY_INFO = {
    'name': 'MRCHRYS ENT NIG LTD',
    'email': 'info@mrchrys.com',
    'phone': '+234 (0) 123 456 7890',
    'whatsapp': '+2341234567890',
    'address': 'Lagos, Nigeria',
}
```

### Add Services via Admin
1. Go to Admin Panel → Services
2. Click "Add Service"
3. Fill in details and save

### Upload Projects
1. Go to Admin Panel → Projects
2. Click "Add Project"
3. Upload image and details

## 🎨 Customize Colors

Edit `website/static/css/style.css`:

```css
:root {
    --primary-color: #003d82;      /* Dark Blue */
    --secondary-color: #ff9500;    /* Orange */
}
```

## 📧 Setup Email (Optional)

### For Gmail:
1. Enable 2-factor authentication on Gmail
2. Generate App Password: https://myaccount.google.com/apppasswords
3. Copy `.env.example` to `.env` and add:

```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=app-password-here
```

## 🧪 Run Tests

```bash
python manage.py test website
```

## 📦 Load Sample Data

Create sample services:

```bash
python manage.py load_initial_data
```

## 🛠️ Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
# Or kill the process using port 8000
```

### Static files not loading
```bash
python manage.py collectstatic
```

### Database error
```bash
python manage.py migrate
```

## 📚 Full Documentation

- See `README.md` for complete documentation
- See `ENVIRONMENT.md` for environment setup
- See `website/` folder for source code

## 🚀 Next Steps

1. **Customize** the content (company info, services, projects)
2. **Add your logo** to `website/static/images/`
3. **Update colors** in CSS to match your branding
4. **Configure email** for contact form responses
5. **Deploy to production** (Heroku, AWS, etc.)

## 📞 Contact Form Testing

When running locally, emails print to console. For real deployment:
- Configure SMTP email server
- See `ENVIRONMENT.md` for email setup

## 🎯 Key Files to Know

- `mrchrys_project/settings.py` - Configuration
- `website/views.py` - Page logic
- `website/templates/` - HTML files
- `website/static/css/style.css` - Styling
- `website/models.py` - Database models

## ✅ You're All Set!

The website is now running and ready for customization. Visit http://localhost:8000 to see your site!

---

**Need Help?**
- Check the README.md for detailed documentation
- Review Django docs: https://docs.djangoproject.com
- Troubleshoot in ENVIRONMENT.md
