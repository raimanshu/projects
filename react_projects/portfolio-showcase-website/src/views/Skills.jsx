import React from "react";

function Skills() {
  const skills = [
    "React",
    "Node.js",
    "TypeScript",
    "System Design",
    "MongoDB",
    "Tailwind CSS",
  ];

  return (
    <section className="py-20 px-6 max-w-4xl mx-auto">
      <h2 className="text-3xl font-bold mb-6">Skills</h2>
      <div className="flex flex-wrap gap-4">
        {skills.map((skill, index) => (
          <span
            key={index}
            className="bg-teal-600 px-4 py-2 rounded-full text-white"
          >
            {skill}
          </span>
        ))}
      </div>
    </section>
  );
}

export default Skills;
