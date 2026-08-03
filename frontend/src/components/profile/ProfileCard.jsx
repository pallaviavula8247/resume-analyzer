import {
  FaUserCircle,
  FaEnvelope,
  FaPhone,
  FaMapMarkerAlt,
  FaCalendarAlt,
  FaUser,
} from "react-icons/fa";

function ProfileCard({ profile }) {

  return (

    <div className="profile-card">

      {/* ============================= */}
      {/* Profile Avatar */}
      {/* ============================= */}

      <div className="profile-avatar">

        <FaUserCircle size={120} />

      </div>

      {/* ============================= */}
      {/* User Name */}
      {/* ============================= */}

      <h2 className="profile-name">
        {profile?.full_name || "User"}
      </h2>

      <p className="profile-role">
        AI Resume Analyzer User
      </p>

      <hr />

      {/* ============================= */}
      {/* Profile Details */}
      {/* ============================= */}

      <div className="profile-details">

        <div className="profile-item">

          <FaUser className="profile-icon" />

          <div>

            <span className="profile-label">
              Full Name
            </span>

            <p>
              {profile?.full_name || "-"}
            </p>

          </div>

        </div>

        <div className="profile-item">

          <FaEnvelope className="profile-icon" />

          <div>

            <span className="profile-label">
              Email
            </span>

            <p>
              {profile?.email || "-"}
            </p>

          </div>

        </div>

        <div className="profile-item">

          <FaPhone className="profile-icon" />

          <div>

            <span className="profile-label">
              Phone
            </span>

            <p>
              {profile?.phone || "Not Available"}
            </p>

          </div>

        </div>

        <div className="profile-item">

          <FaMapMarkerAlt className="profile-icon" />

          <div>

            <span className="profile-label">
              Location
            </span>

            <p>
              {profile?.location || "Not Available"}
            </p>

          </div>

        </div>

        <div className="profile-item">

          <FaCalendarAlt className="profile-icon" />

          <div>

            <span className="profile-label">
              Joined On
            </span>

            <p>

              {profile?.date_joined
                ? new Date(
                    profile.date_joined
                  ).toLocaleDateString()
                : "-"}

            </p>

          </div>

        </div>

      </div>

    </div>

  );

}

export default ProfileCard;