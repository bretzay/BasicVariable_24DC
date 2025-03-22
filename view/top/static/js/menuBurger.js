// Animation du menu mobile
const mobileMenuButton = document.createElement('button');
mobileMenuButton.className = 'mobile-menu-button';
mobileMenuButton.textContent = "☰"; // Par défaut, menu hamburger

const nav = document.querySelector('.nav-links');
const headerContainer = document.querySelector('.main-nav');

headerContainer.insertBefore(mobileMenuButton, nav);

mobileMenuButton.addEventListener('click', () => {
    nav.classList.toggle('nav-open');
    mobileMenuButton.classList.toggle('active');

    // Change le texte entre "☰" et "|||"
    mobileMenuButton.textContent = mobileMenuButton.classList.contains("active") ? "|||" : "☰";
});