document.addEventListener('DOMContentLoaded', () => {
    const updateCarouselItems = () => {
        const isLargeScreen = window.matchMedia('(min-width: 992px)').matches;
        const items = document.querySelectorAll('.carousel-item');

        items.forEach(item => {
            const colDivs = item.querySelectorAll('.custom-recipe-col');
            colDivs.forEach(div => {
                div.style.flexBasis = isLargeScreen ? '50%' : '100%'; // Adjust to 50% for large screens
            });
        });
    };

    // Initial setup and event listener for resizing
    updateCarouselItems();
    window.addEventListener('resize', updateCarouselItems);
});
