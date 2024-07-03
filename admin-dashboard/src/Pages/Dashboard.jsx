import Calendar from "../Components/Calender";
import { Navigation } from "../Components/Navigation/Navigation";
import UserCard from "../Components/UserCard";
import Notification from "../Components/Notification";
import OngoingTasksCard from "../Components/OngoingTasksCard";
import CompletedTasksCard from "../Components/CompletedTasksCard";
import DashboardTasks from "../Components/DashboardTasks";
import styles from "../Styles/Dashboard.module.scss";
import PieChart from "../Components/PieChart";

export const Dashboard = () => {
  return (
    <div className={styles.container}>
      <Navigation />
      <UserCard />
      <Notification />
      <div className={styles.component_container}>
        <Calendar />
        <div className={styles.dataContainer}>
          <DashboardTasks />
        </div>
      </div>
    </div>
  );
};
