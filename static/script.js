async function search_wikipedia() {
    const query = document.getElementById("query").value;

    const response = await fetch("/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });

    const resultBox = document.getElementById("result");

    if (response.ok) {
        const data = await response.json();
        resultBox.innerHTML = `<h4>${data.title}</h4><p>${data.summary}</p><a href="${data.url}" target="_blank">Read more</a>`;
    } else {
        const error = await response.json();
        resultBox.innerHTML = `<p style="color: red;">${error.error}</p>`;
    }
}

async function viewRandomPage() {
    const response = await fetch("/random");
    const resultBox = document.getElementById("result");

    if (response.ok) {
        const data = await response.json();
        resultBox.innerHTML = `<h4>${data.title}</h4><p>${data.summary}</p><a href="${data.url}" target="_blank">Read more</a>`;
    } else {
        resultBox.innerHTML = `<p style="color: red;">Something went wrong.</p>`;
    }
}

async function manageFavorites() {
    const response = await fetch("/favorites");

    const resultBox = document.getElementById("result");
    if (response.ok) {
        const data = await response.json();
        if (data.favorites.length > 0) {
            resultBox.innerHTML = `<h4>Favorite Articles</h4><ul>${data.favorites.map(article => `<li>${article}</li>`).join("")}</ul>`;
        } else {
            resultBox.innerHTML = "<p>No favorite articles found.</p>";
        }
    } else {
        resultBox.innerHTML = `<p style="color: red;">Could not retrieve favorites.</p>`;
    }
}

async function takeQuiz() {
    const response = await fetch("/random");

    const resultBox = document.getElementById("result");
    if (response.ok) {
        const data = await response.json();
        const correctTitle = data.title;

        resultBox.innerHTML = `
            <h4>Guess the Wikipedia Article!</h4>
            <p>${data.summary}</p>
            <input type="text" class="form-control mt-3" id="guess" placeholder="Your guess here...">
            <button class="btn btn-success mt-2" onclick="checkGuess('${correctTitle.replace(/'/g, "\\'")}')">Submit Guess</button>
        `;
    } else {
        resultBox.innerHTML = `<p style="color: red;">Quiz generation failed.</p>`;
    }
}

function checkGuess(correctTitle) {
    const guess = document.getElementById("guess").value.trim();
    const resultBox = document.getElementById("result");
    if (guess.toLowerCase() === correctTitle.toLowerCase()) {
        resultBox.innerHTML += `<p style="color: green;"><strong>Correct!</strong> It was <em>${correctTitle}</em>.</p>`;
    } else {
        resultBox.innerHTML += `<p style="color: red;"><strong>Wrong!</strong> It was <em>${correctTitle}</em>.</p>`;
    }
}

async function setLanguage() {
    const langCode = prompt("Enter language code (e.g., en, hi, ar, ko):");
    if (!langCode) return;

    const response = await fetch("/language", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: langCode })
    });

    const resultBox = document.getElementById("result");
    const data = await response.json();

    if (response.ok) {
        resultBox.innerHTML = `<p style="color: green;"><strong>Success:</strong> ${data.message}</p>`;
    } else {
        resultBox.innerHTML = `<p style="color: red;"><strong>Error:</strong> ${data.error}</p>`;
    }
}




function exit() {
    const resultBox = document.getElementById("result");

    const confirmed = confirm("Are you sure you want to exit Wikipedia Explorer?");
    if (confirmed) {
        resultBox.innerHTML = `
            <p style="color: #dc3545; font-weight: bold;">You have exited Wikipedia Explorer. Have a great day!</p>
        `;
        // Optionally disable buttons or redirect to a goodbye page
        document.querySelectorAll("button").forEach(btn => btn.disabled = true);
    }
}
