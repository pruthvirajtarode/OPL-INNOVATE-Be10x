// Workbook LocalStorage Persistence

document.addEventListener('DOMContentLoaded', () => {
    // Load saved data
    const inputs = document.querySelectorAll('input[type="text"], textarea');
    inputs.forEach(input => {
        const savedValue = localStorage.getItem(`workbook_${input.id}`);
        if (savedValue) {
            input.value = savedValue;
        }

        // Save on input change
        input.addEventListener('input', (e) => {
            localStorage.setItem(`workbook_${e.target.id}`, e.target.value);
        });
    });
});

function printWorkbook() {
    window.print();
}

function resetWorkbook() {
    if (confirm("Are you sure you want to clear all your notes? This cannot be undone.")) {
        const inputs = document.querySelectorAll('input[type="text"], textarea');
        inputs.forEach(input => {
            input.value = '';
            localStorage.removeItem(`workbook_${input.id}`);
        });
        alert("Workbook reset.");
    }
}
