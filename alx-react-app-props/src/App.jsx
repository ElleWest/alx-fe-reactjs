import "./App.css";
import WelcomeMessage from "./components/WelcomeMessage";
import UserProfile from "./components/UserProfile";
import Header from "./components/Header";
import MainContent from "./components/MainContent";
import Footer from "./components/Footer";
import UserContext from "./components/UserContext";

function App() {
  const userData = { name: "Jane Doe", email: "jane.doe@example.com" };

  return (
    <UserContext.Provider value={userData}>
      <Header />
      <MainContent />
      <UserProfile />
      <WelcomeMessage />
      <Footer />
    </UserContext.Provider>
  );
}

export default App;
