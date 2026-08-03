import { useState } from "react";

function ChangePassword() {

  const [formData, setFormData] = useState({
    old_password: "",
    new_password: "",
    confirm_password: "",
  });

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });

  };

  const handleSubmit = (e) => {

    e.preventDefault();

    if (formData.new_password !== formData.confirm_password) {

      alert("Passwords do not match.");

      return;

    }

    alert(
      "Backend API for password change will be connected later."
    );

    setFormData({
      old_password: "",
      new_password: "",
      confirm_password: "",
    });

  };

  return (

    <div className="change-password">

      <h2>Change Password</h2>

      <form onSubmit={handleSubmit}>

        <div className="form-group">

          <label>Current Password</label>

          <input
            type="password"
            name="old_password"
            value={formData.old_password}
            onChange={handleChange}
            required
          />

        </div>

        <div className="form-group">

          <label>New Password</label>

          <input
            type="password"
            name="new_password"
            value={formData.new_password}
            onChange={handleChange}
            required
          />

        </div>

        <div className="form-group">

          <label>Confirm Password</label>

          <input
            type="password"
            name="confirm_password"
            value={formData.confirm_password}
            onChange={handleChange}
            required
          />

        </div>

        <button
          type="submit"
          className="password-btn"
        >
          Change Password
        </button>

      </form>

    </div>

  );

}

export default ChangePassword;