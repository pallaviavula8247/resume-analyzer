import { FaStar } from "react-icons/fa";
import DashboardCard from "./DashboardCard";

function ScoreCard() {
  return (
    <DashboardCard
      title="Resume Score"
      value="92%"
      icon={<FaStar />}
      color="#EF4444"
    />
  );
}

export default ScoreCard;