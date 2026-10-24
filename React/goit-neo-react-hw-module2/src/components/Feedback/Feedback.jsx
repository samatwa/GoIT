import css from "./Feedback.module.css";

const Feedback = ({ feedback, total, positive }) => {
  return (
    <div className={css.feedbackContainer}>
      <ul className={css.feedbackList}>
        {Object.entries(feedback).map(([key, value]) => (
          <li key={key} className={css.feedbackItem}>
            {key.charAt(0).toUpperCase() + key.slice(1)}: {value}
          </li>
        ))}
      </ul>
      <p className={css.totalFeedback}>Total: {total}</p>
      <p className={css.positiveFeedback}>Positive: {positive}%</p>
    </div>
  );
};

export default Feedback;
