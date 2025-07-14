function my_scope() {
    const formularies = document.querySelectorAll('.form-delete');

    for (const formulary of formularies) {
        formulary.addEventListener('submit', function(e) {
            e.preventDefault();
            const confirmed = confirm('Você tem certeza??')

            if (confirmed) {
                formulary.submit();
            }
        })
    }
}

my_scope();