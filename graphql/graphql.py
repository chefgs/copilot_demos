import os

# Define the directory structure
project_name = "hello-world-graphql"
directories = [
    project_name,
    os.path.join(project_name, "src")
]

# Define the files and their content
files = {
    os.path.join(project_name, "src", "index.js"): """
const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const typeDefs = require('./schema');
const resolvers = require('./resolvers');

// Initialize Express app
const app = express();

// Create Apollo Server
const server = new ApolloServer({ typeDefs, resolvers });

// Apply Apollo middleware to Express app
server.start().then(res => {
  server.applyMiddleware({ app });

  // Define a simple GET endpoint
  app.get('/get', (req, res) => {
    res.send('GET request received');
  });

  // Define a simple POST endpoint
  app.post('/post', express.json(), (req, res) => {
    res.send(`POST request received with data: ${JSON.stringify(req.body)}`);
  });

  // Start the server
  app.listen({ port: 4000 }, () =>
    console.log(`Server ready at http://localhost:4000${server.graphqlPath}`)
  );
});
""",
    os.path.join(project_name, "src", "schema.js"): """
const { gql } = require('apollo-server-express');

const typeDefs = gql`
  type Query {
    hello: String
  }

  type Mutation {
    setMessage(message: String): String
  }
`;

module.exports = typeDefs;
""",
    os.path.join(project_name, "src", "resolvers.js"): """
const resolvers = {
  Query: {
    hello: () => 'Hello, world!',
  },
  Mutation: {
    setMessage: (_, { message }) => {
      return `Message received: ${message}`;
    },
  },
};

module.exports = resolvers;
"""
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files with content
for file_path, content in files.items():
    with open(file_path, 'w') as file:
        file.write(content.strip())

print(f"Project '{project_name}' created successfully.")