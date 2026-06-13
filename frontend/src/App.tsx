import { useEffect, useState } from "react";
import "./App.css";
import type { RecordType } from "./types/RecordType";
import { RecordCard } from "./components/RecordCard";

function App() {
  const [records, setRecords] = useState<RecordType[]>([]);
  const [title, setTitle] = useState("");
  const [time, setTime] = useState<number | "">("");
  const [error, setError] = useState("");
  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetch("http://localhost:8000/records");
        const records = await data.json();
        setRecords(records);
      } catch (e) {
        console.log(e);
      }
    };
    fetchData();
  }, []);

  const handleClick = () => {
    if (title === "" || time === 0 || time === "") {
      setError("入力されていない項目があります");
    } else {
      const createRecord = async (title: string, time: number) => {
        try {
          const response = await fetch("http://localhost:8000/records", {
            method: "POST", // POSTメソッドを指定
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title: title, time: time }), // データをJSON文字列に変換
          });
          console.log(response);
          setTitle("");
          setTime(0);
          setError("");
        } catch (e) {
          console.log(e);
          setError("登録に失敗しました");
        }
      };
      const fetchData = async () => {
        try {
          const data = await fetch("http://localhost:8000/records");
          const records = await data.json();
          setRecords(records);
        } catch (e) {
          console.log(e);
        }
      };
      createRecord(title, time);
      fetchData();
    }
  };

  return (
    <div>
      <div>
        <div style={{ display: "flex" }}>
          <p>学習内容</p>
          <input value={title} onChange={(e) => setTitle(e.target.value)} />
        </div>
        <div style={{ display: "flex" }}>
          <p>学習時間</p>
          <input
            type="number"
            value={time}
            onChange={(e) => {
              const value = e.target.value;
              setTime(value === "" ? "" : Number(value));
            }}
          />
          {error ? <p>{error}</p> : null}
        </div>
        <button onClick={handleClick}>登録</button>
      </div>
      {records.map((record) => (
        <RecordCard key={record.id} title={record.title} time={record.time} />
      ))}
    </div>
  );
}

export default App;
