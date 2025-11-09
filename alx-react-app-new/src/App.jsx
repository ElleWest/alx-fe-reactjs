import "./App.css";
import WelcomeMessage from "./components/WelcomeMessage";
import UserProfile from "./components/UserProfile";
import Header from "./components/Header";
import MainContent from "./components/MainContent";
import Footer from "./components/Footer";
import Counter from "./components/Counter";

function App() {
  return (
    <>
      <Header />
      <MainContent />
      <Counter />
      <Footer />
      <WelcomeMessage />
      <UserProfile name="Alice" age={25} bio="Loves hiking and photography" />
    </>
  );
}

export default App;
