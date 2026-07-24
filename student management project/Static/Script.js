// Student Management System - Script.js

// Display a welcome message in the browser console
window.onload = function () {
    console.log("Student Management System Loaded Successfully");
};

// Confirm before deleting a st
function confirmDelete() {
    return confirm("Are you sure you want to delete this student?");
}

// Validate the Add/Edit Student form
function validateForm() {
    let id = document.getElementById("id").value.trim();
    let name = document.getElementById("name").value.trim();
    let course = document.getElementById("course").value.trim();

    if (id === "" || name === "" || course === "") {
        alert("Please fill in all fields.");
        return false;
    }

    return true;
}
//Show  sucess in a message
function showSuccess(message) {
    alert(message);
}