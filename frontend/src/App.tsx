import { useEffect } from "react";
import "./App.css";

function App() {
  useEffect(() => {
    const fetchHello = async () => {
      try {
        const data = await fetch("http://localhost:8000/hello");
        const hello = await data.json();
        console.log(data);
        console.log(hello);
      } catch (e) {
        console.log(e);
      }
    };
    fetchHello();
  }, []);
  return <div>テスト</div>;
}

export default App;
