# Medgrid Healthcare Network — Frappe Theme

A custom Frappe/ERPNext theme app for Medgrid Healthcare Network.

## Colors Used

| Name        | Hex       | Usage                        |
|-------------|-----------|------------------------------|
| Deep Navy   | #0D1B4B   | Navbar, Sidebar, Modal header|
| Medium Blue | #1A3A8F   | Buttons, Links, Active items |
| Steel Blue  | #2A5298   | Hover states, Borders        |
| Hover Blue  | #3D6BC4   | Button hover                 |
| Silver Grey | #C0C8D8   | Text muted, Borders          |
| Grid Dot    | #8A9BBF   | Sidebar labels, Placeholder  |
| Light Silver| #E8ECF4   | Page BG, Table alt row       |
| Off White   | #F4F6FA   | Main page background         |
| Dark Navy   | #0A1740   | Footer                       |
| White       | #FFFFFF   | Cards, Forms                 |

## Installation

```bash
# Step 1 - Go to bench
cd /home/frappe/frappe-bench

# Step 2 - Copy app to apps folder
cp -r medgrid_theme apps/

# Step 3 - Install Python package
uv pip install -e apps/medgrid_theme --python ./env/bin/python

# Step 4 - Install on site
bench --site yoursite.localhost install-app medgrid_theme

# Step 5 - Build assets
bench build --app medgrid_theme

# Step 6 - Clear cache
bench --site yoursite.localhost clear-cache

# Step 7 - Restart
bench restart
```

## Uninstall

```bash
bench --site yoursite.localhost uninstall-app medgrid_theme
bench --site yoursite.localhost clear-cache
bench remove-app medgrid_theme
```

## What it Changes

- Navbar → Deep Navy background
- Sidebar → Deep Navy with blue hover
- Buttons → Medium Blue primary
- Forms → Clean white cards
- Tables → Navy header, alternating rows
- Modals → Navy header
- Badges → Color-coded status indicators
- Scrollbar → Medgrid branded
- Links → Medium Blue

## Version

1.0.0
