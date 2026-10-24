const inputName = document.querySelector('#name-input'); 
const nameOutput = document.querySelector('#name-output'); 

inputName.addEventListener('input', event => {
  const name = event.currentTarget.value.trim(); 
  console.log(nameOutput.textContent = name || 'Anonymous'); 
});
