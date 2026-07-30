import FeatureCard from "./FeatureCard";

import "../../assets/styles/features.css";


const Features = () => {

  const features = [

    {
      icon: "📄",
      title: "Resume Parsing",
      description:
        "Extract skills, education, projects and experience automatically."
    },

    {
      icon: "🤖",
      title: "AI Resume Analysis",
      description:
        "Get intelligent feedback and improve your ATS compatibility."
    },

    {
      icon: "📊",
      title: "Skill Gap Detection",
      description:
        "Discover missing skills required for your dream job."
    },

    {
      icon: "💼",
      title: "Job Recommendations",
      description:
        "Find suitable job roles based on your resume profile."
    }

  ];


  return (

    <section className="features">

      <h2>
        Powerful Features
      </h2>


      <div className="feature-container">

        {
          features.map((feature, index) => (

            <FeatureCard

              key={index}

              icon={feature.icon}

              title={feature.title}

              description={feature.description}

            />

          ))
        }

      </div>

    </section>

  );
};


export default Features;