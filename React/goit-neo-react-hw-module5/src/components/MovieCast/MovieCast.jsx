import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { getMovieCast } from '../../services/api'
import css from './MovieCast.module.css'

const defaultImg =
  'https://dl-media.viber.com/10/share/2/long/vibes/icon/image/0x0/95e0/5688fdffb84ff8bed4240bcf3ec5ac81ce591d9fa9558a3a968c630eaba195e0.jpg'

const MovieCast = () => {
  const { movieId } = useParams()
  const [cast, setCast] = useState([])

  useEffect(() => {
    if (!movieId) return;

    getMovieCast(movieId).then(setCast).catch(console.error);
  }, [movieId]);

  return (
    <div className={css.castContainer}>
      <h2>Cast</h2>
      {cast.length > 0 ? (
        <div className={css.castGrid}>
          {cast.map(({ id, name, profile_path, character }) => (
            <div key={id} className={css.castItem}>
              <img
                src={
                  profile_path
                    ? `https://image.tmdb.org/t/p/w200${profile_path}`
                    : defaultImg
                }
                alt={name}
                className={css.castImage}
              />
              <p className={css.castName}>{name}</p>
              <p className={css.castCharacter}>
                Character: {character || 'Unknown'}
              </p>
            </div>
          ))}
        </div>
      ) : (
        <p className={css.noCast}>
          We don't have any cast information for this movie
        </p>
      )}
    </div>
  );
};

export default MovieCast;
