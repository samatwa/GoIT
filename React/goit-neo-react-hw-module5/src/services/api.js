import axios from 'axios';

const API_KEY =
  'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0OTUwZDg2ZTA1NjRjZWExOWIyYmJlNmE2Y2I0NGQ2YiIsIm5iZiI6MTc0MDY4MDYwMy4zODUsInN1YiI6IjY3YzBhZDliNTkxYjIzOGQyNjM1ODQwOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.z5u_NtpDQO09dLo8XyNwkh7QQjS0aq7gFLa-530PFJQ'; // Замініть на ваш справжній токен
const BASE_URL = 'https://api.themoviedb.org/3';

const options = {
  headers: {
    Authorization: `Bearer ${API_KEY}`,
  },
};

// Отримання популярних фільмів (Trending Movies)
export const getTrendingMovies = async () => {
  const { data } = await axios.get(`${BASE_URL}/trending/movie/day`, options);
  return data.results;
};

// Пошук фільмів за ключовим словом (Search Movies)
export const searchMovies = async query => {
  const { data } = await axios.get(
    `${BASE_URL}/search/movie?query=${query}&include_adult=false&language=en-US&page=1`,
    options
  );
  return data.results;
};

// Отримання деталей фільму (Movie Details)
export const getMovieDetails = async movieId => {
  const { data } = await axios.get(`${BASE_URL}/movie/${movieId}`, options);
  return data;
};

// Отримання акторського складу (Movie Cast)
export const getMovieCast = async movieId => {
  const { data } = await axios.get(
    `${BASE_URL}/movie/${movieId}/credits`,
    options
  );
  return data.cast;
};

// Отримання рецензій (Movie Reviews)
export const getMovieReviews = async movieId => {
  const { data } = await axios.get(
    `${BASE_URL}/movie/${movieId}/reviews`,
    options
  );
  return data.results;
};