
// edit persons
document.addEventListener('DOMContentLoaded', function() {
    function editPerson(record_id) {
        // Find the row with the matching personId
        const row = document.querySelector(`[data-id="${record_id}"]`);
        
        // Check if the row exists before proceeding
        if (!row) return;

        // Populate the form with the row's data
        const form = document.getElementById('edit-form');
        form.querySelector('#record_id').value = record_id;
        form.querySelector('#name').value = row.dataset.name;
        form.querySelector('#designation').value = row.dataset.designation;
        form.querySelector('#validity-date').value = row.dataset.validityDate;
        form.querySelector('#phone').value = row.dataset.phone;
        form.querySelector('#district').value = row.dataset.district;
        form.querySelector('#chapter').value = row.dataset.chapter;

        // Show the form and hide the edit button
        // document.getElementById('edit-form').style.display = 'block';
        // document.querySelector('.edit-button[data-id="' + record_id + '"]').style.display = 'none';
    }

    function submitFormData() {
        const form = document.getElementById('edit-form');
        const formData = new FormData(form);

        // Assuming you're using jQuery for AJAX call
        $.ajax({
            url: form.action, // Use the action attribute value
            type: 'POST',
            headers: {
                'X-CSRFToken': $('input[name=csrfmiddlewaretoken]', form).val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                // Handle successful form submission
                console.log("Form submitted successfully");
                // Optionally, redirect or show a success message
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error("Error submitting form:", error);
                // Optionally, show an error message
            }
        });
    }

    // Attach the submitFormData function to the form's onsubmit event
    document.getElementById('edit-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        submitFormData();
    });

    // Example usage of editPerson (adjust according to your actual implementation)
    document.querySelectorAll('.edit-button').forEach(button => {
        button.addEventListener('click', function() {
            const record_id = this.dataset.id;
            editPerson(record_id);
        });
    });
});

//  search
const searchInput = document.getElementById('searchInput');
const suggestionsList = document.getElementById('suggestions');

// Clear previous search input
searchInput.value = '';

searchInput.addEventListener('input', function() {
    const query = searchInput.value.trim();
    if (query.length > 0) {
        fetch(`/search/?query=${query}`)
            .then(response => response.json())
            .then(data => {
                suggestionsList.innerHTML = ''; // Clear previous suggestions
                data.suggestions.forEach(suggestion => {
                    const li = document.createElement('li');
                    li.textContent = suggestion;
                    suggestionsList.appendChild(li);

                    // Add event listener to clear search input on suggestion click
                    li.addEventListener('click', function() {
                        searchInput.value = ''; 
                        suggestionsList.innerHTML = ''; 
                    });
                });
            })
            .catch(error => console.error('Error fetching suggestions:', error));
    } else {
        suggestionsList.innerHTML = ''; 
    }
});

// delete

$(document).ready(function() {
    // Event listener for delete button
    $('.delete-button').on('click', function() {
        // Get person ID from data attribute
        const personId = $(this).data('id');

        // Confirm deletion
        if (confirm('Are you sure you want to delete this person?')) {
            // Send AJAX request to delete the person
            $.ajax({
                url: `/delete_person/${personId}/`,
                type: 'POST',
                headers: {
                    'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function(response) {
                    if (response.status === 'success') {
                        // Remove the person element from the UI
                        $(`#person-${personId}`).remove();
                    } else {
                        alert('Failed to delete the person.');
                    }
                },
                error: function(xhr, status, error) {
                    console.error('Error deleting person:', error);
                    alert('An error occurred while deleting the person.');
                }
            });
        }
    });
});
