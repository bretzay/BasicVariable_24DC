// Attendre que le DOM soit chargé
document.addEventListener('DOMContentLoaded', function() {
    // Gestion du menu fixe
    const header = document.querySelector('.main-header');
    const headerHeight = header.offsetHeight;

    function handleScroll() {
        if (window.scrollY > 50) {
            header.classList.add('header-scrolled');
        } else {
            header.classList.remove('header-scrolled');
        }
    }

    window.addEventListener('scroll', handleScroll);

    // Défilement fluide pour les ancres
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const targetPosition = target.offsetTop - headerHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Gestion des messages système
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        // Ajouter un bouton de fermeture
        const closeButton = document.createElement('button');
        closeButton.innerHTML = '&times;';
        closeButton.className = 'alert-close';
        message.appendChild(closeButton);

        // Fermeture du message
        closeButton.addEventListener('click', () => {
            message.remove();
        });

        // Auto-fermeture après 5 secondes
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });

    
    


    // Gestion des formulaires
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });

            if (!isValid) {
                e.preventDefault();
                showFormError('Veuillez remplir tous les champs obligatoires');
            }
        });
    });
});

// Utilitaires
function showFormError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'alert alert-error';
    errorDiv.textContent = message;
    
    const form = document.querySelector('form');
    form.insertBefore(errorDiv, form.firstChild);

    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}

// Gestion du chargement des images
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
});

// Détection de la connexion réseau
window.addEventListener('online', () => {
    showNetworkStatus('La connexion est rétablie', 'success');
});

window.addEventListener('offline', () => {
    showNetworkStatus('La connexion est perdue', 'error');
});

function showNetworkStatus(message, type) {
    const statusDiv = document.createElement('div');
    statusDiv.className = `alert alert-${type}`;
    statusDiv.textContent = message;
    document.body.insertBefore(statusDiv, document.body.firstChild);

    setTimeout(() => {
        statusDiv.remove();
    }, 3000);
}
    let isMinimized = true; // Par défaut, chatbox fermée

    function sendMessage() {
        let input = document.getElementById("user-input");
        let chatBox = document.getElementById("chat-box");

        if (input.value.trim() !== "") {
            let message = document.createElement("div");
            message.textContent = input.value;
            message.style.padding = "10px";
            message.style.margin = "5px";
            message.style.background = "#e0e0e0";
            message.style.borderRadius = "10px";
            message.style.textAlign = "right";
            chatBox.appendChild(message);
            input.value = "";
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    function toggleChat() {
        let img = document.getElementById("img-chat");
        let chatContainer = document.getElementById("chat-container");
        let chatBox = document.getElementById("chat-box");
        let chatControls = document.getElementById("chat-controls");
        let toggleButton = document.getElementById("toggle-chat");

        if (isMinimized) {
            //img.src = "view/top/static/media/VraiRayDarkCut.png"
            img.style.bottom = "425px";
            chatContainer.style.height = "400px";
            chatBox.style.display = "block";
            chatControls.style.display = "flex";
            toggleButton.textContent = "−";
        } else {
            //img.src = "view/top/static/media/VraiRayDarkCut.png"
            img.style.bottom = "65px";
            chatContainer.style.height = "40px";
            chatBox.style.display = "none";
            chatControls.style.display = "none";
            toggleButton.textContent = "+";
        }
        isMinimized = !isMinimized;
    }
