import { useState } from "react";

export default function AssistantPanel() {
  const [message, setMessage] = useState("");

  return (
    <section className="panel">
      <h2>AI wellbore assistant</h2>
      <div className="placeholder">Ask about the analyzed well after results are stored.</div>
      <form className="chat-form" onSubmit={(event) => event.preventDefault()}>
        <input
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          placeholder="Ask about this well"
        />
        <button type="submit">Send</button>
      </form>
    </section>
  );
}
