// Navigation
document.addEventListener('DOMContentLoaded', (event) => {
    // Select DOM elements
    const navigation = document.querySelector('.js-navigation');
    const toggleNavigation = document.querySelector('.js-toggle-navigation');
    const navigationLinks = document.querySelectorAll('.js-navigation a');
    const header = document.getElementById('main-header');
    
    // Function to close navigation
    function closeNavigation() {
        navigation.classList.remove('opacity-100');
        navigation.classList.add('opacity-0');
    }
    
    // Add click event listener to the toggle button
    toggleNavigation.addEventListener('click', () => {
        // Toggle the 'hidden' class on navigation
        if(navigation.classList.contains('opacity-0')) {
            // If so, make it visible
            navigation.classList.remove('opacity-0');
            navigation.classList.add('opacity-100');
        } else {
            // Otherwise, make it invisible
            closeNavigation()
        }
    });

    // Add click event listener to the navigation links
    for(let i = 0; i < navigationLinks.length; i++) {
        navigationLinks[i].addEventListener('click', closeNavigation);
    }

    // Logic to show/hide header on scroll
    let lastScrollTop = 0;
    window.addEventListener('scroll', function() {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        if (scrollTop > lastScrollTop) {
            // Down scroll
            header.style.transform = 'translateY(-100%)';
        } else {
            // Up scroll
            header.style.transform = 'translateY(0)';
        }
        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    }, false);
});