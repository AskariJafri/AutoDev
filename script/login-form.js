const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', (e) => {
  e.preventDefault();

  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim();

  if (username && password) {
    // Send request to server or perform authentication logic
    console.log(`Login with ${username} and ${password}`);
  } else {
    alert('Please fill in both username and password');
  }
});