// Workbook LocalStorage Persistence

document.addEventListener('DOMContentLoaded', () => {
    // Load saved data for text inputs, textareas, and selects
    const inputs = document.querySelectorAll('input[type="text"], textarea, select');
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

    // Handle radio buttons separately since they share a name but have different IDs/values
    const radios = document.querySelectorAll('input[type="radio"]');
    radios.forEach(radio => {
        const savedValue = localStorage.getItem(`workbook_radio_${radio.name}`);
        if (savedValue === radio.value) {
            radio.checked = true;
        }

        radio.addEventListener('change', (e) => {
            if (e.target.checked) {
                localStorage.setItem(`workbook_radio_${e.target.name}`, e.target.value);
            }
        });
    });
});

function printWorkbook() {
    window.print();
}

function resetWorkbook() {
    if (confirm("Are you sure you want to clear all your notes? This cannot be undone.")) {
        // Clear text inputs, textareas, selects
        const inputs = document.querySelectorAll('input[type="text"], textarea, select');
        inputs.forEach(input => {
            input.value = '';
            localStorage.removeItem(`workbook_${input.id}`);
        });

        // Clear radio buttons
        const radios = document.querySelectorAll('input[type="radio"]');
        radios.forEach(radio => {
            radio.checked = false;
            localStorage.removeItem(`workbook_radio_${radio.name}`);
        });

        alert("Workbook reset.");
        // Optional reload to ensure UI is completely clean
        // window.location.reload();
    }
}
