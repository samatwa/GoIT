import { useState, useEffect } from 'react'
import css from './App.module.css'
import Options from './components/Options/Options'
import Feedback from './components/Feedback/Feedback'
import Notification from './components/Notification/Notification'
import Description from './components/Description/Description'

const OPTIONS = ["good", "neutral", "bad"];

const App = () => {
  const [feedback, setFeedback] = useState(() => {
    try {
      const savedFeedback = localStorage.getItem("feedback");
      return savedFeedback
        ? JSON.parse(savedFeedback)
        : { good: 0, neutral: 0, bad: 0 };
    } catch (error) {
      console.error("Error reading from localStorage", error);
      return { good: 0, neutral: 0, bad: 0 };
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem("feedback", JSON.stringify(feedback));
    } catch (error) {
      console.error("Error saving to localStorage", error);
    }
  }, [feedback]);

  const updateFeedback = feedbackType => {
    setFeedback((prev) => ({
      ...prev,
      [feedbackType]: prev[feedbackType] + 1,
    }));
  };

  const resetFeedback = () => {
    setFeedback({ good: 0, neutral: 0, bad: 0 });
  };

  const totalFeedback = feedback.good + feedback.neutral + feedback.bad;
  const positiveFeedback =
    totalFeedback > 0 ? Math.round((feedback.good / totalFeedback) * 100) : 0;

  return (
    <div className={css.appContainer}>
      <Description
        title="Sip Happens Café"
        description="Please leave your feedback about our service by selecting one of the options below."
      />
      <Options
        options={OPTIONS}
        onFeedback={updateFeedback}
        onReset={resetFeedback}
        totalFeedback={totalFeedback}
      />
      {totalFeedback > 0 ? (
        <Feedback
          feedback={feedback}
          total={totalFeedback}
          positive={positiveFeedback}
        />
      ) : (
        <Notification />
      )}
    </div>
  );
};

export default App
