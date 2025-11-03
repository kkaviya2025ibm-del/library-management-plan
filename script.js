const books = [];

document.getElementById("addBook").addEventListener("click", () => {
    const title = document.getElementById("title").value.trim();
    const author = document.getElementById("author").value.trim();
    const year = document.getElementById("year").value.trim();

    if (!title || !author || !year) {
        alert("Please fill all fields!");
        return;
    }

    books.push({ title, author, year });
    displayBooks();
    clearFields();
});

function displayBooks(filteredBooks = books) {
    const tbody = document.querySelector("#bookTable tbody");
    tbody.innerHTML = "";

    filteredBooks.forEach((book, index) => {
        const row = `
            <tr>
                <td>${book.title}</td>
                <td>${book.author}</td>
                <td>${book.year}</td>
                <td><button onclick="deleteBook(${index})">Delete</button></td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
}

function clearFields() {
    document.getElementById("title").value = "";
    document.getElementById("author").value = "";
    document.getElementById("year").value = "";
}

function deleteBook(index) {
    books.splice(index, 1);
    displayBooks();
}

document.getElementById("search").addEventListener("keyup", (e) => {
    const keyword = e.target.value.toLowerCase();
    const filtered = books.filter(book =>
        book.title.toLowerCase().includes(keyword)
    );
    displayBooks(filtered);
});
