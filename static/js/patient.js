async function loadPatients() {
    try {
        const response = await fetch("/patients/");
        const data = await response.json();
        const tbody = document.getElementById("patient-table-body");
        tbody.innerHTML = "";

        data.forEach(patient => {
        const doctors = patient.doctor.map(doc => `${doc.name} (${doc.specialization})`).join(", ");
        const paymentStatus = patient.payment_status === 1 ? "Paid" : "Unpaid";

        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${patient.id}</td>
            <td>${patient.name}</td>
            <td>${patient.age}</td>
            <td>${patient.disease}</td>
            <td>${patient.room_id}</td>
            <td>${paymentStatus}</td>
            <td>${doctors || "Unassigned"}</td>
            <td>
            <button class="btn btn-xs btn-info">Edit</button>
            <button class="btn btn-xs btn-danger" onclick="deletePatient(${patient.id})">Delete</button>
            </td>
        `;
        tbody.appendChild(row);
    });

    // Activate DataTable if you're using it
    if (window.$ && $.fn.DataTable && !$.fn.DataTable.isDataTable('#datatable4')) {
    $('#datatable4').DataTable();
    }
} catch (err) {
    console.error("Error loading patients:", err);
}
}


async function deletePatient(id) {
    if (!confirm("Are you sure you want to delete this patient?")) return;

    try {
        const response = await fetch(`/patients/?id=${id}`, {
        method: "DELETE"
        });

        if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Delete failed");
        }

        alert("Patient deleted successfully");
        loadPatients(); // refresh table
    } catch (err) {
        console.error("Error deleting patient:", err);
        alert("Error deleting patient");
    }
}

document.addEventListener("DOMContentLoaded", loadPatients);