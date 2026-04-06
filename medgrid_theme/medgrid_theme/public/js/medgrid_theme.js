/* ============================================================
   MEDGRID HEALTHCARE NETWORK — Frappe JS Theme
   Version: 1.0.0
   ============================================================ */

frappe.provide("medgrid_theme");

medgrid_theme = {

    /* ── App Colors ──────────────────────────────────────── */
    colors: {
        navy:      "#0D1B4B",
        navyDark:  "#0A1740",
        blue:      "#1A3A8F",
        blueMid:   "#2A5298",
        blueHover: "#3D6BC4",
        silver:    "#C0C8D8",
        grid:      "#8A9BBF",
        light:     "#E8ECF4",
        offwhite:  "#F4F6FA",
        white:     "#FFFFFF",
    },

    /* ── Initialize Theme ────────────────────────────────── */
    init: function () {
        medgrid_theme.set_page_title();
        medgrid_theme.customize_navbar();
        medgrid_theme.customize_list_view();
        medgrid_theme.apply_form_enhancements();
        console.log("Medgrid Theme v1.0.0 loaded successfully");
    },

    /* ── Set Custom Page Title ───────────────────────────── */
    set_page_title: function () {
        if (document.title && !document.title.includes("Medgrid")) {
            document.title = document.title + " | Medgrid";
        }
    },

    /* ── Navbar Customizations ───────────────────────────── */
    customize_navbar: function () {
        const navbar = document.querySelector(".navbar");
        if (navbar) {
            navbar.style.backgroundColor = "#0D1B4B";
            navbar.style.borderBottom = "2px solid #1A3A8F";
        }

        /* Add Medgrid text to brand if empty */
        const brand = document.querySelector(".navbar-brand");
        if (brand && !brand.textContent.trim()) {
            brand.textContent = "MEDGRID";
            brand.style.color = "#FFFFFF";
            brand.style.fontWeight = "800";
            brand.style.letterSpacing = "2px";
        }
    },

    /* ── List View Customizations ────────────────────────── */
    customize_list_view: function () {
        /* Style list header rows */
        const headers = document.querySelectorAll(".list-row-head");
        headers.forEach(function (header) {
            header.style.backgroundColor = "#E8ECF4";
            header.style.color = "#0D1B4B";
            header.style.fontWeight = "600";
        });
    },

    /* ── Form Enhancements ───────────────────────────────── */
    apply_form_enhancements: function () {
        /* Highlight mandatory fields */
        const mandatoryFields = document.querySelectorAll(".reqd .control-input .form-control");
        mandatoryFields.forEach(function (field) {
            field.style.borderLeft = "3px solid #1A3A8F";
        });
    },

};

/* ── Frappe Ready Hook ───────────────────────────────────── */
$(document).ready(function () {
    medgrid_theme.init();
});

/* ── Frappe Page Change Hook ─────────────────────────────── */
frappe.router.on("change", function () {
    setTimeout(function () {
        medgrid_theme.init();
    }, 300);
});

/* ── Form Render Hook ────────────────────────────────────── */
frappe.ui.form.on("*", {
    refresh: function (frm) {
        medgrid_theme.apply_form_enhancements();
    },
});
$(document).ready(function() {
    frappe.after_ajax(function() {
        const el = document.querySelector('.main-section');
        if (el) {
            el.style.scrollbarGutter = 'auto';
            el.style.overflow = 'unset';
            el.style.overflowX = 'unset';
            el.style.overflowY = 'unset';
        }
    });
});
$(document).on('login_rendered', function () {
    $(".for-login .page-card-actions").append(`
        <div style="text-align:center; margin-top:12px;">
            <p style="margin:0; font-size:14px;">
                New Seller? 
                <a href="/seller-registration" style="color:#1a73e8; font-weight:500;">
                    Register Here
                </a>
            </p>
        </div>
    `);
});