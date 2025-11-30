function confirmBulkDelete() {
    // Select ANY checkbox whose name starts with selected_products
    const checked = document.querySelectorAll('input[name^="selected_products"]:checked');

    if (checked.length === 0) {
        alert("Please select at least one product to delete.");
        return false;
    }

    return confirm(`Are you sure you want to delete ${checked.length} product(s)? This cannot be undone.`);
}
