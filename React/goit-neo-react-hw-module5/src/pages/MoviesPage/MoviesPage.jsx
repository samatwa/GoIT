import { useState, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import { searchMovies } from '../../services/api'
import MovieList from '../../components/MovieList/MovieList'
import SearchForm from '../../components/SearchForm/SearchForm'
import css from './MoviesPage.module.css'

const MoviesPage = () => {
  const [movies, setMovies] = useState([])
  const [searchParams, setSearchParams] = useSearchParams()
  const [errorMessage, setErrorMessage] = useState('')
  const query = searchParams.get('query') ?? ''

  useEffect(() => {
    if (!query) return;

    searchMovies(query)
      .then(data => {
        if (data.length === 0) {
          setErrorMessage(`No results found for "${query}"`);
          setMovies([]);
        } else {
          setErrorMessage('');
          setMovies(data);
        }
      })
      .catch(() => {
        setErrorMessage('Something went wrong. Please try again later.');
      });
  }, [query]);

  return (
    <div className={css.container}>
      <SearchForm onSubmit={value => setSearchParams({ query: value })} />
      {errorMessage && <p className={css.error}>{errorMessage}</p>}
      <MovieList movies={movies} />
    </div>
  );
};

export default MoviesPage;