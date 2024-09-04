## Commands to Initialize the Project

### Initialize npm:
```
npm init -y
```

### Install Dependencies:
```
npm install @apollo/server graphql
npm install --save-dev nodemon
```

### Execute the app
```
npm run dev
```
To start the application in development mode, use the following command. This will use nodemon to automatically restart the server when file changes are detected.

To start the application in production mode, use the following command.
```
npm start
```

### Access the app
- Open the link `http://localhost:4000/api/graphql` in browser
- It opens up the graphql playground.
  - GraphQL Playground: The GraphQL Playground is enabled by default in development mode. It provides an interactive interface to test your GraphQL queries and mutations.

### TODO - Recommended directory structure
Here is a recommended directory structure for a Node.js and GraphQL project using Apollo Server and Next.js:

```
project-root/
├── .gitignore
├── package.json
├── index.js
├── src/
│   ├── graphql/
│   │   ├── schema.js
│   │   └── resolvers.js
│   ├── server.js
│   └── config/
│       └── env.js
└── README.md
```

#### Directory Structure Explanation

- project-root/: The root directory of your project.
- .gitignore: File to specify which files and directories to ignore in version control.
- package.json: Contains project metadata and dependencies.
- index.js: Entry point of the application.
- src/: Source code directory.
- graphql/: Directory for GraphQL-related files.
- schema.js: File to define the GraphQL schema.
- resolvers.js: File to define the GraphQL resolvers.
- server.js: File to set up and start the server.
- config/: Directory for configuration files.
- env.js: File to manage environment variables.
- README.md: Documentation for the project.