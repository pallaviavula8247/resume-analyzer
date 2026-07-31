import { FaTools } from "react-icons/fa";
import DashboardCard from "./DashboardCard";

function SkillCard() {
  return (
    <DashboardCard
      title="Skills"
      value="18"
      icon={<FaTools />}
      color="#F59E0B"
    />
  );
}

export default SkillCard;