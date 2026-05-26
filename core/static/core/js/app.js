document.addEventListener("DOMContentLoaded", function () {
    var navToggle = document.querySelector("[data-nav-toggle]");
    var nav = document.querySelector("[data-nav]");

    if (navToggle && nav) {
        navToggle.addEventListener("click", function () {
            nav.classList.toggle("is-open");
        });
    }

    var forms = document.querySelectorAll("form");
    forms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            var confirmMessage = form.getAttribute("data-confirm");
            if (confirmMessage && !window.confirm(confirmMessage)) {
                event.preventDefault();
                return;
            }

            var submitButton = form.querySelector('button[type="submit"], input[type="submit"]');
            if (submitButton && !submitButton.dataset.loadingApplied) {
                submitButton.dataset.loadingApplied = "true";
                submitButton.classList.add("loading");
                submitButton.disabled = true;
                submitButton.textContent = "Processing...";
            }
        });
    });

    var yearTarget = document.querySelector("[data-year]");
    if (yearTarget) {
        yearTarget.textContent = new Date().getFullYear();
    }
});