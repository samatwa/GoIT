import css from "./Options.module.css";

const Options = ({ options, onFeedback, onReset, totalFeedback }) => {
  return (
    <div className={css.optionsContainer}>
      {options.map((option) => (
        <button
          key={option}
          className={css.button}
          onClick={() => onFeedback(option)}
        >
          {option.charAt(0).toUpperCase() + option.slice(1)}
        </button>
      ))}
      {totalFeedback > 0 && (
        <button className={css.resetButton} onClick={onReset}>
          Reset
        </button>
      )}
    </div>
  );
};

export default Options;
