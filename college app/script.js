
  const navbar = document.querySelector('nav.navbar');
  const scrollTopBtn = document.getElementById('scrollTopBtn');

  // When the user scrolls, run this function
  window.onscroll = function() {
    // Navbar shadow toggle
    if (window.scrollY > 50) {
      navbar.classList.add('shadow', 'bg-white');
      navbar.classList.remove('bg-primary', 'navbar-dark');
      navbar.classList.add('navbar-light');
    } else {
      navbar.classList.remove('shadow', 'bg-white', 'navbar-light');
      navbar.classList.add('bg-primary', 'navbar-dark');
    }

    // Show/hide scroll to top button
    if (window.scrollY > 300) {
      scrollTopBtn.style.display = "block";
    } else {
      scrollTopBtn.style.display = "none";
    }
  };

  // Scroll to top smoothly when button clicked
  scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

