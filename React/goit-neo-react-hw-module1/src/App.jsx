import userData from "./userData.json";
import friends from "./friends.json";
import transactions from "./transactions.json";
import FriendList from "./components/FriendList/FriendList.jsx";
import Profile from "./components/Profile/Profile.jsx";
import TransactionHistory from "./components/TransactionHistory/TransactionHistory.jsx";
import "./App.css";

const App = () => {
  return (
    <>
      <Profile
        image={userData.avatar}
        name={userData.username}
        tag={userData.tag}
        location={userData.location}
        stats={userData.stats}
      />
      <FriendList friends={friends} />
      <TransactionHistory transactions={transactions} />
    </>
  );
};

export default App;
