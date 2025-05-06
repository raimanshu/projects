// components/ProjectsSection.js
function Projects() {
    const projects = [
      { title: "Project One", description: "A web app for ..." },
      { title: "Project Two", description: "A system design focused project ..." },
    ];
  
    return (
      <section className="py-20 px-6 max-w-4xl mx-auto">
        <h2 className="text-3xl font-bold mb-6">Projects</h2>
        <div className="grid md:grid-cols-2 gap-6">
          {projects.map((project, index) => (
            <div key={index} className="bg-gray-800 p-6 rounded-lg shadow-md">
              <h3 className="text-xl font-semibold mb-2">{project.title}</h3>
              <p>{project.description}</p>
            </div>
          ))}
        </div>
      </section>
    );
  }
  
  export default Projects;
