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
        navigation.classList.add('pointer-events-none');
    }

    // Add click event listener to the toggle button
    toggleNavigation.addEventListener('click', () => {
        // Toggle the 'hidden' class on navigation
        if (navigation.classList.contains('opacity-0')) {
            // If so, make it visible
            navigation.classList.remove('opacity-0');
            navigation.classList.remove('pointer-events-none');
            navigation.classList.add('opacity-100');
            navigation.classList.add('pointer-events-auto');
        } else {
            // Otherwise, make it invisible
            closeNavigation()
        }
    });

    // Add click event listener to the navigation links
    for (let i = 0; i < navigationLinks.length; i++) {
        navigationLinks[i].addEventListener('click', closeNavigation);
    }

    // Logic to show/hide header on scroll
    let lastScrollTop = 0;
    window.addEventListener('scroll', function () {
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


    // // Get all sections
    // let sections = document.querySelectorAll('section');
    //
    // // Function to remove the hash from the URL
    // function removeHash() {
    //     history.pushState("", document.title, window.location.pathname
    //         + window.location.search);
    // }
    //
    // // Options for the observer
    // let options = {
    //     root: null, // document viewport
    //     rootMargin: '0px',
    //     threshold: 0.5 // adjust this value for when you want the callback to fire
    // };
    //
    // let observer = new IntersectionObserver((entries, observer) => {
    //     entries.forEach(entry => {
    //         if (entry.isIntersecting) {
    //             // Remove the current hash
    //             removeHash();
    //             // Add the new hash
    //             window.location.hash = entry.target.id;
    //         }
    //     });
    // }, options);
    //
    // // Observe each section
    // sections.forEach(section => {
    //     observer.observe(section);
    // });

});