import os

# Define the directory structure and file contents
structure = {
    ".gitignore": """
# Node.js
node_modules/
npm-debug.log
yarn-error.log
.env

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Dependency directories
node_modules/
jspm_packages/

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# dotenv environment variables file
.env

# Next.js
.next/
out/

# Build directories
dist/
build/

# Miscellaneous
.DS_Store
*.swp
""",
    "package.json": """
{
  "name": "graphql-server",
  "version": "1.0.0",
  "description": "A basic Node.js and GraphQL server setup",
  "main": "index.js",
  "scripts": {
    "start": "node src/server.js",
    "dev": "nodemon src/server.js"
  },
  "dependencies": {
    "@apollo/server": "^4.0.0",
    "graphql": "^16.0.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.0"
  },
  "author": "",
  "license": "ISC"
}
""",
    "index.js": """
import server from './src/server.js';

server();
""",
    "src/server.js": """
import { ApolloServer } from '@apollo/server';
import { startServerAndCreateNextHandler } from '@as-integrations/next';
import typeDefs from './graphql/schema.js';
import resolvers from './graphql/resolvers.js';

// Create the Apollo Server
const server = new ApolloServer({
  typeDefs,
  resolvers,
  introspection: true, // Enables the GraphQL Playground
});

// Export the default handler for Next.js API route
export default startServerAndCreateNextHandler(server);
""",
    "src/graphql/schema.js": """
import { gql } from 'graphql-tag';

// Define the GraphQL schema
const typeDefs = gql`
  type Query {
    hello: String
  }
`;

export default typeDefs;
""",
    "src/graphql/resolvers.js": """
// Define the resolvers
const resolvers = {
  Query: {
    hello: () => 'Hello, world!',
  },
};

export default resolvers;
""",
    "src/config/env.js": """
import dotenv from 'dotenv';

dotenv.config();

export const PORT = process.env.PORT || 4000;
""",
    "README.md": """
# GraphQL Server

A basic Node.js and GraphQL server setup.
"""
}

# Function to create directories and files
def create_structure(base_path, structure):
    for path, content in structure.items():
        full_path = os.path.join(base_path, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(content.strip())

# Create the directory structure and files
base_path = "project-root"
create_structure(base_path, structure)

print(f"Project structure created at {os.path.abspath(base_path)}")