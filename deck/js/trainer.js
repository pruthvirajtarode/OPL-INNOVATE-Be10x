// Trainer Mode Logic

let isTrainerMode = false;

document.addEventListener('DOMContentLoaded', () => {
    // Check URL parameters for trainer mode
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('trainer') === 'true') {
        toggleTrainerMode(true);
    }

    // Keyboard shortcut (Shift + T)
    document.addEventListener('keydown', (e) => {
        if (e.shiftKey && (e.key === 't' || e.key === 'T')) {
            e.preventDefault();
            toggleTrainerMode();
        }
    });

    // Listen for slide changes to update dashboard
    window.addEventListener('slideChanged', (e) => {
        if (isTrainerMode) {
            updateTrainerDashboard(e.detail.slide);
        }
    });
});

function toggleTrainerMode(forceState = null) {
    const overlay = document.getElementById('trainer-overlay');
    
    if (forceState !== null) {
        isTrainerMode = forceState;
    } else {
        isTrainerMode = !isTrainerMode;
    }

    if (isTrainerMode) {
        overlay.classList.add('active');
        // Initial update for current slide
        const currentActive = document.querySelector('.slide.active');
        if (currentActive) updateTrainerDashboard(currentActive);
    } else {
        overlay.classList.remove('active');
    }
}

function updateTrainerDashboard(slide) {
    // Get dataset from slide
    const module = slide.dataset.module || 'Unknown Module';
    const obj = slide.dataset.trainerObjective || 'N/A';
    const say = slide.dataset.trainerSay || 'N/A';
    const watch = slide.dataset.trainerWatch || '';
    const rescue = slide.dataset.trainerRescue || '';
    const time = slide.dataset.trainerTime || 'As needed';

    // Update DOM
    document.getElementById('trainer-module-badge').textContent = module;
    document.getElementById('trainer-obj').textContent = obj;
    document.getElementById('trainer-say').textContent = say;
    document.getElementById('trainer-time').textContent = time;

    const rescueContainer = document.getElementById('trainer-rescue-container');
    const rescueText = document.getElementById('trainer-rescue');
    
    if (watch || rescue) {
        rescueContainer.style.display = 'block';
        let content = '';
        if (watch) content += `<strong>Watch For:</strong> ${watch}<br>`;
        if (rescue) content += `<strong>Rescue:</strong> ${rescue}`;
        rescueText.innerHTML = content;
    } else {
        rescueContainer.style.display = 'none';
    }
}
