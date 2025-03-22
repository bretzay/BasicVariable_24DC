<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hôtel California - Le Mans</title>
    
    <!-- CSS commun -->
    <link rel="stylesheet" href="view/top/static/css/base.css">
    <link rel="stylesheet" href="view/top/static/css/style.css">
<style>
    /* Add responsive image handling */
    .gallery {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        padding: 20px;
    }

    .gallery img {
        width: 100%;
        height: 300px;
        object-fit: cover;
        border-radius: 8px;
        transition: transform 0.3s ease;
    }

    .gallery img:hover {
        transform: scale(1.05);
    }

    /* Responsive navigation */
    nav {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px;
        padding: 15px;
    }

    /* Responsive sections */
    section {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Make sure images don't overflow their containers */
    img {
        max-width: 100%;
        height: auto;
    }
</style>


    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="view/top/static/favicon.ico">

    <!-- Meta tags -->
    <meta name="description" content="Hôtel California - Votre séjour de luxe au Mans">
    <meta name="keywords" content="hôtel, le mans, luxe, spa, restaurant, hébergement">
</head>
<body>
    <!-- En-tête commune à toutes les pages -->
    <header class="main-header">
        <nav class="main-nav">
            <div class="logo">
                <a href="/">
                    <img src="view/top/static/media/logo.png" alt="Logo Hôtel California">
                </a>
            </div>
            <div class="nav-links">
                <a href="#services">Services</a>
                <a href="#restaurants">Restaurants</a>
                <a href="#spa">Spa</a>
                <a href="#activities">Activités</a>
                <a href="#contact">Contact</a>
                <a href="reservation.php" class="btn-reservation">Réserver</a>
            </div>
        </nav>
    </header>

    <!-- Messages système (notifications, erreurs, etc.) -->
    

    <!-- Contenu principal -->
    <main>
        

<section id="services" class="services">
    <h2>Bienvenue à Hôtel California</h2>
    <p>Situé au cœur de la charmante ville du Mans, l&#x27;Hôtel California vous accueille dans un cadre exceptionnel où le luxe et le raffinement se rencontrent. Notre établissement cinq étoiles offre une expérience inoubliable, alliant confort moderne et élégance classique.</p>
    <div class="gallery">
        <img src="view/top/static/media/lobby.png" alt="Lobby de l'hôtel">
        <img src="view/top/static/media/room.png" alt="Chambre deluxe">
        <img src="view/top/static/media/pool.png" alt="Piscine extérieure">
    </div>
</section>

<section id="restaurants" class="restaurants">
    <h2>Restaurants Gastronomiques</h2>
    <p>Découvrez nos restaurants exquis, chacun proposant une expérience culinaire unique :</p>
    <ul>
        
        <li>
            <strong>Le Maison Royale:</strong> Une expérience gastronomique raffinée mettant en vedette les saveurs de la cuisine française contemporaine
        </li>
        
        <li>
            <strong>Bistrot de la piscine:</strong> Une cuisine décontractée aux saveurs méditerranéennes
        </li>
        
        <li>
            <strong>Le Belvedere:</strong> Une table d&#x27;exception avec vue panoramique sur la ville
        </li>
        
    </ul>
</section>

<section id="spa" class="spa">
    <h2>Spa &amp; Bien-être</h2>
    <p>Notre spa luxueux est un sanctuaire de détente et de revitalisation. Offrez-vous un moment de pur bien-être avec nos soins personnalisés :</p>
    <ul>
        
        <li>Massages thérapeutiques et relaxants</li>
        
        <li>Soin du visage exclusifs avec des produits haut de gamme</li>
        
        <li>Bain turc traditionnel et sauna</li>
        
        <li>Centre de fitness équipé des dernières technologies</li>
        
    </ul>
    <p>Nos thérapeutes professionnels sont dédiés à votre confort et à votre sérénité, vous garantissant une expérience régénératrice.</p>
</section>

<section id="activities" class="activities">
    <h2>Activités &amp; Loisirs</h2>
    <p>À l&#x27;Hôtel California, nous proposons une multitude d&#x27;activités pour agrémenter votre séjour :</p>
    <ul>
        
        <li>
            <strong>Visites Culturelles:</strong> Explorez le patrimoine historique du Mans avec des visites guidées personnalisées de la vieille ville et de la célèbre Cathédrale Saint-Julien.
        </li>
        
        <li>
            <strong>Excursions Œnologiques:</strong> Partez à la découverte des vignobles locaux et dégustez des vins d&#x27;exception dans un cadre pittoresque.
        </li>
        
        <li>
            <strong>Cours de Cuisine:</strong> Participez à des ateliers culinaires animés par nos chefs et apprenez les secrets de la gastronomie française.
        </li>
        
        <li>
            <strong>Golf &amp; Tennis:</strong> Bénéficiez d&#x27;un accès exclusif à des terrains de golf et des courts de tennis de premier ordre à proximité de l&#x27;hôtel.
        </li>
        
    </ul>
    <p>Notre concierge se fera un plaisir de personnaliser votre programme selon vos envies et vos centres d&#x27;intérêt.</p>
</section>

<div id="box-container">
    <img id="img-chat" src="view/top/static/media/RayDarkCut.png" alt="">
    <div id="chat-container">
        
        <button class="button" id="toggle-chat" onclick="toggleChat()">+</button>
        <div id="chat-box"></div>
        <div id="chat-controls">
            <input type="text" id="user-input" placeholder="Tapez votre message...">
            <button class="button" onclick="sendMessage()">➤</button>
        </div>
    </div>
</div>

<footer id="contact">
    
    

    <p>Hôtel California - 123 Avenue de la Liberté, 72000 Le Mans, France</p>
    <p>Téléphone: +33 2 43 00 00 00 | Email: contact@hotelcalifornia.fr</p>
    <p>
        Suivez-nous:
        
        <a href="https://www.facebook.com/hotelcalifornia" target="_blank">Facebook</a>
         | 
        
        <a href="https://www.instagram.com/hotelcalifornia" target="_blank">Instagram</a>
         | 
        
        <a href="https://www.twitter.com/hotelcalifornia" target="_blank">Twitter</a>
        
        
    </p>
    <p>&copy; 2025 Hôtel California. Tous droits réservés.</p>
</footer>

    </main>

    <!-- JavaScript commun -->
    <script src="view/top/static/js/base.js"></script>
    
</body>
</html>