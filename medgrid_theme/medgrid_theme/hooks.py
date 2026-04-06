app_name = "medgrid_theme"
app_title = "Medgrid Theme"
app_publisher = "Medgrid"
app_description = "Medgrid Healthcare Network Theme for Frappe/ERPNext"
app_email = "admin@medgrid.com"
app_license = "MIT"
app_version = "1.0.0"

# Inject CSS into desk (backend)
app_include_css = [
    "/assets/medgrid_theme/css/medgrid_theme.css"
]

# Inject JS into desk (backend)
app_include_js = [
    "/assets/medgrid_theme/js/medgrid_theme.js"
]

# Inject CSS into website (frontend/portal)
web_include_css = [
    "/assets/medgrid_theme/css/medgrid_theme.css"
]

web_include_js = [
    "/assets/medgrid_theme/js/medgrid_theme.js"
]

fixtures = [
    {"dt": "Website Theme", "filters": [["name", "=", "medgrid_theme"]]}
]
website_js = "medgrid_theme/public/js/website_script.js"