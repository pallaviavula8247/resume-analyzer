import { useEffect, useState } from "react";

import ProfileCard from "../components/profile/ProfileCard";
import ProfileStats from "../components/profile/ProfileStats";
import EditProfile from "../components/profile/EditProfile";
import ChangePassword from "../components/profile/ChangePassword";

import {
  getUserProfile,
  getProfileStatistics,
} from "../services/profileService";

import "../assets/styles/Profile.css";

function Profile() {

  const [profile, setProfile] = useState(null);
  const [statistics, setStatistics] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadProfile();
  }, []);

  const loadProfile = async () => {

    try {

      const profileResponse =
        await getUserProfile();

      const dashboardResponse =
        await getProfileStatistics();

      setProfile(profileResponse);

      setStatistics(
        dashboardResponse.data
      );

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }

  };

  if (loading) {
    return (
      <div className="profile-loading">
        Loading Profile...
      </div>
    );
  }

  return (

    <div className="profile-page">

      <h1>My Profile</h1>

      <div className="profile-grid">

        <ProfileCard
          profile={profile}
        />

        <ProfileStats
          statistics={statistics}
        />

      </div>

      <EditProfile
        profile={profile}
        refreshProfile={loadProfile}
      />

      <ChangePassword />

    </div>

  );

}

export default Profile;