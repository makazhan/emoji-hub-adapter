import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div
      style={{
        backgroundColor: "#fbeeca",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1 style={{ fontSize: "3rem", marginBottom: "1rem" }}>
        Do you feel <span style={{ color: "#ff9900" }}>emojized</span>?
      </h1>
      <p style={{ fontSize: "1.2rem", marginBottom: "2rem" }}>
        Dive into the world of emojis and find your vibe!
      </p>
      <Link
        to="/emojis"
        style={{
          padding: "0.75rem 1.5rem",
          backgroundColor: "#ff9900",
          color: "white",
          borderRadius: "8px",
          textDecoration: "none",
          fontWeight: "bold",
          fontSize: "1.1rem",
        }}
      >
        Browse Emojis →
      </Link>
    </div>
  );
}
