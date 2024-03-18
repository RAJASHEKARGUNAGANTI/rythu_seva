// server.js
const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken"); // Import JWT library
const User = require("./models/User");

const app = express();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = "your_jwt_secret"; // Change this to a random secret key

// Middleware
app.use(cors({
  origin: 'http://127.0.0.1:5000',
  methods: 'POST', // Allow POST requests
  credentials: true // Allow cookies to be sent in cross-origin requests
}));
app.use(bodyParser.json());

// MongoDB connection
mongoose
  .connect(
    "mongodb+srv://gunagantirajashekar:gunagantirajashekar@cluster0.pbidgdb.mongodb.net/grafana?retryWrites=true&w=majority&appName=Cluster0/",
    {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    }
  )
  .then(() => {
    console.log("DB connection established");
  })
  .catch((err) => {
    console.log(err);
  });

// Login route
app.post("/signin", async (req, res) => {
  try {
    const { email, password } = req.body;

    // Find user by email
    const user = await User.findOne({ email });
    if (!user) {
      throw new Error("Invalid email or password");
    }

    // Compare passwords
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      throw new Error("Invalid email or password");
    }

    // Create JWT token
    const token = jwt.sign({ userId: user._id }, JWT_SECRET, {
      expiresIn: "1h", // Token expiration time
    });

    // Send token as cookie
    res.cookie("token", token, { httpOnly: true });

    // Login successful
    res.status(200).json({ message: "Login successful", user: user });
    console.log("Login successful");
  } catch (error) {
    console.error("Error:", error);
    res.status(401).json({ error: error.message });
  }
});

// Registration route
app.post("/register", async (req, res) => {
  try {
    const { name, email, password } = req.body;

    // Check if user already exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res
        .status(400)
        .json({ error: "User with this email already exists" });
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create new user
    const newUser = new User({ name, email, password: hashedPassword });
    await newUser.save();

    // Registration successful
    res.status(201).json({ message: "Registration successful", user: newUser });
  } catch (error) {
    console.error("Error:", error);
    res
      .status(500)
      .json({ error: "An error occurred. Please try again later." });
  }
});

// Logout route
app.post("/logout", (req, res) => {
  res.clearCookie("token", { httpOnly: true }); // Clear token cookie
  res.status(200).json({ message: "Logout successful" });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
