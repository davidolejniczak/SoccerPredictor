const express = require("express");
const { Pool } = require("pg");
const cors = require("cors");

const app = express();
const pool = new Pool({
  user: "your_username",
  host: "localhost",
  database: "your_database",
  password: "your_password",
  port: 5432,
});

app.use(cors());

app.get("/matches", async (req, res) => {
  const { limit } = req.query;
  const matchesPerPage = parseInt(limit, 10) || 5; // Default to 5 matches

  try {
    const result = await pool.query(
      "SELECT * FROM matches LIMIT $1",
      [matchesPerPage]
    );
    res.json(result.rows);
  } catch (error) {
    console.error(error);
    res.status(500).send("Server error");
  }
});

app.listen(5000, () => {
  console.log("Server is running on port 5000");
});
