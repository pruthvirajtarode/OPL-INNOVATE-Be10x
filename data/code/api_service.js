/**
 * [SYNTHETIC TRAINING DATA - NOT REAL COMPANY INFORMATION]
 * 
 * Simple Express REST API service for user authentication.
 * Used for GitHub Copilot training demonstrations.
 */

const express = require('express');
const app = express();
app.use(express.json());

// In-memory user store for demo purposes
const users = [
  { id: 1, username: 'admin', role: 'admin', isActive: true },
  { id: 2, username: 'jdoe', role: 'user', isActive: true },
  { id: 3, username: 'inactive_user', role: 'user', isActive: false }
];

// Login endpoint with intentional code smell and missing validation
app.post('/api/login', (req, res) => {
  let user = req.body.username;
  let pass = req.body.password;

  // Code smell: Using var and nested loops unnecessarily
  var found = false;
  var targetUser = null;
  for (var i = 0; i < users.length; i++) {
    if (users[i].username == user) { // Using == instead of ===
      found = true;
      targetUser = users[i];
    }
  }

  if (found) {
    // Missing check: Doesn't check if user is active before granting access
    // Missing check: Doesn't actually verify the password!
    res.status(200).send({
      message: 'Login successful',
      token: 'fake-jwt-token-12345',
      userId: targetUser.id
    });
  } else {
    res.status(401).send({ error: 'Invalid credentials' });
  }
});

// Get user profile endpoint
app.get('/api/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);
  
  // Edge case: NaN check missing if parsing fails
  
  const user = users.find(u => u.id === userId);
  
  if (user) {
    res.json(user);
  } else {
    res.status(404).json({ error: 'User not found' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
