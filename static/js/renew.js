// modal
document.addEventListener("DOMContentLoaded", function () {
    const openRenewButton = document.getElementById('open-renew-button');
    const closeModalBtn = document.getElementById('closeBtn');
    const modal = document.getElementById('modal_sec');

    if (openRenewButton && closeModalBtn && modal) {
        openRenewButton.addEventListener('click', () => {
            modal.classList.remove('hidden');
        });

        closeModalBtn.addEventListener('click', () => {
            modal.classList.add('hidden');
        });
    } else {
        console.error('Some elements are not found in the DOM.');
    }
});
