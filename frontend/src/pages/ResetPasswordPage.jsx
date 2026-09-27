import { useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client";

export default function ResetPasswordPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function onSubmit(event) {
    event.preventDefault();
    setError("");
    setMessage("");
    try {
      await api.resetPassword({ email, new_password: password });
      setMessage("Password reset is not connected yet. The request reached the API.");
    } catch {
      setError("Could not reach the API. Start the backend, then try again.");
    }
  }

  return (
    <main className="auth-page">
      <form className="auth-card" onSubmit={onSubmit}>
        <p className="eyebrow">Wellbore analysis</p>
        <h1>Reset password</h1>
        <label>
          Email
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        <label>
          New password
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </label>
        {error && <p className="form-error">{error}</p>}
        {message && <p className="form-note">{message}</p>}
        <button type="submit">Set new password</button>
        <p className="auth-links">
          <Link to="/login">Back to log in</Link>
        </p>
      </form>
    </main>
  );
}
