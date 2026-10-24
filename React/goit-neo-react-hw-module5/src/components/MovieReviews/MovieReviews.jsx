import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { getMovieReviews } from '../../services/api'
import css from './MovieReviews.module.css'

const MovieReviews = () => {
  const { movieId } = useParams()
  const [reviews, setReviews] = useState([])

  useEffect(() => {
    if (!movieId) return
    getMovieReviews(movieId).then(setReviews)
  }, [movieId]);

  return (
    <div className={css.reviewsContainer}>
      <h2>Reviews</h2>
      {reviews.length > 0 ? (
        <ul>
          {reviews.map(({ id, author, content }) => (
            <li key={id}>
              <h3>Author: {author}</h3>
              <p>{content}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>We don't have any reviews for this movie</p>
      )}
    </div>
  );
};

export default MovieReviews;
