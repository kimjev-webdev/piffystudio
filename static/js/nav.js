// Detect device input type
const isTouch = matchMedia("(pointer: coarse)").matches;
document.body.dataset.input = isTouch ? "touch" : "mouse";

// Elements
const toggle = document.getElementById("nav-toggle");
const menu = document.querySelector(".nav-menu");

// ----------------------------
// CLICK / TAP PERSISTENT STATE
// ----------------------------
toggle.addEventListener("click", () => {
    const isActive = toggle.classList.contains("active");

    if (isActive) {
        // Closing
        toggle.classList.remove("active");
        menu.classList.remove("open-active");
        menu.classList.remove("open-hover");
    } else {
        // Opening persistent
        toggle.classList.add("active");
        menu.classList.add("open-active");
        menu.classList.remove("open-hover");
    }
});


// ----------------------------
// DESKTOP HOVER PREVIEW
// ----------------------------
if (!isTouch) {
    toggle.addEventListener("mouseenter", () => {
        if (!toggle.classList.contains("active")) {
            menu.classList.add("open-hover");
        }
    });

    document.addEventListener("mousemove", (e) => {
        const hoveringToggle = toggle.contains(e.target);
        const hoveringMenu = menu.contains(e.target);

        if (
            !toggle.classList.contains("active") &&
            !hoveringToggle &&
            !hoveringMenu
        ) {
            menu.classList.remove("open-hover");
        }
    });
}


// ----------------------------
// SUBMENU CLICK TO OPEN (TOUCH ONLY)
// ----------------------------
document.querySelectorAll(".submenu-toggle").forEach(btn => {
    btn.addEventListener("click", () => {
        if (!isTouch) return;
        btn.nextElementSibling.classList.toggle("open");
    });
});
