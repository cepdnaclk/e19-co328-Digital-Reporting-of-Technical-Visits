import React, { useState, useEffect, useRef, useContext } from "react";
import styles from "../Styles/DashboardTasks.module.scss";
import { DataContext } from "../Context/dataContext";

const DashboardTasks = () => {
  const { jobs } = useContext(DataContext);
  const { technicians } = useContext(DataContext);
  const [todayCompletedTasks, setTodayCompletedTasks] = useState([]);
  const [todayIncompletedTasks, setTodayIncompletedTasks] = useState([]);
  const [thisMonthTasks, setThisMonthTasks] = useState([]);
  const [thisMonthUpcomingTasks, setThisMonthUpcomingTasks] = useState([]);
  const [thisMonthCompletedTasks, setThisMonthCompletedTasks] = useState([]);

  useEffect(() => {
    const today = new Date();
    console.log(today.toDateString());
    const filteredTasks = jobs.filter((job) => {
      const jobDate = new Date(job.startDate.toDate());
      console.log(jobDate.toDateString());
      return (
        jobDate.toDateString() === today.toDateString() &&
        job.isCompleted === true
      );
    });
    setTodayCompletedTasks(filteredTasks);
  }, [jobs]);

  useEffect(() => {
    const today = new Date();
    console.log(today.toDateString());
    const filteredTasks = jobs.filter((job) => {
      const jobDate = new Date(job.startDate.toDate());
      console.log(jobDate.toDateString());
      return (
        jobDate.toDateString() === today.toDateString() &&
        job.isCompleted === false
      );
    });
    setTodayIncompletedTasks(filteredTasks);
  }, [jobs]);

  useEffect(() => {
    const today = new Date();
    const startOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
    const endOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 1);
    const filteredTasks = jobs.filter((job) => {
      const jobDate = new Date(job.startDate.toDate());
      return jobDate >= startOfMonth && jobDate <= endOfMonth && job.isCompleted === true;
    });
    setThisMonthCompletedTasks(filteredTasks);
  }, [jobs]);

  useEffect(() => {
    const today = new Date();
    const startOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
    const endOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 1);
    const filteredTasks = jobs.filter((job) => {
      const jobDate = new Date(job.startDate.toDate());
      return jobDate >= startOfMonth && jobDate <= endOfMonth && technicians.find(
        (technician) => technician.email === job.email
      );
    });
    setThisMonthUpcomingTasks(filteredTasks);
  }, [jobs]);

  useEffect(() => {
    const today = new Date();
    const startOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
    const endOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 1);
    const filteredTasks = jobs.filter((job) => {
      const jobDate = new Date(job.startDate.toDate());
      return jobDate >= startOfMonth && jobDate <= endOfMonth;
    });
    setThisMonthTasks(filteredTasks);
  }, [jobs]);


  return (
    <div className={styles.tasksCard}>
      <h1>Today</h1>
      <div className={styles.todayTasks}>
        <p className={styles.taskTitle}>
          {todayIncompletedTasks.length} Ongoing Tasks
        </p>
        {todayIncompletedTasks.length == 0 ? (
          <p className={styles.taskFillerOngoing}>There is no any ongoing tasks</p>
        ) : (
        <div className={styles.ongoingTasksContainer}>
          {todayIncompletedTasks.map((job) => (
            <div key={job.id} className={styles.taskCard}>
              <p className={styles.jobTitle}>{job.company}</p>
              <p className={styles.jobContent}>
                {technicians.find(
                  (technician) => technician.email === job.email
                )?.firstName || "No Technician"}{" "}
                {technicians.find(
                  (technician) => technician.email === job.email
                )?.lastName || ""}{" "}
                |{" "}
                {job.startDate.toDate().toLocaleTimeString("en-US", {
                  hour: "numeric",
                  minute: "numeric",
                  hour12: true, // Use 12-hour format
                })}{" "}
                | {job.address.split(",").pop()}
              </p>
            </div>
          ))}
        </div>
      )}
        <p className={styles.taskTitle}>
          {todayCompletedTasks.length} Completed Tasks
        </p>
        {todayCompletedTasks.length == 0 ? (
          <p className={styles.taskFiller}>Any task was not Completed</p>
        ) : (
          <div className={styles.completedTasksContainer}>
            {todayCompletedTasks.map((job) => (
              <div key={job.id} className={styles.taskCard}>
              <p className={styles.jobTitle}>{job.company}</p>
              <p className={styles.jobContent}>
                {technicians.find(
                  (technician) => technician.email === job.email
                )?.firstName || "No Technician"}{" "}
                {technicians.find(
                  (technician) => technician.email === job.email
                )?.lastName || ""}{" "}
                |{" "}
                {job.startDate.toDate().toLocaleTimeString("en-US", {
                  hour: "numeric",
                  minute: "numeric",
                  hour12: true, // Use 12-hour format
                })}{" "}
                | {job.address.split(",").pop()}
              </p>
            </div>
            ))}
          </div>
        )}
      </div>
      <h1>This Month</h1>
      <div className={styles.monthTasks}>
        <div className={styles.countBox}>
          <p className={styles.countBoxTitle}>Tasks Completed</p>
          <p className={styles.countBoxValue}>{thisMonthCompletedTasks.length}</p>
        </div>
        <div className={styles.countBox}>
          <p className={styles.countBoxTitle}>Upcoming Tasks</p>
          <p className={styles.countBoxValue}>{thisMonthUpcomingTasks.length}</p>
        </div>
        <div className={styles.countBox}>
          <p className={styles.countBoxTitle}>Hours Worked</p>
          <p className={styles.countBoxValue}>{thisMonthTasks.length * 2}</p>
        </div>
      </div>
    </div>
  );

  function formatTime(time) {
    const date = new Date(time);
    let hours = date.getHours();
    let minutes = date.getMinutes();
    const ampm = hours >= 12 ? "PM" : "AM";
    hours = hours % 12;
    hours = hours ? hours : 12;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    const formattedTime = hours + ":" + minutes + " " + ampm;
    return formattedTime;
  }
};

export default DashboardTasks;
