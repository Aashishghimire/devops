const apiUrl = "http://localhost:5000/api/contacts";

// Load all contacts
const loadContacts = async () => {
  const res = await fetch(apiUrl);
  const data = await res.json();
  const table = document.getElementById("contactsTable");
  table.innerHTML = "";
  data.forEach((contact) => {
    table.innerHTML += `
          <tr>
            <td><input type="text" value="${contact.name}" class="form-control" id="name-${contact._id}"></td>
            <td><input type="email" value="${contact.email}" class="form-control" id="email-${contact._id}"></td>
            <td><input type="text" value="${contact.phone}" class="form-control" id="phone-${contact._id}"></td>
            <td>
              <button class="btn btn-sm btn-success me-1" onclick="updateContact('${contact._id}')">Save</button>
              <button class="btn btn-sm btn-danger" onclick="deleteContact('${contact._id}')">Delete</button>
            </td>
          </tr>
        `;
  });
};

// Add new contact
document.getElementById("contactForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;

  await fetch(apiUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, phone }),
  });

  e.target.reset();
  loadContacts();
});

// Update a contact
const updateContact = async (id) => {
  const name = document.getElementById(`name-${id}`).value;
  const email = document.getElementById(`email-${id}`).value;
  const phone = document.getElementById(`phone-${id}`).value;

  await fetch(`${apiUrl}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, phone }),
  });

  loadContacts();
};

// Delete a contact
const deleteContact = async (id) => {
  if (confirm("Are you sure you want to delete this contact?")) {
    await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
    loadContacts();
  }
};

// Load contacts on page load
window.onload = loadContacts;
