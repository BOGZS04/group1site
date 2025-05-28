document.addEventListener('DOMContentLoaded', function() {
    const loginError = document.getElementById('loginError');
    if (loginError && loginError.textContent.trim() !== '') {
        const usernameInput = document.getElementById('username');
        const passwordInput = document.getElementById('password');

        usernameInput.style.borderColor = '#ef4444';
        passwordInput.style.borderColor = '#ef4444';
        loginError.classList.remove('hidden');

        function clearError() {
            usernameInput.style.borderColor = '';
            passwordInput.style.borderColor = '';
            loginError.classList.add('hidden');
        }

        usernameInput.addEventListener('input', clearError);
        passwordInput.addEventListener('input', clearError);
    }
});


