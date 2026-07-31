import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { registerUser } from "../services/authService";

const Register = () => {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    full_name: "",
    email: "",
    phone: "",
    password: "",
  });

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setError("");
    setLoading(true);

    try {
      const response = await registerUser(form);

      console.log("Registration Response:", response);

      alert("Registration Successful!");

      // Clear form
      setForm({
        full_name: "",
        email: "",
        phone: "",
        password: "",
      });

      // Redirect to Login page
      navigate("/login");
    } catch (error) {
      console.error("Registration Error:", error.response?.data);

      if (error.response?.data) {
        if (typeof error.response.data === "object") {
          const messages = Object.entries(error.response.data)
            .map(([field, message]) => `${field}: ${message}`)
            .join(", ");

          setError(messages);
        } else {
          setError(error.response.data);
        }
      } else {
        setError("Registration failed. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <h1>Create Account</h1>

      <p>Register to start analyzing your resume.</p>

      {error && (
        <p
          style={{
            color: "red",
            marginBottom: "15px",
            fontWeight: "bold",
          }}
        >
          {error}
        </p>
      )}

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="full_name"
          placeholder="Full Name"
          value={form.full_name}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Email Address"
          value={form.email}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="phone"
          placeholder="Phone Number"
          value={form.phone}
          onChange={handleChange}
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Creating Account..." : "Register"}
        </button>
      </form>
    </div>
  );
};

export default Register;