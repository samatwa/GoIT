const loginForm = document.querySelector('.login-form');
console.dir(loginForm);

loginForm.addEventListener('submit', event => {
  event.preventDefault();

  const { email, password } = loginForm.elements;

  if (!email.value.trim() || !password.value.trim()) {
    alert('All form fields must be filled in');
    return;
  }

  const loginFormData = {
    email: email.value.trim(),
    password: password.value.trim(),    
  };
  console.log(loginFormData);

  loginForm.reset();
});