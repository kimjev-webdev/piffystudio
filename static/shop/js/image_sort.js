document.addEventListener("DOMContentLoaded", function () {
    const el = document.getElementById("image-list");
    if (!el) return;

    new Sortable(el, {
        animation: 150,
        onEnd: function () {
            const order = [];
            document.querySelectorAll("#image-list li").forEach((item, index) => {
                order.push({
                    id: item.dataset.id,
                    position: index
                });
            });

            fetch(window.UPDATE_IMAGE_ORDER_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": window.CSRF_TOKEN,
                },
                body: JSON.stringify({ order: order })
            })
            .then(res => res.json())
            .then(data => console.log("Image order updated:", data))
            .catch(err => console.error("Error:", err));
        }
    });
});
