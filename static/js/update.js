document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('.person-row');
    const profileImage = document.getElementById('profile-image');
    const profileName = document.getElementById('profile-name');
    const idInput = document.getElementById('id');
    const validityDateInput = document.getElementById('validity-date');
    const phoneInput = document.getElementById('phone');
    const districtInput = document.getElementById('district');
    const chapterInput = document.getElementById('chapter');

    rows.forEach(row => {
        row.addEventListener('click', function() {
            // Get the record_id attribute value
            const recordId = this.getAttribute('record_id');
            
            // Extract the ID from the record_id string
            const id = recordId.split('-')[1]; // Assuming the ID is the second part of the record_id string

        
            profileImage.src = this.getAttribute('data-image-src');
            profileName.textContent = this.getAttribute('data-name');
            idInput.value = id;
            validityDateInput.value = this.getAttribute('data-validity-date');
            phoneInput.value = this.getAttribute('data-phone');
            districtInput.value = this.getAttribute('data-district');
            chapterInput.value = this.getAttribute('data-chapter');
        });
    });
});
