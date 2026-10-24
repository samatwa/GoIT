import * as localStorageApi from './localstorage';

console.log(localStorageApi);

const formData = {
  user_name: 'Viacheslav',
  user_email: 'test@test.com',
};

localStorageApi.save('feedback-form-state', formData);

const getFormDataFromLS = () => {
  console.log(localStorageApi.load('feedback-form-state'));
};

getFormDataFromLS();