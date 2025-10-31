import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [feedback, setFeedback] = useState("");

  const askQuestion = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setResponse("");
    setFeedback("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/ask", { query });
      setResponse(res.data.response);
    } catch (err) {
      setResponse("⚠️ Error connecting to backend.");
    } finally {
      setLoading(false);
    }
  };

  const sendFeedback = async (type) => {
    setFeedback(type);
    await axios.post("http://127.0.0.1:8000/feedback", {
      question: query,
      feedback: type,
    });
  };

  return (
    <div className="app">
      <h1>🧠 Math Routing Agent</h1>
      <div className="input-section">
        <input
          type="text"
          placeholder="Ask a math question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={askQuestion} disabled={loading}>
          {loading ? "Solving..." : "Ask"}
        </button>
      </div>

      <div className="output-section">
        {response && (
          <div className="response-box">
            <p>{response}</p>

            <div className="feedback-buttons">
              <button
                className={feedback === "positive" ? "active" : ""}
                onClick={() => sendFeedback("positive")}
              >
                👍
              </button>
              <button
                className={feedback === "negative" ? "active" : ""}
                onClick={() => sendFeedback("negative")}
              >
                👎
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
