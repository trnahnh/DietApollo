/* 1) CSRF */
function getCookie(n) {
  let v = null;
  if (document.cookie && document.cookie !== '') {
    document.cookie.split(';').forEach(c => {
      const [k, val] = c.trim().split('=');
      if (k === n) v = decodeURIComponent(val);
    });
  }
  return v;
}
const csrftoken = getCookie('csrftoken');

/* 2) boot */
document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#recipe-save').addEventListener('click', createRecipe);
  loadRecipes();
});

const cleanToken = s => s.replace(/^[\s'"\[]+|[\s'"\]]+$/g, '').trim();

const tidyLines = raw => {
  if (Array.isArray(raw)) return raw.map(cleanToken).filter(Boolean);

  return raw
    .split(',')
    .map(cleanToken)
    .filter(Boolean);
};

/* 3) render */
function loadRecipes() {
  fetch('/api/recipes/')
    .then(r => r.json())
    .then(recipes => {
      const wrap = document.querySelector('#recipes');
      wrap.innerHTML = '';

      recipes.forEach(r => {
        const ingLines = tidyLines(r.ingredients)
          .map(i => `<li>${i}</li>`).join('');
        const insLines = tidyLines(r.instructions)
          .map(i => `<li>${i}</li>`).join('');

        const card = document.createElement('div');
        card.className = 'recipe-card';
        card.innerHTML = `
          <h3>${r.title}</h3>

          <div class="recipe-table">
            <div>
              <strong>Ingredients:</strong>
              <ul>${ingLines}</ul>
            </div>
            <div>
              <strong>Instructions:</strong>
              <ul>${insLines}</ul>
            </div>
          </div>

          <div class="recipe-actions">
            <button class="star-toggle" data-id="${r.id}">
              ${r.starred ? '★' : '☆'}
            </button>
            <button class="edit-btn" data-id="${r.id}">✎</button>
          </div>
        `;
        wrap.appendChild(card);
      });

      document.querySelectorAll('.star-toggle').forEach(btn =>
        btn.addEventListener('click', () => toggleStar(btn.dataset.id))
      );
    })
    .catch(console.error);
}

/* 4) create */
function createRecipe() {
  const title = document.querySelector('input[name="title"]').value.trim();
  const ingredients = document.querySelector('textarea[name="ingredients"]')
    .value.split(',').map(s => s.trim()).filter(Boolean);
  const instructions = document.querySelector('textarea[name="instructions"]')
    .value.split(',').map(s => s.trim()).filter(Boolean);

  if (!title) return alert('Title is required');

  fetch('/api/recipes/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
    body: JSON.stringify({ title, ingredients, instructions })
  })
    .then(r => { if (!r.ok) return r.json().then(e => Promise.reject(e)); })
    .then(() => {
      document.querySelector('input[name="title"]').value = '';
      document.querySelector('textarea[name="ingredients"]').value = '';
      document.querySelector('textarea[name="instructions"]').value = '';
      loadRecipes();
    })
    .catch(e => { console.error(e); alert('Could not save recipe.'); });
}

/* 5) toggle */
function toggleStar(id) {
  fetch(`/api/recipes/${id}/toggle/`, {
    method: 'PUT',
    headers: { 'X-CSRFToken': csrftoken }
  })
    .then(loadRecipes)
    .catch(console.error);
}
