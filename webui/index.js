import * as msgs from "./messages.js"

let autoScroll = true;
let context = "";

function removeSplashScreen() {
    const splashScreen = document.getElementById('splash-screen');
    if (splashScreen) {
        setTimeout(() => {
            splashScreen.style.opacity = '0';
            setTimeout(() => {
                splashScreen.style.display = 'none';
            }, 500);
        }, 2000);
    }
}

function toggleDarkMode(isDark) {
    if (isDark) {
        document.body.classList.remove('light-mode');
    } else {
        document.body.classList.add('light-mode');
    }
    console.log("Dark mode:", isDark);
    localStorage.setItem('darkMode', isDark);
}

async function sendMessage() {
    console.log("sendMessage called");
}

async function poll() {
    console.log("poll called");
    return false;
}

async function startPolling() {
    const shortInterval = 25
    const longInterval = 250
    const shortIntervalPeriod = 100
    let shortIntervalCount = 0

    async function _doPoll() {
        let nextInterval = longInterval

        try {
            const result = await poll();
            if (result) shortIntervalCount = shortIntervalPeriod;
            if (shortIntervalCount > 0) shortIntervalCount--;
            nextInterval = shortIntervalCount > 0 ? shortInterval : longInterval;
        } catch (error) {
            console.error('Error:', error);
        }

        setTimeout(_doPoll.bind(this), nextInterval);
    }

    _doPoll();
}

function setupEventListeners() {
    const chatInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-button');

    if (chatInput) {
        chatInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
    } else {
        console.error('Chat input element not found');
    }

    if (sendButton) {
        sendButton.addEventListener('click', sendMessage);
    } else {
        console.error('Send button element not found');
    }
}

// Add this function to log failed resource loads
function setupResourceErrorLogging() {
    window.addEventListener('error', function(e) {
        if (e.target.tagName === 'LINK' || e.target.tagName === 'SCRIPT' || e.target.tagName === 'IMG') {
            console.error('Failed to load resource:', e.target.src || e.target.href);
        }
    }, true);
}

document.addEventListener("DOMContentLoaded", () => {
    setupResourceErrorLogging();
    startPolling();
    removeSplashScreen();
    const isDarkMode = localStorage.getItem('darkMode') !== 'false';
    toggleDarkMode(isDarkMode);
    setupEventListeners();
});

// Export functions that need to be accessed globally
window.toggleDarkMode = toggleDarkMode;
window.sendMessage = sendMessage;
window.poll = poll;
window.startPolling = startPolling;
