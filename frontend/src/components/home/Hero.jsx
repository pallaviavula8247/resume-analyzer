import { Link } from "react-router-dom";
import { FaRobot, FaChartLine, FaFileUpload } from "react-icons/fa";

import "../../assets/styles/home.css";


const Hero = () => {
  return (
    <section className="hero">

      <div className="hero-content">

        <h1>
          AI Resume Analyzer
        </h1>


        <h2>
          Analyze Your Resume & Improve Your ATS Score
        </h2>


        <p>
          Upload your resume and get AI-powered insights,
          skill gap analysis, ATS optimization tips,
          and personalized job recommendations.
        </p>


        <div className="hero-buttons">

          <Link 
            to="/upload" 
            className="primary-btn"
          >
            <FaFileUpload />
            Upload Resume
          </Link>


          <Link 
            to="/register"
            className="secondary-btn"
          >
            Get Started
          </Link>

        </div>


        <div className="hero-features">

          <div className="hero-card">
            <FaRobot />
            <span>
              AI Resume Analysis
            </span>
          </div>


          <div className="hero-card">
            <FaChartLine />
            <span>
              ATS Score Prediction
            </span>
          </div>


          <div className="hero-card">
            <FaFileUpload />
            <span>
              Instant Resume Review
            </span>
          </div>

        </div>


      </div>

    </section>
  );
};


export default Hero;