import { useEffect, useState } from "react";

import {
  updateUserProfile,
} from "../../services/profileService";

function EditProfile({
  profile,
  refreshProfile,
}) {

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    phone: "",
    location: "",
  });

  const [loading, setLoading] = useState(false);

  useEffect(() => {

    if (profile) {

      setFormData({
        full_name: profile.full_name || "",
        email: profile.email || "",
        phone: profile.phone || "",
        location: profile.location || "",
      });

    }

  }, [profile]);

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });

  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);

      await updateUserProfile(formData);

      alert("Profile updated successfully.");

      refreshProfile();

    } catch (error) {

      console.error(error);

      alert("Unable to update profile.");

    } finally {

      setLoading(false);

    }

  };

  return (

    <div className="edit-profile">

      <h2>Edit Profile</h2>

      <form onSubmit={handleSubmit}>

        <div className="form-group">

          <label>Full Name</label>

          <input
            type="text"
            name="full_name"
            value={formData.full_name}
            onChange={handleChange}
          />

        </div>

        <div className="form-group">

          <label>Email</label>

          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />

        </div>

        <div className="form-group">

          <label>Phone</label>

          <input
            type="text"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
          />

        </div>

        <div className="form-group">

          <label>Location</label>

          <input
            type="text"
            name="location"
            value={formData.location}
            onChange={handleChange}
          />

        </div>

        <button
          type="submit"
          className="save-btn"
          disabled={loading}
        >
          {loading ? "Saving..." : "Save Changes"}
        </button>

      </form>

    </div>

  );

}

export default EditProfile;