document.addEventListener("DOMContentLoaded", function () {
    const openModalBtn = document.getElementById('openModalBtn');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const modal = document.getElementById('modal');

    openModalBtn.addEventListener('click', () => {
        modal.classList.remove('hidden');
    });

    closeModalBtn.addEventListener('click', () => {
        modal.classList.add('hidden');
    });
});


// upload image

function displayImagePreview(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            document.getElementById('profile_image').src = e.target.result;
        }

        reader.readAsDataURL(input.files[0]);
    }
}

document.getElementById('id_image').addEventListener('change', function () {
    var fileSize = this.files[0].size; // in bytes
    var maxSize = 1024 * 1024; // 1MB
    if (fileSize > maxSize) {
        alert('File size exceeds 1MB limit. Please choose a smaller image.');
        this.value = ''; // clear the input field
        return false; 
    }
});

// filter
// document.addEventListener("DOMContentLoaded", function() {
//     const filterButton = document.getElementById('filterButton');
//     const filterForm = document.getElementById('filterForm');

//     filterButton.addEventListener('click', function() {
//         filterForm.submit();
//     });
// });

