
    document.getElementById('studentSearch').addEventListener('input', function() {
        const filter = this.value.toLowerCase();
        const rows = document.querySelectorAll('.student-row');
        let hasResults = false;

        rows.forEach(row => {
            const name = row.querySelector('.student-name').textContent.toLowerCase();
            if (name.includes(filter)) {
                row.style.display = ""; 
                hasResults = true;
            } else {
                row.style.display = "none"; 
            }
        });

        document.getElementById('noResultRow').style.display = hasResults ? "none" : "";
    });