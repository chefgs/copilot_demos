// Create a new project
project = new Project();
project.setName("My Project");
project.setStartDate(new Date());
project.setHealth("Green");
project.setReleaseStatus("In progress");

// Add the project to the database
db.projects.insert(project);

// Get the project from the database
project = db.projects.findOne({ _id: project._id });

// Display the project details
console.log("Project name:", project.name);
console.log("Project start date:", project.startDate);
console.log("Project health:", project.health);
console.log("Project release status:", project.releaseStatus);

// Create a new user
user = new User();
user.setName("John Doe");
user.setEmail("john.doe@example.com");
user.setPassword("password");

// Add the user to the database
db.users.insert(user);

// Get the user from the database
user = db.users.findOne({ _id: user._id });

// Display the user details
console.log("User name:", user.name);
console.log("User email:", user.email);

// Create a new login endpoint
app.post("/login", (req, res) => {
  // Get the user from the database
  user = db.users.findOne({ email: req.body.email });

  // Check if the user exists
  if (!user) {
    res.status(404).send("User not found");
    return;
  }

  // Check if the password is correct
  if (user.password !== req.body.password) {
    res.status(401).send("Invalid password");
    return;
  }

  // Create a JWT token
  token = jwt.sign({ id: user._id }, process.env.JWT_SECRET);

  // Send the token to the user
  res.status(200).send({ token });
});

// Create a new logout endpoint
app.post("/logout", (req, res) => {
  // Remove the JWT token from the user's browser
  res.clearCookie("token");

  // Redirect the user to the login page
  res.redirect("/login");
});

// Create a new admin panel endpoint
app.get("/admin", (req, res) => {
  // Check if the user is an admin
  if (!req.user.isAdmin) {
    res.status(403).send("Forbidden");
    return;
  }

  // Get all of the projects from the database
  projects = db.projects.find();

  // Display the projects to the user
  res.render("admin", { projects });
});

// Start the server
app.listen(3000, () => {
  console.log("Server listening on port 3000");
});
