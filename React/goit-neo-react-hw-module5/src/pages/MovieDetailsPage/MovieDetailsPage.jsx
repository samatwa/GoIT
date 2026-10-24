import { useEffect, useState, useRef, Suspense } from 'react'
import { useParams, useLocation, Link, Outlet } from 'react-router-dom'
import { getMovieDetails } from '../../services/api'
import css from './MovieDetailsPage.module.css'

const defaultImg =
  'https://dl-media.viber.com/10/share/2/long/vibes/icon/image/0x0/95e0/5688fdffb84ff8bed4240bcf3ec5ac81ce591d9fa9558a3a968c630eaba195e0.jpg'

const MovieDetailsPage = () => {
  const { movieId } = useParams()
  const [movie, setMovie] = useState(null)
  const location = useLocation()
  const backLink = useRef(location.state ?? '/movies')


  useEffect(() => {
    getMovieDetails(movieId).then(setMovie)
  }, [movieId])

  if (!movie) return <p>Loading...</p>

  return (
    <div>
      <Link to={backLink.current}>← Go back</Link>

      <div className={css.movieDetails}>
        <img
          src={
            movie.poster_path
              ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
              : defaultImg
          }
          width={250}
          alt="poster"
          className={css.moviePoster}
        />
        <div className={css.movieInfo}>
          <h1>
            {movie.title} ({movie.release_date?.split('-')[0]})
          </h1>
          <p>
            <strong>User Score:</strong> {Math.round(movie.vote_average * 10)}%
          </p>
          <h2>Overview:</h2>
          <p>{movie.overview}</p>
          <h2>Genres:</h2>
          <p>{movie.genres.map(genre => genre.name).join(', ')}</p>
        </div>
      </div>

      <div className={css.additionalInfo}>
        <h3>Additional information</h3>
        <ul>
          <li>
            <Link to="cast">
              Cast
            </Link>
          </li>
          <li>
            <Link to="reviews">
              Reviews
            </Link>
          </li>
        </ul>
      </div>
      <Suspense fallback={<div>Loading...</div>}>
        <Outlet />
      </Suspense>
    </div>
  );
};

export default MovieDetailsPage;