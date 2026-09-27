import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { api } from "../api/client";

export default function LoginPage() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function onSubmit(event) {
    event.preventDefault();
    setError("");
    try {
      await api.login({ email, password });
      navigate("/dashboard");
    } catch {
      setError("Could not reach the API. Start the backend, then try again.");
    }
  }

  return (
    <main className="auth-page">
      <form className="auth-card" onSubmit={onSubmit}>
        <p className="eyebrow">Wellbore analysis</p>
        <h1>Log in</h1>
        <label>
          Email
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        <label>
          Password
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </label>
        {error && <p className="form-error">{error}</p>}
        <button type="submit">Log in</button>
        <p className="auth-links">
          <Link to="/reset-password">Forgot password</Link>
          <Link to="/signup">Create an account</Link>
        </p>
      </form>
    </main>
  );
}
