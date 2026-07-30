import "../../assets/styles/howworks.css";


const HowItWorks = () => {

  const steps = [

    {
      number: "01",
      icon: "📤",
      title: "Upload Resume",
      description:
        "Upload your resume PDF and start the AI analysis process."
    },

    {
      number: "02",
      icon: "🤖",
      title: "AI Analysis",
      description:
        "AI extracts skills, education, projects and work experience."
    },

    {
      number: "03",
      icon: "📊",
      title: "Get ATS Score",
      description:
        "Receive resume score, strengths and improvement suggestions."
    },

    {
      number: "04",
      icon: "💼",
      title: "Career Recommendation",
      description:
        "Get matching jobs and skills required for your career goal."
    }

  ];


  return (

    <section className="how-section">

      <h2>
        How It Works
      </h2>


      <div className="timeline">

        {
          steps.map((step, index) => (

            <div 
              className="step"
              key={index}
            >

              <div className="step-number">
                {step.number}
              </div>


              <div className="step-icon">
                {step.icon}
              </div>


              <h3>
                {step.title}
              </h3>


              <p>
                {step.description}
              </p>


              {
                index !== steps.length - 1 && (
                  <div className="arrow">
                    →
                  </div>
                )
              }


            </div>

          ))
        }

      </div>


    </section>

  );

};


export default HowItWorks;