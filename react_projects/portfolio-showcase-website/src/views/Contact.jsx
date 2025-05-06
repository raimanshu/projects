import React from "react";

// components/ContactSection.js
function Contact() {
  return (
    <section className="py-20 px-6 max-w-2xl mx-auto">
      <h2 className="text-3xl font-bold mb-6">Contact</h2>
      <form className="flex flex-col gap-4">
        <input
          type="text"
          placeholder="Name"
          className="p-3 rounded bg-gray-800 text-white"
        />
        <input
          type="email"
          placeholder="Email"
          className="p-3 rounded bg-gray-800 text-white"
        />
        <textarea
          placeholder="Your message..."
          className="p-3 rounded bg-gray-800 text-white"
        ></textarea>
        <button
          type="submit"
          className="bg-teal-600 py-2 rounded text-white hover:bg-teal-500 transition"
        >
          Send
        </button>
      </form>
    </section>
  );
}

export default Contact;
