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
