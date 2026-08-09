// Reusable Timer Logic

let timerInterval;
let timeRemaining = 0;
let isTimerRunning = false;

function showTimer() {
    document.getElementById('timer-container').classList.add('active');
}

function hideTimer() {
    document.getElementById('timer-container').classList.remove('active');
}

function setTimer(minutes) {
    clearInterval(timerInterval);
    timeRemaining = minutes * 60;
    isTimerRunning = false;
    updateTimerDisplay();
    document.getElementById('btn-timer-play').textContent = '▶';
    showTimer();
}

function toggleTimer() {
    if (timeRemaining <= 0) return;
    
    if (isTimerRunning) {
        clearInterval(timerInterval);
        isTimerRunning = false;
        document.getElementById('btn-timer-play').textContent = '▶';
    } else {
        isTimerRunning = true;
        document.getElementById('btn-timer-play').textContent = '⏸';
        timerInterval = setInterval(() => {
            timeRemaining--;
            updateTimerDisplay();
            
            if (timeRemaining <= 0) {
                clearInterval(timerInterval);
                isTimerRunning = false;
                document.getElementById('btn-timer-play').textContent = '▶';
                alert('Time is up!'); // Simple offline alert
            }
        }, 1000);
    }
}

function resetTimer() {
    clearInterval(timerInterval);
    timeRemaining = 0;
    isTimerRunning = false;
    updateTimerDisplay();
    document.getElementById('btn-timer-play').textContent = '▶';
}

function updateTimerDisplay() {
    const mins = Math.floor(timeRemaining / 60);
    const secs = timeRemaining % 60;
    document.getElementById('timer-display').textContent = 
        `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        
    // Visual warning near completion (under 1 min)
    const display = document.getElementById('timer-display');
    if (timeRemaining > 0 && timeRemaining <= 60) {
        display.style.color = 'var(--warning)';
    } else if (timeRemaining === 0) {
        display.style.color = 'var(--danger)';
    } else {
        display.style.color = 'var(--text-primary)';
    }
}
